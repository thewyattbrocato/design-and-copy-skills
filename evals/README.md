# Evals

The library's promise is that a skill never makes the model worse, and a skill that should clearly help has to show
that it does. Every skill with evals has to show it: the same model answers the same realistic tasks several times
without the skill and with it, a judge model that is not the generator compares the pairs blind, and the skill ships
only if the with-skill side wins on tasks its writers never saw, counting only the answers where the model actually
used the skill. This page describes protocol 2. Results written before it are marked `protocol: 1` (one answer per
arm per task, a gate that a tie passed) and stay as they are; they validate under their own rules.

## Method

**Two suites.** Every skill has a **heldout** suite (`evals/<skill>/heldout/tasks.json`,
`heldout/results.json`, `heldout/runs/`) written by someone who did not read the skill. A few older skills also have a
**dev** suite (`evals/<skill>/tasks.json`, `results.json`, `runs/`) that the skill writers saw while writing and refining
the skill. Only held-out results are clean evidence; a dev result is development feedback. `--suite dev|heldout` selects one, and held-out is the default
when `heldout/tasks.json` exists. Everything below applies to both suites.

**Task set.** `evals/<skill>/tasks.json` holds 8 to 10 realistic design requests (build a hero, critique a
screenshot, pick a type pairing, lay out a dashboard, design a form, plan motion for a state change). Each task
has an `id`, a `kind`, the `prompt` exactly as the model receives it, and a `rubric` of observable criteria.
Tasks of kind `build` must come back as one self-contained HTML file; everything else is a text answer.
Format and field rules are in [SCHEMA.md](SCHEMA.md).

**Two arms, one prompt.** The WITHOUT and WITH answers use the identical prompt, model and settings. Only the skill differs.

**Samples.** Each arm answers each task `--samples N` times (default 3). Sample i of one arm is judged against
sample i of the other, and a task's verdict is the majority over its samples: an arm must win more than half of them,
otherwise the task is a tie. Every sample's verdict and score is recorded.

**Loaded-only accounting.** In installed mode the model decides whether to load the skill, and a WITH answer produced
without it is just a second sample of the baseline. The runner records per sample whether the skill loaded. A WITH
sample that did not load is regenerated, up to two more times, and flagged `not_loaded` if it still did not. The
summary has two tallies: all samples, and loaded-only (only the samples where the skill loaded). The gate reads the
loaded-only one. In injected mode the skill is part of the system prompt, so every sample counts as loaded.

**Blind pairwise judging.** A judge model that is not the generator sees the request, the rubric and two anonymous answers.
Which arm is shown as A or B is a seeded coin flip per task and is recorded. The judge returns a verdict
(`A`, `B` or `tie`), brief notes and a 1 to 5 score for every rubric item for both answers. The harness then
de-blinds the result. Build answers are rendered to PNG; the judge reads the screenshot from a scratch folder
where the files are named `a.png` and `b.png`, so no path hints at the arm.

**Swap control.** Every task is judged twice with the sides swapped. A win counts only when both passes pick the
same arm; any disagreement (including a win in one pass and a tie in the other) is recorded as a tie. Rubric
scores are averaged over the two passes.

**Ship gate (protocol 2).** On the loaded-only tally:

- fewer than 6 tasks with a loaded sample: `inconclusive`, which is not a pass (the count is absolute, so an 8-task
  suite needs 6 of 8);
- otherwise `pass` when `with_wins > without_wins`, or `with_wins >= without_wins` and the mean rubric advantage is at
  least 0.15; and the mean rubric with the skill is never below the baseline by more than the tolerance (default
  0.1, recorded in `results.json`);
- otherwise `fail`. A tie on wins and losses is therefore not a pass for a skill that should clearly help, unless the
  rubric advantage is there.

The runner prints the decision with its reason, both tallies and the noise floor, and exits 0 on `pass` and 1 on
`fail` or `inconclusive`.

**Noise floor.** Chance moves these numbers more than people expect. If a skill has no effect, each decisive task (a
task that is not a tie) goes either way like a coin flip, so with 9 decisive tasks it wins anywhere from 2 to 7 of
them in 95% of runs, and 6 wins to 3 losses is nothing unusual. The runner prints that range for the run's own number
of decisive tasks, and the chance of at least the observed wins. A gap inside the range is not evidence in either
direction. More samples shrink the noise within each task, not the number of tasks, so the gate also asks for a
rubric advantage when wins and losses are level.

**Secondary row.** `--secondary-model haiku` runs the same suite, samples and judge with a weaker generator and
records it under `secondary` in the same results file. It is reported (its own README column), never gated, and
a rerun without the flag drops it from `results.json` (the answers stay in `runs/<task>/secondary/`).

**Fresh held-out sets.** Results record `suite_hash`, a hash of `tasks.json`. If the tasks change without a new
results run, `scripts/validate_evals.py` warns. A held-out set whose tasks or rubrics were revised after its results
were seen is no longer held out: a revision made after seeing held-out results requires a fresh held-out set, not an
edited one.

