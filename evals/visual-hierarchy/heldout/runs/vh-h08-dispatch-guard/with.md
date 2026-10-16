I'd skip both ideas. Your constraint is that nothing scrolls, pages or hides, so every pixel of height belongs to rows. A hero stat and larger cards take that height from 40 to 60 trucks, and they make the board less consistent to scan.

**Layout**

```
┌──────────────────────────────────────────────────────────────┐
│ 52 on site │ Arriving 6 │ Waiting 9 │ Loading 14 │ Unl. 17 │ Ready 6 │  clock
├───────────────────────────────┬──────────────────────────────┤
│ Door  Truck   Carrier  Status Min  Notes │ Door  Truck  Carrier  Status Min  Notes │
│ 01    …                              │ 31    …                                   │
│ …     (≈30 rows)                     │ …     (≈30 rows)                          │
└───────────────────────────────┴──────────────────────────────┘
```

- **Top strip, one line tall.** It shows total on site and a count per status. This replaces the hero stat: it's the same information at about a tenth of the height, and it doubles as the status legend.
- **Body in two side-by-side panels** with the same columns repeated. At 30 rows per panel, a 1080p screen gives roughly 30px rows. That fits 16–18px text and fits 60 trucks. One 60-row column would force rows of about 15px, which is unreadable.
- **Stable order by dock door.** Trucks without a door (arriving, waiting) go in a block after the doored ones. Rows should never re-sort as statuses change. Dispatchers build spatial memory ("door 14 is bottom of the left panel"), and a jumping list destroys it.
- **Columns in reading order:** door, truck ID, carrier, status, minutes, notes. Door and truck ID are the two things dispatchers look up by, so they get the strongest weight. Carrier and notes are regular weight in a softer value.

**Where the emphasis goes**

Most rows should look calm. Reserve loudness for trucks that need a dispatcher to act, which should be about 10% of rows:
- **Waiting** (needs a door) and **ready to leave** (needs release) get a filled status chip. Loading, unloading and arriving stay plain text.
- **Minutes** are bold and tabular-aligned. Past an overdue threshold, the number and a thin left edge on the row go to the alert color. The thresholds per status are `[to set with dispatchers]`. I haven't invented any.
- **Status uses a label plus a shape or fill, never color alone.** The board has to hold up for color-blind dispatchers and in glare.
- Zebra striping or hairlines between rows, one of them, not both.

**Trade-offs**
- **Notes are one line,** truncated, with a small marker on rows that have more. Full text shows on tap or hover. If notes are usually long, I'd widen that column and shrink carrier.
- **This assumes a wall or desk display around 1080p or larger.** Tell me the real resolution and I'll recompute row height and the font sizes. A smaller screen may need three panels, or a denser status strip.

I can mock this up as HTML with 52 placeholder rows to check the density on your actual screen. Want that?
