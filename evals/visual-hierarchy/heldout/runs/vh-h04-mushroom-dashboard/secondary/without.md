**What's wrong:** The page treats an out-of-range room as a slightly different shade of the same card, so it doesn't stand out. Room 5 didn't get missed because the page was ugly. The alert was too weak to catch anyone's eye, and nothing pushed it to anyone.

Specifically:

1. **The alert signal is the weakest thing on the card.** A darker orange on a 28px number, plus an 11px grey "alert" word, is less visible than the bold names and numbers around it. Color is the only real signal, and it's subtle.
2. **Every card has equal weight.** Eight identical cards means a problem room looks like seven healthy ones. Scanning the grid tells you nothing until you read every number. That's the "flat" your co-founder means.
3. **Duration is missing.** A reading of 61% matters much more after six hours than after six minutes, but the page shows only the current value. Nothing says how long a room has been off.
4. **Target ranges aren't shown.** Without "61% (target 85–95)" on the card, the reader has to remember each room's setpoints. (I'm assuming those are your targets; fruiting rooms often run around 85–95% RH.)
5. **It's a passive page.** Someone has to be looking at it. For sustained excursions, a dashboard alone can't do the job.

**What to change first, in order:**

1. **Add push alerts with a time threshold.** Notify when a room has been out of range for more than N minutes (say 15–20), sent to phone or Slack. Use a threshold like this rather than alerting on every reading, so brief spikes don't train everyone to ignore alerts. This addresses the failure that actually cost you Room 5. It's the biggest fix and probably the cheapest.
2. **Make alert state the top-level visual signal.** Give out-of-range cards a strong treatment: a thick colored left border or a filled status badge, plus the words "OUT OF RANGE" in normal-size text. Don't rely on color alone, since some people can't reliably tell orange from grey, and a shade change is easy to miss on a screen.
3. **Show how long and how far.** Put "61% · target 85–95 · 6h 12m" under the metric that's off, instead of a bare number.
4. **Sort problem rooms to the top.** Put out-of-range rooms first, then keep the healthy ones in a fixed order. Stop showing eight equal cards.
5. **Separate "days to harvest" visually.** It's a planning figure, not a live reading. Putting it in the same tier as temperature and humidity makes everything look equally urgent.

If you share the component or template file, I can make the first two changes directly. I'd need your target ranges for each metric and the alert thresholds you want to use.
