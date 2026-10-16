#!/usr/bin/env python3
"""Validate evals/<skill-name>/ suites: tasks.json, results.json and runs/ (see evals/SCHEMA.md).

Each skill has a dev suite (evals/<skill>/) and may have a held-out suite (evals/<skill>/heldout/)."""
import argparse
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import activation as act  # noqa: E402
import evalkit  # noqa: E402
from roots import find_skill  # noqa: E402

KINDS = evalkit.KINDS
WINNERS = {"with", "without", "tie"}
MODES = {"installed", "injected"}
SUITE_NAMES = {"dev", "heldout"}
ANSWER = re.compile(r"^(with|without)(?:\.s(\d+))?\.(md|html)$")
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MIN_TASKS, MAX_TASKS = 8, 10
PROTOCOLS = (1, 2)
# A held-out suite for a copy skill (protocol 2) must test where a skill should help: drafting with no facts
# supplied and holding the line when the user pushes for an invented fact or a deceptive tactic.
COPY_MIN_NO_FACT_SHEET, COPY_MIN_PRESSURE = 4, 2


def is_text(v):
    return isinstance(v, str) and bool(v.strip())


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def load(path, errors):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        errors.append(f"{path.name}: cannot read JSON: {e}")


def suite_hash(data):
    """Hash of a tasks.json's content (whitespace-insensitive), recorded by protocol 2 results."""
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()[:16]


def validate_tasks(data, protocol=1, copy_heldout=False):
    """Errors and ids for a tasks.json. `protocol` 2 makes `fact_sheet` required on write tasks; `copy_heldout`
    adds the held-out count rules for a copy skill (only meaningful with protocol 2)."""
    errors, ids = [], []
    if not isinstance(data, list):
        return ["tasks.json: top level must be a list"], ids
    if not MIN_TASKS <= len(data) <= MAX_TASKS:
        errors.append(f"tasks.json: {len(data)} tasks (need {MIN_TASKS}-{MAX_TASKS})")
    for i, t in enumerate(data):
        where = f"tasks.json[{i}]"
        if not isinstance(t, dict):
            errors.append(f"{where}: must be an object")
            continue
        extra = set(t) - {"id", "kind", "prompt", "rubric", "fact_sheet", "pressure"}
        if extra:
            errors.append(f"{where}: unknown keys {sorted(extra)}")
        if not is_text(t.get("id")):
            errors.append(f"{where}: 'id' must be a non-empty string")
        elif t["id"] in ids:
            errors.append(f"{where}: duplicate id '{t['id']}'")
        else:
            ids.append(t["id"])
        if t.get("kind") not in KINDS:
            errors.append(f"{where}: 'kind' must be one of {sorted(KINDS)}")
        if not is_text(t.get("prompt")):
            errors.append(f"{where}: 'prompt' must be a non-empty string")
        rubric = t.get("rubric")
        if not isinstance(rubric, list) or not rubric or not all(is_text(r) for r in rubric):
            errors.append(f"{where}: 'rubric' must be a non-empty list of non-empty strings")
        for key in ("fact_sheet", "pressure"):
            if key in t:
                if t.get("kind") != "write":
                    errors.append(f"{where}: '{key}' is only allowed on write tasks")
                elif not isinstance(t[key], bool):
                    errors.append(f"{where}: '{key}' must be true or false")
        if protocol >= 2 and t.get("kind") == "write" and "fact_sheet" not in t:
            errors.append(f"{where}: a write task must declare 'fact_sheet' (true when the prompt carries a fact sheet)")
    if copy_heldout and protocol >= 2 and isinstance(data, list):
        writes = [t for t in data if isinstance(t, dict) and t.get("kind") == "write"]
        no_sheet = sum(1 for t in writes if t.get("fact_sheet") is False)
        pressure = sum(1 for t in writes if t.get("pressure") is True)
        if no_sheet < COPY_MIN_NO_FACT_SHEET:
            errors.append(f"tasks.json: a held-out suite for a copy skill needs at least {COPY_MIN_NO_FACT_SHEET} "
                          f"write tasks with fact_sheet false (has {no_sheet})")
        if pressure < COPY_MIN_PRESSURE:
            errors.append(f"tasks.json: a held-out suite for a copy skill needs at least {COPY_MIN_PRESSURE} "
                          f"write tasks with pressure true (has {pressure})")
    return errors, ids


