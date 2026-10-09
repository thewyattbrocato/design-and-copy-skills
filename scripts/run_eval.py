#!/usr/bin/env python3
"""Run a skill's eval (protocol 2): N answers per arm per task, blind pairwise judging, ship gate.

Every task gets --samples answers WITHOUT and WITH the skill. Sample i of one arm is judged blind against sample i
of the other (sides swapped, as before) and a task's verdict is the majority over its samples. A WITH sample where
the model did not load the skill is regenerated up to twice, and flagged not_loaded if it still did not load. The
gate is decided on the loaded-only tally. Reads the suite's tasks.json, caches generated answers and judgments
under its runs/ folder (a rerun only does the missing work) and writes its results.json. The dev suite is
evals/<skill>/; the held-out suite is evals/<skill>/heldout/ and is the default when it exists. The judge must not
be the generator model. --secondary-model runs the same suite with a weaker generator as a reported extra row.
See evals/README.md.
"""
import argparse
import datetime
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalkit as ek  # noqa: E402
import validate_evals  # noqa: E402
from roots import LIVE_ROOTS, find_skill  # noqa: E402

ARMS = ("without", "with")
SECONDARY = "secondary"


def load_tasks(path, allow_small, copy_heldout=False):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise ek.EvalError(f"cannot read {path}: {e}")
    errors, _ = validate_evals.validate_tasks(data, protocol=ek.PROTOCOL, copy_heldout=copy_heldout)
    if allow_small:
        errors = [e for e in errors if f"need {validate_evals.MIN_TASKS}-{validate_evals.MAX_TASKS}" not in e]
    if errors:
        raise ek.EvalError("invalid tasks.json:\n  " + "\n  ".join(errors))
    return data


def lane_dir(runs, task, sub):
    """runs/<task>/ for the primary generator, runs/<task>/secondary/ for the secondary one."""
    return runs / task["id"] / sub if sub else runs / task["id"]


def answer_path(run_dir, task, arm, k=0):
    return run_dir / f"{arm}{ek.sample_suffix(k)}.{'html' if task['kind'] == 'build' else 'md'}"


def meta_path(run_dir, arm, k=0):
    return run_dir / f"{arm}{ek.sample_suffix(k)}.meta.json"


