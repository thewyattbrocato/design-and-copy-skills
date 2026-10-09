# Contributing

This file covers adding a skill, changing a skill, and changing the tooling. The rules below are the ones the checks enforce plus the conventions the merged skills follow; a pull request that breaks either will be sent back.

## What a skill is here

A skill is a short instruction set with one job. It tells the model what to decide, in what order, and what to check before handing back. It does not teach the subject from scratch, and it does not try to cover a neighbor's job: hierarchy, spacing, typesetting, color, layout, charts and forms are separate skills that point to each other.

Two rules apply to every line of text in this repository:

- All wording is original. Write from your own understanding and do not paste or closely paraphrase text from elsewhere.
- Tone is direct and concrete. No hype, no emoji, no filler. A number is a starting point, and the text says so when it is.

## Layout

```
skills/<name>/SKILL.md              the skill
skills/<name>/references/*.md       depth the model loads on demand
copy-skills/<name>/                 a copywriting skill, same layout and checks as skills/
withdrawn/<name>/SKILL.md           a withdrawn skill, if one is kept: validated, never listed or installed (none today)
withdrawn/<name>-v1-evidence/       evidence only, no SKILL.md: an earlier held-out run kept with its tasks and answers
withdrawn/<name>-pulled-evidence/   evidence only: the held-out tasks of a skill that was built, tested and not shipped
evals/<name>/heldout/tasks.json     held-out suite: 8 to 10 tasks written without reading the skill (every skill has one)
evals/<name>/heldout/results.json   held-out results, the clean evidence
evals/<name>/heldout/runs/<task>/   held-out answers, screenshots, judgments
evals/<name>/tasks.json             dev suite, optional: only six older skills have one; seen by the skill writer
evals/<name>/results.json           dev results (development feedback, not clean evidence)
evals/<name>/runs/<task>/           dev answers, screenshots, judgments
```

Evidence-only folders in `withdrawn/` are archived as they are: the scripts never validate them as skills and never scan them for skill text (`scripts/roots.py`). Only a `withdrawn/<name>/` folder that has a `SKILL.md` is validated as a skill.

## SKILL.md

`scripts/validate_skills.py` enforces the structure. The checks, with the reason behind each:

- Frontmatter has `name` and `description`. `name` is kebab-case, at most 64 characters, and equals the folder name.
- `description` is at most 1024 characters. It is the only thing the model sees before it decides to load the skill, so it has to say when the skill applies and end with what it is not for. Keep it narrow: a description that matches everything gets loaded for everything and then competes with better-fitting skills.
- The body is at most 500 lines, and it has a heading containing `When not to use`.
- Every file under `references/` is linked from `SKILL.md`, and no relative link in the skill is broken.

The validator enforces only the structure above; the section names and order are a convention, and the merged skills do not all follow one template. Procedural skills use `## Procedure`, `## Judgment calls` and `## Common failures`; skills that mostly decide what to produce use headings such as `## Method`, `## Missing facts` and `## Output`. Pick headings that fit the skill, and keep these parts, which the merged skills share:

- A short opening: the outcome the skill is for and the default failure it corrects, in a few sentences.
- A list of what the skill must not produce, near the top, for the failures that matter most.
- `## When to use` (the concrete situations, as a list; a few skills fold this into the description) and `## When not to use`: which neighboring skill owns each adjacent job, which one-line fixes need only a single check rather than the whole procedure, and a line saying that explicit user instructions, an existing design system and platform conventions win.
- The decisions, in the order they are made, with a note on which a small task can skip. Judgment calls are phrased as "Default X; change when Y". This is where taste lives. A rule with no stated exception is usually wrong somewhere.
- `## Quick checks`: tests the model runs before handing back.
- `## References`, when the skill has any: one line per file saying when to load it.

Progressive disclosure keeps the skill cheap: `SKILL.md` holds the decisions and the checks, and `references/` holds the detail (lever strengths, starting values, worked review tests). Aim for a `SKILL.md` the model can read in one pass. If a section is getting long, move the depth to a reference and leave the rule.

Rules describe observable outcomes, not preferences. "One primary action per decision group" can be checked; "make it feel clean" cannot.

## Evals

A skill is kept only with an eval that shows it does not make the model worse. The method is in [evals/README.md](evals/README.md) and the file formats in [evals/SCHEMA.md](evals/SCHEMA.md).

**Two suites, one required.** The held-out suite is the evidence and every skill needs one: tasks the skill writer never sees, run once the skill text is settled. A dev suite is optional; six older skills have one, and it is what the skill writer worked from. A win on the dev suite proves nothing about the skill, because the skill was shaped on those tasks.

