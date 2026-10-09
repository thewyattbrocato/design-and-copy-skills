**Recommendation: a heatmap, with one row per store and one column per week.**

- **Rows:** the 12 stores, sorted by when each peaks. The Christmas stores cluster together at the bottom, and Airport (July) and Harbor Mall stand out in the middle.
- **Columns:** weeks 1–52, with month labels along the bottom.
- **Color:** each store's visitors as a percent of its own peak week, so 0–100%. Raw counts would let the 9,000-a-week store wash out the 400-a-week store. Scaling per store keeps every row readable and makes the timing the focus.
- **Right-hand column:** average weekly visitors or annual total for each store, so the size difference still shows.

This fits 12 × 52 cells on one slide, and each pattern you mentioned is visible without reading a number:
- The Christmas stores form a bright band in the final weeks.
- Airport has a bright band in July.
- Harbor Mall goes dark after week 30. Add a thin vertical line there, labeled "renovation."

**Headline:** state the takeaway, for example "Most stores peak before Christmas; Airport peaks in summer; Harbor Mall has been dark since week 30." Don't leave the title as "Weekly visitors by store."

**Alternative if the audience wants exact numbers:** 12 small line charts in a 3×4 grid, each with its own y-axis labeled with its peak. A shared y-axis would flatten the small stores into lines along the floor. Line charts show the Harbor Mall drop more clearly, but they take more space and are harder to compare at a glance.

I'd go with the heatmap for Monday. If you tell me what you're building it in (Python, Excel, PowerPoint, etc.), I can produce the chart from your CSV.
