I'd skip both the hero stat and the bigger cards. With 40 to 60 trucks, no scrolling and nothing hidden, every pixel of height is needed for rows. A hero and large cards would cut the row budget, and the dispatchers would then have to scroll or you'd have to hide trucks. The overwhelm in the plain table probably comes from every row looking the same, not from the table being a table. So the fix is a ranking that makes a few rows stand out, not a bigger layout.

**Job of the screen:** show who needs a dispatcher's action right now, while keeping every truck visible.

**Layout (1920×1080, no scroll)**

```
┌──────────────────────────────────────────────────────────────────────────┐
│ Yard   Arriving [n]  Waiting [n]  Loading [n]  Unloading [n]  Ready [n]  │  ~56px slim strip
├───────────────────────────────────┬──────────────────────────────────────┤
│ DOOR TRUCK    CARRIER     STATUS MIN NOTES │ DOOR TRUCK    CARRIER   STATUS MIN NOTES │
│ 12   T-4471   Carrier A   ● Waiting  74 ▮ notes…   │ …                        │
│ 07   T-4302   Carrier B   ● Ready    31   notes…   │                          │
│ …    (≈30 rows per column, ~30px each)             │                          │
└───────────────────────────────────┴──────────────────────────────────────┘
```

- **Two columns of about 30 rows**, each row one line at roughly 30px. That fits 60 trucks in about 900px under the strip. On a wall display, or if you need bigger text, go to three columns of 20 and let notes truncate.
- **Slim status strip instead of a hero.** It's one line of counts per status, which also acts as the color legend. Clicking a count could highlight those rows, but it must never filter them out.
- **Sort order:** group by status in priority order (ready to leave, waiting, then the rest). Within each group, put the longest time on site first. The trucks that need action end up at the top-left, where people look first.

**Ranking inside each row**

1. **Primary:** door number, then truck ID. Dispatchers talk in doors and IDs, so these are bold and sit at the left edge.
2. **Primary, by exception only:** rows over a time threshold get a tinted background and a bold minutes value. Each status needs its own threshold, for example waiting is the one that matters most. I haven't invented numbers; [threshold per status] is yours to set. At most about 10% of rows should ever look this way. If half the rows are flagged, the thresholds are wrong.
3. **Secondary:** status, as a colored dot plus the word, so it still reads in grayscale and for color-blind users. Minutes are right-aligned in tabular numerals so they scan as a column.
4. **Tertiary:** carrier and notes, in a regular weight and a softer gray. Notes are one line, truncated, with the full text on hover or click. If a row has a note, a small marker makes that visible at a glance.

**Keep it calm:** use hairline dividers or very faint zebra striping, with no card borders, shadows or icons per row. Color is for status and for the over-threshold flag only.

**Trade-off:** sorting by status and time means rows move when a truck changes status. If dispatchers rely on a truck staying in one place, sort by door instead and keep the same flagging. You lose the "urgent at top" grouping, but positions stay stable.
