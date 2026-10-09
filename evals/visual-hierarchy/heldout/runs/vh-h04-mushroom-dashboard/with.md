**What's wrong:** the page has no ranking. It's "flat" because every card, every number and every state looks the same. The room-5 miss follows directly from that. A bad room differs from a good one only by a slightly darker orange number and an 11px grey "alert". In a grid of 32 identical bold numbers, that doesn't register. The page's real job is "tell me which room needs me right now", and it currently shows all eight rooms as equally important.

**Change this first: make out-of-range state the loudest thing on the page, and make healthy rooms quieter.**

1. **Give an alerting card a different structure, not just a different number color.**
   - Add a thick (4–6px) colored left edge or top bar, plus a tinted card background.
   - Put a status line at the top of the card that names the problem, e.g. "Humidity 61% – low (target 85–95%)". Use real text at the card-title size or larger, not 11px grey.
   - Pair the color with the text and a icon-free shape cue so it survives grayscale and works for colorblind viewers.
   - Use one alert treatment, applied the same way everywhere.

2. **Quiet the healthy rooms so the alert has something to stand out against.**
   - Drop the shadow and keep a faint border.
   - Make in-range numbers regular or medium weight in a dark neutral, not 28px bold.
   - Emphasis should cover roughly a tenth of what's visible, so with 8 rooms, one or two loud cards is the right amount.

3. **Rank the numbers inside each card.** Four equal 28px numbers mean none of them matters.
   - Only the out-of-range metric gets the big, bold, colored treatment. The others drop to about 18–20px in a regular weight.
   - In a healthy room, keep all four at the smaller size.
   - "Days to harvest" is planning information, not a condition to watch. Make it the quietest of the four.
   - Show the target range in small grey text next to each reading, so "61%" is read against "85–95%" without any mental lookup.

4. **Sort or pin alerting rooms to the top-left.** Position is the strongest cue. If you'd rather keep a fixed room order, add a one-line banner above the grid: "1 room needs attention: Room 5 – humidity low for 6h".

5. **Add duration to the alert.** Six hours out of range is a very different situation from six minutes. Escalate the treatment as time passes (e.g. normal alert → stronger red after 30 min). This catches exactly the failure you had, where the reading sat there unnoticed.

**Notes:**
- A color-only change would repeat the original problem. The shape, position and text cues are what make it noticeable.
- Page visuals alone won't wake anyone at 2am. If a 6-hour miss is costly, a push, SMS or email alert on out-of-range readings is worth adding alongside the redesign.

I can mock this up as HTML/CSS if you share the page's code or path.
