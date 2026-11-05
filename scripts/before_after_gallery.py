#!/usr/bin/env python3
"""Generate the before-and-after gallery in README.md from docs/before-after/*/meta.json.

Each skill folder holds meta.json (the task and the picking rule), without.md and with.md and, for
build tasks, the two stored screenshots. Everything a reader could check is checked against the eval files rather
than typed in:

- the prompt must be the task's prompt in evals/<skill>/heldout/tasks.json, word for word;
- the tally, the marginal mark and the judged difference are read from evals/<skill>/heldout/results.json (the
  loaded-only numbers and the marginal rule of scripts/results_table.py);
- the task must be one where the skill loaded, with the largest judged difference among those tasks (a tie may go
  to a task with screenshots; a task with a larger difference may be passed over only with a reason in meta.json);
- the answers shown are the first sample in which the skill loaded (sample 1 is <side>.md, sample 2 <side>.s1.md);
- for a text answer, every piece of without.md and with.md between `[...]` cuts must appear in the stored answer of
  that sample, word for word (whitespace aside);
- for a build answer (stored as HTML), the screenshots must be byte-identical copies of the stored renders of that
  sample, and without.md and with.md are plain descriptions of them.

The gallery is rewritten between

  <!-- before-after:start --> ... <!-- before-after:end -->

as one collapsible panel per skill, design skills first and copywriting skills second. A second block,

  <!-- before-after:featured:start --> ... <!-- before-after:featured:end -->

shows the one skill whose meta.json says `"featured": true` in full near the top of the README: the prompt, the two
answers side by side and the judge result read from that skill's held-out results.json. Excerpt text is escaped so it
renders as plain text, with newlines as <br> inside table cells. A third block,

  docs/img/ALT.md   <!-- before-after:alt:start --> ... <!-- before-after:alt:end -->

lists every gallery screenshot with the same alt text the README gives it. With --check nothing is written; the exit
code is 1 when the README or ALT.md does not match the files (CI uses this).
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import results_table  # noqa: E402

START, END = "<!-- before-after:start -->", "<!-- before-after:end -->"
FEATURED_START, FEATURED_END = "<!-- before-after:featured:start -->", "<!-- before-after:featured:end -->"
ALT_START, ALT_END = "<!-- before-after:alt:start -->", "<!-- before-after:alt:end -->"
ALT = Path("docs") / "img" / "ALT.md"
GALLERY = Path("docs") / "before-after"
KINDS = (("design", "Design skills"), ("copy", "Copywriting skills"))
CUT = "[...]"
SIDES = ("without", "with")

MD_SPECIAL = re.compile(r"[\\`*_\[\]#~$!]")
ENTITIES = {"&": "&amp;", "<": "&lt;", ">": "&gt;", "|": "&#124;", "@": "&#64;"}


def escape(text):
    """Text that renders as itself in markdown: markup characters are backslash-escaped, the rest become entities."""
    text = MD_SPECIAL.sub(lambda m: "\\" + m.group(0), text)
    return re.sub(r"[&<>|@]", lambda m: ENTITIES[m.group(0)], text)


def alt(text):
    return escape(" ".join(text.split()))


def cell(text):
    """One table cell: escaped, with each line break as <br>. Leading spaces are kept as non-breaking."""
    lines = [escape(ln.rstrip()) for ln in text.strip().splitlines()]
    lines = [re.sub(r"^ +", lambda m: "&nbsp;" * len(m.group(0)), ln) for ln in lines]
    return "<br>".join(lines)


def blockquote(text):
    return "\n".join(("> " + escape(ln)).rstrip() for ln in text.strip().splitlines())


def squash(text):
    return " ".join(text.split())


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise ValueError(f"{path}: {e}") from e


def suffix(sample):
    return "" if sample == 0 else f".s{sample}"


def stored_answer(run, side, sample):
    """(path, 'text' | 'build') of one stored answer: <side>[.sN].md for text, <side>[.sN].html for a build."""
    found = [(run / f"{side}{suffix(sample)}{ext}", kind) for ext, kind in ((".md", "text"), (".html", "build"))]
    found = [(path, kind) for path, kind in found if path.is_file()]
    if len(found) != 1:
        raise ValueError(f"{run}: expected one stored {side} answer for sample {sample}, found {len(found)}")
    return found[0]


def loaded_gaps(results):
    """{task_id: judged difference} over the tasks where the skill loaded, with minus without on the loaded samples
    (protocol 2) or the one pair (protocol 1)."""
    protocol2 = results["summary"].get("protocol", 1) == 2
    gaps = {}
    for v in results.get("verdicts", []):
        if protocol2:
            if v.get("loaded_winner") is None:
                continue
            scores = v["loaded_rubric_scores"]
        else:
            if v.get("with_skill_invoked") is not True:
                continue
            scores = v["rubric_scores"]
        gaps[v["task_id"]] = round(scores["with"] - scores["without"], 3)
    return gaps


def first_loaded_sample(results, task_id):
    """Index of the first sample of a task in which the skill loaded (0 for a protocol 1 pair that loaded)."""
    verdict = next(v for v in results["verdicts"] if v["task_id"] == task_id)
    samples = verdict.get("samples")
    if not samples:
        return 0 if verdict.get("with_skill_invoked") is True else None
    return next((i for i, s in enumerate(samples) if s.get("loaded") is True), None)


class Entry:
    """One gallery skill: its meta.json checked against the eval files, plus the numbers read from them."""

    def __init__(self, root, folder):
        self.root, self.folder = Path(root), folder
        meta = read_json(folder / "meta.json")
        self.meta, self.skill = meta, meta.get("skill")
        where = folder / "meta.json"
        if self.skill != folder.name:
            raise ValueError(f"{where}: skill is {self.skill!r}, expected {folder.name!r}")
        if meta.get("kind") not in dict(KINDS):
            raise ValueError(f"{where}: needs kind design|copy")
        evals = self.root / "evals" / self.skill / "heldout"
        self.results = read_json(evals / "results.json")
        tasks = {t["id"]: t for t in read_json(evals / "tasks.json")}
        task = tasks.get(meta.get("task_id"))
        if task is None:
            raise ValueError(f"{where}: task {meta.get('task_id')!r} is not in {evals / 'tasks.json'}")
        if meta.get("prompt") != task["prompt"]:
            raise ValueError(f"{where}: prompt differs from the task prompt in {evals / 'tasks.json'}")
        self.run = Path("evals") / self.skill / "heldout" / "runs" / meta["task_id"]
        if not (self.root / self.run).is_dir():
            raise ValueError(f"{where}: the run folder {self.run} does not exist")
        outcome = results_table.loaded_outcome(self.results)
        if outcome is None:
            raise ValueError(f"{where}: {self.skill} has no loaded-only result")
        tally = outcome[0]
        self.tally = (tally["with_wins"], tally["without_wins"], tally["ties"])
        self.marginal = bool(results_table.marginal_reasons(self.results))
        self.check_pick(where)
        self.sample = first_loaded_sample(self.results, meta["task_id"])
        if self.sample is None:
            raise ValueError(f"{where}: no sample of {meta['task_id']} loaded the skill")
        self.answer_kind = self.check_answers(where)

    def check_pick(self, where):
        gaps = loaded_gaps(self.results)
        task_id = self.meta["task_id"]
        if task_id not in gaps:
            raise ValueError(f"{where}: the skill did not load on {task_id}")
        self.gap = gaps[task_id]
        passed = {p.get("task_id"): p.get("reason") for p in self.meta.get("passed_over", [])}
        for tid, reason in passed.items():
            if not (tid in gaps and reason):
                raise ValueError(f"{where}: passed_over needs a loaded task and a reason, got {tid!r}")
        bigger = [t for t, g in gaps.items() if g > self.gap + 1e-9 and t not in passed]
        if bigger:
            raise ValueError(f"{where}: {', '.join(sorted(bigger))} had a larger judged difference than {task_id}; "
                             "pick it or list it under passed_over with a reason")

    def check_answers(self, where):
        run = self.root / self.run
        kinds = set()
        shots = {i.get("side"): i for i in self.meta.get("images", [])}
        for side in SIDES:
            path, kind = stored_answer(run, side, self.sample)
            kinds.add(kind)
            excerpt = (self.folder / self.meta[f"{side}_file"]).read_text(encoding="utf-8")
            if kind == "text":
                stored = squash(path.read_text(encoding="utf-8"))
                for piece in (squash(p) for p in excerpt.split(CUT)):
                    if piece and piece not in stored:
                        raise ValueError(f"{self.folder / self.meta[side + '_file']}: this text is not in "
                                         f"{path.relative_to(self.root)}: {piece[:80]!r}")
            else:
                shot = shots.get(side)
                png = run / f"{side}{suffix(self.sample)}.png"
                if not shot:
                    raise ValueError(f"{where}: a build answer needs the {side} screenshot")
                if (self.folder / shot["file"]).read_bytes() != png.read_bytes():
                    raise ValueError(f"{self.folder / shot['file']} is not a copy of {png.relative_to(self.root)}")
        if len(kinds) != 1:
            raise ValueError(f"{where}: one side is a page and the other text")
        return kinds.pop()

    def text(self, side):
        return (self.folder / self.meta[f"{side}_file"]).read_text(encoding="utf-8")

    def shot_row(self):
        shots = {i["side"]: i for i in self.meta.get("images", [])}
        if not shots:
            return None
        rel = GALLERY / self.skill
        return "| " + " | ".join(f"![{alt(shots[k]['alt'])}]({(rel / shots[k]['file']).as_posix()})" if k in shots
                                 else "" for k in SIDES) + " |"


def load(root):
    """[Entry] for every docs/before-after/*/meta.json, sorted by skill name."""
    return [Entry(root, path.parent) for path in sorted((Path(root) / GALLERY).glob("*/meta.json"))]