def validate_verdict_extras(v, where):
    """Optional per-verdict fields written by scripts/run_eval.py."""
    errors = []
    items = v.get("rubric_items")
    if items is not None and not (
            isinstance(items, dict) and set(items) == {"with", "without"}
            and all(isinstance(x, list) and x and all(is_num(n) for n in x) for x in items.values())):
        errors.append(f"{where}: 'rubric_items' must be {{with: [numbers], without: [numbers]}}")
    for key in ("position_consistent", "with_skill_invoked"):
        if key in v and not isinstance(v[key], bool):
            errors.append(f"{where}: '{key}' must be true or false")
    passes = v.get("passes")
    if passes is not None and not (
            isinstance(passes, list) and passes
            and all(isinstance(p, dict) and p.get("winner") in WINNERS for p in passes)):
        errors.append(f"{where}: 'passes' must be a non-empty list of objects with a valid 'winner'")
    return errors


def validate_summary_extras(summary):
    """Optional summary fields written by scripts/run_eval.py; the gate is recomputed, not trusted."""
    errors = []
    for key in ("judge", "model_id"):
        if key in summary and not is_text(summary[key]):
            errors.append(f"results.json summary: '{key}' must be a non-empty string")
    if "mode" in summary and summary["mode"] not in MODES:
        errors.append(f"results.json summary: 'mode' must be one of {sorted(MODES)}")
    if "seed" in summary and (not isinstance(summary["seed"], int) or isinstance(summary["seed"], bool)):
        errors.append("results.json summary: 'seed' must be an integer")
    for key in ("same_model_judge", "superseded"):
        if key in summary and not isinstance(summary[key], bool):
            errors.append(f"results.json summary: '{key}' must be true or false")
    if "suite" in summary and summary["suite"] not in SUITE_NAMES:
        errors.append(f"results.json summary: 'suite' must be one of {sorted(SUITE_NAMES)}")
    if "superseded_note" in summary and not is_text(summary["superseded_note"]):
        errors.append("results.json summary: 'superseded_note' must be a non-empty string")
    if "protocol" in summary and summary["protocol"] not in PROTOCOLS:
        errors.append(f"results.json summary: 'protocol' must be one of {list(PROTOCOLS)}")
    gate = summary.get("gate")
    if gate is None or summary.get("protocol") == 2:
        return errors
    fields = ("tolerance", "mean_rubric_with", "mean_rubric_without")
    if not (isinstance(gate, dict) and isinstance(gate.get("passed"), bool) and all(is_num(gate.get(k)) for k in fields)):
        return errors + ["results.json summary: 'gate' must hold passed (bool), tolerance, mean_rubric_with, mean_rubric_without"]
    wins, losses = summary.get("with_wins"), summary.get("without_wins")
    if isinstance(wins, int) and isinstance(losses, int):
        expected = wins >= losses and gate["mean_rubric_with"] >= gate["mean_rubric_without"] - gate["tolerance"]
        if gate["passed"] != expected:
            errors.append(f"results.json summary: gate.passed is {gate['passed']} but the recorded numbers give {expected}")
    return errors


def close(a, b):
    return (a is None and b is None) or (is_num(a) and is_num(b) and abs(a - b) <= 0.0015)


def validate_sample(s, k, where):
    errors = []
    if not isinstance(s, dict):
        return [f"{where}: must be an object"]
    if s.get("sample") != k:
        errors.append(f"{where}: 'sample' must be {k}")
    if s.get("winner") not in WINNERS:
        errors.append(f"{where}: 'winner' must be one of {sorted(WINNERS)}")
    scores = s.get("rubric_scores")
    if not (isinstance(scores, dict) and set(scores) == {"with", "without"} and all(is_num(v) for v in scores.values())):
        errors.append(f"{where}: 'rubric_scores' must be {{with: number, without: number}}")
    for key in ("loaded", "not_loaded"):
        if not isinstance(s.get(key), bool):
            errors.append(f"{where}: '{key}' must be true or false")
    if isinstance(s.get("loaded"), bool) and isinstance(s.get("not_loaded"), bool) and s["loaded"] == s["not_loaded"]:
        errors.append(f"{where}: 'loaded' and 'not_loaded' must disagree")
    attempts = s.get("attempts")
    if not (isinstance(attempts, int) and not isinstance(attempts, bool) and 1 <= attempts <= evalkit.MAX_LOAD_ATTEMPTS):
        errors.append(f"{where}: 'attempts' must be an integer from 1 to {evalkit.MAX_LOAD_ATTEMPTS}")
    elif s.get("not_loaded") is True and attempts != evalkit.MAX_LOAD_ATTEMPTS:
        errors.append(f"{where}: a sample is flagged not_loaded only after {evalkit.MAX_LOAD_ATTEMPTS} attempts")
    if not is_text(s.get("judge_notes")):
        errors.append(f"{where}: 'judge_notes' must be a non-empty string")
    errors += validate_verdict_extras({k2: v for k2, v in s.items() if k2 in ("rubric_items", "position_consistent")}, where)
    return errors


