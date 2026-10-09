I'd skip both ideas. Each one spends screen space, and your constraint is that all 40 to 60 trucks stay visible with no scrolling. A hero stat and oversized cards take rows away from the trucks. They also change which trucks look important, and that's the wrong thing to decide by default.

**Job of the screen:** a dispatcher glances up and sees which trucks need action, then finds a specific truck or door quickly.

## Layout (1920×1080 assumed)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Yard · 14:32      52 on site │ 6 Arriving  14 Waiting  18 Loading  9 Unl  5 Rdy│  ~56px
├───────────────────────────────────────┬──────────────────────────────────────┤
│ DOOR TRUCK   CARRIER   STATUS  MIN NOTES │ DOOR TRUCK   CARRIER   STATUS  MIN NOTES │
│ 01   T-4471  Acme      ▶ Loading  42  …  │ 31   T-4502  Delta     ● Waiting  95  …  │
│ 02   T-4410  Bolt      ■ Ready    12  …  │ 32   …                                   │
│ …    (30 rows, ~32px each)               │ …    (30 rows)                           │
└───────────────────────────────────────┴──────────────────────────────────────┘
```

- **Top strip, not a hero.** It's a single line with the total on the left and one count per status. The counts also work as the legend for the status marks below. It stays one line tall.
- **Two side-by-side panels of the same table.** Each holds 30 rows at about 32px with 16 to 18px text. That fits 60 trucks with a little room to spare. Fewer trucks leave blank space at the bottom, and the rows never grow to fill it. If the board runs on a larger or higher-resolution display, add a third panel instead of making rows taller.
- **Stable order: by dock door.** Dispatchers think in doors, and rows that don't move build spatial memory. Arriving trucks have no door yet, so they go at the end of the second panel. Don't re-sort by urgency, because rows that jump around cost more attention than they save.

## Ranking inside the rows

1. **Needs action:** ready to leave, or waiting or on site past a threshold. These rows get a tinted background and bold minutes. Only these rows get the tint, so it covers roughly 10% of the board and stays noticeable.
2. **Identity:** the door number and truck ID, in bold at the left edge. Dispatchers look trucks up by these.
3. **Status and minutes:** the status as a small shape plus a word, in regular weight. The minutes column is right-aligned with tabular figures.
4. **Carrier and notes:** a softer gray, still readable. Notes truncate to one line, with a small marker on rows that have more text. The full note opens on tap or hover.

Make the status distinct without relying on color alone. Use a different glyph for each (▶ ● ■ and so on), and color only the two states that need action. Colored pills on all five statuses would make every row compete.

## Assumptions to check

- **Truck count:** if you can exceed about 60 on this display, the rows get too tight. The fix is a third panel or a larger screen, not smaller text.
- **"Important" thresholds:** I assumed the action state comes from a rule such as "waiting over X minutes" or "ready to leave". Please tell me the real rules, because they decide which rows get the tint.

If you want, I can build this as an HTML mockup with 52 sample trucks, so you can test the density on the actual monitor.
