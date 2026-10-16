# Alt text for the README images

Paste these as the alt text of each image. The numbers behind the chart are in the README Results tables.

| File | Alt text |
|---|---|
| `docs/img/banner.svg` | design-and-copy-skills set very large on two lines in heavy white sans-serif on near-black, with amber hyphens. Beside it, an amber rule and an italic serif note: 30 skills for AI coding agents. Along the bottom, a strip of 30 small amber marks: 18 squares labelled 18 design, then 12 dashes labelled 12 copywriting. |
| `docs/img/results.svg` (2x copy: `docs/img/results.png`) | Horizontal bar chart of the held-out results for every listed skill, loaded runs only. Each bar shows the mean rubric score with the skill minus without it, starting at zero and ordered from the largest gain to the smallest. Beside each bar are the skill's wins, losses and ties and its number of loaded tasks. Every skill scored higher with the skill than without; all but typeface-selection won more tasks than they lost (it won and lost two each), and marginal passes are drawn as hollow bars tagged "marginal". |
| `docs/img/how-it-works.svg` | Four steps from left to right. A design-shaped task arrives. The agent scans the skill list, where only each skill's name and one-line description are in context. A matching skill loads its short instructions. Longer reference notes are opened only when a step needs them. With no match, nothing loads. |
| `docs/img/how-we-test.svg` | Four steps from left to right. A task set is written first by someone who has not read the skill. The same model gives three answers per side, with and without the skill. A different model judges each pair blind, in both orders, and a win must hold in both. Only runs where the model loaded the skill are counted, giving wins, losses and ties plus the mean rubric difference. |