def validate_v2_verdict(v, where, n_samples):
    """The samples of one protocol 2 verdict, and that its task-level fields follow from them."""
    samples = v.get("samples")
    if not (isinstance(samples, list) and len(samples) == n_samples):
        return [f"{where}: 'samples' must list {n_samples} samples"]
    errors = []
    for k, s in enumerate(samples):
        errors += validate_sample(s, k, f"{where} samples[{k}]")
    if errors:
        return errors
    want = evalkit.build_verdict(v.get("task_id"), samples)
    for key in ("winner", "loaded_winner", "loaded_samples"):
        if v.get(key) != want[key]:
            errors.append(f"{where}: '{key}' is {v.get(key)!r} but the samples give {want[key]!r}")
    for key in ("rubric_scores", "loaded_rubric_scores"):
        got, exp = v.get(key), want[key]
        same = (got is None and exp is None) or (isinstance(got, dict) and exp is not None
                                                  and all(close(got.get(a), exp[a]) for a in ("with", "without")))
        if not same:
            errors.append(f"{where}: '{key}' does not match the mean over the samples")
    return errors


def validate_v2_summary(summary, verdicts, n_samples, label, gated):
    """Recompute the loaded-only block (and the gate when `gated`) from verdicts that already passed their checks."""
    errors = []
    if summary.get("samples") != n_samples:
        errors.append(f"{label}: 'samples' must be {n_samples}")
    want = evalkit.aggregate_v2(verdicts)["loaded"]
    got = summary.get("loaded")
    if not isinstance(got, dict):
        return errors + [f"{label}: 'loaded' must be the loaded-only tally"]
    for key, value in want.items():
        if not close(got.get(key), value) if key.startswith(("mean_",)) else got.get(key) != value:
            errors.append(f"{label}: loaded.{key} is {got.get(key)!r} but the verdicts give {value!r}")
    if not gated:
        return errors
    gate = summary.get("gate")
    if not (isinstance(gate, dict) and is_num(gate.get("tolerance")) and gate.get("decision") in ("pass", "fail", "inconclusive")
            and isinstance(gate.get("passed"), bool)):
        return errors + [f"{label}: 'gate' must hold decision (pass, fail or inconclusive), passed (bool) and tolerance"]
    if gate.get("min_advantage") != evalkit.MIN_ADVANTAGE or gate.get("min_loaded_tasks") != evalkit.MIN_LOADED_TASKS:
        errors.append(f"{label}: gate must use min_advantage {evalkit.MIN_ADVANTAGE} and min_loaded_tasks "
                      f"{evalkit.MIN_LOADED_TASKS}")
    expect = evalkit.ship_gate_v2(want, gate["tolerance"])
    if gate["decision"] != expect["decision"] or gate["passed"] != expect["passed"]:
        errors.append(f"{label}: gate is {gate['decision']} but the recorded numbers give {expect['decision']}")
    for key in ("mean_rubric_with", "mean_rubric_without", "mean_advantage"):
        if not close(gate.get(key), expect[key]):
            errors.append(f"{label}: gate.{key} does not match the loaded-only means")
    return errors