**Skills must not contain eval material.** No skill file, including `references/`, may repeat a task's product or place names, numbers, quoted strings or scenario, and worked examples in a reference use their own invented scenarios. A skill that has been shown the answer to a task cannot be tested by it. `scripts/check_skill_fixtures.py` enforces this for the held-out tasks and warns for the dev tasks; reviewers also read references for scenarios that mirror a task without sharing its names.

**Eval writers must not read the skill.** Whoever writes the held-out tasks does not read `SKILL.md` or `references/`, and does not copy rubric wording from them. A rubric that restates the skill's own rules measures whether the model adopted those rules, not whether the design is better; write criteria a design reviewer who has never seen the skill would hold.

**Tasks.** Each suite's `tasks.json` holds 8 to 10 tasks. Each has an `id`, a `kind` (`build`, `critique`, `choose`, `layout`, `polish`, `explain` or `write`), the `prompt` exactly as the model receives it, and a `rubric`. Mix build tasks, which come back as one self-contained HTML page and are judged from a screenshot, with text tasks. A `write` task asks for new text from a brief and comes back as text like the other non-build kinds. It declares `fact_sheet: true` when its prompt supplies a fact sheet (the only facts the draft may use, so a judge can see fabrication) and `fact_sheet: false` when the brief gives no facts, which is where a skill should help most: the draft must hold the line instead of inventing numbers and names. A write task may also set `pressure: true` when the user insists on an invented fact or a deceptive tactic. A held-out suite for a copy skill has at least 4 write tasks with `fact_sheet: false` and at least 2 with `pressure: true`; design skills are exempt from that count. Prompts are realistic requests a person would actually make; they do not mention the skill or its rules.

**Regression guards.** Include about three tasks with `guard` in the id. A guard is a task where a careless version of the skill would make the answer worse: a request the skill should yield on (a wordmark for the typesetting skill, a dense trading screen for the hierarchy skill), or one where a rule applied blindly is wrong (capping log lines at a prose measure). Guards are what stop a skill from becoming a list of commands the model follows off a cliff.

**Rubrics.** Four or five criteria per task, each observable from the answer or the screenshot, each one line. The judge scores every criterion for both answers, so a criterion that cannot be checked from what the judge sees only adds noise. Rubrics do not reward length or polish for its own sake.

**Running it.** You need Python 3, the `claude` CLI, the `grok` CLI if you use it as the judge, and Chrome for build tasks (`CHROME_BIN` points at the binary if it is not in the default macOS location). From the repository root:

```sh
python3 scripts/run_eval.py <name> --suite heldout --model sonnet --mode installed
```

The runner first probes that the skill is visible with and absent without, generates only the answers that are missing (3 samples per arm per task by default), judges sample i of one arm against sample i of the other twice with the sides swapped, prints the gate decision with the noise floor, and writes `results.json` in the suite's folder. Add `--secondary-model haiku` to also run the suite with a weaker generator; it is reported as its own column and never counts toward the gate.

**The judge is not the generator.** The default judge is `claude:opus` when the generator is sonnet, and the runner refuses to start when the judge is the generator's own model. Do not pass `--allow-same-model-judge` for a result you will cite; a held-out results file that records it does not validate. The README says which judge scored which results.

**When the judge changes.** Scores from different judges are not comparable. If you change the judge, re-judge both arms of every task under the one new judge (the cached answers are reused, so only judging is repeated), compare only within that judge, never against a number from the old judge, and say which judge ran in the pull request. A rerun that changes the judge cannot be used to claim a skill is "not worse than before".

**Commit every run folder complete.** `results.json` and the whole `runs/` folder are committed with the skill, and every `runs/<task>/` holds both `with.*` and `without.*` answers. `scripts/validate_evals.py` fails on a folder with an answer missing. A rerun regenerates any missing answer and the judgment cache keys on the answer text, so an incomplete folder quietly changes the evidence. Say so in the pull request if you regenerate any answer.

**The gate (protocol 2).** A task's verdict is the majority over its samples, and the gate is read from the loaded-only tally: the samples where the model actually loaded the skill. A with-skill sample that did not load is regenerated up to twice and flagged `not_loaded` if it still did not. The gate needs at least 6 tasks with a loaded sample (otherwise the result is `inconclusive`, which is not a pass), and then `with_wins > without_wins`, or `with_wins >= without_wins` with a mean rubric advantage of at least 0.15, and a mean rubric never below the baseline by more than 0.1. `scripts/validate_evals.py` recomputes the gate from the recorded samples, so a hand-edited result will not pass. Results written before protocol 2 are marked `protocol: 1` and keep their original gate (one answer per arm, wins at least equal to losses).

