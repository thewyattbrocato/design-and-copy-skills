# Support dashboard review

## The "Tickets this month" tile

It compares 11 days of this month with all of last month. "Down 65%" is an artifact of the calendar, not a real change.

- **The real comparison:** Last month ran about 298 tickets/day (8,940 ÷ 30, assuming a 30-day month). This month is running about 284/day (3,120 ÷ 11). That's roughly **5% down**, not 65%.
- **Why it hurts trust:** Every month, the first half shows a scary red number that "fixes itself" by month end. People learn the dashboard cries wolf.
- **The fix:** Compare like with like. Use month-to-date versus the same days last month. Better still, show a run rate or projection (about 8,500 for the month at the current pace). Also account for weekday mix, because 11 days can hold a different number of weekends.
- **Also consider cutting it:** It overlaps with "tickets created today" and the 12-month line chart. If you keep it, label it "MTD vs same period last month".

## The rest of the page

**Red/green lights vs. yesterday**
- Daily noise means most tiles will be red about half the time, so red stops carrying information.
- Weekend and Monday effects will make it flip on a predictable schedule.
- "Worse" differs by metric: open tickets going up is bad, while CSAT going up is good. Check the direction logic is correct on every tile.
- "Tickets created today" is a partial day compared with a full day, so it's almost always "down" in the morning. CSAT and first response have the same problem, because few of today's surveys or tickets have come in yet.
- Red/green alone is also unreadable for colorblind users.
- **Fix:** Color only against a target or a normal range, such as the trailing 4-week average for the same weekday. Show the value, the delta and a small sparkline, and leave the tile neutral when nothing is wrong.

**Tile definitions.** Nobody can tell what these mean, and that's likely a big driver of the distrust.
- Is "avg first response" in business hours or wall-clock time? Averages are dominated by outliers, so show the median and the 90th percentile.
- Is "backlog age" the mean, the median or the oldest ticket?
- Which tickets count toward "SLA %"?
- Add a one-line definition on hover and an "as of" timestamp.
- Reconcile every number against the helpdesk tool before Monday. One visible mismatch undermines everything.

**Three donuts (channel, priority, product area)**
- Humans compare angles and arc lengths poorly, and three side by side invite comparing them to each other, which is meaningless.
- Product area probably has many slices.
- **Fix:** Use sorted horizontal bars. Better, show change versus the prior period, since the mix only matters when it shifts.

**3D pie of CSAT by agent**
- 3D distorts slice sizes.
- CSAT by agent isn't parts of a whole, so a pie is the wrong form. Slices from 46 agents would be unreadable anyway.
- Per-agent CSAT usually rests on very small samples. An agent with 4 surveys and a 100% score will outrank one with 80 surveys and 94%.
- **Fix:** Remove it from the main page. In the drill-down, use a sorted dot plot that shows survey count (n) and flags low-n agents. Decide deliberately whether public agent rankings are something you want at all.

**12-month line chart with the y-axis starting at 4,000**
- The truncation makes ordinary variation look dramatic. A drop from 5,000 to 4,500 appears to cut the volume by more than half.
- Daily points over 12 months are mostly noise and weekly seasonality.
- **Fix:** Start at zero, or aggregate weekly with a 7-day average. Mark the current partial period so it doesn't read as a cliff at the right edge. Annotate known events such as launches and outages.

**46-agent × 11-column table**
- This is a reference table sitting on an executive page. It makes the whole page feel heavy.
- **Fix:** Move it to a drill-down page that's sortable and filterable by team. On the main page, show only exceptions, such as agents or queues outside range. Cut the columns to the 4 or 5 anyone acts on.

**Whole page**
- There's no hierarchy. Everything is the same weight, so there's no obvious "look here first".
- Stock metrics (open tickets, backlog) are mixed with flow metrics (created today) and quality metrics (CSAT, SLA).
- No filters, no date range and no freshness indicator.

## What I'd do before Monday

1. **Talk to 3 or 4 of the people who say it's too much.** Ask what decision they make with it and which number they check first. Also find out which numbers they've seen disagree with the helpdesk. That tells you what to cut and where trust broke.
2. **Fix what's objectively wrong (about a day of work):**
   - Fix the month tile.
   - Replace the daily red/green with target-based status.
   - Remove the 3D pie.
   - Fix the y-axis.
   - Add definitions and an "as of" time.
3. **Cut the page down.** Keep four to six tiles in a hierarchy:
   - Row 1: SLA %, median first response, open tickets and backlog age, each with its target and a sparkline. Show CSAT and MTD volume alongside them.
   - Row 2: weekly volume trend, plus one bar chart of the tickets that drive volume (by product area).
   - Everything else (channel, priority, agent table) moves to a "Details" tab.
4. **Reconcile and say so.** Before the VP sees it, check every tile against the source system. Add a small footer saying the data is verified against the helpdesk, with the date.

For the VP, the pitch is simple. The page has a few real errors (the month tile, the lights, the axis, the pie) that explain the distrust. Fixing those and cutting the volume of information gets you something people believe.

If you share the dashboard tool (Tableau, Looker, Zendesk Explore, etc.) or the underlying queries, I can help build the revised version or check the metric definitions.
