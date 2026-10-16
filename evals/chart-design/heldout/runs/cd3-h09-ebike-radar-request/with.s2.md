**Skip the radar chart.** I'd use a comparison table with small inline bars, or failing that, small multiples (one mini bar chart per spec).

**Why radar is a poor fit here**
- **The axes don't share a unit.** Km, kg, dollars, watts, hours and years can't sit on one scale. You'd have to rescale each to 0–100, and that hides the real numbers.
- **Better isn't the same direction on every axis.** Higher range is good. Higher weight, price and charge time are bad. A big polygon wouldn't mean a better bike, and shoppers will read it that way.
- **The shape depends on axis order.** Reorder the six spokes and each bike's outline changes. Polygon area is also hard to compare by eye.
- **You can't read exact values off it.** A shopper deciding on a purchase wants to see "110 km" and "$2,400".

**Recommended setup: table with in-cell bars**

Rows are specs and columns are the three bikes. Each cell shows the actual value with a thin bar on a shared scale for that row. The bars start at zero and are scaled within each row only.

| | Trekline | Ridgeway | Cove |
|---|---|---|---|
| Price | $1,850 | $2,400 | $1,350 |
| Range | 80 km | 110 km | 60 km |
| Motor | 500 W | 750 W | 350 W |
| Weight | 24 kg | 28 kg | 19 kg |
| Charge time | 4.5 h | 5.5 h | 3.5 h |
| Warranty | 2 yr | 3 yr | 2 yr |

- **Order the rows by what shoppers care about.** Price, range and motor go first, with weight, charge time and warranty after.
- **Don't color good and bad.** Use one neutral color for all bars. If you want a highlight, mark the best value in each row with bold text or a small marker. For price, weight and charge time, the best value is the lowest. For range, motor and warranty, it's the highest. Add a note like "lowest is best" so the direction is clear. Avoid red versus green, which fails for color-blind shoppers.
- **Put the bike names at the top of each column.** Use the same color or position for each bike everywhere on the page.
- **Make it work on mobile.** Stack each spec as a small group of three bars, or keep the table and let it scroll horizontally.
- **Add a text takeaway.** For example: "Ridgeway has the longest range and strongest motor. Cove is the lightest and cheapest. Trekline sits in the middle on every spec." That also covers accessibility.

**If you want a real chart instead**

Use six small bar panels, one per spec, with three bars each. Keep the bike order the same in every panel, start each axis at zero, and label the values directly on the bars. Use gray bars with one accent color. This is more visual than a table, but takes more room.

**Price per km of range**

With only three bikes, you could add one derived row: price per km of range. That works out to about $23/km for Trekline, $22/km for Ridgeway and $22.50/km for Cove. It would show shoppers that Ridgeway costs more but isn't worse value. I'd only include it if you're happy to show that comparison.

If you'd like, I can build this as HTML/CSS for your product page. Tell me your stack (plain HTML, React, etc.) and whether you have brand colors.
