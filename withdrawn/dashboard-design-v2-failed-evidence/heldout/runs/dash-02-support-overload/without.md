# Support dashboard review

## The tile you called out is wrong

It compares 11 days of this month to a full month of last month. That gives "down 65%," which is an artifact. Using your numbers:

- This month: 3,120 / 11 days ≈ 284 tickets/day.
- Last month: 8,940 / ~30 days ≈ 298 tickets/day.
- Real difference: about **-5% per day**. If the pace holds, October ends near 8,800, or about -2%.

Someone who sees "-65%" will either panic or conclude the dashboard is broken. This tile is probably a big reason nobody trusts it. Fix it by comparing the same elapsed period (days 1-11 vs days 1-11 last month), or by showing a daily rate. You could also add a projected month-end, labeled as a projection.

The "tickets created today" tile has the same flaw. If it's compared with yesterday's full-day total, it will be red every morning.

## Other problems

**Tiles and lights**
- Day-over-day red/green is mostly noise. Weekends, Mondays and small CSAT samples make tiles flip red or green at random. With 6 tiles, something is red almost every day, so red stops meaning anything.
- "Worse than yesterday" is undefined for some tiles. Is fewer tickets created good or bad?
- Red/green alone fails for colorblind viewers. There's no threshold or target, so you can't tell "worse than yesterday" from "actually a problem."
- Averages hide the pain. Avg first response and backlog age are skewed by outliers. Use median plus p90 for response time, and oldest ticket or count over N days for backlog.
- The tiles don't show definitions, time windows or a data-as-of timestamp.

**Charts**
- **3D pie of CSAT by agent:** this is wrong on two counts. CSAT is a rate, not parts of a whole, so slices of it mean nothing. 3D also distorts slice sizes. Per-agent CSAT often rests on a handful of responses, so it ranks people on noise. Replace it with a sorted bar chart that shows n (responses), and hide or gray out agents below a minimum n.
- **Three donuts:** angles and arc lengths are hard to compare, and three of them are hard to scan side by side. Use sorted horizontal bars, or a single small table if the categories are few.
- **Line chart with y-axis starting at 4,000:** truncation makes ordinary swings look dramatic. Start at 0, or plot weekly totals or a 7-day average with the raw daily series faint behind it. 365 daily points will be spiky because of weekends. Annotate known events like launches and outages.
- **46 × 11 table:** nobody reads that on a dashboard. Cut it to the 3-4 columns people act on, sorted by something meaningful. Put the full table behind a drill-down or an export.

**Overall:** one page with about 14 elements and no hierarchy or stated question. People say "too much" because nothing says what to look at first.

## What I'd do before Monday

You probably can't redesign everything by Monday, so I'd do this in order:

1. **Fix the misleading numbers (about an hour).** Make the month tile and the "today" tile compare like periods. Add an as-of timestamp. Replace the 3D pie. Start the line chart at 0 or switch to weekly.
2. **Rebuild the top row.** Show each tile as a value plus a 7-day sparkline plus a comparison to the same weekday last week or a 7-day average. Use color only when a metric crosses a defined threshold, such as SLA below 90%. Add a hover or footnote with the definition.
3. **Cut the rest.**
   - Move channel, priority and product area into one bar-chart section.
   - Show the agent view as a sorted bar with n.
   - Move the 46-row table to a second tab.
4. **Check the numbers before presenting.** Pick 2-3 tiles and reconcile them against the source system (Zendesk, Jira or whatever you use). If they don't match, find out why. That does more for trust than any visual change.
5. **Take your VP a short list.** Say what you changed and why, and include the -65% example. Then ask the 3-4 people who complain what decision they'd want the dashboard to help them make. That tells you what the page should be for.

I'd also confirm who the dashboard is for. Managers watching queue health, agents, and the VP need different views. Right now it tries to serve all three.

If you share the tool (Looker, Tableau, Metabase, or something else) and the underlying queries, I can help write the like-for-like comparison logic or mock up the redesigned layout.
