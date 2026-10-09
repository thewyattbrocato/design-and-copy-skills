# Choosing the form

Load this when the right form is not obvious from the table in SKILL.md.

## Start from the reader's question

Ask what comparison the reader must make, then pick the form that makes that comparison easiest.

| Question | Form that answers it |
| --- | --- |
| Is it going up or down, and how fast? | Line over time |
| Which is biggest, which is smallest? | Bars sorted by value |
| How did each piece change between two moments? | Slope chart, or paired dots |
| Who is above or below a target? | Bars or dots with a target line; or plot the gap itself |
| What share is each part? | One 100% bar, or labeled bars |
| How are values spread? | Histogram, dot strip, or box summary |
| Do two measures move together? | Scatter, one point per item |
| How does one series compare with many others? | Highlight it in color, gray the rest, or use small multiples |
| Where is it? | Map, only if location explains the pattern |

## A sentence or a table instead

- One or two numbers: write a sentence ("Churn fell to 2.1%, down from 2.6%") or show a large figure with its change. Drawing a bar for two values adds nothing.
- Exact lookup, many values, or mixed units: a table. As a rough guide, around twenty values or fewer with no shape to see is table territory.
- A small number of values where the order matters and the gap is the story: a short sorted list with inline bars can beat both.

If the user asked for a chart anyway, build it, then keep it honest and minimal.

## Time series

- Line by default. The slope between points is the message.
- Bars when each period is a discrete count or total and there are not too many (roughly a dozen to two dozen). Bars for time need a zero baseline.
- Do not connect points across missing periods without showing the gap.
- Two series that share units: two lines with direct labels. Shade the gap between them if the gap is the point.
- Cumulative values hide recent change; plot per-period values if the question is about the recent past.

## Categories

- Sort by value unless the categories have a natural order (age bands, months, ratings).
- Horizontal bars when labels are long or there are more than about seven categories.
- Many categories with a long tail: show the top few and group the rest as "Other", with a note on what it contains.
- Stacked bars compare only the bottom segment accurately. If the reader must compare the upper segments, use grouped bars or small multiples.

## Part to whole

- The parts must sum to something meaningful. Independent percentages (each respondent could choose several) are not parts of a whole; use bars on a common base and state the base.
- A single stacked bar scaled to 100% handles two to five parts well and sits easily beside text.
- A pie is acceptable for a one-off summary with two to five parts, printed values, and a sum of 100%. Start the first slice at twelve o'clock, order slices by size, and avoid exploded or 3D slices.
- A donut gains nothing over a pie except space for a central number. Treat it the same way.
- Small groups of people (four of six interviewees) are better drawn as individual marks than as a percentage.

## Distribution and relationship

- Histograms: choose bin width so the shape is visible, keep bins equal width, and label the unit. Changing bin width can change the story, so look at one or two widths before settling.
- With only a handful of observations, a dot strip shows every value and needs no binning.
- Scatter: label notable points directly; use transparency or small multiples when points overlap heavily. Do not imply cause from a fitted line.

## Maps

- Use a map only when position or neighborhood explains something. If the question is "which region is highest", sorted bars answer it better.
- Shade by rate (per person, per household), not by raw count, or the map just redraws population.
- Use one hue ramp from light to dark, a modest number of classes, and a legend that shows the ranges. Large sparse regions dominate visually; consider a small label or inset for small dense ones.

## Forms to avoid by default

- Gauges and speedometers for a single value: a number with a comparison is clearer and smaller.
- Radar or spider charts of unrelated categories: the shape depends on axis order and means nothing.
- 3D, perspective, or exploded forms: they distort the values they carry.
- Word clouds as a measurement tool: fine for a rough impression of themes, not for comparing frequencies.
- Area charts stacked with many layers: only the bottom and total are readable.
