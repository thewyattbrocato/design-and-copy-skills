I'd skip both the hero stat and the bigger cards. They fight the one constraint you can't bend: all 40–60 trucks visible with no scrolling. Anything that makes some rows taller pushes other trucks off screen. I'd make every truck the same size and get the importance from emphasis instead.

**Layout (1920×1080 assumed)**

```
┌──────────────────────────────────────────────────────────────────────┐
│ Arriving 6 │ Waiting 14 │ Loading 11 │ Unloading 9 │ Ready 5 │ 45 on site │  ← slim strip, ~48px
├───────────────────────────────┬──────────────────────────────────────┤
│ WAITING                       │ LOADING (continued)                  │
│▌T-4471 Acme   —  Waiting  94m ▲ no door │ T-4390 Brex  D12 Loading 31m  note… │
│ T-4502 Brex   —  Waiting  61m │ …                                    │
│ …                             │ UNLOADING                            │
│ LOADING                       │ …                                    │
│ …                             │ READY TO LEAVE                       │
└───────────────────────────────┴──────────────────────────────────────┘
```

- **Two columns of about 30 rows** at roughly 34px each. Use three columns of about 20 on a larger or higher-resolution screen. Fill each column top to bottom.
- **One line per truck.** The order is truck ID, carrier, door, status, minutes, then notes. Notes get the leftover width, since they're the only free-text field. Door and minutes are right-aligned or in fixed-width columns so the eye can run down them.
- **Group rows by status** under thin band labels, in workflow order. Within a group, sort by longest time on site. Rows shift only when a truck changes group or passes another one.
- **The summary strip** replaces the hero stat. It's the same five statuses with counts, so it doubles as a legend, plus the total. It's a quick reference and shouldn't be the focal point.

**Importance**
- Rows are quiet by default: neutral text, no per-row boxes, and status shown as plain text with a small dot.
- Only exceptions get loud. These are trucks over their dwell limit, waiting with no door assigned, and ready to leave. Use one treatment for all of them: a colored left bar, bold minutes, and a symbol such as ▲. The symbol means it still reads in grayscale and for color-blind dispatchers.
- Aim for fewer than about 10% of rows loud at any time. If more are, the thresholds are wrong, because the screen stops saying anything when everything is highlighted.
- Make the minutes number the strongest element in a row. It's what dispatchers act on.

**Why this fixes "overwhelming"**
The current table is probably uniformly dense and equally loud. Grouping by status and quieting the normal rows lets the eye skip most of the screen and land on the few trucks that need action. That calms the screen without hiding anyone.

**Assumptions to check**
- I assumed a 1080p display. Row height scales with screen size, and at 60 trucks on a 1080p screen, 34px is about the floor for text readable from a desk.
- You need to define "important" with real thresholds, for example minutes waiting over X. I don't know your yard's numbers.
