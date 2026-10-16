**What's wrong:** the page has no order, so the one thing that matters looks like everything else. Every card has the same surface, the same type sizes, and the same weight. Days-to-harvest gets the same visual weight as humidity, which is an alarm. The out-of-range signal is a slight color shift on one number plus an 11px grey word, so the alert is the quietest thing on the card. In a grid of eight identical cards, Room 5 at 61% looks like Room 4 at 90%. The page also doesn't show how long a reading has been out of range, so six hours and six minutes look the same.

Your co-founder is right. It's flat because there's one size, one weight, and one surface, and nothing says "look here."

**What to change first:** the status layer, not the typography.

1. **Add a "needs attention" strip at the top.** Show a count and list each out-of-range reading with room, metric, value, and duration, for example "Room 5 · Humidity 61% · 6 h". If nothing is out of range, show a quiet "All rooms in range." Keep this above the grid. It's the first thing a person sees.
2. **Make out-of-range cards unmistakable with more than color.** Use a status border or band, a text label such as "HUMIDITY LOW · 6 h" in the card, and a shape or icon next to the number. Color stays as a secondary cue for people who can't see it well. Drop the 11px grey word.
3. **Quiet the normal cards.** Use default ink for the values, and drop the repeated shadow and borders where you can. Let the alerting cards be the only loud things on the page.
4. **Sort alerting rooms first**, or group them, so the order matches priority rather than room number.
5. **Demote days-to-harvest** to a smaller or grey secondary value. It's informational, so it shouldn't compete with the alarm metrics.

**Two checks outside the design:**

- **Confirm the threshold.** If Room 5's humidity target is nowhere near 61%, the alert logic may be wrong, and no visual change fixes that.
- **Don't rely on the page as the alarm.** A monitoring page only helps when someone is looking at it. Sustained out-of-range readings (say, more than 30 minutes) should push a notification to a phone. That's the fix that would have caught Room 5 last week.
