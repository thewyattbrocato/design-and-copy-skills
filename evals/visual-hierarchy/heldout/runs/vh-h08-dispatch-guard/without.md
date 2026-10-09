Your instinct to fix "overwhelming" is right, but the hero stat and bigger cards would work against your constraints.

**Why I'd drop them**
- **Bigger cards:** Fifty to sixty trucks with no scrolling means every truck gets a fixed, small slice of the screen. Enlarging some shrinks the rest. Cards that change size or move also break the spatial memory dispatchers build ("door 14 is bottom left").
- **Hero stat:** A single big number tells a dispatcher nothing they act on. They need to know which truck needs attention, not the total.

**What I'd do instead**

1. **Slim summary strip (~60px)**
   - Show five status counts (arriving, waiting, loading, unloading, ready) plus one "over dwell limit" count.
   - Make it small. It's a legend and a glance check, not a hero.

2. **Two side-by-side banks of dense rows**
   - On a 1080p screen, 60 rows at about 30px each fit as 2 columns of 30 with no scroll.
   - Scale row height to the truck count, so at 40 trucks the rows get roomier.
   - Columns per row: truck ID, carrier, door, status chip, minutes on site, notes.

3. **Stable ordering**
   - Sort by dock door so rows don't jump around.
   - Trucks without a door (arriving, waiting) go in their own block, sorted by longest wait first.
   - Don't re-sort live. Let rows change in place.

4. **Calm by default, loud by exception**
   - Use neutral rows with zebra striping or hairlines. Show status as a small colored chip plus a text label, so color isn't the only signal.
   - Reserve strong color for rows that need action: over dwell threshold, or ready to leave and blocking a door.
   - The "important" trucks get a colored left edge and bolder minutes, not a bigger size. They stay in place and stay scannable.

5. **Notes without hiding anything**
   - Show the first ~30 characters inline, with an icon when a note exists.
   - Put the full note in a click or hover popover.
   - Truncating is a sensible compromise because no truck is hidden.

6. **Type**
   - Use tabular numerals for minutes and a monospace or semi-mono face for IDs.
   - Keep at least 14–16px text for a screen read from a desk.
   - Use light text on a dark, low-glare background if the board runs all shift.

**Two things I'd need to confirm**
- **Display:** What are the screen size and resolution, and is it a wall display or a desk monitor? Row height, and whether two banks are enough, depend on this.
- **"Important":** What makes a truck important to your dispatchers? If it's dwell time, door conflicts, or flagged notes, I'd turn that into the exception rules in point 4.

I can mock this up as an HTML prototype with 40 and 60 truck sample data so you can test it with dispatchers.
