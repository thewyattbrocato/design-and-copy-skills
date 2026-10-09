"""Shared pieces for the eval runner and the example renderer.

Generation and judging shell out to CLIs (`claude -p`, `grok -p`). Tests and CI replace them with
stub executables through EVAL_GENERATOR_CMD, EVAL_JUDGE_CMD and EVAL_RENDER_CMD. A stub receives one
JSON object on stdin and prints its answer on stdout.
"""
import json
import math
import os
import random
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render as render_mod  # noqa: E402

PROBE_PROMPT = "List the names of every skill available to you, comma separated, nothing else. If none, say NONE."
BUILD_SUFFIX = (
    "\n\nReturn the result as a single self-contained HTML file: all CSS inline, no external requests, "
    "system fonts only. Reply with one ```html fenced block and nothing else."
)
# Every claude call needs --strict-mcp-config: without it account-level connectors are loaded into the
# context (hundreds of thousands of tokens per call).
CLAUDE_BASE = ["--setting-sources", "project", "--strict-mcp-config", "--no-session-persistence"]
JUDGE_SCHEMA_HINT = (
    'Reply with only a JSON object: {"verdict": "A" | "B" | "tie", "notes": "two or three sentences", '
    '"scores": {"A": [one integer 1-5 per rubric item, in order], "B": [same]}}'
)


# Task kinds. Only "build" returns an HTML page and is judged from a screenshot; every other kind is a text
# answer judged as text. "write" drafts copy from a brief (with a fact sheet when the task says fact_sheet: true).
BUILD_KIND = "build"
TEXT_KINDS = {"critique", "choose", "layout", "polish", "explain", "write"}
KINDS = {BUILD_KIND} | TEXT_KINDS


class EvalError(RuntimeError):
    pass


# ---------- suites ----------

SUITES = ("dev", "heldout")


def suite_dir(skill_evals_dir, suite):
    """evals/<skill>/ for the dev suite, evals/<skill>/heldout/ for the held-out suite."""
    if suite not in SUITES:
        raise EvalError(f"unknown suite '{suite}' (use one of {', '.join(SUITES)})")
    base = Path(skill_evals_dir)
    return base if suite == "dev" else base / "heldout"


def resolve_suite(skill_evals_dir, suite=None):
    """The requested suite, or heldout when it has tasks and dev otherwise."""
    if suite:
        return suite
    return "heldout" if (Path(skill_evals_dir) / "heldout" / "tasks.json").is_file() else "dev"


def same_model_judge(judge, generator):
    """True when the judge spec would be the generator's own model (or the same family).

    Only a claude judge can be the claude generator. Compared case-insensitively after stripping
    the `claude:` prefix; an empty judge model means `opus`; either name containing the other counts,
    so the alias `sonnet` and the id `claude-sonnet-5-5` are the same model."""
    kind, _, jm = (judge or "").partition(":")
    if kind.lower() != "claude":
        return False
    j = (jm or "opus").strip().lower()
    g = (generator or "").strip().lower()
    if g.startswith("claude:"):
        g = g[len("claude:"):]
    return bool(g) and (j == g or j in g or g in j)


def default_judge(generator):
    """A judge that is not the generator: opus, or sonnet when the generator is an opus model."""
    return "claude:sonnet" if "opus" in (generator or "").lower() else "claude:opus"


# ---------- subprocess helpers ----------

