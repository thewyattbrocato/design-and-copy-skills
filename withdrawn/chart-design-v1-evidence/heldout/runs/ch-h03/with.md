**Use a line chart.** The question is whether weekly actives are growing over time, and a line shows that best through its slope. Twelve evenly spaced weeks suit it well.

**Why not the other two:**
- **Bar chart:** this is a defensible alternative, since the weeks are discrete. But twelve bars add visual weight and make the trend harder to see than one line does.
- **Area chart:** it's a line with a filled region, and the fill adds nothing here. The area is only meaningful if you're showing a cumulative total or stacked parts. It would also force a zero baseline, which is fine but unnecessary.

**Y-axis: it's fine not to start at zero for a line, but I'd start at zero here anyway.**
- Bars and areas must start at zero, because their length or area is the value. A line only encodes position, so a zoomed axis is acceptable if it's labeled.
- Here, though, the growth is real and large: 41k to 75k is about +83%. A zero baseline still shows a clear upward line and keeps the size of the growth honest.
- A zoomed axis (say 35–80) would make the line steeper and look more dramatic. For a stakeholder audience that can read as spin, and it isn't needed because the story is already strong.
- If you do zoom, label the axis clearly and don't draw it as bars.

**Details that help:**
- Title with the finding, e.g. "Weekly active users up 83% in 12 weeks (41k → 75k)".
- Label the first and last points directly (41k, 75k) instead of using a legend. There's only one series, so no legend is needed.
- Axis labels with units ("Weekly active users, thousands" and "Week 1–12").
- Faint or no gridlines, and a single solid color.
- If you have a prior-period or target line, add it for comparison. Otherwise the line stands on its own.
- Add a short text takeaway or a data table for accessibility.
- If the latest week is still in progress, mark it as partial (hollow or dashed).

The data isn't perfectly monotonic. There are small dips at weeks 3, 6 and 9. That's normal noise, so I'd leave them in rather than smooth them. The overall trend is clear.

I can build this as SVG/HTML or in a specific library if you tell me which you use.
