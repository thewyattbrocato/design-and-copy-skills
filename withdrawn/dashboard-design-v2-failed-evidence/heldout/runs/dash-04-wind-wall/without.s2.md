# 55" control-room wall layout

**Principle:** the wall is for situational awareness from 3–6 m. Detail work happens at the operators' own workstations. The wall should look calm when things are normal, and anything abnormal should be visible from the back of the room.

## Layout (16:9, roughly 120 × 68 cm)

Use a dark background. The left two-thirds holds the farm state and the right third holds things that need action.

```
┌───────────────────────────────────────────────────────────┐
│ Weather warning strip (full width, thin, always reserved) │  ~5% height
├──────────────────────────────────────────┬────────────────┤
│ OUTPUT MW vs forecast │ Wind  │ Curtail- │                │
│ (50% of row)          │ (25%) │ ment(25%)│  ACTIVE ALARMS │
│                       │       │          │  (tall column, │
├──────────────────────────────────────────┤  ~35% width,   │
│                                          │  ~72% height)  │
│  TURBINE STATUS GRID (22)                │                │
│  2 rows × 11 (or match site layout)      │                │
│                                          ├────────────────┤
├──────────────────────────────────────────┤ Maintenance    │
│ 7-day output chart                       │ this week      │
└──────────────────────────────────────────┴────────────────┘
   left ~65% width                            right ~35%
```

Rows on the left take about 28% (output, wind, curtailment), 44% (turbine grid) and 28% (7-day chart) of the height.

## Relative size (share of screen area)

| Piece | Area | Why |
|---|---|---|
| Turbine grid | ~25% | The main "is the farm healthy" view. It's readable as a colour pattern from far away. |
| Alarm list | ~22% | The thing most likely to need action. It gets a tall column so 6–8 rows can be large. |
| Output MW vs forecast | ~14% | The headline number. |
| 7-day chart | ~10% | Context only, not urgent. |
| Wind speed/direction | ~7% | Explains the output. Put it right next to it. |
| Curtailment | ~7% | Small, but it explains a gap between output and forecast. |
| Maintenance | ~7% | Planning info, glanced at a few times per shift. |
| Weather strip | ~5% | Thin, but permanently reserved so nothing shifts when it activates. |

## Readable from across the room (3–6 m)

At 6 m, aim for cap height of about 25 mm or more, which is roughly 60 px text on a 1080p panel (about 120 px on 4K). Use that only for the items below.

- **Output MW:** a very large number, with the forecast value beside it at about half that size. Add a simple bar or marker for "above/below forecast" so you don't have to compare digits.
- **Turbine tiles:** state by colour and shape or icon (running, stopped, fault, offline, curtailed), not colour alone. About 1 in 12 men has some colour-vision deficiency, so a shape difference matters. The turbine number is small and is for up-close reading.
- **Alarm count and top 3–4 alarms:** large severity-coloured text with a short description. Unacknowledged alarms get a distinct treatment, such as a bold marker or slow pulse. Don't flash fast.
- **Curtailment:** a single state chip. It's dim grey for "none" and a strong colour with the cap value (for example "CURTAILED – 14 MW limit") when active.
- **Weather strip:** dim text when there are no warnings. It turns amber or red and gets larger text when one is active.
- **Wind:** a compass arrow plus a speed number about half the size of the MW figure. The arrow reads from a distance and the number is for up close.

## Readable only up close (walk-up)

- Alarm rows 5 and beyond, timestamps, tag IDs and acknowledgement state.
- Individual turbine IDs and any per-tile values such as kW or rpm.
- The 7-day chart's axes, gridlines and labels. From across the room it should only show the overall shape, with a thin "today" marker.
- Maintenance entries: turbine, task, window, and who's on it. Use small text, and make anything happening now or today bolder than the rest of the week.
- Forecast figures and the units next to the headline numbers.

## Design rules that make it work

1. **Quiet normal, loud abnormal.** Healthy turbines are muted green or grey, with no bright fills. Saturated colour is reserved for faults, alarms, curtailment and warnings. A glance should answer "is anything wrong?"
2. **Limit the severity palette** to three levels (for example grey/blue for info, amber for warning, red for critical), and use the same colours in every panel.
3. **Link related items.** If a turbine is in the alarm list, its tile should be visibly marked, and ideally it shares the alarm's severity colour. If it's in this week's maintenance, show a small wrench icon on the tile.
4. **Match the physical layout** for the turbine grid if the farm has a clear geometry (rows or strings). If not, a 2×11 grid ordered by turbine number is fine.
5. **Avoid motion** except for new unacknowledged critical alarms. With three operators, constant animation becomes noise.
6. **Reduce glare.** Use a matte or dark theme, and check the screen at the actual viewing angles. The 3 m and 6 m positions may see different contrast.

If your panel is 4K, the proportions stay the same. You can just fit more detail into the up-close text, such as more alarm rows or maintenance lines.
