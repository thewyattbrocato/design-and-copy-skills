I'd use small multiples: a 4×3 grid with one small line chart per store, all on one slide.

**Why not one chart.** Twelve lines on one axis would be a mess. The 9,000 and 400 stores also can't share a y-axis, because the small stores would flatten into the floor and you'd lose their seasonality.

**Layout**
- **Grid:** 4 columns × 3 rows. Every panel uses the same x-axis (weeks 1–52, with ticks at roughly quarter or month starts). Only label the x-axis on the bottom row.
- **Y-axes:** give each panel its own y-axis, starting at zero. Print the store's peak value in the panel, for example "peak 9,100". Say once in a footnote that scales differ per store. Without that note, a reader will think the small stores are as busy as the big ones.
- **Order:** sort panels by annual visitors, largest first. That way the size differences still show up in the order even though the scales differ.
- **Color:** draw ten stores in one muted gray or blue-gray. Give the two exceptions one accent color each, or a single shared accent.
- **Annotations:** only on the two exceptions.
  - Airport: mark the July peak, for example "Peak: July".
  - Harbor Mall: shade or dash the weeks after 30 and label it "Renovation from wk 30". The drop is a closure, not a demand trend, so it should be marked as such.
- **Christmas peak:** a faint vertical reference line at the week before Christmas (week 51) in every panel makes the "most peak here" pattern visible without any text.
- **Title:** state the finding, for example "10 of 12 stores peak the week before Christmas; Airport peaks in July, and Harbor Mall dropped after its week-30 renovation". Keep the footnote short with the scale note and the data source.

**Alternative if the panels feel too busy.** A heatmap with stores as rows and weeks as columns, each row shaded relative to that store's own max. It fits in less space and shows peak timing at a glance, with the December column lighting up and Airport as the odd row. It's weaker for showing the Harbor Mall drop and gives no exact values, so I'd choose it only if you want the "everyone peaks in December" message over the detail.

**Avoid**
- Two y-axes.
- A log scale, which is hard for a Monday audience to read.
- A legend. Put the store name in each panel.
- Rotated labels.

If you give me the CSV path, I can build the slide chart (PNG or SVG) with this layout.