## Running it

```
python3 scripts/run_eval.py <skill-name> [--suite dev|heldout] [--model sonnet] [--judge claude:opus]
    [--samples 3] [--secondary-model haiku] [--allow-same-model-judge] [--mode installed|injected]
    [--concurrency 2] [--seed 0] [--tasks id,id] [--effort low] [--tolerance 0.1] [--timeout 600] [--dry-run]
```

- `--mode installed` (default, the faithful one): the WITH run copies `skills/<skill>/` (or `copy-skills/<skill>/`) into a temporary
  project's `.claude/skills/` and the WITHOUT run uses an empty project. Both run from that temporary
  directory with only the project settings source, so personal skills and memory do not leak in. Before any
  generation a probe asks the model to list its skills in each arm (twice) and fails the run unless the skill
  is visible WITH, absent WITHOUT, and everything else is identical and repeatable.
- `--mode injected`: no skill folder; the SKILL.md body is appended to the system prompt for the WITH run.
- `--suite dev|heldout`: which task set to run. Held-out when `evals/<skill>/heldout/tasks.json` exists, else dev.
  Answers, judgments and results stay inside the chosen suite's folder.
- `--judge claude:<model>` or `--judge grok:<model>`. Generation uses `claude`; model names are whatever the CLI accepts.
  The default is `claude:opus` (`claude:sonnet` when the generator is an opus model). The runner refuses to start,
  exit code 2 and before any model call, when the judge is the generator's own model; `sonnet` and
  `claude-sonnet-5-5` count as the same model. `--allow-same-model-judge` overrides that for experiments. The
  result records `judge` and `same_model_judge`, and the validator rejects a held-out results file whose judge is
  the generator.
- `--samples N`: answers per arm per task. Raising it on a finished run adds only the new samples. A WITH sample that
  did not load the skill (installed mode) is regenerated up to twice; the attempts are recorded in its meta file.
- Re-running is cheap: finished answers (`runs/<task>/{with,without}.{md,html}`, and `.s<k>` for later samples) and
  judgments (`runs/<task>/judgment.json`, keyed by judge, seed and answer content) are reused, so only missing work runs.
  Delete a file to redo it. Run folders are committed next to `results.json` so a verdict can be re-read.
- `--tasks a,b` runs a subset and prints the gate line without writing `results.json`.
- `--dry-run` lists the tasks, what is cached and the blind order, and calls nothing.
- `--allow-small` accepts fewer than 8 tasks; it exists for smoke tests on a throwaway skill, not for real runs.
- Exit code: 0 when the gate passes, 1 when it fails or is inconclusive, 2 on an error (missing skill, invalid tasks, a CLI that
  did not answer). Errors are printed with an `error:` prefix on stderr.

Check that no skill text repeats a task with `python3 scripts/check_skill_fixtures.py` (see below).
`python3 scripts/results_table.py` regenerates the README tables from the results files.

`results.json` extends the format in SCHEMA.md with per-item rubric scores, both judge passes, the judge, mode,
seed, model and the gate numbers, so a verdict can be audited and the gate recomputed.

### Keeping the skills and the tasks apart

`scripts/check_skill_fixtures.py` pulls distinctive strings out of every `tasks.json` prompt and rubric (quoted
strings, capitalized product and place names, specific numbers, counts and listed values, URL paths) and fails with
file and line when one appears in any file of a skill folder: `skills/`, `copy-skills/`, and any skill folder under
`withdrawn/` that has a `SKILL.md` (evidence-only folders there are archived answers, not skill text, and are skipped).
Held-out hits always fail. Dev-suite hits are printed
as warnings, because the dev tasks predate the guard and the skills are being cleaned of them; `--strict` makes them
fail too, and `--list` prints what was extracted. Ordinary design values such as `14px` or `1.5` are too common to
count, so the guard is a floor, not proof: a reviewer still reads a skill's references for scenarios that mirror a
task without sharing its names.

When the judge changes, re-judge both arms of every task under the one new judge and compare only within that judge;
never set a number from one judge next to a number from another. State the judge in the pull request. The cached
answers are reused, so only the judging is repeated.

### Rendering

`scripts/render.py <html> <out.png> [--width 1280 --height 800]` takes a headless Chrome screenshot. It looks
for Chrome at `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`; set `CHROME_BIN` to a Chrome or
Chromium binary anywhere else, including on Linux. It is offline: every
non-local host is blocked, so remote fonts, scripts and images never load and pages that rely on them fall back
to system fonts. Generated pages must therefore use system or open-licensed fonts shipped locally and avoid
time-dependent content. The device scale is fixed, so the same page gives the same PNG.

### Before-and-after examples

`scripts/make_example.py <config.json>` produces the showcase images:

