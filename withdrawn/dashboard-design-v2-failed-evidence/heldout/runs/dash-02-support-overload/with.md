**Short version:** the dashboard has too many items, and it also tells people false things. The false things are why nobody trusts it, so fix those first.

## What's wrong, ranked

**1. The "Tickets this month" tile compares 11 days to a full month.**
- Down 65% is an artifact. At 3,120 over 11 days you're running about 284 tickets a day. September's 8,940 over 30 days is about 298 a day. That's roughly 5% lower, not 65%.
- Anyone who spots this will write off the whole page, and that is probably part of why trust is gone.
- **Fix:** compare like with like. Use "Oct 1–11: 3,120 vs Sep 1–11: [n]", or a daily rate vs last month's daily rate. Say "partial month" on the tile. Show the gap in words, such as "5% lower per day".

**2. The numbers may not reconcile with each other.**
- The line chart is "tickets per day" with the axis starting at 4,000, but the tile implies about 300 tickets a day. Both can't be right.
- Either the chart isn't per day, or the tile or its source is wrong.
- **Fix:** before Monday, check both against the source system and make sure they use the same definition of "ticket created". Write each metric's definition in a small info note.

**3. The red/green lights fire on "worse than yesterday".**
- Day-to-day noise and weekday patterns (Monday volume vs Sunday) mean lights flip constantly. "Created today" is also a partial day compared with a full one.
- Direction is ambiguous. Is more tickets "worse"?
- If lights are red half the time, people learn to ignore them.
- **Fix:** compare each tile to a target, or to the same weekday over the last 4–8 weeks. Go red only when a value is outside its normal range. Use one alert color, with an icon and words: "SLA 91%, target [set by team], 4 pts under since Tue". Healthy tiles stay neutral. I won't invent targets. Leave "target: set by team" where they're missing.

**4. Nothing is ranked, so nothing stands out.**
- The page has 6 tiles, 3 donuts, a pie, a line chart and a 46×11 table, all about the same size and weight.
- The viewer has to work out what matters.

**5. The 3D pie of CSAT by agent is the worst chart on the page.**
- 46 slices can't be read, and 3D distorts the angles.
- Per-agent CSAT is usually based on a handful of responses each. Ranking people on it is statistically shaky, and it will cause friction.
- **Fix:** remove it. If you need agent-level CSAT, put it in the table with the response count (n) beside it.

**6. Three donuts of category splits.**
- Donuts are hard to compare, and the page doesn't say what you're meant to conclude.
- **Fix:** keep one or two as sorted horizontal bars, only where a split drives a decision (for example, priority mix and product area). Title each with its finding: "Billing is 31% of tickets, up from [x]%". Cut channel unless someone acts on it.

**7. The line chart's y axis starts at 4,000.**
- This exaggerates every wiggle.
- 12 months of daily points is also noisy and hides the weekly cycle.
- **Fix:** plot weekly totals, or a daily line with a 7-day average. Start at zero, or label the axis break clearly. Mark the current partial week, and put the title as the finding: "Volume flat since June, spike in August".

**8. A 46×11 table sits on the page.**
- It's reference material, not an at-a-glance view.
- **Fix:** move it behind a click ("By agent"). On the main page, show only exceptions, such as agents or queues outside the normal range.

**9. Some tiles are ambiguous or lack context.**
- "Avg first response" is skewed by outliers, so use median plus 90th percentile.
- "Backlog age" doesn't say whether it's the oldest ticket, the mean or the median.
- "SLA %" shows no target.
- There's no "last updated" timestamp, and no visible state when data is stale or missing.

## What I'd do

I'm assuming the VP does a Monday weekly review and team leads glance at it daily.

1. **Top, attention strip:** what's out of range right now, with the gap and since when. If nothing is, one line: "All 6 measures within normal range".
2. **Headline row, 4–5 cards:** open tickets, median first response, SLA % vs target, backlog age (defined), CSAT. Each card has the label and period, the value, and one comparison in words. Fold "created today" and "this month" into one volume card, like-for-like.
3. **Middle, two charts only:** weekly volume with the trend, and one sorted bar of the split that matters most.
4. **Bottom or one click down:** the agent table, sorted by exception, with n shown beside CSAT.
5. **Corner:** last-updated time and metric definitions.

## Before Monday

- **Highest value, a few hours:** fix the partial-month tile (#1), reconcile it with the chart (#2), and replace "worse than yesterday" lights with range-based ones (#3). That addresses the trust problem.
- **Then:** delete the 3D pie, move the table down a level, and fix the axis.
- **Worth asking the team:** which decision each remaining number supports. If nobody can name one, cut it.

I can sketch the layout or write the tile copy if you share the data source or a screenshot.
