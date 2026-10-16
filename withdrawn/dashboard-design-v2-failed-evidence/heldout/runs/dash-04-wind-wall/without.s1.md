# 55" control-room wall layout

**Principle:** Put what drives action at the top and right, put numbers people read from the chairs in the middle, and put reference material at the bottom. Anything that is "normal" most of the time (curtailment, weather warnings, alarms) should be quiet when clear and impossible to miss when active.

## Text sizes

The screen is about 120 × 68 cm. I'm assuming a 1080p-equivalent canvas. Double the pixel sizes for 4K, since the physical sizes are what matter.

| Tier | Who reads it | Approx. size | Use for |
|---|---|---|---|
| Far | 6 m, from the chairs | 64 px and up (about 4 cm tall) | MW, alarm count, curtailment and warning state, turbine state colours |
| Mid | 3–4 m | 36–48 px | Alarm text, turbine IDs, wind speed, section titles |
| Near | Someone who walks up | 22–28 px | Maintenance rows, chart axes, per-turbine MW, alarm timestamps |

Don't go below about 22 px for anything. If a person needs to walk up to read it, it should be detail that doesn't matter at a glance.

## Layout

```
┌──────────────────────────────────────────────────────────┐
│ STATUS STRIP: Curtailment │ Weather warnings │ Time      │ 10%
├────────────────────────────────────────┬─────────────────┤
│ FARM OUTPUT vs FORECAST     │  WIND    │                 │
│ (big MW number + short      │ speed +  │  ACTIVE ALARMS  │ 34%
│  trace with forecast line)  │ direction│  (sorted by     │
├─────────────────────────────┴──────────┤   severity)     │
│ TURBINE STATUS GRID (22 tiles)         │                 │ 30%
│                                        │                 │
├───────────────────────┬────────────────┤                 │
│ 7-DAY OUTPUT CHART    │ MAINTENANCE    │                 │ 26%
│                       │ THIS WEEK      │                 │
└───────────────────────┴────────────────┴─────────────────┘
        left column ≈ 68% wide            right ≈ 32%
```

## Each element

| Element | Share of screen | Placement | Far / near |
|---|---|---|---|
| **Active alarms** | ~29% | Full-height right column | **Far:** a large count and the top alarm's turbine and text. **Mid:** about 8 rows, with "+N more" below. **Near:** timestamps and acknowledgement state. |
| **Farm output vs forecast** | ~16% | Upper left, the largest block on the left | **Far:** the MW figure, plus a ± delta against forecast, coloured only when the gap matters. **Near:** a trace of the last ~6 hours and the next ~6 hours, with the forecast as a dashed line. Draw the curtailment limit on this chart as a step line, because it explains a gap. |
| **Turbine grid** | ~20% | Middle left, full left-column width | **Far:** tile colour plus a shape or icon for state (running, stopped, fault, offline, curtailed), so it never relies on colour alone. **Mid:** turbine ID. **Near:** per-turbine MW. Use 2 rows of 11, or match the physical site layout if it's recognisable. |
| **Wind speed and direction** | ~7% | Upper left, beside output | **Far:** speed as one big number. **Mid:** a compass arrow. Skip gust and history. |
| **Curtailment status** | ~5% | Top strip, left | **Far:** one state word. Clear is a thin grey or green "No curtailment". Active turns amber and shows the limit in MW and the end time. It sits next to the MW figure because it explains underperformance. |
| **Weather warnings** | ~5% | Top strip, right of curtailment | **Far:** the same quiet-when-clear behaviour. When active it expands to show the type, severity and valid-until time. |
| **7-day output chart** | ~11% | Bottom left | **Near only.** It's trend context, not an action driver. Keep it simple: one line, a daily gridline, a forecast overlay if you have one. |
| **Maintenance this week** | ~7% | Bottom, beside the chart | **Near only.** Show today and tomorrow first (turbine, task, window, crew), with the rest of the week compressed. Highlight any item overlapping a current alarm. |

## Behaviours worth specifying

- **Escalation:** When an alarm, curtailment or warning goes active, its block should change colour and grow. A fault should take over some of the grid or the strip. A small coloured dot is too easy to miss.
- **Colour:** Use a dark background, limit colour to state (normal is muted and only exceptions are saturated), and pair every colour with a shape or label.
- **Grid versus alarms:** Clicking is not an option on a wall display, so both need to agree. A turbine with an active alarm should show its tile in the fault state and be listed in the alarm column with the same ID.
- **Stale data:** If a feed drops, grey out that block and show "no data, last update HH:MM". A frozen display that looks live is the most dangerous failure here.

If it's useful, I can sketch the escalated state, for example a curtailment event with one turbine faulted and a high-wind warning.
