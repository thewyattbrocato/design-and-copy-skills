**What's wrong:** the page has no ranking, and the one thing it exists for, "which room needs me now?", is the quietest thing on it. Your co-founder's "flat" is the same problem.

- **All 8 cards look the same, and all 32 numbers are equally loud.** Four 28px bold numbers per card means 32 things competing. Nothing is primary, so the eye has nowhere to land. Most of them are also fine at any given moment, so they're noise.
- **An alert is a small change.** It's a slightly darker orange on one number plus an 11px grey "alert" label. That is a tint shift and a tiny word, where it should be a different state. Grey 11px text is the lowest-priority style on the page, and you used it for the highest-priority fact. Room 5 at 61% humidity looked like seven other cards.
- **Status relies on color alone.** Orange against black text is a weak cue, and it disappears for anyone colorblind or glancing from across the room.
- **The decoration does no work.** Every card has the same border and shadow, so they only add weight. They separate cards that already have gaps, and they don't carry any information.
- **The room name is the only label, and it's small.** At 14px bold it's the smallest "loud" thing, so it can't act as a heading either.

**What to change first:** make an out-of-range room look structurally different from a healthy one, and quiet the healthy ones.

1. **Healthy cards:** drop the shadow, use a flat light fill or a hairline border, and make the numbers regular weight at about 20px. A healthy room should be calm and easy to skip.
2. **Alert cards:** give them a heavier border (2–3px) or a solid tinted background in your alert color. Add a status line at the top of the card that says what's wrong in plain words, for example "Humidity 61% · low (target 80–90%)". Make the out-of-range number itself larger and bold, and leave the other values quiet. That gives you two cues beyond color: structure and text.
3. **Sort alert rooms first,** or pin them to the top row. Position beats styling. If six hours of 61% should never go unseen again, an alert card shouldn't sit at position 5 in a grid.

Aim for emphasis on about 10% of what's visible. If 1–2 rooms are in alert, the page should be calm with those cards obviously loud. If most rooms are in alert, you have a thresholds problem, not a design one.

**Smaller fixes, later:**
- Fold the labels into the values ("61% RH", "22 °C") so the cards need less small grey text.
- Move "days to harvest" down a level. It's planning information, not an alarm, so it can be smaller and grey.
- Use one alert style everywhere, with a second, quieter "warning" tier only if you need it.

**One thing the design can't fix:** a page nobody is looking at won't catch a six-hour excursion. If Room 5 matters that much, add a push, SMS or Slack alert when a value stays out of range for more than about 15 minutes. The redesign makes problems obvious to whoever's looking, and the notification covers the times nobody is.

I'm assuming your target ranges are already defined per room. If you share the HTML or CSS, I can make these changes directly.
