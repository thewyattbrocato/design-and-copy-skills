**I'd skip the radar chart.** For this comparison I'd use a spec table with small inline bars, and keep a chart only for the one or two specs shoppers care about most.

**Why radar fails for these specs**
- **Mixed units on one scale.** Range is in km, weight in kg, price in dollars, and so on. Each axis has to be rescaled to 0–100, so the shape depends on arbitrary min and max choices, and the shopper can't read real values off it.
- **"Lower is better" axes.** Weight, price and charge time are better when smaller, and the other three are better when larger. On a radar, a bigger polygon looks better, so you'd have to invert some axes. The Cove would then look strong on inverted axes in a way that confuses people.
- **Area misleads.** Polygon area changes with the order of the axes, so the same data can make a model look bigger or smaller.
- **Hard to read.** People can't compare positions around a circle accurately. Three overlapping polygons also hide each other, and you can't scan for a single number like price.

**What I'd build**

1. **Main comparison: a table with models as columns and specs as rows.** Put the exact value in each cell, with a thin horizontal bar behind or beside it showing magnitude on that row's own scale. Shoppers read real numbers and can still see at a glance who leads.
   - Use one neutral hue for the bars. Each row has its own scale, so don't compare bar lengths between rows.
   - Add a small "best in row" marker, such as a dot or bold text. Make "best" mean lowest for weight, price and charge time, and highest for range, motor and warranty.
2. **Optional chart above the table: one chart for the trade-off most shoppers weigh.** A scatter of price (x) against range (y) with three labeled points works well. It shows Cove as cheap and short-range, Ridgeway as expensive and long-range, and Trekline in the middle, without any rescaling.
3. **Color, if you color by model.** With only three models, use three distinct categorical hues in a fixed order, the same on every chart, and label each model directly. The same model should never change color between the table and the scatter. Run the palette through a colorblind check, and keep text in your normal text color rather than the series color.
4. **Interaction and accessibility.** Add hover tooltips on the scatter points. Keep the table as the accessible version of the data. Make sure identity doesn't rely on color alone, using direct labels or legend text.

If you still want a radar for visual appeal, limit it to 4–5 axes that all point the same direction (convert weight, price and charge time to "lightness", "value" and "fast charging"). Keep the exact-value table next to it. I wouldn't make the radar the main comparison.

I can build the table and scatter as an HTML/CSS snippet you can drop into the product page if you'd like. Tell me which framework or stylesheet the page uses, and your brand colors if you have them.
