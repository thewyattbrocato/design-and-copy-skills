#!/usr/bin/env python3
"""Run the activation check: does a model pick each skill from its name and description alone?

For every skill under skills/ and copy-skills/ this reads evals/<skill>/activation.json (6 `should_load` requests and
4 `should_not_load` requests) and puts each request to a model once, together with the name and description of ALL
skills and nothing else (no skill body is shown). The model says which single skill, if any, it would load. Per skill
it records recall on `should_load` (the skill was the pick), the false-pick rate on `should_not_load` (the skill was
picked when it should not be) and, for every request, which skill was picked instead. The result is written to
evals/<skill>/activation-results.json (format in evals/SCHEMA.md). Default model: haiku. The call goes through the same
mechanism as the eval runner's generator, so EVAL_GENERATOR_CMD replaces it with a stub in tests. This checks routing
from descriptions only; whether the model then loads a skill in a real task is measured by the held-out runs.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import activation as act  # noqa: E402
import evalkit as ek  # noqa: E402
import validate_evals  # noqa: E402

RESULTS = "activation-results.json"
REQUEST_ATTEMPTS = 3


def ask(rows, request, model, effort, timeout, task_id):
    """One model call for one request: the picked skill name or None. A reply that names no listed skill (or two) is
    asked again, up to three times; if it still does, nothing valid was picked and the request counts as no pick."""
    prompt = act.router_prompt(rows, request)
    names = [n for n, _ in rows]
    for _ in range(REQUEST_ATTEMPTS):
        reply, meta = ek.generate(prompt, "activation", None, None, False, "injected", model, effort, timeout, task_id)
        try:
            return act.parse_pick(reply, names), meta
        except ValueError:
            continue
    return None, meta


def load_activation(root, skill):
    path = Path(root) / "evals" / skill / "activation.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise ek.EvalError(f"cannot read {path}: {e}")
    errors = validate_evals.validate_activation(data, skill)
    if errors:
        raise ek.EvalError(f"invalid {path.name} for {skill}:\n  " + "\n  ".join(errors))
    return data


def run(args):
    root = Path(args.root)
    rows = act.catalog(root)
    known = [n for n, _ in rows]
    wanted = [s for s in args.skills.split(",") if s] if args.skills else known
    unknown = sorted(set(wanted) - set(known))
    if unknown:
        raise ek.EvalError(f"unknown skills: {unknown}")
    suites = {s: load_activation(root, s) for s in wanted}
    jobs = [(s, key, i, text) for s in wanted for key in ("should_load", "should_not_load")
            for i, text in enumerate(suites[s][key])]
    if args.dry_run:
        print(f"model={args.model} catalog={len(rows)} skills ({act.catalog_hash(rows)}) skills_to_run={len(wanted)} "
              f"requests={len(jobs)}")
        print("dry run: nothing asked")
        return 0

    def work(job):
        skill, key, i, text = job
        try:
            pick, meta = ask(rows, text, args.model, args.effort, args.timeout, f"{skill}/{key}/{i + 1}")
        except ek.EvalError as e:
            return f"{skill}/{key}/{i + 1}: {e}", None, None
        return None, pick, meta.get("model_id")

    outcomes = ek.pmap(work, jobs, args.concurrency)
    errors = [e for e, _, _ in outcomes if e]
    picks = {(job[0], job[1], job[2]): pick for job, (_, pick, _) in zip(jobs, outcomes)}
    model_ids = sorted({m for _, _, m in outcomes if m})
    today = datetime.date.today().isoformat()
    written, failed = [], sorted({e.split("/")[0] for e in errors})
    for s in wanted:
        if s in failed:
            continue
        lists = {key: suites[s][key] for key in ("should_load", "should_not_load")}
        got = {key: [picks[(s, key, i)] for i in range(len(lists[key]))] for key in lists}
        data = {"skill": s, "model": args.model, **({"model_id": model_ids[0]} if len(model_ids) == 1 else {}),
                "date": today, "catalog_size": len(rows), "catalog_hash": act.catalog_hash(rows),
                "should_load": act.load_section(s, lists["should_load"], got["should_load"]),
                "should_not_load": act.not_load_section(s, lists["should_not_load"], got["should_not_load"])}
        out = root / "evals" / s / RESULTS
        out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        written.append(s)
        flag = act.flagged(data)
        print(f"{s}: recall {data['should_load']['picked']}/{data['should_load']['total']}, false picks "
              f"{data['should_not_load']['false_picks']}/{data['should_not_load']['total']}"
              + (f"  [{'; '.join(flag)}]" if flag else ""))
    print(f"wrote {len(written)} {RESULTS} files")
    if errors:
        print("\n".join(f"error: {e}" for e in errors), file=sys.stderr)
        return 2
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--skills", help="comma-separated skill names (default: every skill under skills/ and copy-skills/)")
    p.add_argument("--model", default="haiku", help="model asked to pick (default %(default)s, the weaker model)")
    p.add_argument("--concurrency", type=int, default=6)
    p.add_argument("--effort", help="effort level passed to claude (default: CLI default)")
    p.add_argument("--timeout", type=int, default=300)
    p.add_argument("--dry-run", action="store_true", help="list what would be asked and call nothing")
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = p.parse_args(argv)
    try:
        return run(args)
    except ek.EvalError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
