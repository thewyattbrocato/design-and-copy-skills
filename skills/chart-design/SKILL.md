---
name: chart-design
description: Use when you make, choose, fix or review a single chart, graph, sparkline or simple map (HTML, SVG, canvas or a chart library) - including a chart card, a trend line for a report or newsletter, or a survey result chart: picking the form for the question, honest axes and baselines, money and time handling, direct labels, restrained color, small multiples and chart accessibility. Not for multi-chart dashboards or KPI screens, data tables, interface or brand palettes, diagrams that explain a mechanism, or statistical analysis.
---

# Chart design

A chart exists to let one reader see one thing quickly and correctly. This skill keeps the form matched to the question, the encoding honest, and the styling quiet so the data is the loudest thing on the page.

## When to use

- Building a chart from supplied numbers, in SVG, canvas, HTML or a charting library.
- Choosing which chart form fits a question or a dataset.
- Fixing or critiquing an existing chart: axes, labels, legend, color, scale, title.
- Planning a figure with many series (small multiples) or a tiny inline trend line.
- Deciding whether something needs a chart at all.

## When not to use

- Several charts, KPI tiles and filters arranged on one screen: multi-chart dashboard layout, outside this skill. This skill still applies to each chart inside it.
- Tables for exact lookup: use data-tables if installed.
- Interface palettes, brand colors, theming: use color-palette if installed. Only data color is handled here.
- Diagrams that explain how something works (flows, architectures, mechanisms): use teaching-interfaces if installed, or another diagramming approach.
- Choosing statistical tests or interpreting the statistics. Charting the result is in scope; the analysis is not.
- Formatting numbers in a spreadsheet or document with no chart involved. Answer that directly.
- An explicit user instruction, an established house style, or a chart library's required convention outranks any default below. Follow it, and mention a misleading consequence once if there is one.

Scale the effort to the request. A one-line fix ("start the axis at zero") needs only the relevant check, not the whole procedure.

## Procedure

Work through these in order. Skip steps that are already settled.

1. **State the question.** Write one sentence naming what the reader should be able to see ("is the backlog shrinking?"). For an explanatory chart that finding becomes the title. For an exploratory view, keep the title descriptive and neutral.
2. **Decide whether a chart is needed.** One or two numbers: a sentence, or a large figure with its comparison. Exact values, or many values with no shape worth seeing: a table. If the data is a handful of values and the answer is obvious in words, say so.
3. **Match the form to the relation.** See the table below, and [choosing the form](references/choosing-the-form.md) for edge cases.
4. **Encode by accuracy.** Readers judge position on a shared scale best, then length, then angle and area, then color intensity. Put the comparison that matters on the strongest channel. Use hue to tell categories apart, not to carry quantity.
5. **Set honest scales.** Bars and areas start at zero. Lines and dots may zoom with a clearly labeled axis. Time runs in equal steps. Adjust long money series for inflation. Mark incomplete periods. Details in [honest scales](references/honest-scales.md).
6. **Show the comparison.** Put the target, prior period, benchmark or peer on the chart. A number alone has no meaning.
7. **Label directly.** Name lines at their ends, put values on bars when exact numbers matter, give axes units, keep text horizontal.
8. **Quiet the structure.** Faint or no gridlines, no frame, no shadows, gradients or 3D. Data gets the strongest ink.
9. **Use color with intent.** Muted gray for context, one accent for the focus; see [labels and color](references/labels-and-color.md).
10. **Pick the frame.** Wider than tall for a time series, sized so the main slope is neither flat nor cliff-steep.
11. **Make it accessible.** A text takeaway, the data reachable as a table, and no meaning carried by color or hover alone; see [many series and accessibility](references/multiples-and-accessible-charts.md).
12. **Re-read the finished chart** against the quick checks at the end.

### Form by relation

| The reader needs to see | Default form | Notes |
| --- | --- | --- |
| Change over time | Line | Bars when there are few, discrete periods or counts per period |
| Compare categories | Bars sorted by value | Horizontal when labels are long; keep the order stable across related charts |
| Part of a whole | One stacked or 100% bar, or labeled bars | A pie only under the rule below |
| Independent shares (multi-select answers) | Bars on a common base | They do not sum to 100%, so a whole-shaped chart is false |
| Distribution | Histogram, box summary or dot strip | Choose bin widths deliberately |
| Relationship of two measures | Scatter | Add a fitted line only if it helps and say what it is |
| Rank change between two moments | Slope chart | Label both ends |
| Many series | Small multiples, or one highlighted line over gray context | Avoid more than about five lines in one frame |
| Place matters to the insight | Map of rates, not raw totals | If place is not the point, use sorted bars |

