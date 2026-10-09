**What's wrong:** the page treats every room and every reading the same, so nothing tells you where to look. Three problems compound:

1. **The alert is too quiet to catch at a glance.** A slightly darker orange number and an 11px grey "alert" word are the weakest signals on the card. The eye lands on the largest, boldest, most saturated element, and at this size an out-of-range value looks like any other number. Color shift alone also fails for colorblind users and on a dim screen.
2. **There is no sense of time.** The page shows the current value only. Room 5 at 61% for six hours looks identical to Room 5 at 61% for six seconds. The most important fact about a grow alert is how long it has persisted, and the page doesn't show it.
3. **No hierarchy.** Eight identical cards with identical type sizes make the room layout a flat wall. Your co-founder's "flat" is accurate: nothing is more important than anything else, so nothing draws the eye.

Also, a dashboard only helps if someone is looking at it. Room 5 went unnoticed because nobody was watching the page, not only because the page was hard to read. If there's no push notification for a sustained out-of-range condition, that's the bigger gap.

**What to change first, in order:**

1. **Add a notification for sustained out-of-range conditions** (phone push, SMS, or a loud channel you check). Fire when a reading has been out of range for a set time, such as 15 to 30 minutes, not on a single spike. This is the change that would have caught Room 5 at hour one. It's independent of the design and the cheapest fix with the largest payoff.
2. **Put a status strip at the top of the page** that lists only the rooms with active alerts, with the metric and duration, e.g. "Room 5 · Humidity 61% (target 85–95%) · 6h 12m." If nothing is wrong, show "All rooms in range." This makes the page answer "what's wrong and for how long" before anything else.
3. **Make alert cards unmistakable and make normal cards recede.** An alerted card gets a tinted background or thick left border plus an icon and text label, not a color change on one number. Healthy cards get muted styling, so the eye goes to the alerts. Don't make everything red or you lose the signal.
4. **Add a small trend line per metric** (last 6 to 12 hours). It shows whether humidity is drifting or stuck, which a single number can't.

**Check your thresholds too.** Fruiting mushrooms typically need very high humidity, often 85 to 95%, so 61% is far outside a healthy range and probably should have been loud. Also, the target range usually depends on growth stage (colonization vs. fruiting), so a single global range may be wrong for some rooms. If Room 5's range is set for colonization but it's fruiting, the alert logic is wrong, not just the display.

If you tell me what the page is built with and where the sensor data comes from, I can make the status strip and alert styling changes directly.
