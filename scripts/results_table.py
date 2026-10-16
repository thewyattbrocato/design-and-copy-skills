#!/usr/bin/env python3
"""Generate the skills and results tables in README.md from the files they describe.

Reads skills/*/SKILL.md, copy-skills/*/SKILL.md, withdrawn/*/SKILL.md, evals/*/heldout/results.json (clean evidence) and evals/*/results.json (the dev set,
which the skill writers saw), evals/*/activation.json and evals/*/activation-results.json, and rewrites eight blocks of
README.md between marker comments:

  <!-- results-table:headline:start --> ... <!-- results-table:headline:end -->
  <!-- results-table:tryit:start --> ... <!-- results-table:tryit:end -->
  <!-- results-table:skills:start --> ... <!-- results-table:skills:end -->
  <!-- results-table:copy:start --> ... <!-- results-table:copy:end -->
  <!-- results-table:heldout:start --> ... <!-- results-table:heldout:end -->
  <!-- results-table:marginal:start --> ... <!-- results-table:marginal:end -->
  <!-- results-table:dev:start --> ... <!-- results-table:dev:end -->
  <!-- results-table:withdrawn:start --> ... <!-- results-table:withdrawn:end -->

Each results row shows its protocol (1: one answer per arm, 2: samples and a loaded-only gate), samples, the all-samples
and loaded-only tallies, the gate decision and the secondary row (a weaker generator, never gated). Skills under copy-skills/ are listed in the copy block ("none yet" while the folder is empty) and, like skills/, in the
results tables. Skills and evidence-only folders under withdrawn/ appear only in the withdrawn block (the README calls it
archived evidence; a held-out results.json at the folder root counts). Held-out rows of a passing skill carry a `marginal` marker
when the mean rubric advantage is below +0.15, fewer than 7 tasks had a loaded sample, or the loaded-only win margin is at most
one task. The headline block sums the loaded-only tallies of the listed skills and counts the marginal passes; the marginal block
lists them in plain words; the tryit block prints five example requests taken word for word from activation.json, each
checked against activation-results.json to have been routed to the right skill. Protocol 1 loaded-only tallies are recomputed from `with_skill_invoked`. A skill with no held-out results is shown as "pending clean rerun". With --check nothing is written; the exit
code is 1 when the README does not match the files (CI uses this).
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalkit  # noqa: E402
import validate_evals  # noqa: E402
import validate_skills  # noqa: E402
from roots import LIVE_ROOTS, find_skill  # noqa: E402

BLOCKS = ("headline", "tryit", "skills", "copy", "heldout", "marginal", "dev", "withdrawn")
NONE_YET = "none yet"
# One example request per skill for the README "Try it" list: (skill, index into should_load of its activation.json).
TRY_IT = (("visual-hierarchy", 0), ("chart-design", 1), ("form-design", 0), ("email-and-sequences", 2),
          ("honest-claims", 2))
PENDING = "pending clean rerun"


def marker(block, edge):
    return f"<!-- results-table:{block}:{edge} -->"


def cell(text):
    return " ".join(str(text).split()).replace("|", "\\|")


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


NOT_FOR = re.compile(r"(?<=[.;:])\s+not for\s", re.IGNORECASE)


def split_description(desc):
    """(use-when text, not-for text). The not-for part starts at the first `Not for`, `; not for` or `: not for`."""
    m = NOT_FOR.search(desc)
    return (desc[:m.start()], desc[m.end():]) if m else (desc, "")


def skill_rows(root, folder="skills"):
    """[(name, applies_when, not_for)] for every skill folder under `folder`, sorted by name."""
    rows = []
    for d in sorted((Path(root) / folder).glob("*/")):
        md = d / "SKILL.md"
        if not md.is_file():
            continue
        fields, _ = validate_skills.parse_frontmatter(md.read_text(encoding="utf-8"))
        desc = validate_skills.unquote((fields or {}).get("description", "")).strip()
        main, rest = split_description(desc)
        first = re.split(r"(?<=[.!?])\s", main, maxsplit=1)[0]
        clause = re.split(r": | - ", first, maxsplit=1)[0].strip().rstrip(".;:, ")
        clause = re.sub(r"^Use (?:when|whenever)\s+", "", clause)
        rows.append((d.name, clause, rest.strip().rstrip(".")))
    return rows


def skills_table(root):
    lines = ["| Skill | Use when | Not for |", "|---|---|---|"]
    for name, when, not_for in skill_rows(root):
        lines.append(f"| [{name}](skills/{name}/SKILL.md) | {cell(when)} | {cell(not_for)} |")
    return lines


def copy_table(root):
    rows = skill_rows(root, "copy-skills")
    if not rows:
        return [NONE_YET]
    lines = ["| Skill | Use when | Not for |", "|---|---|---|"]
    for name, when, not_for in rows:
        lines.append(f"| [{name}](copy-skills/{name}/SKILL.md) | {cell(when)} | {cell(not_for)} |")
    return lines


def live_rows(root):
    """Rows for every listed skill: skills/ then copy-skills/. Used by the results tables."""
    return [row for folder in LIVE_ROOTS for row in skill_rows(root, folder)]


RESULT_HEAD = ["Protocol", "Samples per arm", "Wins / losses / ties, all samples",
               "Wins / losses / ties, loaded only", "Mean rubric, with / without (loaded only under protocol 2)",
               "Skill loaded by the model", "Gate", "Judge", "Secondary row (weaker generator, not gated)"]
NOT_RECORDED = "not recorded"


def loaded_text(results):
    """`N of M samples (K of T tasks)`: samples that loaded the skill, and tasks with at least one such sample."""
    summary = results.get("summary", {})
    loaded = summary.get("loaded")
    verdicts = results.get("verdicts", [])
    if summary.get("protocol") == 2 and isinstance(loaded, dict):
        return (f"{loaded['loaded_samples']} of {loaded['total_samples']} samples "
                f"({loaded['tasks_with_loaded_sample']} of {len(verdicts)} tasks)")
    flags = [v["with_skill_invoked"] for v in verdicts if isinstance(v.get("with_skill_invoked"), bool)]
    return f"{sum(flags)} of {len(flags)} samples ({sum(flags)} of {len(flags)} tasks)" if flags else NOT_RECORDED


def loaded_tally(results):
    """Loaded-only tally of a protocol 1 file, recomputed from `with_skill_invoked`; None when it was not recorded."""
    pairs = [(v.get("winner"), v["with_skill_invoked"]) for v in results.get("verdicts", [])
             if isinstance(v.get("with_skill_invoked"), bool)]
    if not pairs:
        return None
    winners = [w for w, invoked in pairs if invoked]
    return {"with_wins": winners.count("with"), "without_wins": winners.count("without"),
            "ties": winners.count("tie"), "tasks_with_loaded_sample": len(winners)}


MARGINAL_ADVANTAGE = 0.15
MARGINAL_TASKS = 7


def loaded_outcome(results):
    """(loaded-only tally, mean rubric with, mean rubric without) of a result, or None when it recorded none.
    Rubric means are loaded-only under protocol 2 and cover every pair under protocol 1 (those files do not record
    loaded-only means); the tally is loaded-only under both."""
    s = results["summary"]
    g = s.get("gate", {})
    if s.get("protocol", 1) == 2 and isinstance(s.get("loaded"), dict):
        tally = s["loaded"]
        if not tally["tasks_with_loaded_sample"]:
            return None
        return tally, tally["mean_rubric_with"], tally["mean_rubric_without"]
    tally = loaded_tally(results)
    if tally is None or "mean_rubric_with" not in g:
        return None
    return tally, g["mean_rubric_with"], g["mean_rubric_without"]


def marginal_checks(results):
    """[(short reason, plain-words reason)] why a passing result is marginal: a mean rubric advantage below +0.15,
    fewer than 7 tasks with a loaded sample, or a win margin of at most one task (see loaded_outcome for what the
    means and the tally cover). Empty for a result that did not pass or is not marginal."""
    s = results["summary"]
    g = s.get("gate", {})
    protocol2 = s.get("protocol", 1) == 2 and isinstance(s.get("loaded"), dict)
    passed = g.get("decision") == "pass" if protocol2 else bool(g.get("passed"))
    outcome = loaded_outcome(results)
    if not passed or outcome is None:
        return []
    tally, mean_with, mean_without = outcome
    checks = []
    advantage = round(mean_with - mean_without, 3)
    if advantage < MARGINAL_ADVANTAGE:
        level = abs(advantage) < 0.005
        checks.append(("rubric level" if level else f"rubric {advantage:+.2f}",
                       "its mean rubric score was level with the baseline" if level
                       else f"its mean rubric edge was {advantage:+.2f}, under the +{MARGINAL_ADVANTAGE:.2f} bar"))
    loaded = tally["tasks_with_loaded_sample"]
    if loaded < MARGINAL_TASKS:
        checks.append((f"{loaded} loaded tasks",
                       f"the model loaded it on only {loaded} of {len(results.get('verdicts', []))} tasks"))
    margin = tally["with_wins"] - tally["without_wins"]
    if margin <= 1:
        checks.append(("one-task win margin" if margin == 1 else "no win margin",
                       "it won just one more task than it lost" if margin == 1
                       else "it won no more tasks than it lost"))
    return checks


def marginal_reasons(results):
    """Why a passing result is marginal, in the short words of the Gate column."""
    return [short for short, _ in marginal_checks(results)]


def judge_text(summary):
    judge = summary.get("judge", NOT_RECORDED)
    model = summary.get("model_id") or summary.get("model", "")
    same = summary.get("same_model_judge")
    if same is None and isinstance(judge, str) and model:
        same = evalkit.same_model_judge(judge, model)
    if same:
        return f"`{judge}`, same model as the generator"
    return f"`{judge}`, a different model from the generator" if isinstance(judge, str) and judge != NOT_RECORDED \
        else cell(judge)


def wlt(t):
    return f"{t['with_wins']} / {t['without_wins']} / {t['ties']}"


def secondary_text(results):
    sec = results.get("secondary")
    if not (isinstance(sec, dict) and isinstance(sec.get("summary"), dict)):
        return "none"
    s = sec["summary"]
    loaded = s.get("loaded", {})
    return f"`{s.get('model', '?')}`: {wlt(loaded)} loaded only" if loaded.get("tasks_with_loaded_sample") \
        else f"`{s.get('model', '?')}`: {wlt(s)}, no loaded samples"


def result_cells(results, mark_marginal=False):
    s = results["summary"]
    g = s.get("gate", {})
    protocol = s.get("protocol", 1)
    if protocol == 2 and isinstance(s.get("loaded"), dict):
        loaded = s["loaded"]
        gate = g.get("decision", NOT_RECORDED)
        means = (f"{loaded['mean_rubric_with']} / {loaded['mean_rubric_without']}"
                 if loaded["tasks_with_loaded_sample"] else "no loaded samples")
        loaded_only = f"{wlt(loaded)} ({loaded['tasks_with_loaded_sample']} tasks)"
    else:
        gate = ("pass" if g.get("passed") else "fail") if g else NOT_RECORDED
        means = f"{g['mean_rubric_with']} / {g['mean_rubric_without']}" if g else NOT_RECORDED
        tally = loaded_tally(results)
        loaded_only = f"{wlt(tally)} ({tally['tasks_with_loaded_sample']} tasks)" if tally else "n/a"
    reasons = marginal_reasons(results) if mark_marginal else []
    if reasons:
        gate = f"{gate}, marginal ({'; '.join(reasons)})"
    return [str(protocol), str(s.get("samples", 1)), wlt(s), loaded_only, means, loaded_text(results), gate,
            judge_text(s), secondary_text(results)]


def pending_row(name, label=PENDING, extra=0):
    return f"| {name} | {label} |" + " |" * (len(RESULT_HEAD) - 1 + extra)


def table_head(*extra):
    cols = ["Skill", *RESULT_HEAD, *extra]
    return ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]


def heldout_table(root):
    lines = table_head()
    for name, _, _ in live_rows(root):
        results = load_json(Path(root) / "evals" / name / "heldout" / "results.json")
        if isinstance(results, dict) and isinstance(results.get("summary"), dict):
            lines.append(f"| {name} | " + " | ".join(result_cells(results, mark_marginal=True)) + " |")
        else:
            lines.append(pending_row(name))
    return lines


def missing_answers(evals_dir):
    task_ids = [t.get("id") for t in (load_json(evals_dir / "tasks.json") or []) if isinstance(t, dict)]
    return len(validate_evals.validate_runs(evals_dir, task_ids, None, strict=False))


def dev_table(root):
    lines = table_head("Notes")
    for name, _, _ in live_rows(root):
        evals_dir = Path(root) / "evals" / name
        results = load_json(evals_dir / "results.json")
        if not (isinstance(results, dict) and isinstance(results.get("summary"), dict)):
            lines.append(pending_row(name, "no development results", extra=1))
            continue
        has_heldout = (evals_dir / "heldout" / "results.json").is_file()
        notes = ["superseded by the held-out run" if has_heldout else "superseded, held-out rerun pending"]
        missing = missing_answers(evals_dir)
        if missing:
            notes.append(f"{missing} answer files not committed")
        lines.append(f"| {name} | " + " | ".join(result_cells(results)) + f" | {'; '.join(notes)} |")
    return lines


def evidence_results(folder):
    """Results of an evidence-only folder: heldout/results.json, else a results.json at the folder root that is a
    held-out run. A root results.json from the dev suite is never used."""
    results = load_json(folder / "heldout" / "results.json")
    if not (isinstance(results, dict) and isinstance(results.get("summary"), dict)):
        results = load_json(folder / "results.json")
        if not (isinstance(results, dict) and isinstance(results.get("summary"), dict)
                and results["summary"].get("suite") == "heldout"):
            return None
    return results


def withdrawn_table(root):
    lines = table_head()
    for name, _, _ in skill_rows(root, "withdrawn"):
        results = load_json(Path(root) / "evals" / name / "heldout" / "results.json")
        if isinstance(results, dict) and isinstance(results.get("summary"), dict):
            lines.append(f"| [{name}](withdrawn/{name}/SKILL.md) | " + " | ".join(result_cells(results)) + " |")
        else:
            lines.append(pending_row(f"[{name}](withdrawn/{name}/SKILL.md)", "no held-out results"))
    base = Path(root) / "withdrawn"
    for d in sorted(p for p in base.iterdir() if p.is_dir() and not (p / "SKILL.md").is_file()) if base.is_dir() else []:
        results = evidence_results(d)
        if results:
            lines.append(f"| {d.name} | " + " | ".join(result_cells(results)) + " |")
    return lines


def heldout_results(root):
    """[(name, results)] for every listed skill that has held-out results, in table order."""
    found = []
    for name, _, _ in live_rows(root):
        results = load_json(Path(root) / "evals" / name / "heldout" / "results.json")
        if isinstance(results, dict) and isinstance(results.get("summary"), dict):
            found.append((name, results))
    return found


def headline_lines(root):
    """One line: the loaded-only wins, losses and ties summed over the listed skills, and how many passes are marginal."""
    wins = losses = ties = skills = marginal = 0
    for _, results in heldout_results(root):
        outcome = loaded_outcome(results)
        if outcome is None:
            continue
        tally = outcome[0]
        skills += 1
        wins, losses, ties = wins + tally["with_wins"], losses + tally["without_wins"], ties + tally["ties"]
        marginal += bool(marginal_reasons(results))
    if not skills:
        return [NONE_YET]
    return [f"**Across {skills} skills, counting only the held-out tasks where the skill loaded ({wins + losses + ties} in all): "
            f"{wins} wins, {losses} losses and {ties} ties against the same model without it. {marginal} of the {skills} "
            "passes are marginal.**"]


def marginal_lines(root):
    """A bullet per marginal pass, with the reasons in plain words."""
    lines = []
    for name, results in heldout_results(root):
        checks = marginal_checks(results)
        if checks:
            reasons = "; ".join(plain for _, plain in checks)
            lines.append(f"- **{name}**: {reasons[0].upper()}{reasons[1:]}.")
    return lines or [NONE_YET]


def tryit_lines(root):
    """A table of the TRY_IT requests, each word for word from activation.json and routed correctly in activation-results.json."""
    lines = ["| Type this | The agent should load |", "|---|---|"]
    for name, index in TRY_IT:
        folder = Path(root) / "evals" / name
        requests = (load_json(folder / "activation.json") or {}).get("should_load", [])
        recorded = (load_json(folder / "activation-results.json") or {}).get("should_load", {}).get("results", [])
        if not 0 <= index < len(requests):
            raise ValueError(f"evals/{name}/activation.json has no should_load request {index}")
        prompt = requests[index]
        if not any(r.get("prompt") == prompt and r.get("correct") is True and r.get("picked") == name
                   for r in recorded):
            raise ValueError(f"evals/{name}/activation-results.json does not show {prompt!r} routed to {name}")
        found = find_skill(root, name)
        if found is None:
            raise ValueError(f"{name} is not a listed skill")
        lines.append(f"| \u201c{cell(prompt)}\u201d | [{name}]({found[0]}/{name}/SKILL.md) |")
    return lines


def render(root):
    return {"headline": headline_lines(root), "tryit": tryit_lines(root), "skills": skills_table(root),
            "copy": copy_table(root), "heldout": heldout_table(root), "marginal": marginal_lines(root),
            "dev": dev_table(root), "withdrawn": withdrawn_table(root)}


def replace_block(text, block, lines):
    start, end = marker(block, "start"), marker(block, "end")
    i, j = text.find(start), text.find(end)
    if i < 0 or j < i:
        raise ValueError(f"README.md is missing the {start} ... {end} markers")
    return text[:i + len(start)] + "\n" + "\n".join(lines) + "\n" + text[j:]


def update(text, blocks):
    for name in BLOCKS:
        text = replace_block(text, name, blocks[name])
    return text


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--check", action="store_true", help="exit 1 if README.md differs from the generated tables")
    args = p.parse_args(argv)
    readme = Path(args.root) / "README.md"
    try:
        current = readme.read_text(encoding="utf-8")
        new = update(current, render(args.root))
    except (OSError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if new == current:
        print("README.md tables are up to date")
        return 0
    if args.check:
        print("README.md tables are out of date; run: python3 scripts/results_table.py")
        return 1
    readme.write_text(new, encoding="utf-8")
    print("README.md tables updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