```json
{"model": "sonnet", "mode": "installed", "runs": 1, "judge": "claude:opus", "effort": null,
 "width": 1280, "height": 800,
 "examples": [{"id": "landing-hero", "skill": "<skill-name>", "prompt": "The exact request."}]}
```

For each example it runs the same model on the same prompt once without and once with the skill, renders both,
and writes `docs/examples/<id>/` with `without.png`, `with.png`, a side-by-side `compare.png`, the generated
`without.html` and `with.html`, and `meta.json` (exact prompt, model, date, mode, run policy). Images are scaled
to at most 1000px wide and about 250 KB (PNG, JPEG only if a PNG will not fit). Nothing is edited by hand.
With `runs: 1` the single answer per arm is used as is. With `runs: N` it picks the answer per arm with the
highest blind absolute score from the judge model, which never sees the arm, and `meta.json` records all scores.

## Headless CLI usage (verified)

- Generation: `claude -p <prompt> --model <m> --output-format stream-json --verbose --setting-sources project
  --strict-mcp-config --no-session-persistence --tools Skill,Read`, run with stdin closed and from the temporary
  project directory. `--tools Skill,Read` gives both arms the same tools; the stream shows whether the model
  actually invoked the skill (recorded as `with_skill_invoked`). Add `--effort low` for quick runs.
- `--strict-mcp-config` is required. Without it, account-level connectors load into every call and a trivial
  prompt costs hundreds of thousands of tokens.
- `--tools ""` hides all skills, so it is only used in injected mode. `--safe-mode` breaks JSON output; do not use it.
- Built-in bundled skills of the CLI are present in both arms; the probe checks the two arms differ only by the skill under test.
- Judge, claude: `claude -p <prompt> --model <m> --tools Read --setting-sources project --strict-mcp-config
  --no-session-persistence` from a scratch folder holding `a.png`/`b.png`. It reads images through the Read tool.
- Judge, grok: `grok -p <prompt> --output-format plain --cwd <scratch> -m <model>`. It also reads images given by file name
  and is noticeably slower.

## Tests

`python3 -m unittest discover -s tests` never calls a live model and needs nothing beyond Python 3.
`EVAL_GENERATOR_CMD`, `EVAL_JUDGE_CMD` and `EVAL_RENDER_CMD` select stub executables (see
`tests/mock_eval_cmd.py`) that take one JSON object on stdin and print the answer; the tests cover blind
assignment and de-blinding, the swap tie rule, sampling and majority verdicts, loaded-only gating, regeneration of
samples that did not load, the inconclusive case, the schema rules and the gate, resumable caching and the output
schema. `scripts/ci_local.py` runs the CI workflow's steps locally; a test fails when the workflow and the script
drift apart. The one test
that drives real Chrome is skipped when Chrome is not installed.

## Honest limits

- One judge model per run; judges have their own taste and can favor longer or more polished-looking answers.
  Run a second judge (`--judge grok:...`) before trusting a close result. Early dev results were judged by
  `grok:grok-4.7`; the three refinements by `claude:sonnet`, which is the generator's own model. The runner now
  prevents that for new runs.
- The dev suite was seen by the skill writers, and some skill references mirrored its tasks. Treat dev results as
  superseded; the held-out suite is the evidence.
- Rubrics are written next to the skill and some criteria echo its rules, so an eval partly measures adoption of
  those rules. Guard tasks, where a rule applied blindly is wrong, are the counterweight.
- Noise floor: 8 to 10 tasks cannot detect small effects. With about 9 decisive tasks a skill with no effect wins 2
  to 7 of them by chance, so a few more wins than losses is inside the noise. Samples average out the model's
  run-to-run variation within a task but do not add tasks. The runner prints the range for each run; a gap inside it
  is not a result.
- Model nondeterminism: samples reduce it but do not remove it; rerunning with a different seed or fresh answers
  can still move a close result. The seed fixes the A/B assignment only, not the model. Protocol 1 files have one
  sample per task per arm and are noisier still.
- A held-out set revised after its results were seen is not held out. Revising it requires a fresh held-out set;
  the validator warns when `tasks.json` no longer matches the recorded `suite_hash`.
- In installed mode a skill only helps if the model chooses to invoke it. Protocol 2 gates on the samples where it
  did and reports how many that was; a skill the model rarely loads can still come out `inconclusive`. Protocol 1
  recorded `with_skill_invoked` per task but counted every pair.
- The secondary row (a weaker generator) shows whether a result holds on a smaller model. It is not part of the gate.
- A bundled skill of the CLI that covers the same ground is available to both arms and can fire in the baseline arm. The
  comparison is then against the model using that skill, not against a bare model, and a tie can mean the skill under test
  adds little beyond it. The `skills_invoked` list in each arm's meta file shows what each side actually used.
- Screenshots are a fixed viewport, so below-the-fold content and interaction are not judged.