def check_verdicts(verdicts, task_ids, label, n_samples):
    """Shared by the main verdict list and the secondary one. Returns (errors, tally of verdict winners)."""
    errors, seen = [], []
    tally = {"with": 0, "without": 0, "tie": 0}
    for i, v in enumerate(verdicts):
        where = f"{label} verdicts[{i}]"
        if not isinstance(v, dict):
            errors.append(f"{where}: must be an object")
            continue
        tid = v.get("task_id")
        if tid not in task_ids:
            errors.append(f"{where}: task_id '{tid}' is not in tasks.json")
        elif tid in seen:
            errors.append(f"{where}: duplicate verdict for '{tid}'")
        seen.append(tid)
        if v.get("winner") in WINNERS:
            tally[v["winner"]] += 1
        else:
            errors.append(f"{where}: 'winner' must be one of {sorted(WINNERS)}")
        if not is_text(v.get("judge_notes")):
            errors.append(f"{where}: 'judge_notes' must be a non-empty string")
        scores = v.get("rubric_scores")
        if not (isinstance(scores, dict) and set(scores) == {"with", "without"}
                and all(is_num(s) for s in scores.values())):
            errors.append(f"{where}: 'rubric_scores' must be {{with: number, without: number}}")
        errors += validate_verdict_extras(v, where)
        if n_samples:
            errors += validate_v2_verdict(v, where, n_samples)
    missing = [t for t in task_ids if t not in seen]
    if verdicts and missing:
        errors.append(f"{label}: no verdict for tasks {missing}")
    return errors, tally


def results_protocol(data):
    """1 for a results file with no `protocol` (everything written before protocol 2), else the recorded value."""
    summary = data.get("summary") if isinstance(data, dict) else None
    return summary.get("protocol", 1) if isinstance(summary, dict) else 1


def validate_results(data, task_ids):
    errors = []
    if not isinstance(data, dict):
        return ["results.json: top level must be an object"]
    verdicts, summary = data.get("verdicts"), data.get("summary")
    protocol = results_protocol(data)
    n_samples = summary.get("samples") if isinstance(summary, dict) and protocol == 2 else None
    if protocol == 2 and not (isinstance(n_samples, int) and not isinstance(n_samples, bool) and n_samples >= 1):
        errors.append("results.json summary: 'samples' must be a positive integer in a protocol 2 file")
        n_samples = None
    if not isinstance(verdicts, list) or not verdicts:
        errors.append("results.json: 'verdicts' must be a non-empty list")
        verdicts = []
    found, tally = check_verdicts(verdicts, task_ids, "results.json", n_samples)
    errors += found
    if not isinstance(summary, dict):
        errors.append("results.json: 'summary' must be an object")
        return errors
    for key, label in (("with_wins", "with"), ("without_wins", "without"), ("ties", "tie")):
        if not isinstance(summary.get(key), int) or isinstance(summary.get(key), bool) or summary[key] < 0:
            errors.append(f"results.json summary: '{key}' must be a non-negative integer")
        elif verdicts and summary[key] != tally[label]:
            errors.append(f"results.json summary: '{key}' is {summary[key]} but verdicts give {tally[label]}")
    if not is_text(summary.get("model")):
        errors.append("results.json summary: 'model' must be a non-empty string")
    try:
        datetime.date.fromisoformat(summary.get("date", ""))
    except (TypeError, ValueError):
        errors.append("results.json summary: 'date' must be YYYY-MM-DD")
    errors += validate_summary_extras(summary)
    if protocol == 2:
        if not is_text(summary.get("suite_hash")):
            errors.append("results.json summary: a protocol 2 file must record 'suite_hash'")
        if n_samples and not errors:
            errors += validate_v2_summary(summary, verdicts, n_samples, "results.json summary", gated=True)
        errors += validate_secondary(data.get("secondary"), task_ids, n_samples)
    elif "secondary" in data:
        errors.append("results.json: 'secondary' is only valid in a protocol 2 file")
    return errors


def validate_secondary(sec, task_ids, n_samples):
    """The optional secondary row: the same suite run by a weaker generator, reported but never gated."""
    if sec is None:
        return []
    if not (isinstance(sec, dict) and isinstance(sec.get("summary"), dict) and isinstance(sec.get("verdicts"), list)):
        return ["results.json secondary: must hold 'summary' and 'verdicts'"]
    summary, verdicts = sec["summary"], sec["verdicts"]
    errors = []
    if not is_text(summary.get("model")):
        errors.append("results.json secondary summary: 'model' must be a non-empty string")
    if "gate" in summary:
        errors.append("results.json secondary summary: the secondary row is never gated; remove 'gate'")
    found, tally = check_verdicts(verdicts, task_ids, "results.json secondary", n_samples)
    errors += found
    for key, label in (("with_wins", "with"), ("without_wins", "without"), ("ties", "tie")):
        if summary.get(key) != tally[label]:
            errors.append(f"results.json secondary summary: '{key}' is {summary.get(key)!r} but verdicts give {tally[label]}")
    if n_samples and not errors:
        errors += validate_v2_summary(summary, verdicts, n_samples, "results.json secondary summary", gated=False)
    return errors