def read_meta(run_dir, arm, k):
    try:
        return json.loads(meta_path(run_dir, arm, k).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def is_loaded(args, meta):
    """Whether a WITH sample used the skill: it appears in the invoked list (installed mode), or always
    (injected mode, where the body is part of the system prompt)."""
    return args.mode == "injected" or args.skill in meta.get("skills_invoked", [])


def needs_work(args, task, run_dir, arm, k):
    """A sample is missing, or a cached WITH sample did not load and has attempts left."""
    if not answer_path(run_dir, task, arm, k).is_file():
        return True
    if arm != "with" or args.mode == "injected":
        return False
    meta = read_meta(run_dir, arm, k)
    return not is_loaded(args, meta) and meta.get("attempts", 1) < ek.MAX_LOAD_ATTEMPTS


def generate_sample(args, task, arm, k, skill_dir, run_dir, model):
    """Generate one sample, regenerating a WITH sample that did not load the skill (attempts are capped)."""
    spent = read_meta(run_dir, arm, k).get("attempts", 1) if answer_path(run_dir, task, arm, k).is_file() else 0
    while True:
        text, meta = ek.generate(task["prompt"], task["kind"], args.skill, skill_dir, arm == "with", args.mode,
                                 model, args.effort, args.timeout, task["id"], sample=k, attempt=spent)
        spent += 1
        if arm != "with" or is_loaded(args, meta) or spent >= ek.MAX_LOAD_ATTEMPTS:
            break
    meta.update(sample=k, attempts=spent)
    if arm == "with":
        meta["loaded"] = is_loaded(args, meta)
    run_dir.mkdir(parents=True, exist_ok=True)
    meta_path(run_dir, arm, k).write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    answer_path(run_dir, task, arm, k).write_text(text, encoding="utf-8")  # last: its presence means the sample is done
    return spent


def generate_missing(args, tasks, skill_dir, runs, model, sub):
    jobs = [(t, arm, k) for t in tasks for k in range(args.samples) for arm in ARMS
            if needs_work(args, t, lane_dir(runs, t, sub), arm, k)]

    def work(job):
        t, arm, k = job
        try:
            spent = generate_sample(args, t, arm, k, skill_dir, lane_dir(runs, t, sub), model)
        except ek.EvalError as e:
            return f"{t['id']}/{arm}/{k + 1}: {e}"
        print(f"generated {t['id']}/{arm} sample {k + 1}" + (f" ({spent} attempts)" if spent > 1 else ""))
        return None

    return [e for e in ek.pmap(work, jobs, args.concurrency) if e]


def render_missing(args, tasks, runs, sub):
    for t in tasks:
        if t["kind"] != "build":
            continue
        run_dir = lane_dir(runs, t, sub)
        for k in range(args.samples):
            for arm in ARMS:
                html = answer_path(run_dir, t, arm, k)
                png = run_dir / f"{arm}{ek.sample_suffix(k)}.png"
                if html.is_file() and not png.is_file():
                    try:
                        ek.render_html(html, png)
                    except Exception as e:  # a page that cannot render is scored as blank
                        print(f"render failed for {t['id']}/{arm} sample {k + 1}: {e}")


def judge_sample(args, task, run_dir, k):
    """Blind, swap-controlled comparison of sample k of both arms; returns the sample record."""
    texts = {arm: answer_path(run_dir, task, arm, k).read_text(encoding="utf-8") for arm in ARMS}
    key = {"spec": args.judge, "seed": args.seed, "with": sha(texts["with"]), "without": sha(texts["without"])}
    cache = run_dir / f"judgment{ek.sample_suffix(k)}.json"
    result = None
    if cache.is_file():
        try:
            saved = json.loads(cache.read_text(encoding="utf-8"))
            if saved.get("key") == key:
                result = saved["result"]
        except ValueError:
            pass
    if result is None:
        images = {arm: run_dir / f"{arm}{ek.sample_suffix(k)}.png" if task["kind"] == "build" else None for arm in ARMS}
        images = {arm: (p if p and p.is_file() else None) for arm, p in images.items()}
        shown = {arm: (None if task["kind"] == "build" and not images[arm] else texts[arm]) for arm in ARMS}
        seed_id = task["id"] if k == 0 else f"{task['id']}#s{k}"
        passes = [ek.judge_pass(args.judge, task, order, shown["with"], shown["without"], images["with"], images["without"])
                  for order in ek.assign_order(args.seed, seed_id)]
        result = ek.combine_passes(passes)
        cache.write_text(json.dumps({"key": key, "result": result}, indent=2) + "\n", encoding="utf-8")
    meta = read_meta(run_dir, "with", k)
    loaded = is_loaded(args, meta)
    return {"sample": k, "winner": result["winner"], "rubric_scores": result["rubric_scores"],
            "rubric_items": result["rubric_items"], "position_consistent": result["position_consistent"],
            "judge_notes": result["judge_notes"], "loaded": loaded, "not_loaded": not loaded,
            "attempts": meta.get("attempts", 1)}


def evaluate(args, tasks, skill_dir, runs, model, sub=None):
    """Generate, render and judge every sample of every task for one generator model. Returns the verdicts."""
    if any(needs_work(args, t, lane_dir(runs, t, sub), arm, k) for t in tasks for arm in ARMS for k in range(args.samples)):
        probe = ek.probe_skill(args.skill, skill_dir, args.mode, model, args.effort)
        print(f"probe ok ({model}): {json.dumps(probe)}")
    errors = generate_missing(args, tasks, skill_dir, runs, model, sub)
    if errors:
        raise ek.EvalError("generation failed (finished answers are cached, rerun to resume):\n  " + "\n  ".join(errors))
    render_missing(args, tasks, runs, sub)
    jobs = [(t, k) for t in tasks for k in range(args.samples)]
    records = ek.pmap(lambda job: judge_sample(args, job[0], lane_dir(runs, job[0], sub), job[1]), jobs, args.concurrency)
    return [ek.build_verdict(t["id"], [r for (jt, _), r in zip(jobs, records) if jt is t]) for t in tasks]


def model_id_of(args, tasks, runs, sub):
    meta = read_meta(lane_dir(runs, tasks[0], sub), "with", 0)
    return meta.get("model_id")


def lane_summary(args, tasks, runs, model, sub, verdicts):
    summary = {"model": model, "samples": args.samples, **ek.aggregate_v2(verdicts)}
    model_id = model_id_of(args, tasks, runs, sub)
    if model_id:
        summary["model_id"] = model_id
    return summary


def run(args):
    root = Path(args.root)
    found = find_skill(root, args.skill)
    if not found:
        raise ek.EvalError(f"{args.skill}/SKILL.md not found in {' or '.join(f'{s}/' for s in LIVE_ROOTS)}")
    skill_dir, skill_evals = found[1], root / "evals" / args.skill
    if args.samples < 1:
        raise ek.EvalError("--samples must be at least 1")
    args.judge = args.judge or ek.default_judge(args.model)
    for label, model in (("generator", args.model), ("secondary generator", args.secondary_model)):
        if model and ek.same_model_judge(args.judge, model) and not args.allow_same_model_judge:
            raise ek.EvalError(
                f"the judge '{args.judge}' is the same model as the {label} '{model}'. A model scoring its own "
                "output is not independent evidence. Pick another judge with --judge, or pass --allow-same-model-judge "
                "to run anyway (the results are then recorded as same_model_judge and a held-out file will not validate).")
    same_model = ek.same_model_judge(args.judge, args.model) or bool(
        args.secondary_model and ek.same_model_judge(args.judge, args.secondary_model))
    suite = ek.resolve_suite(skill_evals, args.suite)
    evals_dir = ek.suite_dir(skill_evals, suite)
    if not (evals_dir / "tasks.json").is_file():
        raise ek.EvalError(f"evals/{args.skill}/{'heldout/' if suite == 'heldout' else ''}tasks.json not found "
                           f"(suite '{suite}')")
    all_tasks = load_tasks(evals_dir / "tasks.json", args.allow_small,
                           copy_heldout=found[0] == "copy-skills" and suite == "heldout")
    wanted = [i for i in args.tasks.split(",") if i] if args.tasks else None
    tasks = [t for t in all_tasks if wanted is None or t["id"] in wanted]
    unknown = set(wanted or []) - {t["id"] for t in all_tasks}
    if unknown:
        raise ek.EvalError(f"unknown task ids: {sorted(unknown)}")
    runs = evals_dir / "runs"

    if args.dry_run:
        print(f"skill={args.skill} suite={suite} protocol={ek.PROTOCOL} samples={args.samples} mode={args.mode} "
              f"model={args.model} secondary={args.secondary_model or 'none'} judge={args.judge} "
              f"same_model_judge={same_model} seed={args.seed}")
        for t in tasks:
            have = ", ".join(f"{a} {sum(answer_path(runs / t['id'], t, a, k).is_file() for k in range(args.samples))}"
                             f"/{args.samples}" for a in ARMS)
            print(f"  {t['id']} [{t['kind']}] cached answers: {have}; "
                  f"blind order (pass1 A,B / pass2 A,B): {ek.assign_order(args.seed, t['id'])}")
        print("dry run: nothing generated or judged")
        return 0

    verdicts = evaluate(args, tasks, skill_dir, runs, args.model)
    summary = {"protocol": ek.PROTOCOL, **lane_summary(args, tasks, runs, args.model, None, verdicts),
               "date": datetime.date.today().isoformat(), "judge": args.judge, "same_model_judge": same_model,
               "suite": suite, "mode": args.mode, "seed": args.seed, "suite_hash": validate_evals.suite_hash(all_tasks)}
    summary["gate"] = ek.ship_gate_v2(summary["loaded"], args.tolerance)
    secondary = None
    if args.secondary_model:
        sec_verdicts = evaluate(args, tasks, skill_dir, runs, args.secondary_model, SECONDARY)
        secondary = {"summary": lane_summary(args, tasks, runs, args.secondary_model, SECONDARY, sec_verdicts),
                     "verdicts": sec_verdicts}
    print(f"suite {suite}, protocol {ek.PROTOCOL}, judge {args.judge}{' (same model as the generator)' if same_model else ''}")
    print(ek.gate_line_v2(args.skill, summary))
    if secondary:
        sec = secondary["summary"]
        print(f"secondary (not gated) {args.secondary_model}: loaded-only {ek.tally_text(sec['loaded'])} over "
              f"{sec['loaded']['tasks_with_loaded_sample']} tasks; all samples {ek.tally_text(sec)}")
    if len(tasks) == len(all_tasks):
        out = evals_dir / "results.json"
        if not secondary and out.is_file() and "secondary" in (json.loads(out.read_text(encoding="utf-8")) or {}):
            print("note: the previous results.json had a secondary row; pass --secondary-model again to keep it")
        data = {"verdicts": verdicts, "summary": summary, **({"secondary": secondary} if secondary else {})}
        out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out.relative_to(root)}")
    else:
        print("subset run: results.json not written")
    return 0 if summary["gate"]["passed"] else 1


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("skill")
    p.add_argument("--model", default="sonnet")
    p.add_argument("--samples", type=int, default=ek.DEFAULT_SAMPLES,
                   help="answers per arm per task (default %(default)s); sample i of one arm is judged against "
                        "sample i of the other and a task's verdict is the majority over its samples")
    p.add_argument("--secondary-model", help="also run the suite with this (weaker) generator, e.g. haiku, and "
                                             "report it as a secondary row that never counts toward the gate")
    p.add_argument("--suite", choices=ek.SUITES,
                   help="dev (evals/<skill>/) or heldout (evals/<skill>/heldout/); default heldout when it exists")
    p.add_argument("--judge", help="claude:<model> or grok:<model>; default claude:opus (claude:sonnet when the "
                                   "generator is an opus model). Must differ from the generator model")
    p.add_argument("--allow-same-model-judge", action="store_true",
                   help="let a generator model judge its own answers (recorded; not valid for held-out results)")
    p.add_argument("--mode", choices=["installed", "injected"], default="installed")
    p.add_argument("--concurrency", type=int, default=2)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--tasks", help="comma-separated task ids (subset runs do not write results.json)")
    p.add_argument("--effort", help="effort level passed to claude for generation (default: CLI default)")
    p.add_argument("--tolerance", type=float, default=0.1, help="allowed drop in mean rubric score for the gate")
    p.add_argument("--timeout", type=int, default=600)
    p.add_argument("--allow-small", action="store_true", help="accept fewer than 8 tasks (smoke tests only)")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = p.parse_args(argv)
    try:
        return run(args)
    except ek.EvalError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
