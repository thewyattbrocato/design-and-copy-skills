# Alt text for the README images

Paste these as the alt text of each image. The numbers behind the chart are in the README Results tables.

| File | Alt text |
|---|---|
| `docs/img/banner.svg` | design-and-copy-skills: a mark of four corner crop marks around one teal dot, beside the wordmark and the line "Design guidance a coding agent loads when the task calls for it." |
| `docs/img/results.svg` (2x copy: `docs/img/results.png`) | Horizontal bar chart of the held-out results for every listed skill, loaded runs only. Each bar shows the mean rubric score with the skill minus without it, starting at zero and ordered from the largest gain to the smallest. Beside each bar are the skill's wins, losses and ties and its number of loaded tasks. Every skill won more tasks than it lost; marginal passes are drawn as hollow bars tagged "marginal", and ui-motion is level with the baseline on rubric score. |
| `docs/img/how-it-works.svg` | Four steps from left to right. A design-shaped task arrives. The agent scans the skill list, where only each skill's name and one-line description are in context. A matching skill loads its short instructions. Longer reference notes are opened only when a step needs them. With no match, nothing loads. |
| `docs/img/how-we-test.svg` | Four steps from left to right. A task set is written first by someone who has not read the skill. The same model gives three answers per side, with and without the skill. A different model judges each pair blind, in both orders, and a win must hold in both. Only runs where the model loaded the skill are counted, giving wins, losses and ties plus the mean rubric difference. |
