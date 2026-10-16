**Use small multiples: one panel per store, all on the same week axis, on one slide.** Twelve lines on one chart would be unreadable, and a single chart can't show the three different stories without tangling them.

**Layout (4 columns × 3 rows, widescreen)**

- **Slide headline states the takeaway**, e.g. "Most stores peak before Christmas; Airport peaks in summer; Harbor Mall fell after its week-30 renovation." Readers should get the point before they study the panels.
- **Shared x-axis: weeks 1–52**, with month labels along the bottom. Every panel uses the same range so timing lines up across stores.
- **Group panels by peak timing, not by size.** Put the 10 pre-Christmas stores first, then Airport, then Harbor Mall, so the exceptions sit together at the end and are easy to spot.
- **Each panel gets a small title with the store name and its average weekly visitors** (e.g. "Airport · avg 3,200"). That keeps the absolute size information without a size axis.

**Y-axis: the main decision**

A shared linear axis from 0 to 9,000 would flatten the 400-visitor store into a line along the bottom, so its seasonal pattern would be invisible. I'd do one of these:

- **Index each store to its own average (= 100)** and use the same axis for all panels. This is my recommendation, since the slide is about *when* stores peak, not how big they are. Pattern comparisons become fair, and the size goes in the panel title.
- If the audience needs absolute size on the chart, use a free y-scale per panel and label each axis max clearly. Don't use one shared scale.

**Highlighting the three stories**

- Draw every line in neutral gray, then color only the exceptions: Airport in one accent color and Harbor Mall in another. The 10 Christmas-peaking stores can be a single muted color, with a lighter highlight on their week-51/52 peak.
- **Harbor Mall:** add a dashed vertical rule at week 30 labeled "renovation," plus a dashed line for its pre-week-30 average so the drop is measured against something. A short callout with the percentage drop (computed from your data) makes it concrete.
- **Airport:** shade or label July so the summer peak is obvious.
- **Christmas stores:** a light vertical band over the last two weeks of December works across all panels.

**Data prep**

Weekly counts are noisy, so a 4-week trailing average smooths the lines. Note that in a footer, and show raw weekly points only if someone asks.

**Slide footer:** source, the date range, "Index: store average = 100" if you go that route, and a one-line definition of the renovation window.

If you want, I can build this as a matplotlib or SVG figure from your CSV. Send me the file path and tell me whether you want the indexed or absolute y-axis. I'd pick indexed.
