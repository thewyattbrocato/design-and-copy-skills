# Eval layout

Each skill with evals has a folder `evals/<skill-name>/` with up to two suites. The held-out suite is the one every skill has;
the dev suite exists for only a few older skills:

```
evals/<skill>/tasks.json            dev suite: tasks the skill writers saw
evals/<skill>/results.json          dev results
evals/<skill>/runs/<task>/          dev answers and judgments
evals/<skill>/heldout/tasks.json    held-out suite: written without reading the skill
evals/<skill>/heldout/results.json  held-out results
evals/<skill>/heldout/runs/<task>/  held-out answers and judgments
```

`scripts/validate_evals.py` checks both suites. `heldout` is not a skill folder. An `evals/` directory with no
skill folders is valid. Both files have the same format below; `tasks.json` is required in a suite that exists.

## runs/

`runs/<task-id>/` holds `with.md` or `with.html` and `without.md` or `without.html` (`.html` for build tasks only; every other kind, `write` included, is a `.md` text answer), plus
`*.meta.json`, `judgment.json` and screenshots. Under protocol 2 the first sample keeps those names and sample k
after it adds `.s<k>` before the extension (`with.s1.md`, `without.s2.html`, `with.s1.meta.json`, `judgment.s1.json`,
`with.s1.png`); a `--secondary-model` run keeps the same names under `runs/<task-id>/secondary/`. Every run folder must contain both answer files for every sample, because a verdict
cannot be re-read without them. For a held-out suite every verdict also needs its run folder. A dev results file
with `summary.superseded: true` may have missing answer files; the validator reports them as warnings.

## tasks.json

A list of 8 to 10 task objects:

```json
{
  "id": "spacing-01",
  "kind": "critique",
  "prompt": "The request given to the model, verbatim.",
  "rubric": ["One observable criterion per string.", "Another criterion."]
}
```

- `id`: non-empty, unique within the file.
- `kind`: one of `build`, `critique`, `choose`, `layout`, `polish`, `explain`, `write`. Only `build` returns an HTML page and is judged from a screenshot; all other kinds are text answers judged as text. `write` drafts new text from a brief. With `fact_sheet: true` its `prompt` includes a fact sheet (the only facts the draft may use), so a judge can see an invented claim, and its `rubric` should check the draft against that sheet.
- `prompt`: non-empty string.
- `rubric`: non-empty list of non-empty strings.
- `fact_sheet` (`write` tasks only, boolean): `true` when the prompt carries a fact sheet, `false` when the brief supplies no facts, so the draft can only be honest by not inventing any. Required on every write task of a suite whose results are protocol 2; optional before that.
- `pressure` (`write` tasks only, boolean, default false): the user insists on an invented fact or a deceptive tactic. The prompt states the demand the way a person would; the rubric checks that the draft does not comply with the part that is untrue.

A held-out suite for a copy skill (a skill under `copy-skills/`) must, under protocol 2, contain at least 4 tasks with `fact_sheet: false` and at least 2 with `pressure: true`. Design skills are exempt from that count.

## results.json

```json
{
  "verdicts": [
    {
      "task_id": "spacing-01",
      "winner": "with",
      "judge_notes": "Why the judge preferred this side.",
      "rubric_scores": {"with": 4, "without": 2}
    }
  ],
  "summary": {
    "with_wins": 1,
    "without_wins": 0,
    "ties": 0,
    "model": "model identifier used for the runs",
    "date": "2026-01-31"
  }
}
```

- One verdict per task in `tasks.json`, no extras. `task_id` must match a task.
- `winner`: `with` (skill loaded), `without` (baseline) or `tie`.
- `rubric_scores`: numbers for each side.
- `summary` counts must equal the tallies of the verdicts. `date` is `YYYY-MM-DD`.

## Fields written by `scripts/run_eval.py`

All optional, validated when present. Per verdict: `rubric_items` (`{with: [...], without: [...]}`, mean score per
rubric item over both judge passes), `position_consistent` (both swapped passes agreed), `passes` (the two
de-blinded judgments with `order`, `raw_verdict`, `winner`, `notes`) and `with_skill_invoked` (installed mode).
In `summary`: `judge` (`claude:<model>` or `grok:<model>`), `same_model_judge` (true when the judge was the
generator's own model), `suite` (`dev` or `heldout`, must match the folder), `mode` (`installed` or `injected`),
`seed`, `model_id`, `superseded` (bool, dev only) with `superseded_note`, and `gate`:

```json
"gate": {"passed": true, "tolerance": 0.1, "mean_rubric_with": 4.2, "mean_rubric_without": 3.6}
```

For a protocol 1 file, `gate.passed` must equal `with_wins >= without_wins and mean_rubric_with >= mean_rubric_without - tolerance`;
the validator recomputes it. A rubric score is the mean of the 1-5 item scores over both passes.

## Held-out results

A `heldout/results.json` must record `summary.judge`, must not have `same_model_judge: true`, must not name a judge
that is the same model as `model_id` (`claude:sonnet` against `claude-sonnet-5-5` counts), and cannot be marked
`superseded`.

## Protocol 2

Results written by `scripts/run_eval.py` since protocol 2 carry `summary.protocol: 2`. A file with no `protocol`, or
`protocol: 1`, is a protocol 1 file (one answer per arm per task) and keeps its original format and gate; nothing
above changes for it. Protocol 2 adds:

- `summary.samples`: answers per arm per task. `summary.suite_hash`: a hash of `tasks.json`'s content (whitespace
  does not matter). `summary.with_wins`, `without_wins` and `ties` are task counts, each task decided by the
  majority of its samples (more than half; a tie when no arm has that).
- Per verdict: `samples`, one record per sample with `sample` (0-based), `winner`, `rubric_scores`, `rubric_items`,
  `position_consistent`, `judge_notes`, `loaded` and `not_loaded` (opposites; the WITH sample used the skill or not),
  and `attempts` (1 to 3; a sample that did not load is regenerated up to twice and flagged `not_loaded` only
  after three attempts). The verdict's `winner` and `rubric_scores` are the majority and the mean over all samples;
  `loaded_winner`, `loaded_rubric_scores` and `loaded_samples` are the same over loaded samples only
  (`null` when the task has none).
- `summary.loaded`: the loaded-only tally, which the gate reads: `with_wins`, `without_wins`, `ties` (over tasks, by
  `loaded_winner`), `tasks_with_loaded_sample`, `loaded_samples`, `total_samples`, `mean_rubric_with`,
  `mean_rubric_without` and `mean_advantage` (means over tasks that have a loaded sample).
- `summary.gate`: `decision` (`pass`, `fail` or `inconclusive`), `passed` (true only for `pass`), `tolerance`,
  `min_advantage` (0.15), `min_loaded_tasks` (6), the loaded-only means and `reason`. Rules, in order:
  `inconclusive` when `tasks_with_loaded_sample < 6` (an absolute count, so an 8-task suite needs 6 of 8); otherwise
  `pass` when (`with_wins > without_wins` or (`with_wins >= without_wins` and `mean_advantage >= 0.15`)) and
  `mean_rubric_with >= mean_rubric_without - tolerance`; otherwise `fail`. The validator recomputes all of it from the
  samples, so a hand-edited result will not pass.
- `secondary` (optional, top level): `{summary, verdicts}` for the same suite run by a weaker generator
  (`--secondary-model`). Its summary has `model`, `samples` and the same tallies and `loaded` block as the primary
  one, and no `gate`; it is reported and never decides anything.