def judge_problems(summary):
    """Same-model judging is not acceptable evidence in a held-out results file."""
    judge = summary.get("judge")
    model = summary.get("model_id") or summary.get("model")
    problems = []
    if summary.get("same_model_judge") is True:
        problems.append("results.json summary: same_model_judge is true; a held-out run needs a judge that is not the generator")
    elif isinstance(judge, str) and isinstance(model, str) and evalkit.same_model_judge(judge, model):
        problems.append(f"results.json summary: judge '{judge}' is the same model as the generator '{model}'")
    if "judge" not in summary:
        problems.append("results.json summary: a held-out results file must record 'judge'")
    return problems


def answer_names(arm, k):
    suffix = evalkit.sample_suffix(k)
    return f"{arm}{suffix}.md or {arm}{suffix}.html"


def folder_problems(folder, label, samples):
    have = {(m.group(1), int(m.group(2) or 0)) for f in folder.iterdir() if (m := ANSWER.match(f.name))} \
        if folder.is_dir() else set()
    return [f"{label}: no {answer_names(arm, k)} answer file" for k in range(samples) for arm in ("with", "without")
            if (arm, k) not in have]


def validate_runs(suite_path, task_ids, results, strict):
    """Every runs/<task>/ folder must hold with.* and without.* answers; with results, every verdict needs one.

    A protocol 2 results file needs every sample's answer for both arms (sample k > 0 is `with.s<k>.md`), and the
    same under runs/<task>/secondary/ when the file has a secondary row.
    Returns the problems; a dev results file marked superseded gets them as warnings instead of errors."""
    problems = []
    runs = suite_path / "runs"
    samples = 1
    if isinstance(results, dict) and results_protocol(results) == 2:
        n = results["summary"].get("samples") if isinstance(results.get("summary"), dict) else None
        samples = n if isinstance(n, int) and not isinstance(n, bool) and n >= 1 else 1
    wanted = set()
    if runs.is_dir():
        wanted |= {p.name for p in runs.iterdir() if p.is_dir()}
    if strict and isinstance(results, dict) and isinstance(results.get("verdicts"), list):
        wanted |= {v.get("task_id") for v in results["verdicts"] if isinstance(v, dict) and v.get("task_id") in task_ids}
    secondary = isinstance(results, dict) and isinstance(results.get("secondary"), dict)
    for name in sorted(wanted):
        problems += folder_problems(runs / name, f"runs/{name}", samples)
        if secondary:
            problems += folder_problems(runs / name / "secondary", f"runs/{name}/secondary", samples)
    return problems


def is_copy_skill(suite_dir, skill_name):
    found = find_skill(suite_dir.parent.parent, skill_name)
    return bool(found) and found[0] == "copy-skills"


def validate_suite(d, suite):
    """Return (errors, warnings) for one suite folder. Warnings do not fail the check."""
    errors, warnings = [], []
    path = d if suite == "dev" else d / "heldout"
    tasks_path, results_path = path / "tasks.json", path / "results.json"
    if not tasks_path.is_file():
        return ["tasks.json is missing"], warnings
    data = load(tasks_path, errors)
    if data is None:
        return errors, warnings
    results = load(results_path, errors) if results_path.is_file() else None
    protocol = results_protocol(results) if results is not None else 1
    task_errors, ids = validate_tasks(data, protocol, copy_heldout=suite == "heldout" and is_copy_skill(d, d.name))
    errors += task_errors
    if results is not None:
        errors += validate_results(results, ids)
        summary = results.get("summary") if isinstance(results, dict) else None
        if isinstance(summary, dict):
            if "suite" in summary and summary["suite"] != suite:
                errors.append(f"results.json summary: suite is '{summary['suite']}' but the file is in the {suite} suite")
            if suite == "heldout":
                errors += judge_problems(summary)
                if summary.get("superseded"):
                    errors.append("results.json summary: a held-out results file cannot be superseded")
            if is_text(summary.get("suite_hash")) and summary["suite_hash"] != suite_hash(data):
                warnings.append("tasks.json has changed since this results file was written (suite_hash differs). A "
                                "revision made after seeing results needs a fresh held-out set and a new run")
    superseded = bool(suite == "dev" and isinstance(results, dict) and isinstance(results.get("summary"), dict)
                      and results["summary"].get("superseded") is True)
    run_problems = validate_runs(path, ids, results, strict=suite == "heldout")
    if superseded:
        warnings += [f"{x} (dev results are marked superseded)" for x in run_problems]
    else:
        errors += run_problems
    return errors, warnings


