# ui-polish-pass held-out run before the page-and-focus reference

Evidence only. This is the shipped held-out result for ui-polish-pass as of base commit 4ae8adbf, replaced in place when the page-and-focus access reference was added and the held-out suite was rerun.

- Generator Sonnet, judge Opus, installed mode, 3 samples per arm, 10 tasks, 2026-10-27, suite_hash 9691a58d2b29bb24 (the tasks and rubrics are unchanged in the rerun).
- Loaded-only: with 7 wins, without 2, 0 ties over 9 tasks; mean rubric 3.867 with, 3.5 without. All samples: 7 / 3 / 0. Gate: pass.
- Cross-model check, Haiku (the `secondary` block): loaded-only 2 / 0 / 2 over 4 tasks, mean rubric 3.159 with, 2.892 without; all samples 4 / 3 / 3.
- Only results.json is kept. The generated answers and judgments for this run are in git history at 4ae8adbf under evals/ui-polish-pass/heldout/runs/.
