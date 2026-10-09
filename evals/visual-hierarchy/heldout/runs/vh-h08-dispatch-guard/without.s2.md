I'd skip both ideas, and I'd change the layout approach.

**Why not the hero stat and bigger cards**
- **Space:** On a 1080p screen, 60 trucks at about 40px each is already most of the height. A hero stat and oversized cards come out of that budget, so the other trucks get shrunk.
- **Stability:** If important trucks get bigger cards, the layout reflows as priorities change. Dispatchers who stare at this all shift rely on a truck staying in the same place.
- **Relevance:** A single big number (say, "52 trucks on site") isn't something a dispatcher acts on. They need to know which trucks are in trouble.

**What I'd do instead: group by status, keep every tile the same size, and show only the exceptions**

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ARRIVING 8 │ WAITING 14 (3 over 45m) │ LOADING/UNLOADING 22 │ READY 9    │  slim strip, ~48px
├────────────┬─────────────────────────┬──────────────────────┬────────────┤
│ T-4471  —  │ T-4388  Acme    —  62m  │ D07 T-4102 Acme  38m │ D03 T-3990 │
│ Acme    8m │ T-4390  Swift   —  51m  │ D08 T-4115 Swift 12m │ D11 T-4001 │
│ ...        │ ...                     │ ...                  │ ...        │
│            │                         │                      │            │
└────────────┴─────────────────────────┴──────────────────────┴────────────┘
```

- **Top strip:** The status counts double as the column headers, so there's no separate hero. Show a count of overdue trucks next to each one.
- **Columns:** One per status. Arriving and Ready are narrow. Waiting and Loading/Unloading are wide and can split into two sub-columns.
- **Tiles:** Every tile is a fixed-size, two-line block, about 36 to 40px tall.
  - Line 1: dock door, truck ID, and minutes on site, right-aligned in large type.
  - Line 2: carrier and the note, truncated to one line.
- **Order:** Sort by dock door in the loading column, so it maps to the physical yard. Sort longest-waiting first in Waiting. Leave the order alone otherwise, so tiles don't jump around.
- **Emphasis:** Keep tiles plain by default. Use color only when something needs action, and base it on thresholds (for example, minutes on site over a limit per status).
  - Amber is a warning and red is overdue. Add a small icon so it doesn't rely on color alone.
  - A note could also add a small marker. Unremarkable trucks stay gray and quiet.
- **Capacity:** Size the grid for 60 trucks even when only 40 are on site. Empty space is fine, and nothing should reflow.

**Why this should feel less overwhelming**
- Grouping by status gives dispatchers a mental map without sorting anything.
- A table of 60 equal rows is overwhelming because everything has the same weight. Here only the exceptions stand out.

**What I'd confirm before building**
1. **Display size:** Is this a 1080p monitor, a 4K wall display, or both? Below about 1080p, 60 tiles with readable text gets tight.
2. **Viewing distance:** Minutes on site should be readable at arm's length. I'd make that the largest text on each tile.
3. **Notes length:** If notes are long, a one-line truncation may lose important content. A short note-type tag (for example "damaged", "hold", "VIP") would help more than free text.
4. **Thresholds:** Ask dispatchers what counts as overdue per status. They'll have strong opinions, and the color coding depends on them.

I can mock this up as an HTML prototype with 60 sample trucks so you can see how dense it gets on a real screen. Want me to?