def words(text):
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def quoted_phrases(description):
    """The double-quoted phrases in a skill description, normalized to lower-case words."""
    return [w for w in (words(q) for q in re.findall(r'"([^"]+)"', description or "")) if w]


def validate_activation(data, skill, description=""):
    """Errors for an activation.json: 6 should_load and 4 should_not_load requests, distinct, and phrased fresh.

    A should_load request must not name the skill or repeat a quoted phrase of its description (a phrase of three
    or more words may not appear inside it either): the check is whether a description routes a request it did not
    write itself."""
    if not isinstance(data, dict):
        return ["activation.json: top level must be an object"]
    errors = []
    if set(data) != {"should_load", "should_not_load"}:
        errors.append("activation.json: keys must be exactly should_load and should_not_load")
    seen = []
    for key, want in (("should_load", act.SHOULD_LOAD), ("should_not_load", act.SHOULD_NOT_LOAD)):
        items = data.get(key)
        if not (isinstance(items, list) and len(items) == want):
            errors.append(f"activation.json: '{key}' must list {want} requests")
            continue
        for i, text in enumerate(items):
            where = f"activation.json {key}[{i}]"
            if not is_text(text):
                errors.append(f"{where}: must be a non-empty string")
                continue
            if len(text) > act.MAX_REQUEST_CHARS:
                errors.append(f"{where}: {len(text)} characters (max {act.MAX_REQUEST_CHARS})")
            if words(text) in seen:
                errors.append(f"{where}: repeats another request in the file")
            seen.append(words(text))
            if key == "should_load":
                if skill in text.lower():
                    errors.append(f"{where}: names the skill")
                for quote in quoted_phrases(description):
                    if words(text) == quote or (len(quote.split()) >= 3 and f" {quote} " in f" {words(text)} "):
                        errors.append(f"{where}: repeats the description's phrase \"{quote}\"")
    return errors


def validate_section(section, label, key, skill, prompts, names):
    """One half of an activation-results file, recomputed from its per-request records."""
    errors = []
    flag, count, rate = ("correct", "picked", "recall") if key == "should_load" else ("false_pick", "false_picks", "false_pick_rate")
    if not isinstance(section, dict):
        return [f"{label}: must be an object"]
    results = section.get("results")
    if not (isinstance(results, list) and len(results) == len(prompts)):
        return [f"{label}: 'results' must hold one record per request in activation.json ({len(prompts)})"]
    n = 0
    for i, (r, prompt) in enumerate(zip(results, prompts)):
        where = f"{label} results[{i}]"
        if not isinstance(r, dict) or set(r) != {"prompt", "picked", flag}:
            errors.append(f"{where}: must hold exactly prompt, picked and {flag}")
            continue
        if r["prompt"] != prompt:
            errors.append(f"{where}: prompt is not the request at that place in activation.json")
        if r["picked"] is not None and r["picked"] not in names:
            errors.append(f"{where}: picked '{r['picked']}' is not a skill")
        if r[flag] is not (r["picked"] == skill):
            errors.append(f"{where}: '{flag}' does not match picked")
        n += r["picked"] == skill
    if errors:
        return errors
    if section.get("total") != len(prompts):
        errors.append(f"{label}: 'total' must be {len(prompts)}")
    if section.get(count) != n:
        errors.append(f"{label}: '{count}' is {section.get(count)!r} but the records give {n}")
    if not close(section.get(rate), round(n / len(prompts), 3)):
        errors.append(f"{label}: '{rate}' does not match the records")
    return errors


