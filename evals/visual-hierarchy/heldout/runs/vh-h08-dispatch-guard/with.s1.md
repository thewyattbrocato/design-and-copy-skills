I'd skip the hero stat and the bigger cards. Both spend space that 40 to 60 no-scroll rows can't spare, and neither fixes what makes the table overwhelming.

**Why those two don't work**
- **Bigger cards:** on a 1080p display, 60 rows in one column leaves about 16px each. Making some trucks larger forces the rest to shrink or drop off the screen, and the dispatchers have ruled that out.
- **Hero stat:** a big number like "52 trucks on site" doesn't help a dispatcher decide anything. A slim summary strip does the job in about 56px.
- **The real problem:** the table is overwhelming because every row and column is equally loud. The fix is to quiet the normal trucks and make the exceptions stand out.

**Layout (1920×1080, one screen, no scroll)**

1. **Summary strip (about 56px, full width).** It's a single row of status counts that double as the legend: `Arriving 6 · Waiting 11 · Loading 14 · Unloading 9 · Ready 4`. Next to it are the clock and a count of trucks over their time limit. Keep it modest in size. This is the only place status counts appear.

2. **Truck list (the remaining ~1000px).** It's one list that flows into two columns of up to 30 rows each, at about 32px per row. At 60 trucks that fits exactly. With fewer trucks, row height can grow slightly to fill the space, up to a cap.
   - **Row order, left to right:** Door → Truck ID → Status → Minutes → Carrier → Notes.
   - **Sort by dock door,** so each truck stays in the same spot while it's at the door. Rows that jump around as statuses change are hard to track on a screen watched all shift. Trucks with no door yet (arriving, waiting) go at the end, ordered by arrival time.

3. **How the rows rank**

| Level | Content | Treatment |
|---|---|---|
| Primary | Trucks that need action: waiting or on site past the threshold, or ready to leave | Tinted row background, bold Minutes and Status, plus a text cue like "▲ 95m" |
| Secondary | Door, truck ID, status | Regular text, high contrast, door and ID in bold or tabular figures |
| Tertiary | Carrier, minutes (when normal) | Softer gray, same size |
| Meta | Notes | Smallest, softest, truncated to one line. A small marker appears when a note is cut off |

   - **Emphasis budget:** keep highlighted rows to about 10 to 15% of the list. If a quarter of the board is highlighted, the threshold is wrong, so make it configurable.
   - **Status:** show it as a short word with a small colored dot, so it still reads in grayscale and for color-blind users. Use four or five muted hues at most. Only "ready to leave" and "overdue" should be saturated.
   - **Minutes:** right-align it in tabular figures so the durations are easy to scan down the column.

4. **Notes.** Notes can't be hidden, but they can be quiet. Give them the widest flexible column, one line each, in muted text. Rows with a note get a small marker, and a tap or hover opens the full text.

**Two assumptions to check**
- I assumed a 1080p wall display or a large monitor. On a smaller screen the same design goes to three columns with Carrier and Notes dropped to a second line, and I'd need the actual resolution to size it.
- I assumed "needs attention" is defined by dwell-time thresholds per status. If dispatchers define it differently (for example by carrier priority), the highlighted rows change, but the layout doesn't.
