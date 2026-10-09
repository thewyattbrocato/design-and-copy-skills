#!/usr/bin/env python3
"""Generate the before-and-after gallery in README.md from docs/before-after/*/meta.json.

Each skill folder holds meta.json (the task, the tally, the judged difference, the picking rule), without.md and with.md
(shortened excerpts of the two stored answers) and, for some skills, screenshots. The gallery is rewritten between

  <!-- before-after:start --> ... <!-- before-after:end -->

as one collapsible panel per skill, design skills first and copywriting skills second. Excerpt text is escaped so it
renders as plain text, with newlines as <br> inside table cells. With --check nothing is written; the exit code is 1
when the README does not match the files (CI uses this).
"""
import argparse
import json
import re
import sys
from pathlib import Path

START, END = "<!-- before-after:start -->", "<!-- before-after:end -->"
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


def update(text, lines):
    i, j = text.find(START), text.find(END)
    if i < 0 or j < i:
        raise ValueError(f"README.md is missing the {START} ... {END} markers")
    return text[:i + len(START)] + "\n" + "\n".join(lines) + "\n" + text[j:]


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--check", action="store_true", help="exit 1 if README.md differs from the generated gallery")
    args = p.parse_args(argv)
    readme = Path(args.root) / "README.md"
    try:
        current = readme.read_text(encoding="utf-8")
        new = update(current, render(args.root))
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
