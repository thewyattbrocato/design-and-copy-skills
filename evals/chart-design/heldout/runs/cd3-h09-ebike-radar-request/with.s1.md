I wouldn't use a radar chart for this. I'd use one small bar chart per spec (small multiples), or a comparison table with a mini bar in each cell.

**Why radar is a poor fit here**
- **Mixed units.** Your six specs are km, kg, dollars, watts, hours and years. A radar has to rescale each one to a made-up 0–100 axis, so the shape depends on those choices.
- **Opposite directions.** Higher is better for range, motor and warranty. Lower is better for weight, price and charge time. On a radar, a bigger polygon looks "better" even when it isn't. You'd have to flip some axes, and shoppers wouldn't notice.
- **Axis order changes the shape.** Reordering the same six axes gives a different polygon.
- **Area misleads.** Readers compare the filled areas, but the area has no real meaning. Shoppers also can't read exact values off it.

**How I'd set it up**

*Option A (my pick): small multiples, six panels in a 3×2 grid.*
- Each panel is one spec with three horizontal bars (Trekline, Ridgeway, Cove). Bars start at zero.
- Give every panel the same model order and the same model colors. The order should follow the model lineup, such as price low to high: Cove, Trekline, Ridgeway.
- Print the value at the end of each bar (e.g. "110 km"). Then you need no legend or axis.
- Put the unit in each panel title and add a short cue like "lower is better" on weight, price and charge time. Don't use red/green for this.
- Use three distinct, muted hues, one per model. Alternatively, use gray for all and one accent for the model you want to promote.
- Start each panel with the plain finding, e.g. "Ridgeway leads on range, power and warranty. Cove is lightest and cheapest."

*Option B: a comparison table with in-cell bars.*
- Rows are specs and columns are models. Each cell shows the number plus a thin bar scaled within that row.
- This works best on mobile, where six panels would stack into a long scroll.
- Shoppers can also look up exact values quickly.

**Both options**
- **Accessibility.** Include a text summary and make sure the values are readable without hovering.
- **Mobile.** Stack the panels into one column, keeping the same order.
- **Price.** Show it as the nominal sticker price. Say so in the label if you add a sale price.

If you share the page's stack (plain HTML/SVG, React, a chart library), I can write the markup or component for either option.