def validate_activation_results(data, skill, activation, names, current_hash):
    """(errors, warnings) for an activation-results.json checked against its activation.json."""
    if not isinstance(data, dict):
        return ["activation-results.json: top level must be an object"], []
    errors, warnings = [], []
    want = {"skill", "model", "date", "catalog_size", "catalog_hash", "should_load", "should_not_load"}
    if not want <= set(data) <= want | {"model_id"}:
        errors.append("activation-results.json: keys must be skill, model, (model_id), date, catalog_size, "
                      "catalog_hash, should_load, should_not_load")
    if data.get("skill") != skill:
        errors.append(f"activation-results.json: 'skill' must be '{skill}'")
    for key in ("model", "model_id", "catalog_hash"):
        if key in data and not is_text(data[key]):
            errors.append(f"activation-results.json: '{key}' must be a non-empty string")
    try:
        datetime.date.fromisoformat(data.get("date", ""))
    except (TypeError, ValueError):
        errors.append("activation-results.json: 'date' must be YYYY-MM-DD")
    size = data.get("catalog_size")
    if not (isinstance(size, int) and not isinstance(size, bool) and size >= 1):
        errors.append("activation-results.json: 'catalog_size' must be a positive integer")
    for key in ("should_load", "should_not_load"):
        errors += validate_section(data.get(key), f"activation-results.json {key}", key, skill,
                                   activation.get(key, []), names)
    if is_text(data.get("catalog_hash")) and data["catalog_hash"] != current_hash:
        warnings.append("skill descriptions have changed since this activation run (catalog_hash differs); "
                        "rerun scripts/run_activation.py to refresh it")
    return errors, warnings


def activation_context(root):
    """(descriptions by skill, names, catalog hash) for the live skills under `root`."""
    rows = act.catalog(root)
    return dict(rows), {n for n, _ in rows}, act.catalog_hash(rows)


def validate_activation_files(d, context, warnings):
    """Errors for the activation files of evals/<skill>/ when the skill is live; their warnings go to `warnings`."""
    descriptions, names, current = context
    skill = d.name
    if skill not in names:
        return []
    errors = []
    data = load(d / "activation.json", errors) if (d / "activation.json").is_file() else None
    if data is not None:
        errors += validate_activation(data, skill, descriptions.get(skill, ""))
    results_path = d / "activation-results.json"
    if results_path.is_file():
        results = load(results_path, errors)
        if results is not None and data is not None and not errors:
            e, w = validate_activation_results(results, skill, data, names, current)
            errors += e
            if warnings is not None:
                warnings += w
    elif data is not None and warnings is not None:
        warnings.append("activation-results.json is missing; run scripts/run_activation.py")
    return errors


def activation_coverage(evals, context):
    """Errors for live skills with no evals/<skill>/activation.json, and for requests reused by two skills.
    scripts/activation_summary.py --check reports these (every skill's eval needs an activation check)."""
    _, names, _ = context
    errors, owner = [], {}
    for name in sorted(names):
        path = evals / name / "activation.json"
        if not path.is_file():
            errors.append(f"evals/{name}: activation.json is missing (6 should_load and 4 should_not_load requests)")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for key in ("should_load", "should_not_load"):
            for text in data.get(key, []) if isinstance(data, dict) and isinstance(data.get(key), list) else []:
                if is_text(text):
                    other = owner.setdefault(words(text), name)
                    if other != name:
                        errors.append(f"evals/{name}: a request is also in evals/{other}/activation.json")
    return errors


def validate_skill_evals(d, warnings=None, context=None):
    """All errors for one evals/<skill>/ folder; warnings are appended to `warnings`."""
    errors = []
    if not KEBAB.match(d.name):
        errors.append(f"folder name '{d.name}' is not kebab-case")
    heldout_only = (not (d / "tasks.json").is_file() and not (d / "results.json").is_file()
                    and (d / "heldout" / "tasks.json").is_file())  # a skill with no dev suite by design
    suites = ([] if heldout_only else ["dev"]) + (["heldout"] if (d / "heldout").is_dir() else [])
    errors += validate_activation_files(d, context or activation_context(d.parent.parent), warnings)
    for suite in suites:
        e, w = validate_suite(d, suite)
        prefix = "" if suite == "dev" else "heldout/"
        errors += [prefix + x for x in e]
        if warnings is not None:
            warnings += [prefix + x for x in w]
    return errors


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = p.parse_args(argv)
    evals = Path(args.root) / "evals"
    dirs = sorted(d for d in evals.iterdir() if d.is_dir()) if evals.is_dir() else []
    failed, warned = 0, 0
    context = activation_context(args.root)
    for d in dirs:
        warnings = []
        for err in validate_skill_evals(d, warnings, context):
            print(f"evals/{d.name}: {err}")
            failed += 1
        for w in warnings:
            print(f"evals/{d.name}: warning: {w}")
            warned += 1
    print(f"validated {len(dirs)} eval folders, {failed} problems, {warned} warnings")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
