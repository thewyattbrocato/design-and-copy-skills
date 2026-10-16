**I'd skip the radar chart. Use a comparison table, with small bar rows for the numeric specs.**

**Why radar doesn't fit this data**
- **Mixed units.** Km, kg, dollars, watts, hours and years all get squeezed onto one 0–100 scale. That requires normalizing, and the choices you make while normalizing change how the chart looks.
- **"Bigger" doesn't mean "better."** A high price, a heavy frame and a long charge time are bad, but they push the shape outward. Shoppers will read a bigger polygon as the better bike. You'd have to flip those axes, and then the labels no longer match the numbers.
- **The shape depends on axis order.** Reorder the six spokes and each bike looks different.
- **Exact values are hard to read.** Shoppers want to know "how much lighter is the Cove?", and a radar can't answer that.

**Setup I'd recommend**
1. **Layout.** Put one column per bike (Trekline, Ridgeway, Cove) and one row per spec.
2. **Values.** Print the real value with its unit in each cell, so shoppers can read exact figures.
3. **Bars.** Add a thin horizontal bar behind or under each number. Scale each row from zero to its own maximum, so the longest bar is the largest value in that row. The bars are flat and in one neutral color.
4. **Direction.** Don't color anything red or green. Add a small "lower is better" or "higher is better" note to each row label. For price, weight and charge time, a smaller bar is the better result, and a note is more honest than a color.
5. **Order.** Group the rows by what shoppers care about:
   - Performance: range, motor
   - Practicality: weight, charge time
   - Value: price, warranty
6. **Highlight.** Add a one-line takeaway per bike, for example "Ridgeway: most range and power, heaviest and priciest" or "Cove: lightest and cheapest, shortest range."
7. **Mobile.** Keep the table readable on a phone. If three columns are too wide, stack one bike per card with the same rows.

**If you still want a graphic**
Use small multiples: one small horizontal bar chart per spec, with three bars each (one per bike), in the same bike order and the same color for each bike throughout. That's essentially the table above, drawn out. It shows rank at a glance without combining units.

**If you keep the radar**
- Normalize each axis from 0 to the maximum among the three bikes.
- Invert price, weight and charge time, and label them "lighter," "cheaper" and "faster charge" so outward always means better.
- Fix the axis order.
- Put the raw values next to the chart, because the polygon alone can't carry them.

I can build the table version as HTML/CSS you can drop into the product page. Tell me if you want that, and what the page's fonts and colors are.
