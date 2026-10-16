# Relationship recipes

Load this when the request names a relation the form table does not settle: over or under a target, a few items dominating, a funnel, waterfall, donut, radar or stacked area, scattered sample dates, one series against many, or "typical" values.

## Over or under a reference

- If the question is "how far off", plot the difference, not the two values. Bars diverge from a zero line that is labeled with what zero means ("on budget", "prior year"). Two clustered bars make the reader subtract.
- Absolute and percent gaps tell different stories (a small team can be far off in percent and trivial in money). Pick the one the question needs and say which; show both as two aligned views only if both matter.
- Sort by gap or by size, never alphabetically. Direction must not rely on red versus green: put over on one side, under on the other, and say so in the labels.
- Keep the actual and reference values in labels or a table so nothing is lost.
- Actual against target for one measure: a bar with a tick at the target, not a gauge.

## A few items dominate

- Sorted bars, largest first, with the cumulative share as a thin line on a 0 to 100% axis (the line shares the bars' category axis, so it is the one dual-scale case that is honest). Mark where the line crosses the share the headline names.
- Past about a dozen categories, show the leaders and fold the rest into one "Other" bar with its count.
- Title with the finding that can be checked in the chart: "Three of 20 categories account for most volume" only if the cumulative line shows it.

## Funnels, waterfalls, donuts, radar, stacked area

If the user named a form, build it honestly; if another form answers the question better, say so in one line and offer it. Swap without asking only when the request named the question, not the form.

| Asked for | Why it fails | Build instead |
| --- | --- | --- |
| Funnel graphic | Shape area implies a quantity it does not carry | Horizontal bars in stage order, count and step conversion beside each |
| Waterfall | Fine only for a running balance across dated additions and subtractions | Otherwise sorted bars of the contributions plus one total bar |
| Donut or pie dashboard | Slices cannot be compared across many | One 100% bar per period, or sorted bars |
| Radar | Shape depends on axis order | Bars per attribute, or a small table |
| Stacked area with many parts | Only the bottom layer and the total are readable | Total as one line, parts as small multiples or lines |
| Icon grid or sized bubbles | Width and height both scale | Bars |

## Irregular or sparse time

- Sample dates unevenly spaced: put them on a true time axis and mark each reading with a dot. Join dots with a line only if the gaps are short relative to how fast the thing changes.
- Whether a short series is "rising" can flip with one point. Do not add a fitted line to under about ten points; if a trend is asked for, show a moving average with its window stated, or say the data cannot support a direction and show the dots against any limit or reference.
- Wider than tall; give the first and last values as labels.

## One series against many

- One focus series against many others: small multiples, one panel per other series. Draw the focus series in the accent color and the panel's own series in gray, both in every panel, so each panel is a pairwise comparison. Same months, same y-range, zero included for bars or areas.
- Order panels by the quantity of interest (gap to the focus series), not alphabetically. Label axes on the outer panels only.
- A single frame with eight colored lines is the fallback only when the user wants one picture: gray all but the focus, label line ends.

## Typical values

- "Typical" over a skewed set is the median, not the mean; say which one the label shows and give the count. A mean beside no spread hides whether the group is uniform.
- Under about 30 values: dot strip. More: histogram with equal bins. For a lay audience, a median with the middle half as a thick bar beats a full box plot.

## Provenance line

Under every explanatory chart, one quiet line: unit, period, as-of date, source ("Orders per week, last 12 weeks, as of 3 Oct, source: store database"). If the source or date was not supplied, write a visible placeholder in brackets rather than a plausible-looking one.

## Consistency across a set of charts

Same category keeps the same color and position; same measure keeps the same unit and decimals; panels that will be compared share axis ranges and aspect ratio; small marks and lines use darker, more saturated color than large filled areas.