## Judgment calls

**Baselines.** Default: bars and areas start at zero, because their length or area is the value. Change when the chart is a line or dot plot of values far from zero (a temperature, an index, a rate that moves within a narrow band): zoom is fine if the axis is labeled and the zoom does not invent drama. When a bar chart truly cannot start at zero, switch to dots, or cut the axis fully through the bars with a visible break and show the zero-based view alongside.

**Pies.** Default: not a pie. Change when there are about two to five parts that really sum to one whole, the values are printed on the slices, and a coarse "most of it versus a sliver" read is the goal, such as a friendly one-off summary. A single 100% bar is the safe alternative. A pie is wrong for multi-select answers, for parts that do not sum, for more than about five parts, and on any screen people monitor repeatedly.

**Two y-axes.** Default: avoid. Their scales are arbitrary, so the crossing points and apparent correlation are manufactured. Instead use two charts stacked with a shared time axis, index both series to 100 at the start, or plot a ratio such as revenue per order. Change only when the user insists on a dual axis: label each axis in its series color and say that the scales are independent.

**Log scales.** Default: linear. Change when values span orders of magnitude or the question is about growth rate. Label the axis as logarithmic, use round powers for ticks, and consider whether the audience will read it.

**Money and populations.** Default: long money series in constant terms, or as an index or a share of income; counts as rates per person when group sizes differ; equal-length periods. Change when the nominal figure is the point (a contract price, a budget actually approved). Say which one is plotted.

**Annotation.** Default for an explanatory chart: a title that states the finding, plus one or two notes at the moments that matter. Default for an exploratory view: a neutral title and no editorializing. Change when the audience will not read a legend or caption: put the note on the chart.

**Library defaults.** Treat them as suggestions. Override the legend position, gridlines, palette, animation and 3D options; keep sensible tick spacing and number formatting.

## Common failures

| Symptom | Fix |
| --- | --- |
| Pie or donut with eight or nine slices and a legend | Sorted horizontal bars with values on them |
| A long tail of tiny categories, each with its own bar or slice | Show the top few and group the rest as "Other", with a note on what it holds |
| Pie of survey answers where people could pick several | Bars on one base; state the number of respondents and that several answers were allowed |
| Bar axis starts well above zero and exaggerates a small gap | Start at zero, or use dots and label the zoom |
| Two unrelated measures drawn on two crossing y-axes | Two aligned charts, an index, or a ratio |
| Every series saturated in a different hue | Gray for context, one accent for the subject |
| Legend sits below the plot and the eye ping-pongs | Direct labels at line ends |
| Rotated, clipped x labels | Horizontal bars, shorter labels, or fewer ticks |
| Gradient, shadow or 3D on bars | Flat solid marks |
| Decades of prices in nominal dollars | Inflation-adjusted values, an index, or share of income |
| Current partial month drawn as a full bar or point | Mark it hollow or dashed and label it as partial |
| Bubble or icon sized by width or radius | Size by area, or use bars |
| Title says "Sales by month" for a chart meant to persuade | State the finding; keep the descriptive title for exploration |
| Trend line or fit added without being asked | Remove it, or say what it is and why |
| One KPI number turned into a full chart | Show the number with its comparison |
| A written answer that runs past a length limit the user gave | Keep to it; cut material before the limit |

## Quick checks

- Does the visual change match the data change? A doubled value should look doubled.
- Do bars and areas start at zero, and is any zoomed or broken axis labeled?
- Are lines and bars labeled where the eye lands, with no legend needed?
- Is there a comparison (target, prior period, benchmark) on the chart?
- Are there at most about six to eight hues, and does the same category keep the same color everywhere?
- Do the series stay distinguishable without red versus green or any hue alone?
- Is any partial period, estimate or adjusted value marked as such?
- Does the title say what the reader should conclude, or honestly describe the view?
- Is the takeaway in text, and are values reachable without hovering?
- Would a sentence or a table have served this reader better?

## References

- [choosing-the-form.md](references/choosing-the-form.md): load when the form is not obvious, when picking between a chart, a number and a table, or when a map or unusual relation is involved.
- [honest-scales.md](references/honest-scales.md): load when setting axes, comparing across time, adjusting money, handling partial periods, sizing bubbles, binning, or choosing an aspect ratio.
- [labels-and-color.md](references/labels-and-color.md): load when styling: direct labels, legends, annotation, gridlines, text sizes, and sequential, diverging or categorical color.
- [multiples-and-accessible-charts.md](references/multiples-and-accessible-charts.md): load for many series, tiny inline trend lines, or any chart that must be accessible or work without hover.
