I'd skip the radar chart. Use a small-multiples bar layout instead: one small panel per spec, with three bars (one per model) in each panel.

**Why not radar**
- The six specs have different units: km, kg, dollars, watts, hours and years. To share one radial scale, each has to be rescaled to something like 0–100, and the shopper can no longer read the real numbers.
- Direction is mixed. More range is good, but more weight, price and charge time are bad. You'd have to flip some axes, and then a bigger polygon doesn't clearly mean "better".
- The polygon's shape and area change with the order of the axes, so the same data can look quite different.
- A shopper can't read "Ridgeway costs $550 more" off a polygon.

**Setup**
1. **Layout:** a 3×2 grid of panels, or a single column on mobile. Each panel has a plain-language title with its unit: "Range (km)", "Weight (kg)", "Price ($)", "Motor (W)", "Charge time (h)", "Warranty (years)".
2. **Bars:** horizontal, three per panel, starting at zero. Put the value at the end of each bar so no axis or gridlines are needed.
3. **Color:** one fixed color per model, the same in every panel. Label the models directly on the bars or in the first panel, so there's no separate legend. Use three clearly different hues that don't depend on red versus green.
4. **Order:** keep the models in the same order in every panel (for example Cove, Trekline, Ridgeway, from cheapest up). Don't re-sort each panel, because shoppers will be comparing across panels.
5. **Better/worse:** add a small note in each panel title, such as "longer is better" or "lighter is better". Don't color the winner. That keeps the chart neutral, and the shopper decides what matters.
6. **Panel order:** lead with the specs shoppers weigh most, probably price, range and weight.
7. **Accessibility:** include a text summary, for example "Ridgeway has the longest range and warranty but is the heaviest and most expensive." Also provide the same numbers as a table, which can sit behind a "View as table" toggle.

**Alternative:** if you want something more compact, a plain comparison table with the six specs as rows and the three models as columns also works well. Add a thin in-cell bar behind each number if you want a visual cue. Shoppers often want the exact figures, so a table may suit a product page better than any chart.

If you tell me your stack (plain HTML/SVG, React, a chart library), I can write the code. I'd also add a provenance line under the chart, such as "Specs as of [date], source: [your spec sheet]".
