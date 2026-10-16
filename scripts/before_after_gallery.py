#!/usr/bin/env python3
"""Generate the before-and-after gallery in README.md from docs/before-after/*/meta.json.

Each skill folder holds meta.json (the task, the tally, the judged difference, the picking rule), without.md and with.md
(shortened excerpts of the two stored answers) and, for some skills, screenshots. The gallery is rewritten between

  <!-- before-after:start --> ... <!-- before-after:end -->

as one collapsible panel per skill, design skills first and copywriting skills second. A second block,

  <!-- before-after:featured:start --> ... <!-- before-after:featured:end -->

shows the one skill whose meta.json says `"featured": true` in full near the top of the README: the prompt, the two
answers side by side and the judge result read from that skill's held-out results.json. Excerpt text is escaped so it
renders as plain text, with newlines as <br> inside table cells. With --check nothing is written; the exit code is 1
when the README does not match the files (CI uses this).
"""
import argparse
import json
import re
import sys
from pathlib import Path

START, END = "<!-- before-after:start -->", "<!-- before-after:end -->"
FEATURED_START, FEATURED_END = "<!-- before-after:featured:start -->", "<!-- before-after:featured:end -->"
GALLERY = Path("docs") / "before-after"
KINDS = (("design", "Design skills"), ("copy", "Copywriting skills"))
TALLY = re.compile(r"^(\d+) / (\d+) / (\d+)$")

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


def load(root):
    """[(folder name, meta)] for every docs/before-after/*/meta.json, sorted by skill name."""
    metas = []
    for path in sorted((Path(root) / GALLERY).glob("*/meta.json")):
        meta = json.loads(path.read_text(encoding="utf-8"))
        if meta.get("skill") != path.parent.name:
            raise ValueError(f"{path}: skill is {meta.get('skill')!r}, expected {path.parent.name!r}")
        if meta.get("kind") not in dict(KINDS) or not TALLY.match(str(meta.get("loaded_only", ""))):
            raise ValueError(f"{path}: needs kind design|copy and loaded_only like '5 / 2 / 3'")
        metas.append((path.parent, meta))
    return metas


def tally(meta):
    wins, losses, ties = map(int, TALLY.match(meta["loaded_only"]).groups())
    return wins, losses, ties


def panel(root, folder, meta):
    skill = meta["skill"]
    wins, losses, ties = tally(meta)
    run = Path("evals") / skill / "heldout" / "runs" / meta["task_id"]
    if not (Path(root) / run).is_dir():
        raise ValueError(f"{folder / 'meta.json'}: the run folder {run} does not exist")
    rel = GALLERY / skill
    without = (folder / meta["without_file"]).read_text(encoding="utf-8")
    with_ = (folder / meta["with_file"]).read_text(encoding="utf-8")
    marginal = " &middot; marginal" if meta.get("marginal") else ""
    lines = [
        "<details>",
        f"<summary><b>{skill}</b> &middot; {wins} / {losses} / {ties} loaded only{marginal}</summary>",
        "",
        blockquote(meta["prompt"]),
        "",
        "| Without the skill | With the skill |",
        "|---|---|",
        f"| {cell(without)} | {cell(with_)} |",
    ]
    shots = {i["side"]: i for i in meta.get("images", [])}
    if shots:
        def shot(side):
            i = shots.get(side)
            return f"![{alt(i['alt'])}]({(rel / i['file']).as_posix()})" if i else ""
        lines.append(f"| {shot('without')} | {shot('with')} |")
    lines += [
        "",
        f"[Full run files]({run.as_posix()}/)",
        "",
        f"Judged difference on this task: {float(meta['judge_gap']):+.2f} rubric points. Overall for this skill: "
        f"{wins} wins / {losses} losses / {ties} ties (loaded-only) over {wins + losses + ties} tasks.",
        "",
        "</details>",
    ]
    return lines


