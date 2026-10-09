# Report format

For full reviews, audits and scored reviews. A small ask uses the verdict and a few findings, then stops.

## Order

1. **Verdict.** One to three sentences: does it do its job, the biggest problem, the biggest strength. The overall score goes here if scored.
2. **Scores** (only when scoring applies). Fidelity and assumptions in one line, then a compact table: dimension, 0 to 4, one-line reason.
3. **Top findings.** Five to ten, ranked by severity then reach. Group repeats with a count.
4. **What works.** Two to four decisions to keep and why.
5. **Limits and open questions.** What could not be assessed, what would change the verdict, whether to watch people try it.
6. **Appendix.** Minor and polish items as short lines, grouped by area.

## Finding

- **Title** in plain words, with a severity label.
- **Seen:** the element and what is on screen, with a number where one exists.
- **Why it matters:** who is affected and what goes wrong.
- **Change:** a fix someone can make without asking another question. Taste is marked "taste" or "my read".

## Severity

- **Blocker:** prevents the main task or excludes a group of people.
- **Major:** causes errors, abandonment or heavy friction for many.
- **Minor:** noticeable friction or inconsistency; people cope.
- **Polish:** refinement, after the rest.

For a quick triage of a chart or graphic: ugly (taste), bad (hard to read or perceive), wrong (the data is misrepresented). Wrong outranks bad outranks ugly.

## Score anchors (same for every dimension)

- **0** broken: the main task fails or some people are excluded.
- **1** serious: the task works only with effort, guessing or workarounds.
- **2** notable friction: most succeed with hesitation or repeated small errors.
- **3** solid: clear and usable; minor issues.
- **4** exemplary: hard to improve for this purpose; say why.

Dimensions: purpose clarity, hierarchy, layout and spacing, typography, color and contrast, interaction and feedback, content, accessibility; add data display, motion, brand consistency when present. Skip what the fidelity cannot show ("not assessed").

- Overall is a judgment, not a mean; name the lowest dimension beside it.
- A blocker caps the overall at 2 (1 if it ends the main flow) and its dimension at 1.
- Whole numbers only; no decimals or percentages.
- Scores summarize findings and never replace them.

## Compact template

```
Verdict: <what works, the main problem, the order to fix>.
1. [Major] <title>. Seen: <...>. Why: <...>. Change: <...>.
2. [Minor] ...
Keep: <two decisions>.
Not checked: <limits>.
```
