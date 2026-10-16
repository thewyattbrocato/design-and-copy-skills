**I'd skip the radar chart.** Use a small comparison table with a mini bar in each cell. If you want a chart as well, use one small bar panel per spec.

**Why radar doesn't work here**
- **Mixed units.** Km, kg, dollars, watts, hours and years have no shared scale. You'd have to normalize each to 0–100, and then the shape shows your normalization choices, not the bikes.
- **Direction conflicts.** Higher is better for range, motor power and warranty. Lower is better for price, weight and charge time. On a radar, a bigger polygon would look better, but it wouldn't be.
- **Axis order changes the shape.** Reordering the spokes changes the polygons. Shoppers can't read exact values, and three overlapping polygons are hard to tell apart.

**What to build instead**
1. **A table is the main element.** Models are columns and the six specs are rows, so shoppers get exact values. Add a thin horizontal bar in each cell, scaled from zero to the highest value in that row. Bars start at zero so the lengths stay honest.
2. **Mark the better value in each row** with a bold weight or a small "best" tag, not red/green. For price, weight and charge time, "better" means lowest. Say so in a note, for example "Lower is better".
3. **Use one color per model, consistently.** Ridgeway might be a dark blue, Trekline a mid-tone and Cove a muted gray. Keep the same colors and the same column order everywhere on the page.
4. **Make the takeaway text.** For example: "Ridgeway goes farthest and has the strongest motor and warranty. Cove is the lightest, quickest to charge and cheapest. Trekline sits in the middle." This should be real text so screen readers and search engines can read it.
5. **Optional chart version.** Use six small panels, one per spec. Each panel has three bars on a shared zero baseline, with values printed on the bars and the same model order and colors in every panel.

**Optional extra.** Shoppers often decide on a trade-off such as range against price. A scatter with three labeled dots would show that, and Ridgeway's extra range costs about $550 more than Trekline. It's a bonus, not a replacement for the table.

If you still want the radar, I can build it honestly. I'd normalize each spec to 0–100, flip price, weight and charge time so outward always means better, put zero at the center, and label every spoke with the raw values. I'd still recommend the table.

If you give me your stack (plain HTML, React, or a CMS), I can write the table with the inline bars.
