**What's wrong:** the page has no hierarchy, so nothing is loud when something is wrong. Every card, number, and label has the same weight. The only danger signal is a slightly darker orange on a 28px number, plus an 11px grey "alert" word that is the quietest thing on the card. Orange-vs-darker-orange is hard to see at a glance, and it fails for colorblind viewers. A room can be off-target and look almost identical to a healthy one.

The Room 5 incident has a second cause that styling won't fix. A dashboard only helps if someone is looking at it, and nobody was. Your alerts also probably check the current value against a threshold, not how long it has been out of range. A 61% reading that lasts six hours is a different problem from a brief dip, but a point-in-time check treats them the same, or doesn't flag 61% at all if the threshold is loose. The "feels flat" comment is the same problem seen from the design side: the page can't say what matters right now.

**What to change first, in order:**

1. **Fix the alerting, not the look.** For each metric, set a target band per room and growth stage (fruiting humidity and pinning humidity usually differ a lot, so one global range is likely wrong). Alert only when a reading has been outside its band for a set duration, such as 15–30 minutes, so brief spikes don't page you. Send the alert to something that interrupts people, like SMS, a phone push, or a Slack channel with mentions. Not having that is the most likely reason Room 5 went unnoticed.

2. **Make status the first thing on the page.** Sort rooms so any with active alerts appear first, and give each card a status that doesn't rely on color alone: a left-edge bar or badge plus text such as "RH 61% · target 85–95% · out 6h." Showing the target next to each number lets someone read a value without memorizing ranges. Keep the four metrics, but don't give them equal visual weight. Temperature and humidity matter for safety, and days-to-harvest is planning information, so it can be smaller or secondary.

3. **Add a small trend line per metric.** A 24-hour sparkline would have shown Room 5's flat line at 61% immediately. It also shows whether a problem is getting worse or recovering.

Leave the card styling alone until these are done. Borders and shadows are not what's causing the problem.

If you share the code for the page and the alert rules, I can make the alert-duration change and the status-first layout directly. Also tell me your target ranges for each stage, because I'd be guessing at them.
