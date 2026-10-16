# Layout: A4 portrait, one page

**Use small multiples: 12 identical mini-charts in a 3-column × 4-row grid.** One chart with 12 lines would be unreadable, and 12 separate scales would make branches hard to compare. A 3×4 grid fits A4 portrait well, with each panel roughly 6 cm wide.

## Top to bottom

1. **Title (the finding):** something like "Visits peaked in summer at most branches; Dunmere fell sharply after its July roof closure". Use a neutral title if the board would prefer that.
2. **Subtitle (one line):** "Monthly visits per branch, Jan–Dec 2025", plus the source and as-of date. I don't have those, so leave `[source]` and `[as of date]` placeholders for you to fill.
3. **The 3×4 grid**, taking about 75–80% of the page.
4. **Footer notes (small):** what the shaded band means, the scale note, and whether July was a partial month for Dunmere.
5. **Optional: a 2–3 line text takeaway** under the title or at the bottom. Add a Dunmere figure there only if you have one, such as "down X% from Jan–Jun average". I haven't invented a number.

## Each panel

- **Same shape everywhere.** Use a thin dark-gray line, or columns if you prefer to read exact months.
- **Shared y-axis across all 12 panels.** This keeps the comparison honest, so a big branch looks big. If your smallest branches are less than about a third the size of the largest, their summer peaks will flatten. In that case switch to each panel having its own scale, and print the peak value in each panel so nobody misreads it. Either way, say which one you used in the footer.
- **Y-axis:** start at zero, with labels only on the left column. Use faint or no gridlines.
- **X-axis:** month initials (J F M A M J J A S O N D), shown only on the bottom row.
- **Summer band:** a light-gray vertical band behind the summer reading months, in the same position in every panel. It shows the seasonal peak without any extra text. Fill in the exact months from your program dates.
- **Panel label:** the branch name, top-left, in bold, horizontal. Use your alphabetical order (Ashby → Linden), which makes lookup easy.

## Dunmere

- It's the only panel with color. Use one accent color, a thicker line, and a bold name.
- Add a thin vertical marker at July with the note "Roof closed, July" inside the panel.
- Label the last point or the post-July level directly.
- Because this is printed, don't rely on color alone. The thicker line, the marker and the annotation carry it in black and white too.
- If Dunmere's grid position matters, keep it in alphabetical order (row 2, column 1) rather than moving it to the top. The accent makes it findable.

## Print details

- Minimum text size is about 7–8 pt, with the title around 16–18 pt.
- Use generous gutters between panels instead of borders or boxes.
- No gradients, shadows or legends. Direct labels and the footer note cover everything.
- Leave about 15 mm margins.

## Questions for you

1. **How different are branch sizes?** That decides shared versus per-panel scale.
2. **Was July a full or partial month for Dunmere?** If it's partial, mark it with a hollow point or dashed segment.
3. **Has Dunmere reopened?** If so, the line should show the recovery, and the annotation should say so.

I can build this as an SVG or a matplotlib script sized to A4 if you send me the monthly numbers.
