# 55" control-room wall layout

**Sizing rule.** A 55" 16:9 screen is about 122 × 68 cm. For text to be comfortable at 6 m, you need roughly 30 mm cap height (20 mm is the bare minimum). On a 1080p-equivalent canvas, that is about 60 px font for "readable from the back" and about 40 px for "readable from the front of the room". Anything under about 24 px is walk-up only. A 4K panel doubles those pixel numbers but not the physical size.

## Layout (percent of screen width × height)

```
┌──────────────────────────────────────────────────────────┐
│ CURTAILMENT (60w)                  │ WEATHER WARNINGS(40w)│  ~9h
├───────────────────────────────┬──────────────────────────┤
│ OUTPUT vs FORECAST            │ ACTIVE ALARMS            │
│ 60w × 30h                     │ 40w × 55h                │
├───────────────────────────────┤                          │
│ TURBINE GRID (22)             │                          │
│ 60w × 38h                     ├──────────────────────────┤
│                               │ WIND speed + direction   │
├───────────────────────────────┤ 40w × 17h                │
│ 7-DAY OUTPUT                  ├──────────────────────────┤
│ 60w × 23h                     │ MAINTENANCE THIS WEEK    │
│                               │ 40w × 19h                │
└───────────────────────────────┴──────────────────────────┘
```

Approximate share of screen area: turbine grid 23%, alarms 22%, output 18%, 7-day chart 14%, banner 9%, wind 7%, maintenance 7%.

## What goes where and why

**Top banner: curtailment (left) and weather warnings (right).**
- These are states, not data, so they should be quiet when normal and loud when not.
- Normal: a slim, muted strip reading "No curtailment" and "No warnings".
- Active: the strip grows, changes colour, and shows the key facts in 60 px type, for example "CURTAILED to 12 MW until 14:00". Warnings show type and time window.
- Across the room: only the state and the headline number or warning type.
- Up close: the issuing party, the reason, and the full text.

**Top left: output vs forecast (the hero).**
- The current MW is the largest type on the screen (about 150 px+). Next to it, in smaller type, are the forecast MW and the delta (for example "−3.2 MW vs forecast").
- Behind or under the number, draw a thin line of today's actual vs forecast. It is small and meant for up-close reading only.
- Across the room: the MW number and whether the delta is good or bad (colour plus a sign).
- Up close: the line chart.

**Left middle: turbine grid.**
- Use 2 rows of 11, or follow the physical layout if the farm has a clear one. Keep the positions fixed so operators learn where each turbine sits.
- Each tile shows the turbine number in large type (about 50 px) and a state colour. Use a second cue as well as colour, such as an icon or a border style, because colour-blind operators exist.
- Put the per-turbine MW in small type inside the tile. That is walk-up only.
- Across the room: the count of non-green tiles and which ones. The pattern is what matters here.

**Right: active alarms (tallest panel).**
- The top 4–5 alarms by severity appear in large type (about 40 px), each with a severity colour, the turbine ID, and a short description.
- Below that, a "+N more" count and a smaller list for close reading.
- Don't auto-scroll on a wall display, because people miss things as the list moves. Sort by severity, then by age.
- Across the room: severity colour, turbine ID, and the alarm count.
- Up close: timestamps, acknowledgement state, and the long descriptions.

**Right middle: wind speed and direction.**
- Speed in large type (about 80 px), with a compass arrow beside it and the direction in degrees and as a cardinal point.
- It is context for the output number, so it doesn't need to be bigger.

**Bottom left: 7-day output chart.**
- This is trend context and nothing needs doing in the moment, so it gets a modest, quiet panel.
- Label the axes and "today" in 24 px type. A reader at 6 m can see the shape but not the numbers.
- This is mainly for people who walk up.

**Bottom right: this week's maintenance.**
- Show a compact list of today's and tomorrow's jobs (turbine, task, time window), with the rest of the week in smaller type.
- It is almost entirely walk-up reading. The one exception is a turbine that is currently in maintenance: that should also show on its grid tile, so the room can see why it's offline.

## Principles that apply across the layout

- **Colour budget.** Use a dark background, with grey and white for normal values. Reserve amber and red for things that need attention. If everything is coloured, nothing stands out.
- **Alarms and the grid share a story.** A turbine in alarm should be visible in both places, so make the colours match.
- **Curtailment explains the output delta.** If you are curtailed, "below forecast" is expected. Consider greying out the delta, or labelling it "curtailed", so operators don't chase a non-problem.
- **Left-to-right reading order.** Status banner, then output, then grid, then alarms matches how people scan.
- **Test from the real seat.** Put a mockup on the screen and check it from 6 m. The first thing to shrink is whatever you can't read from there.

If you tell me whether the turbines sit in rows or strings, or whether alarms are mostly one or two types, I can refine the grid shape and how many alarms to show large.
