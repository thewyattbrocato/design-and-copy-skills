# Layout for the 55" control-room wall

I've assumed three operators on shift act on this screen, mostly from their desks. The decision it supports is "do I need to do something now?". It follows the wall-display rules: nothing rotates, healthy items stay quiet, and the last-updated time is always visible.

I planned on a 1920×1080 canvas. At 6 m, body text needs to be about 36 px or larger. The hero number can be far larger.

```
┌──────────────────────────────────────────────────────────────────┐
│ A. EXCEPTIONS STRIP: Curtailment │ Weather warnings │ Updated   │  ~8%
├───────────────────────┬──────────────────────────────────────────┤
│ B. FARM OUTPUT        │ C. ACTIVE ALARMS                         │
│  big MW               │  ranked list, newest/most severe first   │  ~48%
│  gap vs forecast      │                                          │
│  today: actual vs fc  │                                          │
├───────────────────────┴───────────────────────┬──────────────────┤
│ D. TURBINE GRID, 2 rows × 11                  │ E. WIND          │  ~25%
├───────────────────────────┬───────────────────┴──────────────────┤
│ F. 7-DAY OUTPUT           │ G. MAINTENANCE THIS WEEK             │  ~19%
└───────────────────────────┴──────────────────────────────────────┘
```

## What goes where

**A. Exceptions strip (top, full width, thin).** This holds curtailment and weather warnings, the two "outside world is telling us something" items.
- **Curtailment:** when quiet, it reads "No curtailment" in muted grey. When active, it turns the alert color with an icon and states the limit and start time, for example "CURTAILED to __ MW by grid operator, since 14:05".
- **Weather warnings:** these work the same way. They stay quiet when there are none. When active, they give the type and the time window.
- **Last updated:** this sits at the far right, large enough that a dead feed is noticeable.
- Each slot has a fixed position, so an operator's eye learns where to look. When something fires, the strip is the only element that changes color.

**B. Farm output vs forecast (top-left, ~20% of the screen).** This is the hero.
- The MW figure is the largest thing on the wall, about 140 px, readable from 6 m.
- Directly under it is the computed gap in words, such as "3.2 MW below forecast", at about 48 px. The forecast value is secondary.
- Below that is a small line chart of today's actual against forecast, which shows whether the gap is growing.
- The 7-day chart does not belong here. It is context, not something to act on.

**C. Active alarms (top-right, ~30%, the biggest block).** It's biggest because alarms are what operators act on.
- Each row shows turbine ID, what happened, and how long ago, for example "T14 Gearbox oil temp, 12 min".
- Order is severity first, then newest first. There are at most two levels: "needs a look" and "act now".
- It shows about 6 rows at 36–40 px, then "+N more".
- With no alarms it reads "No active alarms" in calm grey and keeps its footprint, so nothing shifts.

**D. Turbine grid (middle-left, ~16%).** There are 22 tiles in 2 rows of 11, in a fixed order that matches the site numbering.
- Healthy tiles are dim and show only the ID.
- Faulted, stopped, or curtailed tiles get the alert color plus an icon and a short word, so they're never color-only.
- Maintenance turbines get a neutral, distinct treatment, for example an outline with a wrench icon. They are expected, so they shouldn't look like faults.
- Up close, each tile can show its own MW in smaller type.
- A summary line above the grid reads "20 of 22 generating".

**E. Wind (middle-right, ~8%).**
- It has a direction arrow, speed in a large number, and compass text such as "WSW".
- This is the "why" behind the output gap. It's glanceable but rarely acted on alone.

**F. 7-day output (bottom-left, ~8%).** This is a line chart of actual against forecast.
- It gets a plain-language title with the takeaway, and its axis labels are only readable up close.
- It is the smallest chart because it is background for a shift, not for the next minute.

**G. Maintenance this week (bottom-right, ~10%).**
- Today's jobs come first, then the rest of the week, each with turbine ID, job, and time window.
- It's a short table at about 24–28 px, mainly for walking up to the screen.
- Anything affecting a turbine today also shows on that turbine's tile in D.

## Across the room versus up close

| Tier | Elements | Approx. size (1080p) |
|---|---|---|
| **Readable at 6 m** | MW figure, gap vs forecast, curtailment and weather banners, alarm rows, tile states in D, "20 of 22" summary | 36 px and up; MW figure ~140 px |
| **Readable at 3 m** | Wind speed and direction, turbine IDs, last-updated time | 28–36 px |
| **Walk-up only** | 7-day chart axes, maintenance table, per-turbine MW, today's forecast line detail | 20–26 px |

Nothing essential is in the walk-up tier. If you can't act on the screen from across the room, it should be rearranged.

## Rules for the whole screen
- **One alert color** with an icon and a word, and no permanent green. Healthy things stay grey or white.
- **High contrast only for data and alerts.** Panel borders and labels stay low-contrast.
- **No auto-rotating tabs or animation** on healthy items.
- **Stale data is its own state.** If a feed stops, that tile shows "no data since HH:MM" and never a zero or a green tick.
- **Tell operators what changed.** A new alarm can briefly pulse its row or show a "NEW" tag until acknowledged.

## What I left open
- **Thresholds and severity levels:** I haven't invented any. You'll need to set which alarms count as "needs a look" and which as "act now".
- **Forecast source and refresh interval:** I'd flag the forecast as stale if it's older than its normal update cycle.
