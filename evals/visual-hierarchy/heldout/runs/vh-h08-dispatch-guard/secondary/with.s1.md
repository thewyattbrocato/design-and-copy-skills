I'd push back on the hero stat and the big cards. They pull against your constraints. A big card takes several times the space of a table row, so 40 to 60 trucks won't fit on one screen. Once the screen is full, the remaining trucks either scroll off or get shrunk into the same overwhelming table. And any "most important" ranking is a judgment the dispatchers will reasonably dispute, which creates a second problem: "why is that truck small?"

For a board nobody can scroll or page, the goal is every truck visible at once with less noise per truck, and the screen's structure does more of that work than emphasis does.

**Organize by status lane, not one long list or a grid of tiles.**

```
┌──────────────────────────────────────────────────────────────────┐
│ SITE 14 · 06:40–14:40   On site 52   ⚠ Over 90 min: 7   Doors 18/24 │  ← slim header, not a hero
├────────────┬────────────┬────────────┬────────────┬──────────────┤
│ ARRIVING 6 │ WAITING 11 │ LOADING 14 │ UNLOADING 9│ READY 12     │
├────────────┼────────────┼────────────┼────────────┼──────────────┤
│ TRK-4471   │ TRK-4402   │ TRK-4390   │ TRK-4375   │ TRK-4360     │
│ D-07 ACME  │ — ABC  94m │ D-03 XYZ   │ D-11 ...   │ D-02 ...     │
│ 4m         │ note...    │ 38m        │ 61m        │ 102m ⚠       │
│ ...        │ ...        │ ...        │ ...        │ ...          │
└────────────┴────────────┴────────────┴────────────┴──────────────┘
```

- Lanes follow the workflow left to right, so a truck moves visibly across the board. Dispatchers think in transitions, and the lanes match that.
- Sort each lane by minutes on site, longest first. The problems sit at the top of each lane without anything being hidden.
- Give every card the same size and let the lane's card height flex with its count. Lanes are sized to the tallest lane, which is probably "Waiting" or "Loading" at peak. Check the real peak counts per status before you commit to sizes.

**Put the hierarchy inside each card, not in card size.**
- Dock door and truck ID are the largest text, since they're what dispatchers act on.
- Minutes on site is the second strongest element. Use a threshold color and a warning treatment for trucks over the dwell limit. Don't use a bigger box.
- Carrier is small and secondary.
- Notes are one truncated line. Show the full note on click or on hover.
- Keep each card to two or three lines so the same information always sits in the same place. Dispatchers will learn to scan by position.

**Make the exceptions the summary, not a hero stat.**
The most useful number on the header is "trucks past the dwell threshold," because it's actionable. Put it in the header as a count with a jump-to-lane action, not a 120px number. If you want a hero element, make it the "over threshold" count, not total trucks, which they already see from the cards.

**Reduce the overwhelm without hiding anything:**
- Color only for status and alerts. Use one or two alert colors and keep the rest neutral. This helps more than any layout change.
- Don't rely on color alone. Keep lane headers, text labels, and a small icon on warning cards so colorblind dispatchers and glances from across the room still work.
- Use a dark or muted base with high-contrast text. Dispatchers look at this all shift, so glare and eye strain matter.
- Keep text large enough to read from where they sit. Test the truck ID and door at actual viewing distance on the real monitor, not on your laptop.

**Before you commit, test three things:**
1. The peak count in the busiest lane on your worst shift. If it's 20 or more, the lane needs a two-column mini-grid inside it, not a scroll.
2. Whether a dispatcher can find a specific truck by ID in under a few seconds. If not, consider a small search or highlight field.
3. Whether the warning state is noticeable from across the room. If it isn't, the layout is fine but the alert treatment isn't.

If you can share the real peak counts per status and the monitor size, I can work out the card dimensions and lane widths concretely.
