**I'd use a heatmap: 12 rows (stores) by 52 columns (weeks).** Each cell is one store's visitors in one week, and the color shows how busy that week was.

- **Color each row against that store's own peak** (0% to 100% of its best week), not against the global maximum. Otherwise the 400-visitor stores look flat next to the 9,000-visitor store. Put each store's peak in a label at the right edge (e.g., "Downtown · peak 9,012") so the absolute size is still visible.
- **Sort rows by peak week**, so the December stores form one band near the bottom, Airport sits apart in July, and the timing differences are visible at a glance.
- **Label the x-axis by month** (Jan to Dec) rather than week numbers. Mark Christmas week with a thin line.
- **Mark Harbor Mall's renovation** with a vertical line at week 30. Its row should go pale after that point, which shows the cliff. Add a short note such as "avg. weeks 1–30: X; weeks 31–52: Y" so the size of the drop is stated, not just implied.
- **Use one sequential color scale** (light to dark, one hue), with a legend reading "% of store's peak week." Avoid a rainbow palette, and make sure the lightest and darkest colors are still distinguishable on a projector.
- **Put a takeaway title on the slide**, e.g., "Eleven stores peak the week before Christmas; Airport peaks in July; Harbor Mall dropped after its week-30 renovation." The chart then supports a claim instead of making the audience find it.

If the audience cares more about the shape of each store's trend than about timing, the alternative is 12 small-multiple line charts in a 4×3 grid, sharing the x-axis, each with its own y-scale labeled with its peak. That's more readable per store but takes more space and makes the cross-store comparison harder. For a single slide with a timing story, I'd go with the heatmap.

If you give me the CSV path, I can build the heatmap as an SVG or a matplotlib PNG, with the Harbor Mall break and the peak labels included.