def sample_note(entry):
    n = entry.sample + 1
    if entry.answer_kind == "build":
        return (f"Both answers are web pages; the screenshots are the stored renders of sample {n} of each side, and "
                "the text is a plain description of each screenshot.")
    return f"The excerpts are from sample {n} of each side."


def panel(entry):
    wins, losses, ties = entry.tally
    marginal = " &middot; marginal" if entry.marginal else ""
    lines = [
        "<details>",
        f"<summary><b>{entry.skill}</b> &middot; {wins} / {losses} / {ties} loaded only{marginal}</summary>",
        "",
        blockquote(entry.meta["prompt"]),
        "",
        "| Without the skill | With the skill |",
        "|---|---|",
        f"| {cell(entry.text('without'))} | {cell(entry.text('with'))} |",
    ]
    shots = entry.shot_row()
    if shots:
        lines.append(shots)
    lines += [
        "",
        f"{sample_note(entry)} [Full run files]({entry.run.as_posix()}/)",
        "",
        f"Judged difference on this task: {entry.gap:+.2f} rubric points. Overall for this skill: "
        f"{wins} wins / {losses} losses / {ties} ties (loaded-only) over {wins + losses + ties} tasks.",
        "",
        "</details>",
    ]
    return lines


def pick_rule(entries):
    rules = {e.meta.get("pick_rule") for e in entries}
    if len(rules) != 1 or None in rules:
        raise ValueError("every meta.json must carry the same pick_rule")
    return rules.pop().rstrip(".").removeprefix("Chosen ")