def run_cmd(cmd, stdin_text=None, cwd=None, timeout=600, env=None):
    try:
        proc = subprocess.run(cmd, input=stdin_text, capture_output=True, text=True, cwd=cwd,
                              timeout=timeout, env=env, stdin=None if stdin_text is not None else subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        raise EvalError(f"timed out after {timeout}s: {cmd[0]}")
    except FileNotFoundError:
        raise EvalError(f"command not found: {cmd[0]}")
    return proc


def stub_call(env_var, payload, timeout=600):
    """Run the stub named by env_var, or return None when it is not set."""
    spec = os.environ.get(env_var)
    if not spec:
        return None
    proc = run_cmd(shlex.split(spec), stdin_text=json.dumps(payload), timeout=timeout)
    if proc.returncode != 0:
        raise EvalError(f"{env_var} failed: {proc.stderr.strip()[:300]}")
    return proc.stdout


# ---------- skills ----------

def skill_body(skill_dir):
    text = (Path(skill_dir) / "SKILL.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "\n".join(lines[i + 1:]).strip()
    return text.strip()


def extract_html(reply):
    m = re.search(r"```html\s*\n(.*?)```", reply, re.S | re.I)
    if m:
        return m.group(1).strip() + "\n"
    m = re.search(r"```\s*\n(.*?)```", reply, re.S)
    if m and "<" in m.group(1):
        return m.group(1).strip() + "\n"
    return reply.strip() + "\n"


# ---------- generation ----------

def primary_model(usage):
    """The model that did most of the work: the modelUsage key with the most tokens (first on a tie)."""
    if not isinstance(usage, dict) or not usage:
        return None

    def tokens(v):
        return sum(n for k, n in (v or {}).items()
                   if k.lower().endswith("tokens") and isinstance(n, (int, float)) and not isinstance(n, bool)) \
            if isinstance(v, dict) else 0
    return max(usage, key=lambda k: tokens(usage[k]))


def parse_stream(stdout):
    """Pull the final answer, cost, resolved model and invoked skills out of stream-json output."""
    answer, cost, model_id, skills = "", None, None, []
    for line in stdout.splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "assistant":
            for block in ev.get("message", {}).get("content", []):
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    skills.append(str(block.get("input", {}).get("skill", "")))
        elif ev.get("type") == "result":
            if ev.get("is_error"):
                raise EvalError(f"claude reported an error: {str(ev.get('result'))[:300]}")
            answer = ev.get("result") or ""
            cost = ev.get("total_cost_usd")
            model_id = primary_model(ev.get("modelUsage"))
    return answer, {"cost_usd": cost, "model_id": model_id, "skills_invoked": skills}


def claude_generate(prompt, skill, skill_dir, mode, model, effort, timeout):
    """One headless generation. skill is None for the WITHOUT arm."""
    cmd = ["claude", "-p", prompt, "--model", model, "--output-format", "stream-json", "--verbose", *CLAUDE_BASE]
    if effort:
        cmd += ["--effort", effort]
    with tempfile.TemporaryDirectory(prefix="eval-gen-") as tmp:
        if mode == "installed":
            # Same tool set in both arms; the only difference is the skill folder in the project.
            cmd += ["--tools", "Skill,Read"]
            if skill:
                shutil.copytree(skill_dir, Path(tmp) / ".claude" / "skills" / skill)
        else:
            cmd += ["--tools", ""]
            if skill:
                cmd += ["--append-system-prompt", skill_body(skill_dir)]
        proc = run_cmd(cmd, cwd=tmp, timeout=timeout)
    if proc.returncode != 0:
        raise EvalError(f"claude exited {proc.returncode}: {proc.stderr.strip()[:300]}")
    return parse_stream(proc.stdout)


def parse_stub_output(out, model):
    """A stub prints plain answer text, or a JSON object {"answer": ..., "skills_invoked": [...]} when it
    also needs to say which skills the generator used."""
    meta = {"cost_usd": None, "model_id": model, "skills_invoked": []}
    if out.lstrip().startswith("{"):
        try:
            data = json.loads(out)
        except ValueError:
            return out, meta
        if isinstance(data, dict) and "answer" in data:
            meta["skills_invoked"] = [str(s) for s in data.get("skills_invoked", [])]
            return str(data["answer"]), meta
    return out, meta


def generate(prompt, kind, skill, skill_dir, with_skill, mode, model, effort=None, timeout=600, task_id="",
             retries=1, sample=0, attempt=0):
    """Return (answer_text, meta). The prompt is identical in both arms."""
    full = prompt + (BUILD_SUFFIX if kind == BUILD_KIND else "")
    last = None
    for _ in range(retries + 1):
        try:
            out = stub_call("EVAL_GENERATOR_CMD", {
                "prompt": full, "kind": kind, "arm": "with" if with_skill else "without", "skill": skill,
                "mode": mode, "model": model, "task_id": task_id, "sample": sample, "attempt": attempt}, timeout)
            if out is not None:
                answer, meta = parse_stub_output(out, model)
            else:
                answer, meta = claude_generate(full, skill if with_skill else None, skill_dir, mode, model, effort, timeout)
            if not answer.strip():
                raise EvalError("empty answer")
            return (extract_html(answer) if kind == BUILD_KIND else answer.strip() + "\n"), meta
        except EvalError as e:
            last = e
    raise EvalError(f"generation failed for {task_id or 'prompt'}: {last}")


def skill_names(text):
    return {n.strip() for n in re.split(r"[,\n]", text) if n.strip() and n.strip().upper() != "NONE"}


def probe_skill(skill, skill_dir, mode, model, effort=None, timeout=300):
    """Confirm the skill is visible WITH and absent WITHOUT, and that the check repeats."""
    if mode == "injected":
        if not skill_body(skill_dir):
            raise EvalError("SKILL.md body is empty")
        return {"mode": mode, "note": "injected: body appended to the system prompt, no visibility probe"}
    def ask(with_skill):
        out = stub_call("EVAL_GENERATOR_CMD", {
            "prompt": PROBE_PROMPT, "kind": "probe", "arm": "with" if with_skill else "without", "skill": skill,
            "mode": mode, "model": model, "task_id": "probe"}, timeout)
        if out is None:
            out, _ = claude_generate(PROBE_PROMPT, skill if with_skill else None, skill_dir, mode, model, effort, timeout)
        return skill_names(out)
    with_runs, without_runs = [ask(True), ask(True)], [ask(False), ask(False)]
    if not all(skill in r for r in with_runs):
        raise EvalError(f"probe: skill '{skill}' is not visible in the WITH run")
    if any(skill in r for r in without_runs):
        raise EvalError(f"probe: skill '{skill}' is visible in the WITHOUT run")
    if with_runs[0] - {skill} != without_runs[0] or with_runs[1] - {skill} != without_runs[1]:
        raise EvalError("probe: the two arms differ by more than the skill under test")
    return {"mode": mode, "with": sorted(with_runs[0]), "without": sorted(without_runs[0]), "reproducible": True}


# ---------- rendering ----------

def render_html(html_path, png_path, width=1280, height=800):
    html_path, png_path = Path(html_path), Path(png_path)
    spec = os.environ.get("EVAL_RENDER_CMD")
    if spec:
        proc = run_cmd(shlex.split(spec) + [str(html_path), str(png_path)], timeout=120)
        if proc.returncode != 0 or not png_path.is_file():
            raise render_mod.RenderError(proc.stderr.strip()[:300] or "render stub failed")
    else:
        render_mod.render(html_path, png_path, width, height)
    return png_path


# ---------- blind judging ----------

def assign_order(seed, task_id):
    """Seeded coin flip: which arm is shown as A in the first pass. The second pass swaps."""
    rng = random.Random(f"{seed}:{task_id}")
    first = ["with", "without"] if rng.random() < 0.5 else ["without", "with"]
    return [first, first[::-1]]


def extract_json(text):
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end <= start:
        raise EvalError("no JSON object in reply")
    return json.loads(text[start:end + 1])


def parse_judgment(text, n_items):
    data = extract_json(text)
    verdict = data.get("verdict")
    if verdict not in ("A", "B", "tie"):
        raise EvalError(f"bad verdict {verdict!r}")
    scores = data.get("scores") or {}
    for side in ("A", "B"):
        vals = scores.get(side)
        if not (isinstance(vals, list) and len(vals) == n_items
                and all(isinstance(v, (int, float)) and not isinstance(v, bool) and 1 <= v <= 5 for v in vals)):
            raise EvalError(f"scores for {side} must be {n_items} numbers from 1 to 5")
    return {"verdict": verdict, "notes": str(data.get("notes", "")).strip() or "(no notes)",
            "scores": {"A": list(scores["A"]), "B": list(scores["B"])}}


def judge_prompt(task, answers, images):
    """answers: {"A": text|None, "B": text|None}; images: {"A": filename|None, "B": ...}. Never names the arms."""
    rubric = "\n".join(f"{i + 1}. {r}" for i, r in enumerate(task["rubric"]))
    parts = ["You are comparing two anonymous answers to the same design request. Judge only the answers.",
             f"REQUEST:\n{task['prompt']}", f"RUBRIC (score each item 1-5 for each answer):\n{rubric}"]
    for side in ("A", "B"):
        if images[side]:
            parts.append(f"=== ANSWER {side} ===\nThe answer was rendered to a screenshot. Read the image file "
                         f"'{images[side]}' in the current directory.")
        elif answers[side] is None:
            parts.append(f"=== ANSWER {side} ===\n(the page failed to render and shows nothing)")
        else:
            parts.append(f"=== ANSWER {side} ===\n{answers[side]}")
    parts.append("Pick the better answer overall, or 'tie' if they are equally good. " + JUDGE_SCHEMA_HINT)
    return "\n\n".join(parts)


def call_judge(spec, prompt, image_files, timeout=600):
    """image_files: {name: source path}; they are copied into a scratch dir under neutral names."""
    kind, _, model = spec.partition(":")
    with tempfile.TemporaryDirectory(prefix="eval-judge-") as tmp:
        for name, src in image_files.items():
            shutil.copy(src, Path(tmp) / name)
        out = stub_call("EVAL_JUDGE_CMD", {"spec": spec, "prompt": prompt, "dir": tmp,
                                           "images": sorted(image_files)}, timeout)
        if out is not None:
            return out
        if kind == "claude":
            cmd = ["claude", "-p", prompt, "--model", model or "opus", "--tools", "Read", *CLAUDE_BASE]
        elif kind == "grok":
            cmd = ["grok", "-p", prompt, "--output-format", "plain", "--cwd", tmp]
            if model:
                cmd += ["-m", model]
        else:
            raise EvalError(f"unknown judge '{spec}' (use claude:<model> or grok:<model>)")
        proc = run_cmd(cmd, cwd=tmp, timeout=timeout)
        if proc.returncode != 0:
            raise EvalError(f"{kind} judge exited {proc.returncode}: {proc.stderr.strip()[:300]}")
        return proc.stdout


def judge_pass(spec, task, order, with_answer, without_answer, with_image=None, without_image=None, retries=2):
    """One blind judgment. order = [arm shown as A, arm shown as B]. Returns the de-blinded result."""
    by_arm = {"with": (with_answer, with_image), "without": (without_answer, without_image)}
    answers, names, files = {}, {}, {}
    for side, arm in zip(("A", "B"), order):
        text, image = by_arm[arm]
        if image:
            names[side] = f"{side.lower()}.png"
            files[names[side]] = image
            answers[side] = None
        else:
            answers[side], names[side] = text, None
    prompt = judge_prompt(task, answers, names)
    last = None
    for _ in range(retries + 1):
        try:
            return deblind(parse_judgment(call_judge(spec, prompt, files), len(task["rubric"])), order)
        except (EvalError, ValueError) as e:
            last = e
    raise EvalError(f"judge gave no usable verdict for {task['id']}: {last}")


def deblind(j, order):
    arm_of = {"A": order[0], "B": order[1]}
    winner = "tie" if j["verdict"] == "tie" else arm_of[j["verdict"]]
    return {"order": list(order), "raw_verdict": j["verdict"], "winner": winner, "notes": j["notes"],
            "scores": {arm_of["A"]: j["scores"]["A"], arm_of["B"]: j["scores"]["B"]}}


def combine_passes(passes):
    """Position-bias control: a win counts only if both passes (sides swapped) agree, otherwise tie."""
    winners = {p["winner"] for p in passes}
    winner = winners.pop() if len(winners) == 1 else "tie"
    n = len(passes[0]["scores"]["with"])
    items = {arm: [round(sum(p["scores"][arm][i] for p in passes) / len(passes), 2) for i in range(n)]
             for arm in ("with", "without")}
    means = {arm: round(sum(v) / len(v), 3) for arm, v in items.items()}
    notes = " | ".join(f"pass {i + 1} (A={p['order'][0]}, B={p['order'][1]}): {p['notes']}" for i, p in enumerate(passes))
    return {"winner": winner, "judge_notes": notes, "rubric_scores": means, "rubric_items": items,
            "position_consistent": len({p["winner"] for p in passes}) == 1,
            "passes": [{k: p[k] for k in ("order", "raw_verdict", "winner", "notes")} for p in passes]}


# ---------- tally and ship gate ----------

def tally(verdicts):
    t = {"with_wins": 0, "without_wins": 0, "ties": 0}
    for v in verdicts:
        t[{"with": "with_wins", "without": "without_wins", "tie": "ties"}[v["winner"]]] += 1
    return t


def ship_gate(verdicts, tolerance=0.1):
    """A skill ships only if it wins at least as often as it loses and its mean rubric score is not worse
    than the baseline by more than the tolerance."""
    t = tally(verdicts)
    n = len(verdicts) or 1
    mean = {arm: round(sum(v["rubric_scores"][arm] for v in verdicts) / n, 3) for arm in ("with", "without")}
    passed = t["with_wins"] >= t["without_wins"] and mean["with"] >= mean["without"] - tolerance
    return {"passed": passed, "tolerance": tolerance, "mean_rubric_with": mean["with"],
            "mean_rubric_without": mean["without"]}


def gate_line(skill, summary):
    g = summary["gate"]
    return (f"{'PASS' if g['passed'] else 'FAIL'} {skill}: with {summary['with_wins']} / without {summary['without_wins']} / "
            f"ties {summary['ties']}, mean rubric {g['mean_rubric_with']} vs {g['mean_rubric_without']} "
            f"(tolerance {g['tolerance']})")


# ---------- protocol 2: samples, loaded-only tallies, gate ----------

PROTOCOL = 2
DEFAULT_SAMPLES = 3
MAX_LOAD_ATTEMPTS = 3         # a WITH sample that did not load the skill is regenerated up to twice
MIN_LOADED_TASKS = 6          # an absolute count: fewer tasks with a loaded sample and the result is inconclusive
MIN_ADVANTAGE = 0.15          # mean rubric advantage that lets a tie on wins and losses pass
WINNER_KEY = {"with": "with_wins", "without": "without_wins", "tie": "ties"}


def sample_suffix(k):
    """File-name part for sample k: none for the first sample (so v1 file names stay valid), `.s<k>` after."""
    return "" if k == 0 else f".s{k}"


def majority(winners):
    """The arm that won strictly more than half of the samples; a tie when no arm did."""
    for arm in ("with", "without"):
        if winners.count(arm) * 2 > len(winners):
            return arm
    return "tie"


def mean_scores(samples):
    n = len(samples)
    return {arm: round(sum(s["rubric_scores"][arm] for s in samples) / n, 3) for arm in ("with", "without")}


def build_verdict(task_id, samples):
    """One task's verdict from its sample records: majority over all samples and over the loaded ones."""
    loaded = [s for s in samples if s["loaded"]]
    winners = [s["winner"] for s in samples]
    winner = majority(winners)
    return {"task_id": task_id, "winner": winner,
            "judge_notes": f"{len(samples)} samples ({', '.join(winners)}): majority {winner}. "
                           "Each sample's notes are in samples[].judge_notes.",
            "rubric_scores": mean_scores(samples), "samples": samples, "loaded_samples": len(loaded),
            "loaded_winner": majority([s["winner"] for s in loaded]) if loaded else None,
            "loaded_rubric_scores": mean_scores(loaded) if loaded else None}


def tally_by(verdicts, key="winner"):
    t = {"with_wins": 0, "without_wins": 0, "ties": 0}
    for v in verdicts:
        if v.get(key) is not None:
            t[WINNER_KEY[v[key]]] += 1
    return t


def aggregate_v2(verdicts):
    """Summary numbers from protocol 2 verdicts: the all-samples tally and the loaded-only block."""
    with_loaded = [v for v in verdicts if v["loaded_winner"] is not None]
    n = len(with_loaded)

    def mean(arm):
        return round(sum(v["loaded_rubric_scores"][arm] for v in with_loaded) / n, 3) if n else None
    mw, mo = mean("with"), mean("without")
    loaded = {**tally_by(verdicts, "loaded_winner"), "tasks_with_loaded_sample": n,
              "loaded_samples": sum(v["loaded_samples"] for v in verdicts),
              "total_samples": sum(len(v["samples"]) for v in verdicts),
              "mean_rubric_with": mw, "mean_rubric_without": mo,
              "mean_advantage": round(mw - mo, 3) if n else None}
    return {**tally_by(verdicts), "loaded": loaded}


def ship_gate_v2(loaded, tolerance=0.1):
    """The protocol 2 gate, on the loaded-only block of the summary. Three outcomes:

    inconclusive: fewer than MIN_LOADED_TASKS tasks have a loaded sample (not a pass);
    pass: with_wins > without_wins, or with_wins >= without_wins with a mean rubric advantage of at least
          MIN_ADVANTAGE; and the with-skill mean is not below the baseline by more than the tolerance;
    fail: anything else. A tie on wins is therefore not a pass unless the rubric advantage is there."""
    n = loaded["tasks_with_loaded_sample"]
    gate = {"tolerance": tolerance, "min_advantage": MIN_ADVANTAGE, "min_loaded_tasks": MIN_LOADED_TASKS,
            "mean_rubric_with": loaded["mean_rubric_with"], "mean_rubric_without": loaded["mean_rubric_without"],
            "mean_advantage": loaded["mean_advantage"]}
    if n < MIN_LOADED_TASKS:
        return {"decision": "inconclusive", "passed": False, **gate,
                "reason": f"only {n} tasks have a sample where the skill loaded; at least {MIN_LOADED_TASKS} are needed"}
    wins, losses, adv = loaded["with_wins"], loaded["without_wins"], loaded["mean_advantage"]
    beats = wins > losses or (wins >= losses and adv >= MIN_ADVANTAGE - 1e-9)
    not_worse = loaded["mean_rubric_with"] >= loaded["mean_rubric_without"] - tolerance - 1e-9
    passed = beats and not_worse
    if passed:
        reason = "with-skill wins outnumber losses" if wins > losses else \
            f"wins and losses are level and the mean rubric advantage is {adv:+.3f}"
    elif not not_worse:
        reason = f"mean rubric is more than {tolerance} below the baseline"
    elif wins < losses:
        reason = "with-skill losses outnumber wins"
    else:
        reason = f"wins and losses are level and the mean rubric advantage {adv:+.3f} is below {MIN_ADVANTAGE}"
    return {"decision": "pass" if passed else "fail", "passed": passed, **gate, "reason": reason}


def noise_floor(decisive, wins):
    """What chance alone does at this n. A skill with no effect splits each decisive task (a task that is not a
    tie) like a fair coin, so its wins are Binomial(decisive, 1/2). Returns the mean, the central 95% range of
    wins, and the one-sided chance of at least `wins` wins; None entries when there are no decisive tasks."""
    if decisive <= 0:
        return {"decisive_tasks": 0, "expected_wins": None, "wins_low": None, "wins_high": None, "p_at_least": None}
    pmf = [math.comb(decisive, k) / 2 ** decisive for k in range(decisive + 1)]
    low = next(k for k in range(decisive + 1) if sum(pmf[:k + 1]) >= 0.025)
    high = next(k for k in range(decisive, -1, -1) if sum(pmf[k:]) >= 0.025)
    return {"decisive_tasks": decisive, "expected_wins": decisive / 2, "wins_low": low, "wins_high": high,
            "p_at_least": round(sum(pmf[min(wins, decisive):]), 3)}


def noise_line(loaded):
    decisive = loaded["with_wins"] + loaded["without_wins"]
    nf = noise_floor(decisive, loaded["with_wins"])
    if not decisive:
        return "noise floor: no decisive tasks (every loaded-only task tied), so there is no win count to compare with chance"
    return (f"noise floor: of {decisive} decisive tasks a skill with no effect wins {nf['wins_low']} to {nf['wins_high']} "
            f"(95% of runs, {nf['expected_wins']:g} on average); this run won {loaded['with_wins']} "
            f"(chance of at least that: {nf['p_at_least']:.2f}). A gap inside that range is not evidence either way.")


def tally_text(t):
    return f"with {t['with_wins']} / without {t['without_wins']} / ties {t['ties']}"


def gate_line_v2(skill, summary):
    g, loaded = summary["gate"], summary["loaded"]
    mean = (f"mean rubric {g['mean_rubric_with']} vs {g['mean_rubric_without']} ({g['mean_advantage']:+.3f}, "
            f"tolerance {g['tolerance']})") if loaded["tasks_with_loaded_sample"] else "no loaded samples to score"
    return "\n".join([
        f"{g['decision'].upper()} {skill}: loaded-only {tally_text(loaded)} over {loaded['tasks_with_loaded_sample']} tasks, {mean}",
        f"  all samples: {tally_text(summary)} over {summary['samples']} samples per arm; skill loaded in "
        f"{loaded['loaded_samples']} of {loaded['total_samples']} with-skill samples",
        f"  gate: {g['reason']}",
        f"  {noise_line(loaded)}"])


def pmap(fn, items, concurrency):
    with ThreadPoolExecutor(max_workers=max(1, concurrency)) as pool:
        return list(pool.map(fn, items))
