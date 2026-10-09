# Why dual-axis charts mislead (and what to do instead)

## The core problem
With two y-axes, **you choose the scales, and the scales decide the story.** Nothing about spend in dollars and signups in counts says where the two lines should sit relative to each other. Whoever builds the chart picks that, often without meaning to.

## How it misleads

1. **Manufactured correlation.** Stretch or shift either axis and the lines can be made to track each other, or diverge. If spend runs $0–$100k and signups run 0–1,000, the lines overlap. Change signups to 0–5,000 and the "relationship" disappears. The data didn't change, only the axes did.
2. **Crossing lines look meaningful.** Readers see the point where the lines cross and read it as "signups overtook spend" or "efficiency changed." That crossing is an artifact of the axis ranges and means nothing.
3. **Truncated axes exaggerate.** If either axis doesn't start at zero, a small change looks dramatic. Autoscaling in Excel, Tableau, and similar tools often does this by default.
4. **Hard to read.** Viewers have to work out which line belongs to which axis. Tick marks on the two axes also rarely line up, so the gridlines only apply to one series.
5. **It implies causation.** Two lines moving together invite "spend drove signups." The chart can't show that. It ignores lag, seasonality, organic growth, and diminishing returns.

## What to do instead

Pick based on the question you're answering:

- **"How did each metric trend?"** Use **two stacked charts** (small multiples) that share the same x-axis (time). Spend on top, signups below. You can still compare timing by eye, and neither scale is distorted.
- **"Is spend efficient?"** **Plot the ratio directly**, i.e. cost per signup (CPA) over time. This is usually the metric stakeholders actually care about, and it fits on one honest axis.
- **"Do they move together?"** Use a **scatter plot** with spend on x and signups on y, one point per week or day. This shows the relationship and any diminishing returns. If you want to claim a relationship, also check the correlation, and consider lagging spend by a few days or weeks.
- **"How do they compare in relative terms?"** **Index both to a base period** (for example, 100 = first week) and plot them on one axis. Both series are then in the same unit (percent change from baseline), so one axis is legitimate.

## Rules of thumb

- If you feel you *need* two axes, it usually means you should be plotting a ratio or using two panels.
- Start bar charts at zero. Label axes with units.
- If a dual axis is truly unavoidable, color-code each axis to its line, start both at zero, and state the scaling choice in a note. Treat it as a last resort.
- Don't write a title or takeaway that claims causation unless you've done more than eyeball two lines.

**Short version:** two axes let the chart's author pick the story. Use stacked panels, a ratio like CPA, a scatter, or an indexed chart so the data makes the argument.