def render(root):
    entries = load(root)
    rule = pick_rule(entries)
    lines = [
        f"Each panel below opens to one task from a skill's held-out run: the answer without the skill beside the "
        f"answer with it. Each task shown was chosen {rule}, so these are favorable examples by construction. "
        "The answers shown are the first of the three samples in which the skill loaded, not the best one. Text "
        f"answers are shortened but never rewritten (a cut is marked `{CUT}`), and `scripts/before_after_gallery.py` "
        "checks every excerpt against the stored answer. The tally in each heading is the skill's wins / losses / "
        "ties over the tasks where it loaded, and `marginal` marks a pass the [Results](#results) section calls "
        "marginal. The full run files are in `evals/<skill>/heldout/runs/`. For the unselected, real-request examples "
        "see [Showcase](#showcase).",
    ]
    for kind, title in KINDS:
        lines += ["", f"### {title}", ""]
        panels = [panel(e) for e in entries if e.meta["kind"] == kind]
        for n, p in enumerate(panels):
            lines += ([""] if n else []) + p
    return lines


def sample_phrase(winners, side):
    """`3 of 3 samples` style count of the samples a side won."""
    return f"{winners.count(side)} of {len(winners)} samples"


def featured_lines(root):
    """The featured skill's task in full: prompt, both answers side by side, and the judge result under them."""
    entries = load(root)
    featured = [e for e in entries if e.meta.get("featured")]
    if len(featured) != 1:
        raise ValueError(f"exactly one meta.json must set featured to true, found {len(featured)}")
    entry = featured[0]
    skill, results = entry.skill, entry.results
    wins, losses, ties = entry.tally
    verdict = next(v for v in results["verdicts"] if v["task_id"] == entry.meta["task_id"])
    winners = [s["winner"] for s in verdict.get("samples") or [verdict]]
    side = verdict["winner"]
    judge = results["summary"]["judge"]
    other = "a different model from the one that wrote the answers" if not results["summary"].get("same_model_judge") \
        else "the same model as the one that wrote the answers"
    outcome = {"with": "The answer with the skill won this task",
               "without": "The answer without the skill won this task",
               "tie": "This task was a tie"}[side]
    count = "" if side == "tie" else f", {sample_phrase(winners, side)}"
    lines = [f"The same request, given to the same model with and without the `{skill}` skill installed:", "",
             blockquote(entry.meta["prompt"]), "", "| Without the skill | With the skill |", "|---|---|"]
    shots = entry.shot_row()
    if shots:
        lines.append(shots)
    lines += [
        f"| {cell(entry.text('without'))} | {cell(entry.text('with'))} |",
        "",
        f"**Judge result.** {outcome}{count}, by {entry.gap:+.2f} rubric points on the 5-point scale. "
        f"The judge was `{judge}`, {other}; it saw the two answers "
        "unlabelled, in both orders. Over all of this skill's held-out tasks where it loaded, the skill won "
        f"{wins}, lost {losses} and tied {ties}. {sample_note(entry)} "
        f"[Full run files]({entry.run.as_posix()}/).",
        "",
        "This is one example, not a typical one: it is the task with the biggest judged gap in the skill's favor "
        f"among the tasks where the skill loaded. Examples for {len(entries) - 1} other skills are in "
        "[More before and after examples](#more-before-and-after-examples).",
    ]
    return lines


