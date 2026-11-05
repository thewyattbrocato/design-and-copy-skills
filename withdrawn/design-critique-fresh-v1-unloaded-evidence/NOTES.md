# design-critique: accessibility-review reference and AI-features pass, shelved

Evidence only. Built and tested, not shipped.

- Committed-suite rerun (sonnet, judge claude:opus, installed, 3 samples, seed 0): passed. Loaded-only 7 wins, 0 losses, 1 tie over 8 tasks, mean rubric 4.382 vs 4.007 (+0.375) against the committed 7/0/2 and +0.45. Its results file is in `committed-rerun/`.
- Fresh blind set (10 tasks, 3 guards, same settings): inconclusive. The skill loaded in 9 of 30 with-skill samples and on 3 of 10 tasks; the gate needs 6. Loaded-only 3 wins, 0 losses over 3 tasks, rubric 4.454 vs 3.663. All samples: with 3, without 2, ties 5.
- Under the not-worse rule a fail on the fresh set ships nothing. The skill text was reverted; the reference and pass were not merged.
