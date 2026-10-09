# Labels and color

Load this when styling a chart: direct labels, legends, annotation, gridlines, text sizes, and color for data.

## Direct labeling

- Label each line at its right end, in the same color or a darker shade of it. The reader finds the series without looking up a key.
- Bars: print each value just past the bar tip, or inside the bar in a contrasting color. Put the category name at the left of horizontal bars.
- Use a legend only when direct labels will not fit (a dense scatter with several groups, a stacked area with narrow bands). Order its entries as the series appear in the data, top to bottom, and place it next to the plot, not below it.
- A chart with one series needs no legend. Its title or axis label is enough.
- Axis titles carry units ("Tickets per week", "USD, 2024 prices"). Drop an axis title when the chart title already says it.
- Keep text horizontal. If category labels collide, switch to horizontal bars, shorten the labels, or show every second tick.
- Label the points that matter (the latest value, the peak, the target) and let the rest speak through position.

## Annotation

- Explanatory chart: one or two short notes where the story changes ("Hiring freeze begins"), placed beside the point they describe, not in a footnote.
- Exploratory chart: little or no commentary; let the reader find the pattern.
- Put the finding in the title for explanatory pieces ("Median delivery time fell below two days in March"). The subtitle gives the unit and period.
- Use the same sentence-case style throughout. Avoid all caps in annotations.

## Quiet structure

- Gridlines: light gray, thin, and few; or none when the bars carry their values. Horizontal only for most line and bar charts.
- No chart border, no background panel, no drop shadows, no gradients, no bevels. Rounded bar ends are fine if every bar uses them.
- Ticks: only as many as help reading values. Short or no tick marks.
- Axis line: a single baseline is enough. Remove the other three sides of the frame.
- Make the data the darkest or most saturated layer; everything else recedes.

## Text sizes

- Keep chart text readable at the size it will be shown. In an interface, roughly 12 to 14 px for labels and about 16 to 20 px for a chart title; larger for slides.
- Direct labels and annotations can be the same size as axis labels. Use weight, not a larger size, to rank them.
- Use tabular (fixed-width) figures for numbers that line up, and format them consistently: the same decimals, thousands separators and units everywhere.
- Shorten large numbers with a unit suffix (3.8M) when the exact digits do not matter.

## Color for data

Color has three jobs: highlight, separate categories, and encode magnitude. Pick the job first.

**Highlight plus context.** The default for most charts. Draw everything in a muted gray and the subject in one accent color. This works for one bar among many, one line among many, or the current period against the history. The accent should have clearly stronger contrast than the gray.

**Categories.** Use hue to separate categories. Keep it to about six to eight hues at most; beyond that, readers cannot match colors to a key, so use direct labels, grouping, or small multiples. Keep one category's color the same in every related chart. Choose hues with similar lightness so none looks more important by accident. If color is the only difference between lines, also vary the line style or add direct labels.

**Sequential (low to high).** A single hue ramp from light to dark, with even perceived steps, for magnitude on maps and heat tables. Higher values should be darker on a light background. Use five to seven steps; more cannot be told apart.

**Diverging.** Two hues meeting at a light neutral, only when the data has a meaningful midpoint (zero change, a target, a neutral rating). Not for plain low-to-high data.

**Color-vision checks.**

- Red versus green must not be the only signal for good versus bad, up versus down, or two series. Use blue versus orange, or vary lightness, or add a sign, arrow or label.
- Check the chart in grayscale. If two series merge, change their lightness or style.
- Thin lines and small marks need more contrast against the background than large fills. A pale yellow line on white may disappear.
- Text on colored bars needs enough contrast; the current accessibility standard asks for about 4.5 to 1 for normal text, 3 to 1 for large text and graphics.

**Brand colors.** A brand palette is not automatically a data palette. Use the brand accent for the highlight and neutral grays for the rest. Choose separate hues if categories need them, and keep the brand color for the subject or title.

**Dark backgrounds.** Lighten the data colors slightly, reduce the saturation of large fills, and soften gridlines further. Recheck contrast; gray context that was readable on white may vanish.