def alt_lines(root):
    """ALT.md rows for every gallery screenshot: its path and the alt text the README gives it."""
    rows = ["| File | Alt text |", "|---|---|"]
    for entry in load(root):
        for shot in sorted(entry.meta.get("images", []), key=lambda i: SIDES.index(i["side"])):
            path = (GALLERY / entry.skill / shot["file"]).as_posix()
            rows.append(f"| `{path}` ({shot['side']} the skill) | {results_table.cell(' '.join(shot['alt'].split()))} |")
    return rows


def update(text, lines, start=START, end=END, where="README.md"):
    i, j = text.find(start), text.find(end)
    if i < 0 or j < i:
        raise ValueError(f"{where} is missing the {start} ... {end} markers")
    return text[:i + len(start)] + "\n" + "\n".join(lines) + "\n" + text[j:]


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--check", action="store_true", help="exit 1 if README.md differs from the generated gallery")
    args = p.parse_args(argv)
    readme, alt_md = Path(args.root) / "README.md", Path(args.root) / ALT
    try:
        current, current_alt = readme.read_text(encoding="utf-8"), alt_md.read_text(encoding="utf-8")
        new = update(update(current, render(args.root)), featured_lines(args.root), FEATURED_START, FEATURED_END)
        new_alt = update(current_alt, alt_lines(args.root), ALT_START, ALT_END, ALT.as_posix())
    except (OSError, ValueError, KeyError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    stale = [(path, text) for path, text, old in ((readme, new, current), (alt_md, new_alt, current_alt)) if text != old]
    if not stale:
        print("README.md before-and-after gallery and its ALT.md rows are up to date")
        return 0
    if args.check:
        names = " and ".join(path.name for path, _ in stale)
        print(f"before-and-after gallery is out of date in {names}; run: python3 scripts/before_after_gallery.py")
        return 1
    for path, text in stale:
        path.write_text(text, encoding="utf-8")
        print(f"{path.name}: before-and-after gallery updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