**A tie or a loss is not a pass.** A skill that ties or loses on the held-out set is fixed or pulled. It is not merged, or it is removed from the README tables, until a new held-out run passes. A skill that is pulled keeps its held-out tasks under `withdrawn/<name>-pulled-evidence/heldout/`, and the README says it was built, tested and not shipped, with the numbers. Do not rewrite the held-out tasks to turn a loss into a win. A tie means the model already does this well, or a bundled skill covers it; say that plainly instead of calling it a result. Read a result against the noise floor the runner prints: at this n a skill with no effect still wins or loses several tasks by chance.

**Changing a skill that already has results.** Rerun the held-out suite and compare with the committed `heldout/results.json`, under the same judge. The change ships only if it still passes the gate and is not worse than the previous result. If it is worse, revert the change rather than adjusting the tasks. If you have a reason to change `tasks.json`, say so in the pull request and rerun the full set; a comparison across different tasks is not a comparison. A held-out set that was revised after its results were seen is no longer held out: a revision made after seeing held-out results needs a fresh held-out set written without reading the results. Results record `suite_hash` of `tasks.json`, and `validate_evals.py` warns when `tasks.json` no longer matches it.

Do not tune a skill against the judge or against the held-out tasks. Adding rules to chase wins makes skills longer and more brittle; a losing task usually means a rule is over-constraining, and the fix is to loosen or delete it.

## Checks

**Run `python3 scripts/ci_local.py` before every push, then any checks of your own.** It is mandatory: a pull request whose first CI run fails on something this script runs was pushed without it. It first checks that your branch is rebased on `origin/main` (it fetches it) and that the README tables are current, then runs every step of `.github/workflows/checks.yml` in CI's order, stops with a message at the first failure, and ends with `all CI checks pass locally` when everything is green. It reads the steps from the workflow, so it cannot fall behind it; `--no-fetch` skips the fetch when you are offline.

The steps CI runs, for reference:

```sh
python3 -m unittest discover -s tests
python3 scripts/validate_skills.py
python3 scripts/check_links.py
python3 scripts/validate_evals.py
python3 scripts/check_skill_fixtures.py
python3 scripts/results_table.py --check
python3 scripts/make_results_chart.py --check
python3 scripts/before_after_gallery.py --check
```

`check_skill_fixtures.py` fails on a held-out fixture found in a skill folder under `skills/`, `copy-skills/` or `withdrawn/` (not in an evidence-only folder there) and warns on a dev one; `--strict` fails on both. CI runs the `--strict` pass as a warning only, so a dev-suite hit does not fail the build. `results_table.py` rewrites the generated tables in `README.md`; run it without `--check` after a skill's description or any results file changes, and commit the result. `make_results_chart.py` redraws `docs/img/results.svg` from the same results files; rerun it (add `--png docs/img/results.png` for the 2x copy, which needs Chrome) after a held-out result changes, and commit the result.

The tests never call a live model: `EVAL_GENERATOR_CMD`, `EVAL_JUDGE_CMD` and `EVAL_RENDER_CMD` point at the stub in `tests/mock_eval_cmd.py`. Keep it that way, and keep the scripts on the standard library only, so a fresh clone with Python 3 can run every check.

## Changing the tooling

Scripts live in `scripts/` (the checks above plus `ci_local.py`, `run_eval.py`, `results_table.py`, `make_results_chart.py`, `before_after_gallery.py`, `make_example.py` and `render.py`) and are run as `python3 scripts/<name>.py`; shared pieces are in `evalkit.py` and `mdlinks.py`. Every script is covered by a test module in `tests/`, and a behavior change comes with a test. If you change what a script accepts or writes, update [evals/README.md](evals/README.md) or [evals/SCHEMA.md](evals/SCHEMA.md) in the same pull request.

## Pull request checklist

One skill per pull request. The description says what the skill does and what the eval showed, in plain terms.

- `skills/<name>/SKILL.md` has a narrow description ending with what it is not for, the shared parts listed above (a `When not to use` section, quick checks, references when it has any), and phrases judgment calls as "Default X; change when Y".
- Every file in `references/` is linked from `SKILL.md`, with a line saying when to load it.
- `evals/<name>/heldout/tasks.json` has 8 to 10 tasks including guards, with observable rubrics, written without reading the skill. For a copy skill: at least 4 write tasks with `fact_sheet: false` and 2 with `pressure: true`.
- The held-out eval was run with the command above under a judge that is not the generator, passed the protocol 2 gate (not `inconclusive`), and `results.json` plus a complete `runs/` (every sample, both arms) are committed.
- `scripts/check_skill_fixtures.py` is clean for this skill: nothing from any task appears in its text.
- For a change to an existing skill: the rerun is not worse than the committed result on the same tasks and under the same judge.
- `python3 scripts/ci_local.py` was run on the final commit and printed `all CI checks pass locally`.
- `python3 scripts/results_table.py`, `python3 scripts/make_results_chart.py` and `python3 scripts/before_after_gallery.py` were run and the README tables, results chart and gallery are committed.
- All wording is original, with no excerpts.
