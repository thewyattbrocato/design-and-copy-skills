I'm assuming the operators glance up between tasks and need to know three things: is anything wrong, are we on forecast, and is the grid telling us to cut. The layout puts alarms and exceptions first, then output, then context.

```
┌──────────────────────────────┬─────────────────┬─────────────────┐
│ 1 OUTPUT vs FORECAST         │ 2 CURTAILMENT   │ 3 WEATHER       │  22%
│   18.4 MW   −2.6 vs forecast │                 │   WARNINGS      │
├──────────────────────────────┴─────────────────┼─────────────────┤
│ 4 ACTIVE ALARMS                                │ 7 WIND          │
│                                                │                 │
│                                                ├─────────────────┤
│                                                │ 8 MAINTENANCE   │
├────────────────────────────────────────────────┤   THIS WEEK     │
│ 5 TURBINES (22, 11 × 2, fixed positions)       ├─────────────────┤
│                                                │ 9 7-DAY OUTPUT  │
└────────────────────────────────────────────────┴─────────────────┘
        62% of width                                  38%
```

## Where each piece goes and how big it is

| # | Piece | Position and size | Why there |
|---|---|---|---|
| 1 | Output vs forecast | Top-left, about 45% of width × 22% of height. It has the biggest type on the screen. | It's the first thing anyone looks for, and the eye starts top-left. |
| 2 | Curtailment | Top middle, about 27% × 22% | It explains a gap in #1, so it sits next to it. |
| 3 | Weather warnings | Top right, about 28% × 22% | Same band as #2, because both are "something outside is affecting us". |
| 4 | Alarm list | Left, below the band, about 62% × 46%. It's the largest block. | Alarms are what operators act on. They arrive in bunches during storms, so the space is deliberate. |
| 5 | Turbine grid | Below the alarms, about 62% × 32% | It's the spatial overview of the alarm list. |
| 7 | Wind speed and direction | Right column, about 38% × 22% | Context for #1, not an action item. |
| 8 | Maintenance | Right column, about 38% × 28% | Mostly read up close. |
| 9 | 7-day chart | Right column, about 38% × 28% | Pure context. Only the shape needs to read from far away. |

**1. Output vs forecast**
- Show the number and the gap together, for example "18.4 MW" and "2.6 MW under forecast".
- Add a thin today-only line of actual against forecast underneath for the trend. It's decoration at 6 m, but useful up close.

**2. Curtailment**
- When there's no curtailment, show a muted "No curtailment" in mid-size text.
- When active, it takes the alert colour and states the instruction, for example "Grid limit 12 MW since 14:10".
- If curtailed, show #1's gap as "curtailed" rather than as a shortfall. Otherwise operators will chase a fault that isn't there.

**3. Weather warnings**
- It's muted when there are none.
- When active, it gives the warning type and when it starts or ends, for example "High wind 18:00–23:00".

**4. Alarm list**
- Sort by severity, then by age. Each row has the turbine, what happened, and how long ago it started.
- Put the count at the top ("3 active"). If nothing's active, show a calm "No active alarms".
- Show about 6 rows and then "+N more". Don't scroll or rotate.

**5. Turbine grid**
- Use 22 equal tiles in fixed positions, ideally matching the physical layout or string order. Don't re-sort them, so operators learn where each one is.
- Healthy tiles are muted: the ID and a small MW figure.
- Faulted tiles use the alert colour with an icon and a word.
- Planned maintenance is a separate neutral state, not an alert colour. Otherwise the schedule looks like faults.
- No data from a turbine is its own hatched "no data" state, never zero or green.

**7. Wind**
- A big speed number with a compass arrow for direction.

**8. Maintenance**
- Today and tomorrow in full. The rest of the week collapses to one line per day.

**9. 7-day chart**
- One line for output, with a headline that states the answer (for example "Output down 15% on last week"). Keep the forecast off it unless you want the comparison.

## What's readable from where

Sizes are font heights at 1080p-equivalent. Double them for a 4K panel. They are rules of thumb, so test on the real wall.

| Distance | Size | What lives there |
|---|---|---|
| **Across the room (6 m)** | 48 px and up, with the hero figure at 120 px or more | MW value and gap, the curtailment word, the weather-warning word, the alarm count, turbine IDs and state colours, and the last-updated time |
| **Mid-range (3–4 m)** | 32–36 px | Alarm rows, turbine MW values, wind speed, and warning text |
| **Walk-up (about 1.5 m)** | 22–26 px, as the minimum | Alarm timestamps and detail, maintenance rows, chart axes, and the forecast line |

Nothing goes below 22 px.

## Rules for the whole screen

- **Colour:** use a dark background with muted structure, so data and alerts carry the contrast. Use one reserved alert colour with two levels, "needs a look" and "act now", always paired with an icon and a word. Nothing is permanently green.
- **Motion:** no rotating tabs, no animation, and nothing that moves when it's healthy.
- **Last-updated:** make it large and put it in the top band's corner. It turns to the alert colour if the feed goes stale, so a dead feed doesn't look like a calm farm.

Two things I couldn't tell from your description:
- Does your forecast account for planned outages? If not, the gap in #1 will look worse on maintenance days. In that case, subtract the planned capacity or label it.
- I didn't set any alarm or output thresholds. Set them so red is rare, because if a quarter of the screen is red most days, people will stop looking.
