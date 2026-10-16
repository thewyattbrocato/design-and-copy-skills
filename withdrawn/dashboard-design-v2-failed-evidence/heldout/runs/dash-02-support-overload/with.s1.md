# Support dashboard review

I'm assuming this is a Monday review for your VP, so the question it has to answer is: is support healthy, what's breaching, and where should we look next? The page currently answers none of those quickly.

## What's wrong, in order of damage to trust

**1. The "Tickets this month" tile is wrong, and it's probably why nobody trusts the page.**
- It compares 11 days of this month with a full last month. Per day, that's about 284 vs about 298 (8,940 ÷ 30, assuming last month had 30 days). That's roughly **-5%, not -65%**.
- Even -5% isn't clean. It ignores which weekdays fell in each window.
- Anyone who notices this will stop believing every other tile.
- **Fix:** compare the same window (days 1–11 vs days 1–11 last month), or compare daily rate to daily rate. Label it "Month to date (11 days)". If a full-month comparison matters, show a projection and mark it as one.
- That tile is also a 7th tile on a row you described as 6. Cut it. Volume belongs in the trend chart.

**2. The red/green lights fire on "worse than yesterday".**
- Daily noise makes them flip constantly, so red stops meaning anything.
- Yesterday is the wrong baseline. Monday vs Sunday and a normal Tuesday spike both read as "worse".
- "Tickets created today" is a partial day compared with a full one, so it's red every morning.
- There's no target behind any light, so red doesn't tell anyone whether to act.
- Red and green alone also fail for color-blind readers. No word or icon backs them up.
- **Fix:** light a tile only when it breaches a target or sits outside its normal range. Use same-weekday comparisons, and exclude partial periods.
- Show the gap in words: "SLA 91.2%, target [set by team], 3.1 pts under, since Tue."
- If a quarter of the tiles are red most of the time, the thresholds are wrong, not the team. Healthy tiles should be quiet, with no permanent green.
- I won't invent targets. Leave "target: set by team" slots for you and the VP to fill.

**3. The six tiles are all the same size, and some are redundant or misleading.**
- Open tickets and backlog age overlap.
- Average first response hides the tail. Use median plus % over the first-response target, or p90.
- CSAT on small response counts swings wildly. Show n.
- "Tickets created today" is volume, not performance, so "worse" has no clear meaning for it.
- **Fix:** pick the 4 or so measures that drive a decision: SLA %, first response (p90 or % over target), backlog age (oldest or % older than X), and CSAT with n. Keep open tickets only if someone staffs against it.
- Each tile gets one comparison, as a computed gap: "−2.1 pts vs target".

**4. The 3D pie of CSAT by agent should go.**
- CSAT rates don't add up to a whole, so a pie is meaningless for them.
- 3D distorts slice size.
- With 46 slices nobody can read it.
- Ranking individuals by CSAT on small samples is also unfair, and it hurts trust on the team.
- **Fix:** delete it. If agent CSAT matters, it goes in a drill-down for team leads, with n and a sample-size warning.

**5. The three donuts show composition and answer no question.**
- Angles are hard to compare, and there's no comparison to anything. Does it matter that Email is 38%?
- **Fix:** replace them with one sorted bar chart (from zero) per cut, only if someone acts on it. A better version asks "where is the pain?" and shows breach rate or backlog by channel, priority and product area, not share of volume.
- Better still, make them drill-downs from whichever headline tile is breaching.

**6. The trend line has a truncated axis, and the numbers may not reconcile.**
- Starting the y-axis at 4,000 makes ordinary variation look dramatic.
- At roughly 284 tickets/day, a per-day chart would never reach 4,000. Either the chart is monthly and mislabeled, or the axis cuts off the data. **Check this first.** It's another place where the page contradicts itself.
- **Fix:** use weekly totals (12 months of daily points is mostly weekday and weekend noise), start the axis at zero or switch to a bar chart, and mark the current partial period or leave it off.
- Title it with its finding, for example "Weekly volume is flat since June." I don't have the data, so I can't write the real headline.

**7. The 46-agent × 11-column table is a wall of numbers.**
- Nobody can scan it, and it doubles as an individual leaderboard.
- **Fix:** move it off the main page, behind one click. Default to showing only agents outside range, sorted by severity, with 3 or 4 columns. Keep the full table for team leads.

**8. There's no definitions line, no "last updated", and no data states.**
- Nobody can tell what "open" or "backlog age" mean, or whether the data is stale.
- **Fix:** add a one-line footer with definitions and a timestamp. A stale or failed tile should show as "no data", never as zero or green.

## What I'd ship before Monday

1. **Top strip, "needs attention":** only breaching items, ranked, each with the gap, when it started, and where to click. If nothing is breaching, one line: "All 4 measures within target".
2. **Four headline cards** with the same anatomy: label and period, value, signed gap vs target in words, small trend line.
3. **One weekly volume chart** with an honest axis.
4. **Breakdowns by channel, priority and product area as bars,** shown only when relevant to a breach or reached by drill-down.
5. **Agent detail** moved off the page.
6. **Footer** with definitions and last-updated.

If you only have time for three fixes, do these: **(a)** fix or remove the month tile, **(b)** replace "worse than yesterday" with target-based status, and **(c)** delete the 3D pie. Those three account for most of the distrust.

## Open questions for you

- Who set the targets, if any exist?
- Is the trend chart monthly or daily?
