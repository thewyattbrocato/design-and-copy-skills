# 55" control-room wall: layout

**Assumptions:** the operators are watching for faults and for output falling short of forecast, and they act on alarms. The screen is 16:9, about 120 × 68 cm.

## Layout (percentages of the screen)

```
┌──────────────────────────────────────────────────────────────┐
│ CURTAILMENT        │ WEATHER WARNINGS       │ UPDATED 14:32:05│  ~9% tall
├───────────────────────────────────┬──────────────────────────┤
│                                   │ ACTIVE ALARMS            │
│  FARM OUTPUT vs FORECAST          │ (sorted by severity,     │
│  big MW number, gap, today trace  │  newest first within     │
│  + wind speed/direction inset     │  level; "+N more")       │
│                                   │                          │
│                                   │                          │  ~68% tall
├───────────────────────────────────┤                          │
│  TURBINE GRID  (22, fixed layout) │                          │
│                                   │                          │
├───────────────────────────────────┼──────────────────────────┤
│  7-DAY OUTPUT                     │ MAINTENANCE THIS WEEK    │  ~15% tall
└───────────────────────────────────┴──────────────────────────┘
        left column ≈ 60% wide          right column ≈ 40%
```

## What goes where and how big

| Piece | Position and size | Why there |
|---|---|---|
| **Exceptions strip: curtailment, weather warnings, last-updated** | Full-width band across the top, ~9% of height. Curtailment gets ~40% of the width, weather ~40%, and the clock ~20%. | These are the "is anything unusual" slots, and curtailment explains a gap against forecast. Both are quiet text when clear ("No curtailment", "No warnings"). When active they turn into the loudest block on the screen, with the limit in MW and the start time ("Curtailed to 30 MW since 14:20"). The positions never move. |
| **Output vs forecast** | Upper left, the largest block (~25% of screen area). | This is the main "how are we doing" answer. It shows the current MW in the biggest type on the screen, then the signed gap in words ("−3.2 MW, 8% under forecast"). Below that is a today-only line, with actual as a solid line and forecast as a dashed one. |
| **Wind speed and direction** | An inset inside the output block, about a quarter of its width. | Wind explains output, so it sits beside it. It shows a number plus a direction arrow with the compass word ("9.4 m/s, WSW"). It doesn't need its own panel. |
| **Active alarms** | The right column, ~68% of height and the biggest single block (~27% of area). | This is what the operators act on. It's sorted by severity, then by age. Each row has a severity icon and word, the turbine ID, what happened, and how long ago it started. It shows about 8 rows and then "+N more". An empty list says "No active alarms", not a blank panel. |
| **Turbine status grid** | Left column below the output block, ~28% of height (~17% of area). Use 2 rows × 11 columns, or the physical layout of the farm if it's recognisable. | Positions stay fixed so operators learn where each turbine is. Healthy tiles are muted, showing the ID and MW in grey. A faulted or stopped tile gets the alert colour, an icon and a one-word state ("FAULT"). Sort by position, never by status. The alarm list does the ranking. |
| **7-day output** | Bottom left, ~15% of height. | This is context, not monitoring. It's a single line or bar chart with a headline that states its point, like "Output 12% below last week". It's the first thing to cut if space gets tight. |
| **Maintenance schedule** | Bottom right, same height. | Show only today and tomorrow on the wall, as a short list of turbine, task and time window. Put the full week on a workstation. Highlight any job that affects a turbine currently in the grid, so a "stopped for maintenance" tile isn't mistaken for a fault. |

## What's readable from where

Rough rule: letter height of about 1/200 of the viewing distance.

| Reader | Text size | What it covers |
|---|---|---|
| **6 m, from the back** | Cap height ≥ ~30 mm (≥ ~4% of screen height). | Output MW number, the curtailment and weather banners, alarm count and the state words of any alarm tile. **The farm-level answer must work from here:** the number, the gap, and whether any alert colour is lit. |
| **3 m, mid-room** | ~15 mm (~2%). | Alarm rows (turbine ID, description, age), turbine tile IDs and state words, the clock, the gap wording under the output number, wind readout. |
| **Walk-up, under 1 m** | ≥ ~6 mm, still legible. | Per-turbine MW in the grid, chart axes and the forecast line, maintenance details, "+N more". Nothing essential lives only at this size. |

## Rules that keep it readable

- **Healthy is calm.** Grey and muted, with no permanent green. Use one alert colour, always paired with an icon and a word. Use two levels at most: "needs a look" and "act now".
- **Stale data is its own state.** The clock is large enough to notice at 6 m. If the feed is older than its refresh interval, it turns into "DATA STALE" with the time since the last update. A dead feed must never look like a quiet farm.
- **No rotating pages and no animation on healthy items.** An alarm must never be hidden behind a tab.
- **Mark new alarms** for the first few minutes, so someone returning from a break sees what changed.
- **Use a dark background** with low-contrast structure. Let data and alerts carry the contrast.

## Not decided here

I haven't set any thresholds. When "needs a look" or "act now" applies is yours to set, using your own alarm limits and how large a forecast gap should count. If more than a handful of tiles or alarms are lit on a normal day, loosen the thresholds before you change the layout.
