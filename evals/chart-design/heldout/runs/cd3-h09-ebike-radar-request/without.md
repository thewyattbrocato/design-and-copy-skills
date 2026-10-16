I'd skip the radar chart. Use a small comparison table with an inline bar in each spec cell, or one small bar chart per spec.

**Why not a radar chart**
- **The axes disagree about "better."** Higher is better for range, motor power and warranty. Lower is better for weight, price and charge time. On a radar, a bigger polygon would imply "better," and that isn't true here. You'd have to invert three axes, which makes the chart confusing.
- **Shape and area mislead.** The area depends on the order of the axes. Shoppers can't read exact values off a radar, and with only three products there's nothing for the shape to reveal.
- **The units differ.** km, kg, $, W, hours and years all get rescaled to 0–100%. That hides real differences. For example, Trekline and Cove both have a 2-year warranty, but the rescaling makes them look different.

**What I'd build**

1. **A small-multiples layout.** Make six small horizontal bar charts, one per spec, with three bars each (Trekline, Ridgeway, Cove).
   - Every chart has its own honest axis that starts at zero, so nothing needs normalizing.
   - Put the value label directly on each bar (for example "110 km"). With only three bars per chart, labeling every one is fine.
   - Give each spec a plain-language title that includes the direction, such as "Range (longer is better)" and "Price (lower is better)".

2. **Color by model, consistently.**
   - Each model keeps the same color in all six charts, and the colors are assigned in a fixed order.
   - Use a legend, and also label the bars directly.
   - Don't color bars by "good" or "bad." Red and green would imply a judgment, and these are trade-offs.

3. **Order the specs by what shoppers care about.** I'd go price, range, weight, motor, charge time, warranty. Keep the same model order in every chart.

4. **Add the accessibility basics.**
   - Add hover tooltips with the exact values.
   - Check the palette is colorblind-safe, since you're only using 3 colors.
   - Offer a table view, or just show the table below the charts.
   - Make sure it stacks into one column on mobile.

**Alternative:** if you want something more compact, use a plain comparison table with a small inline bar behind each number. It's the most scannable option on a product page, and shoppers can read all 18 values at once. I'd lean toward this if the page is mobile-heavy.

I can build this as an HTML/SVG component. If you want that, tell me your brand colors and whether the page has a dark mode. Otherwise I'll use a neutral validated palette.
