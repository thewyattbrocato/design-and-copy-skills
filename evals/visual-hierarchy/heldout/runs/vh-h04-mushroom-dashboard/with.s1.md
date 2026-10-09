**What's wrong:** the page has no ranking, so "feels flat" is the right diagnosis. Every card, every number and every state is treated as equally important. The page has one job, which is to show which room needs a person right now. It doesn't do that job. Room 5 sat at 61% humidity for six hours because a problem looked almost the same as a healthy room.

Here are the findings in order of effect:

1. **The alert state is nearly invisible.**
   - **What you see:** a slightly darker orange on one of four numbers, plus an 11px grey "alert" label.
   - **What it costs:** the signal is weak on both counts. Orange vs. dark-orange is a tiny value step, and the cue is color only. Grey 11px text is the quietest thing on the card, so the most important word is the least readable. In grayscale or at a glance across a room, nothing changes.
   - **Fix:** make the card itself change when it's out of range. Use a solid status-colored border or left bar and a tinted background. Add a second cue that isn't color, such as a "Humidity low" line at the top of the card. Move the number that's out of range to the top of the card, bold and in the alert color, with the in-range numbers quieter.

2. **All four metrics are the same 28px bold.**
   - **What it costs:** four equal numbers per card, times eight cards, gives 32 loud things. Nothing is primary, and "days to harvest" (planning information) competes with CO2 (a live safety signal).
   - **Fix:** in a healthy card, drop the numbers to a calmer weight and size so the card reads as "fine". Keep days to harvest as secondary or meta. Give the number that's out of range the biggest, boldest treatment on the page. The failing value should be the only loud thing, which is about a tenth of what's visible.

3. **Normal and alert cards share the same chrome.**
   - **What you see:** identical white background, border and shadow on every card.
   - **What it costs:** the shadow and border do no work, since they say nothing about state. They make healthy rooms look as important as failing ones.
   - **Fix:** quiet the healthy cards by removing the shadow and keeping a faint border or none. That makes the alert card stand out by contrast, without needing anything extra on it.

4. **Order is fixed by room number.**
   - **What it costs:** a room in trouble can sit in the bottom-right corner and look like any other.
   - **Fix:** sort alerting rooms to the top-left, or add a one-line summary strip above the grid ("1 room needs attention: Room 5, humidity 61%, low for 6h"). Showing how long it's been out of range matters. A brief dip and a six-hour drift are different problems.

**Change first:** #1 and #3 together. Give an out-of-range card a distinct treatment (tinted background, strong border, a text label naming the metric and how long it's been off), and strip the shadow and extra weight from healthy cards. That alone would have made Room 5 obvious. Do the sorting and summary strip next, then rebalance the type sizes.

Two notes:
- I'm assuming you have target ranges per metric. If there's also a "warning" band before "out of range", add a second, milder state, not a third color on every card.
- If the page will be on a wall display or checked from across the room, the alert signal should be readable at that distance. A screen-wide status color or banner is worth considering.
