I'd use a **heatmap**: stores as rows, weeks as columns, with the store's name and peak number on the left. With 12 stores and 52 weeks, it shows every pattern at once, and all three of your stories are visible without extra annotation.

**Layout (16:9):**

- **Headline as the takeaway**, e.g. "Most stores peak the week before Christmas; Airport peaks in summer; Harbor Mall dropped after its week-30 renovation."
- **Main area: the heatmap.**
  - Rows: 12 stores, grouped by pattern. Put the holiday peakers together, then Airport, then Harbor Mall, so each group reads as a block.
  - Columns: 52 weeks, with month labels along the bottom.
  - Color: each store's visitors as a percentage of its own peak, not raw counts. A shared absolute scale would make the 400-visitor store look like a blank line next to the 9,000 store. Normalizing per store keeps every row readable.
  - Keep the raw numbers on the left edge (e.g. "9,120 peak") so scale isn't lost.
- **Marker for week 30:** a thin vertical line through the chart, labeled "renovation," so the Harbor Mall drop lines up with it.
- **Right sidebar: three short callouts**, one per story, each with the number behind it (holiday peak week, Airport's July peak, Harbor Mall's drop after week 30 and how far).
- **Footer:** data source, year, and a note that color = % of each store's peak week.

**Alternatives if the heatmap doesn't fit the audience:**
- *Small multiples* (4×3 grid of line charts, shared x-axis, each panel its own y-scale). Better if people want to see the shape of each store's curve, but each panel is small on a slide.
- *One line chart of indexed values* (each store ÷ its own annual average). Only works if you highlight the three exceptions and grey out the other nine. Otherwise it's spaghetti.

I'd go with the heatmap. If you want, I can build it from the CSV in Python (matplotlib) and export a PNG sized for a slide. Tell me the CSV's filename and whether the week column is 1–52, and I'll check the week-30 and holiday-peak alignment against the data before I finalize the labels.
