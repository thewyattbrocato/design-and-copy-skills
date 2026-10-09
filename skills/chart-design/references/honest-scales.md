# Honest scales

Load this when setting axes, comparing across time, adjusting money, handling partial or missing periods, sizing circles, binning, or choosing the aspect ratio.

The test behind every rule here: does the size of the drawing change by the same proportion as the data? If a value doubles, the mark should look about twice as large, and a reader who has never seen the numbers should come away with the right impression.

## Baselines

- Bars and areas encode value by length or area from the baseline, so the baseline must be zero. A bar starting at 40 makes 42 versus 46 look like a doubling.
- Lines and dots encode value by position, so the axis may start above zero when the interesting variation sits in a narrow band. Label the axis clearly and avoid choosing a range that makes noise look dramatic.
- If a reader might mistake a zoomed line for a zero-based one, add a short note ("axis starts at 60") or a faint reference line at the baseline.
- When a bar chart cannot start at zero because values are huge and differences small, switch to a dot plot with a labeled zoomed axis, or plot the difference from a reference value.
- A scale break should cut completely through the marks and have a visible mark on the axis. Pair it with a companion view that starts at zero. Breaks are a last resort.
- Never break a time axis. Do not drop weekends, quiet months or inconvenient years without saying so on the chart.

## Linear, log and indexed scales

- Linear by default. Equal steps on the axis are equal differences in the data.
- Log scale: use when values span many orders of magnitude or when the question is about percentage growth. Label "log scale" on the axis, put ticks at powers of ten or round multiples, and do not mix a log axis with bars (bars from zero are impossible on a log scale).
- Index to 100 at a shared start date when comparing the growth of series with different units or very different sizes. Say what the base period is.
- Percent change charts should state the base. A fall of 50% followed by a rise of 50% is not a return to the start.

## Two series with different units

Avoid a second y-axis; the choice of each range is arbitrary and the point where lines cross carries no meaning. Prefer:

1. Two charts, stacked, sharing one time axis.
2. Both series indexed to 100 at the start.
3. One derived series, such as revenue per order or cost per ticket.
4. A scatter of one against the other, when the relationship is the point.

If a dual axis is required anyway, color each axis title and tick labels to match its series, start both at a sensible baseline, and add a note that the scales are independent.

## Money

- Long series (more than a few years) in dollars, euros or any currency mix inflation into the trend. Plot constant or real values, an index, or a share of income or price of something else, and state the base year.
- When the nominal number is the point (a salary offer, a committed budget), plot nominal and say so; consider showing both in a pair of lines.
- Convert foreign currencies at a stated rate or date, not whichever rate the data happens to use at each point.

## Populations and periods

- When groups differ in size, compare rates (per 1,000 people, per customer, per account) rather than counts.
- Compare equal-length periods. February has fewer days than March; per-day values or a note avoid a false dip. Weekly data with a short first or last week should show those weeks as partial.
- A period still in progress is incomplete. Draw it hollow, dashed, or lighter, and label it ("to date, 12 of 30 days"). Do not let the last point plunge to zero as if the period had ended.
- Seasonal data: compare the same period a year earlier, or show the seasonal pattern, before claiming a trend.
- Forecasts and estimates get a different style (dashed line, lighter band) and a label.

## Sizing marks

- If you encode a value in a circle or square, scale the area to the value. Doubling a radius quadruples the area. Take the square root of value (relative to a reference) to get the radius.
- Icons, logos and pictograms scaled in two dimensions mislead the same way. Use bars, or repeat one fixed-size icon.
- Do not use one value for both height and width of a bar.
- Never use a three-dimensional shape to carry a one-dimensional value.

## Bins and intervals

- Histogram bins have equal width unless the axis is clearly marked otherwise; if bins are unequal, plot density (count per unit width) rather than raw counts.
- Age bands, income bands and similar groups with unequal widths need the same care.
- Rolling averages and smoothing hide spikes. State the window, and show raw data faintly beneath if the spikes matter.

## Aspect ratio and frame

- A time series reads best wider than tall; a common default is a width of about 1.5 to 2.5 times the height.
- A tall, narrow frame makes any rise look dramatic; a very wide, short one flattens it. Choose a frame where the slopes that matter sit roughly near a diagonal, neither flat nor vertical.
- Keep the aspect ratio the same across charts that will be compared directly.
- For a card or a slide, fit the chart to the space, then check that the slopes still read as intended.
