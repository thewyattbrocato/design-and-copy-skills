I'd skip the radar chart. A table with small bars inside the cells shows the same "everything at once" view and avoids the radar's problems.

**Why radar fits poorly here**
- **Mixed units:** your six specs are km, kg, dollars, watts, hours and years. A radar needs each one rescaled to a made-up 0–100 axis, and the rescaling decides how the shapes look.
- **Mixed directions:** higher is better for range, motor and warranty, but lower is better for weight, price and charge time. A bigger polygon wouldn't mean a better bike unless you flip some axes, and shoppers won't guess that you did.
- **Axis order:** the shape changes if you reorder the axes, so the visual impression is partly arbitrary.
- **Hard to read values:** shoppers can't pull out "how much heavier is the Ridgeway?" from a polygon.

**What I'd build**

A comparison table, with specs as rows and the three models as columns:

1. **Layout:**
   - Use a real HTML `<table>`. It's accessible, works on mobile and lets shoppers read exact values.
   - Put a short horizontal bar behind or beside each value.
2. **Bar scale:**
   - Start every bar at zero.
   - Scale each row to its own maximum, so Ridgeway's 110 km is a full bar and Cove's 60 km is about 55%.
   - Add a small note that bars are scaled within each row.
3. **Column order:** Cove, Trekline, Ridgeway (price ascending), the same everywhere on the page.
4. **Row labels:**
   - Include units: "Range (km)", "Weight (kg)", "Price ($)", "Motor (W)", "Charge time (h)" and "Warranty (years)".
   - Add "lower is better" to weight, price and charge time, in text rather than red or green.
5. **Color:**
   - Make the bars one muted neutral.
   - If you want to push one model, give only that model's column an accent color.
   - Don't use a different saturated hue for each model.
6. **Takeaway line above the table:** for example, "Ridgeway goes farthest and has the strongest motor. Cove is the lightest and cheapest." Check it against the numbers before you publish.

**If you want an actual chart**

Use small multiples: six small panels, one per spec, each with three horizontal bars. Keep the same model order and color in every panel, label values directly on the bars, and start each bar at zero. This takes more space than the table, but it's a good fit if the page is chart-led.

**If you still want the radar**

You'd need to:
- normalize every axis to a percentage of the best value;
- flip weight, price and charge time so outward always means better;
- fix a deliberate axis order;
- print the raw values at each vertex;
- say how the scaling works in a caption.

Even then, I'd put the table underneath it.

I can write the table (HTML and CSS) or the small-multiples version (SVG) if you tell me which you prefer.
