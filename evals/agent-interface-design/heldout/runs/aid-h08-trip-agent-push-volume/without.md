**Recommendation:** push only when the user needs to act soon or their trip has changed. Everything else goes to email or the in-app feed. Also give users per-category controls, so "too much" doesn't push them to switch everything off.

**Keep as push (4 of 10)**
- **#5 Cancelled and rebooked:** top priority. Their plans changed.
- **#10 Agent paused (card expired):** the product has stopped protecting them, and only they can fix it. Send an email too.
- **#4 Delay of 20+ minutes:** push it, but only for flights in the next ~24–48 hours, or when the delay threatens a connection. A delay on a flight three weeks out is noise.
- **#3 Gate change:** push only on the day of travel (roughly within 12 hours of departure). Before that, update it silently in the app.

**Check-in (#6):** push by default. It's time-sensitive and useful, and it's often the notification users like most. Make it easy to turn off.

**Move off push**
- **#1 Booking confirmed:** email plus an in-app confirmation. They just did the action, so they don't need a buzz.
- **#2 $12 price drop:** in-app feed only. Push only if the drop is meaningful (for example $50+ or 10%+), or if it hits a target price the user set. If the agent rebooks and saves money automatically, report it afterward in a summary.
- **#9 Seat upgrade:** in-app or email. Push only if the offer is about to expire and the user has opted in.
- **#7 Weekly deals:** email only, and opt-in. This is marketing, and it's probably a big part of why people are muting you.

**Remove as a notification**
- **#8 "Looked and found none":** this is a non-event. Show it as a quiet "last checked 2h ago, no better fare" line on the trip screen. It reassures people without interrupting them.

**Structural changes**
1. **Per-category toggles** with three groups: *Trip-critical* (cancellations, delays, gate changes, agent paused), *Helpful* (check-in, price savings, upgrades), and *Marketing*. Make trip-critical hard to disable by accident, and when someone turns it off, say what they'll miss.
2. **Collapse per trip:** if a delay, a gate change and a rebooking land within minutes, send one push ("Your 3:10 flight is delayed 40 min, gate now B12"), not three.
3. **Quiet hours:** hold non-urgent pushes overnight. Cancellations and delays on same-day flights can bypass this.
4. **Weekly or per-trip digest** for the low-urgency items (price drops, "no better fare," upgrades), so the agent's work stays visible without interrupting.

**How to check it's working:** track the opt-out rate and the share of users with push fully disabled before and after. Also track the open rate per category. If a category's open rate is low, demote it. Roll it out as an A/B test against the current behavior.

I picked the thresholds (24–48 hours, $50 or 10%) from general practice. Tune them against your own open and opt-out data.
