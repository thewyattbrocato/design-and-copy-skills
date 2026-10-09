**Short answer:** Keep the stat, but make it a slim strip, not a hero. Replace the "big cards for important trucks" tier with a fixed grid where every truck is the same size and exceptions get flagged in place. Otherwise the most important trucks will be easy to see, and the rest will still be a wall.

**Why I'd change the hero plan:**
- A giant number answers "how many trucks," which dispatchers already know. It spends the most valuable space on the least actionable fact.
- Big cards for "important" trucks make a second tier that hides the others by comparison. Importance also changes through the shift, so a truck can move from "small" to "urgent" with no visual change.
- The overwhelm probably comes from 60 identical rows of text with no grouping. Equal visual weight plus no structure is what makes a screen feel like noise.

**Proposed layout (1920×1080-ish, no scrolling):**

```
┌──────────────────────────────────────────────────────────────────────┐
│ ON SITE 52   Arriving 6 · Waiting 9 · Loading 14 · Unloading 11 ·    │  stat strip
│              Ready 12 · Over dwell target 7 ▲                        │  (~56px)
├──────────────┬──────────────┬──────────────┬──────────────┬──────────┤
│ ARRIVING  6  │ WAITING   9  │ LOADING  14  │ UNLOADING 11 │ READY 12 │  lanes =
│ ┌──────────┐ │ ┌──────────┐ │ ┌──────────┐ │ ┌──────────┐ │ ┌──────┐ │  status,
│ │TRK-4471  │ │ │TRK-4402  │ │ │TRK-4390  │ │ │TRK-4377  │ │ │…     │ │  fixed order
│ │Carrier   │ │ │…         │ │ │Door 12   │ │ │…         │ │ │      │ │
│ │Door —    │ │ │          │ │ │42 min    │ │ │          │ │ │      │ │
│ └──────────┘ │ └──────────┘ │ └──────────┘ │ └──────────┘ │ └──────┘ │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────┘
```

- **Lanes by status, in process order** (arriving → waiting → loading → unloading → ready). Position tells you the state before you read anything, and the lanes match the workflow.
- **Every card is the same size, in a fixed slot.** Dispatchers learn where trucks sit, so they can find TRK-4471 without reading every card.
- **Exceptions escalate in place.** Compute flags from the data: over dwell target, arriving with no door assigned, ready to leave but still holding a door, notes marked urgent. Show the flag as a border, icon, and label on that card. This is the "priority" signal without a separate big tier.
- **Dock door is the spatial key.** Each card leads with door number, since that's how dispatchers think about the yard. Consider a door-by-door strip as an alternative to lanes if they think in doors more than states.
- **Minutes on site** as a number plus a thin bar against the dwell target. Trucks past target show the warning color and icon, never color alone.
- **Notes** show one truncated line on the card. The full note appears on hover or click. That doesn't hide the truck, only the overflow text.

**Color:** Reserve status colors for exceptions (over dwell, blocked, no door). Use neutral ink for normal state, and let lane headers carry the state name. If every card is colored, nothing stands out.

**Before you commit:** Load a screen with 60 trucks, including several overdue ones, and have a dispatcher find a specific truck and spot the three most urgent ones in under five seconds. Test on the actual monitor they use, since card text legibility at a distance is the usual failure.

I haven't rendered or built anything yet. If you want, I can build a static HTML mockup with seeded data for 60 trucks so you can test this with the dispatchers.
