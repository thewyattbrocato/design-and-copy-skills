I'd skip the radar chart. A small-multiples bar comparison, which is a spec table with a bar in each row, would work better.

**Why not radar**
- **Mixed units.** Your six specs are km, kg, dollars, watts, hours and years. Radar needs each one rescaled to a common 0–100 axis. The rescaling is arbitrary, and shoppers can't read real values off it.
- **Mixed "better" directions.** Longer range is good, but lower weight, price and charge time are good. On a radar, the biggest polygon looks like the winner even though it isn't. You could flip the axes, but then the labels get confusing.
- **Axis order changes the shape.** Reordering the same six axes changes the polygon and what it seems to say.
- **Area misleads.** People judge the filled area, which doesn't correspond to anything meaningful here.
- **Hard to read exact numbers.** Shoppers want to know whether it's 80 km or 110 km, and radar makes them guess.

**What I'd build**
1. **Layout.** Use one row (or small panel) per spec. Each holds three horizontal bars, one per model, and every panel is on its own scale. This keeps the "everything at once" feel without forcing the specs onto one axis.
2. **Labels.** Put the real value and unit at the end of each bar, such as "110 km" or "$1,350". Add a short tag on each row, like "lower is better" for price, weight and charge time. Don't put a number on anything except the bar ends.
3. **Colors.** Give each model one fixed color and use it in every panel. The three should be clearly distinguishable, including for colorblind users, and the order should never change. Include a legend, and also label the bars directly.
4. **Row order.** Lead with what shoppers weigh most, probably price, range, then motor. Put weight, charge time and warranty after.
5. **Best-in-row cue.** Optionally mark the best value in each row with a small check or bold label. Mark it on every row, since for some specs that's the lowest value and for others the highest. Note that Ridgeway wins range, motor and warranty, Cove wins price, weight and charge time, and Trekline wins none outright. That's a useful story, and it shows up clearly this way.
6. **Interaction and accessibility.** Add a hover tooltip on each bar. On mobile, stack the rows vertically. The row labels and values should give the same information as the chart, so it works as a table for screen readers.

If you want one visual summary above the detail, use a short "best for" line per model, for example "Ridgeway: longest range and most power; Cove: lightest and cheapest". That tells shoppers more than a combined score would.

I can build this as an HTML/CSS/SVG snippet you can drop into the product page. Do you want that, and does your site have brand colors I should use for the three models?
