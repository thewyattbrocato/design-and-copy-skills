I'd use small multiples: a 4×3 grid of 12 small line charts, one per store, all with the same 52-week x-axis.

**Why this layout**
- **One chart with 12 lines won't work.** Lines for a 9,000-visitor store and a 400-visitor store can't share a readable y-axis, and 12 overlapping lines are unreadable anyway.
- **Small multiples fit what you're showing.** Your story is about shape: the shared holiday peak, one store that breaks the pattern, and one that collapses.

**Y-axis scaling**
- I'd give each panel its own y-axis, so the 400-visitor store's seasonality is visible instead of a flat line.
- Because the scales differ, print each store's peak value in its panel (for example, "peak 9,0xx"). That keeps the size differences from being hidden.
- The alternative is to index each store to its own peak (100%) and share one axis. That makes shapes directly comparable but loses absolute volume. I'd only do that if volume doesn't matter for Monday.

**Making the exceptions stand out**
- Draw the 10 regular stores in a neutral gray or muted blue, with a small dot on each one's peak week.
- Give **Airport** and **Harbor Mall** one accent color each.
- Annotate the Airport panel with "Peaks in July".
- Annotate the Harbor Mall panel with "Renovation, wk 30" and lightly shade the closed period. Without that note, the drop looks like a performance problem rather than a planned closure.
- Add a faint vertical reference line at the week before Christmas (week 51) in every panel, so the "most peak here" pattern is visible at a glance.

**Ordering**
- Sort the panels by size (largest to smallest), or group them as the 10 regular stores, then Airport, then Harbor Mall. I prefer the grouping, because the exceptions end up together.
- Skip titles on the x-axes of every panel. Label months or weeks only on the bottom row.

**Slide text**
- Use a headline that states the takeaway, for example: "10 of 12 stores peak the week before Christmas. Airport peaks in July, and Harbor Mall dropped after its week-30 renovation."
- Keep a one-line footnote saying the y-axes are scaled per store.

A heatmap (12 rows × 52 weeks, color normalized per row) is the compact alternative. It's denser but harder for a general audience to read, so I'd stick with the small multiples.

If you send me the CSV path, I can build the chart as an image to drop into the slide.
