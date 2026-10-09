**My view: the hero stat and the big cards are a reasonable instinct, but as you've described them they may add clutter rather than remove it.** A hero number tells dispatchers something they can already count. Big cards for "important" trucks shrink everything else, and the board still shows 60 items. Overwhelm usually comes from every truck looking equally loud, not from the count alone. The fix is hierarchy: make the layout show what needs action and let routine trucks recede.

**Proposed layout (1920×1080 assumed)**

```
┌──────────────────────────────────────────────────────────────────────┐
│ ON SITE 52 │ Docks 14/18 used │ ▲ 4 over 90 min │ Ready to leave 7  │  ← slim summary strip, ~64px
├──────────────────────┬──────────────────────────┬────────────────────┤
│ ARRIVING / WAITING   │ DOCKS (door 1–18)        │ READY TO LEAVE     │
│ (queue lane)         │ grid of door tiles       │ (exit lane)        │
│                      │  D01 ■ loading  T-4471   │                    │
│ ▲ T-4422 Acme  142m  │  D02 ■ unloading T-4390  │ T-4311 Velo  12m   │
│   T-4450 Brix   38m  │  D03 ─ empty             │ T-4298 Acme  4m    │
│   ...                │  ...                     │ ...                │
└──────────────────────┴──────────────────────────┴────────────────────┘
```

1. **Summary strip (slim, not hero).** Counts per status plus one alert count, such as "4 over 90 min." Keep it to one line so it doesn't compete with the trucks.
2. **Three lanes by workflow stage, not one list.** Queue on the left, docks in the middle, exit on the right. Dispatchers scan by where a truck is in its process. This also fits the numbers: 60 trucks at about 40px per row is roughly 2,400px, which won't fit in one column. Split across three lanes it's about 800px. No scrolling needed.
3. **Exceptions get rows that stand out, not bigger cards.** Use a small "needs action" band at the top of each lane for trucks past threshold, with larger type and an alert color. Everything else stays in dense rows. This keeps the "bigger for important" idea but ties importance to a rule (time over SLA, a dock conflict, a missing door) instead of a fixed priority.
4. **Minutes on site as a bar, not just a number.** A small fill bar with green, amber, and red thresholds lets dispatchers judge urgency at a glance across the whole screen.
5. **Notes as a flag plus truncated text.** Show a single-line truncation in a fixed-width column, with full text on hover or an inline expand. Don't make it a modal, because that's a click they'd have to make 60 times a shift.
6. **Encode status with position and shape, not only color.** Lane placement plus an icon or label keeps it readable for color-blind users and in poor light.
7. **Stable ordering.** Sort by minutes on site within each lane, but avoid reshuffling every few seconds. Rows that jump constantly are a big source of the "overwhelming" feeling. Update in place and highlight only what changed.

**What I'd test first:** put the lane layout in front of two or three dispatchers with a realistic 55-truck snapshot and ask them to find the three trucks that need action within five seconds. If they can, the hierarchy is working, whatever the size of the hero stat.

To refine this, I need a few things:
- What's the screen size, and is there one monitor or several?
- Do you have an SLA threshold for minutes on site, or should I propose one?
- Is dock assignment always known when a truck arrives, or do some trucks sit in the queue without a door?
- When dispatchers say "overwhelming," do they mean the number of items, the amount of text, or the number of colors?
