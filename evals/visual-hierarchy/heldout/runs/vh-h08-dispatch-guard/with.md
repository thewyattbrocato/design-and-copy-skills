I'd drop both ideas. Dispatchers won't scroll, page or hide trucks, so every pixel of height is spent on rows. A hero stat and bigger cards take space from rows and make the board less scannable.

**What I'd build** (assuming a 1920×1080 display, so tell me if it's different)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ Yard · 52 on site │ Arriving 6 │ Waiting 11 │ Loading 18 │ Unl. 12 │ Ready 5 │  ← 48px strip
├───────────────────────────────────┬──────────────────────────────────────┤
│ ID      Carrier   Door Status  Min Notes │ ID  Carrier  Door Status  Min Notes │
│ ────────────────────────────────  │ ────────────────────────────────     │
│ 26 rows × 36px, same height,      │ 26 rows, continues the sequence      │
│ no cards, no gaps between groups  │ in the second column                 │
└───────────────────────────────────┴──────────────────────────────────────┘
```

1. **Two columns of compact rows, filled top to bottom.**
   - 1080px minus the strip leaves about 1000px. At 36px per row that's 27 rows a column, so 54 trucks fit.
   - If you reach 60, drop to 32px rows. Check this against your real peak count.
   - Each row is a full 960px wide, which is enough for all six fields.

2. **Replace the hero stat with a one-line summary strip.**
   - It shows total on site plus a count per status.
   - The counts double as the status legend and use the same chip styling as the rows.
   - It's useful context, but it isn't what dispatchers act on, so it stays small.

3. **Rank within the row, not between rows.**
   - **Primary:** truck ID and dock door, in the heaviest weight and largest size in the row.
   - **Secondary:** status and minutes on site.
   - **Tertiary:** carrier and notes, in a softer value (not a lighter weight).
   - Only exceptions get emphasis, about a tenth of the board. That means minutes past a threshold (a bold number on a tinted cell) and "ready to leave". Everything else stays quiet, so the exceptions stand out.

4. **Status needs two cues, not color alone.** Use a short text label plus a colored chip, so it still reads in grayscale and for colorblind users. Keep the palette to about three loud colors. "Waiting too long" should be the loudest.

5. **Keep rows in a stable order.**
   - Group by status in a fixed order, and within a group sort by minutes descending. The longest waits then rise to the top of their group.
   - Don't let rows jump around on every refresh, because dispatchers build spatial memory. Re-sort only when a truck changes status.
   - Use thin zebra striping or hairlines to help the eye track across a 960px row. Skip boxes and shadows.

6. **Notes are the hard column.**
   - Give it a fixed width, one line, truncated with an ellipsis.
   - A note marker (a dot) shows when a note exists. Tapping or hovering expands it in place without hiding other trucks.
   - Long notes are mostly a sign the process needs a structured field, such as "hold" or "damaged".

**Trade-offs:** The summary strip is the only thing I'd call a hero, and I deliberately kept it small. The exception threshold (for example, waiting over 45 minutes) needs real numbers from the dispatchers.

I can mock this up as HTML with realistic dummy data to check the density at 60 trucks.