def render(root):
    metas = load(root)
    rules = {m["pick_rule"] for _, m in metas}
    if len(rules) != 1:
        raise ValueError("every meta.json must carry the same pick_rule")
    rule = rules.pop().rstrip(".").removeprefix("Chosen ")
    lines = [
        f"Each panel below opens to one task from a skill's held-out run: the answer without the skill beside the "
        f"answer with it, shortened but never rewritten (a cut is marked `[...]`). Each task shown was chosen {rule}, "
        "so these are favorable examples by construction. The tally in each heading is the skill's wins / losses / ties over the tasks "
        "where it loaded, and `marginal` marks a pass the [Results](#results) section calls marginal. The full run "
        "files are in `evals/<skill>/heldout/runs/`. For the unselected, real-request examples see "
        "[Showcase](#showcase).",
    ]
    for kind, title in KINDS:
        lines += ["", f"### {title}", ""]
        panels = [panel(root, folder, meta) for folder, meta in metas if meta["kind"] == kind]
        for n, p in enumerate(panels):
            lines += ([""] if n else []) + p
    return lines


def sample_phrase(winners, side):
    """`3 of 3 samples` style count of the samples a side won."""
    return f"{winners.count(side)} of {len(winners)} samples"


def featured_lines(root):
    """The featured skill's task in full: prompt, both answers side by side, and the judge result under them."""
    metas = [(f, m) for f, m in load(root) if m.get("featured")]
    if len(metas) != 1:
        raise ValueError(f"exactly one meta.json must set featured to true, found {len(metas)}")
    folder, meta = metas[0]
    skill = meta["skill"]
    wins, losses, ties = tally(meta)
    results = json.loads((Path(root) / "evals" / skill / "heldout" / "results.json").read_text(encoding="utf-8"))
    verdict = next((v for v in results["verdicts"] if v["task_id"] == meta["task_id"]), None)
    if verdict is None:
        raise ValueError(f"{skill}: held-out results.json has no verdict for {meta['task_id']}")
    winners = [s["winner"] for s in verdict["samples"]]
    side = verdict["winner"]
    judge = results["summary"]["judge"]
    other = "a different model from the one that wrote the answers" if not results["summary"].get("same_model_judge") \
        else "the same model as the one that wrote the answers"
    outcome = {"with": "The answer with the skill won this task",
               "without": "The answer without the skill won this task",
               "tie": "This task was a tie"}[side]
    count = "" if side == "tie" else f", {sample_phrase(winners, side)}"
    rel = GALLERY / skill
    shots = {i["side"]: i for i in meta.get("images", [])}
    lines = [f"The same request, given to the same model with and without the `{skill}` skill installed:", "",
             blockquote(meta["prompt"]), "", "| Without the skill | With the skill |", "|---|---|"]
    if shots:
        lines.append("| " + " | ".join(f"![{alt(shots[k]['alt'])}]({(rel / shots[k]['file']).as_posix()})"
                                       for k in ("without", "with")) + " |")
    lines += [
        f"| {cell((folder / meta['without_file']).read_text(encoding='utf-8'))} | "
        f"{cell((folder / meta['with_file']).read_text(encoding='utf-8'))} |",
        "",
        f"**Judge result.** {outcome}{count}, by {float(meta['judge_gap']):+.2f} rubric points on the 5-point scale. "
        f"The judge was `{judge}`, {other}; it saw the two answers "
        "unlabelled, in both orders. Over all of this skill's held-out tasks where it loaded, the skill won "
        f"{wins}, lost {losses} and tied {ties}. [Full run files](evals/{skill}/heldout/runs/{meta['task_id']}/).",
        "",
        "This is one example, not a typical one: it is the task with the biggest judged gap in the skill's favor "
        f"among the tasks where the skill loaded. Examples for {len(load(root)) - 1} other skills are in "
        "[More before and after examples](#more-before-and-after-examples).",
    ]
    return lines


def update(text, lines, start=START, end=END):
    i, j = text.find(start), text.find(end)
    if i < 0 or j < i:
        raise ValueError(f"README.md is missing the {start} ... {end} markers")
    return text[:i + len(start)] + "\n" + "\n".join(lines) + "\n" + text[j:]


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--check", action="store_true", help="exit 1 if README.md differs from the generated gallery")
    args = p.parse_args(argv)
    readme = Path(args.root) / "README.md"
    try:
        current = readme.read_text(encoding="utf-8")
        new = update(update(current, render(args.root)), featured_lines(args.root), FEATURED_START, FEATURED_END)
    except (OSError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if new == current:
        print("README.md before-and-after gallery is up to date")
        return 0
    if args.check:
        print("README.md before-and-after gallery is out of date; run: python3 scripts/before_after_gallery.py")
        return 1
    readme.write_text(new, encoding="utf-8")
    print("README.md before-and-after gallery updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
