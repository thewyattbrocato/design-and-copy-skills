# Support dashboard review

## The tile that's wrong

**"Tickets this month: 3,120 vs 8,940 last month, down 65%"** compares 11 days of data to a full month. That's the bug.

- Last month's pace was about 288 tickets/day (8,940 ÷ 31). Over 11 days that's about 3,170, or about 3,280 if last month had 30 days.
- 3,120 is therefore only about 2–5% below last month's pace. That's roughly flat, not a 65% collapse.
- A VP who sees "down 65%" will either panic or conclude the dashboard is broken. This tile alone probably explains a good part of the distrust.

**Fix:** compare like with like.
- Show the month-to-date count against last month's count through the same day (days 1–11), or compare average tickets per day.
- Label it plainly, for example "MTD (11 days): 3,120 vs 3,240 same period last month, -4%".
- Weekday mix matters for support volume, so compare same-weekday-aligned periods or use a 7-day rolling average.
- Also check that "tickets this month" doesn't duplicate the "tickets created today" tile.

## Other problems

**1. The red/green light means "worse than yesterday."**
- Day-over-day change is mostly noise, and weekends and Mondays swing it hard.
- Tiles will flicker red constantly, so people learn to ignore them or distrust them.
- It also treats all metrics the same. Is "tickets created today" going up bad, or is it just demand? Is "backlog age" worse by 0.1 days really red?
- The light has no threshold, so it doesn't mean anything.

**Fix:**
- Judge each tile against a target or SLA.
- Use a tolerance band, such as red only if it's outside the band for N consecutive periods.
- Add a small sparkline and a delta against the trailing 4-week same-weekday average.
- Don't use red/green alone, because it's inaccessible to colorblind viewers. Add an icon or label.

**2. Six tiles are given equal weight, and they're mixed types.**
- Open tickets, backlog age and tickets created are volume and flow metrics.
- First response, SLA % and CSAT are quality metrics.
- Pick the 3–4 that answer "are we keeping up and are customers OK?" Candidates are SLA %, first response time, backlog (open count and age), and CSAT.
- Make "tickets created today" a trend, not a tile. It's partial by definition until the day ends, so it's always low and misleading when compared to yesterday.
- Define each metric on hover or in a footnote. Say whether first response is business hours or wall-clock, mean or median, and what window CSAT covers. Use median or p90 for response time, since the mean gets skewed by outliers.

**3. Three donuts are hard to read and low value.**
- Donuts make it hard to compare slices, and with many categories (product area, probably) they turn into a rainbow.
- Replace them with sorted horizontal bars.
- Better, show each category's change over time or against its share last period, because a static share doesn't tell anyone what to do.
- Consider dropping one. Priority mix is only useful if it ties to SLA.

**4. The 3D pie of CSAT by agent is the worst chart on the page.**
- 3D distorts the angles and areas.
- CSAT scores are not parts of a whole, so a pie is the wrong form entirely. Agent A's 92% and agent B's 88% don't sum to anything.
- With 46 agents it's unreadable anyway.
- Replace it with a sorted bar or dot plot, with the response count shown (a CSAT of 100% from 3 surveys is not meaningful) and a team average line. Better yet, merge it into the agent table.
- Be careful with how it's used. Ranking individuals by CSAT can create unfair incentives, since ticket mix and sample sizes differ between agents.

**5. The line chart's y axis starts at 4,000.**
- Truncated axes exaggerate changes in a line chart. Small movements look like huge swings.
- It may be the cause of "too much" alarm. It's also a trust problem if anyone notices.
- Either start at 0, or if you want to see variation, say so clearly and show a rolling 7-day average over the daily figures.
- Daily points for 12 months is about 365 noisy points. Use weekly totals or a 7-day average, mark holidays, product launches and incidents, and overlay the prior year if you have it.
- Check that the last data point isn't a partial day or partial week, which would show a false drop at the end. That's the same kind of bug as the monthly tile.

**6. The 46-agent, 11-column table is the main reason it's "too much."**
- It's a data dump, not an answer to a question. Nobody can scan 506 cells.
- Cut it to the 4–5 columns managers act on, with sort and filter.
- Put the table behind a drill-down or a second page, and default it to exceptions: agents with high open load, aging tickets or SLA breaches.
- Add team or shift grouping, since 46 individuals is too many to manage as a flat list.
- Be wary of using it for performance management without context.

**7. The page has no hierarchy or story.**
- One page with six tiles, four charts and a table puts everything at the same level.
- Nothing says what to look at first or what to do.
- Say what the data time frame is on each chart (today, MTD, last 30 days, 12 months). Right now they're all different and unlabeled.

## What I'd do before Monday

I'd do this in order, from the cheapest fix to the most expensive.

1. **Fix the monthly tile first** (about 30 minutes). It's a factual error, and it's the first thing the VP will notice. Use a same-period comparison and label it.
2. **Fix the lights.** Turn off the day-over-day red/green and show target-based status, or at minimum a neutral delta with a 7-day comparison.
3. **Fix the y axis** to start at 0, or switch to weekly values. Check that the latest period isn't partial.
4. **Replace the 3D pie** with a sorted bar chart that shows sample size.
5. **Collapse the table** to the default 4–5 columns, and move the rest to a drill-down.
6. **Swap the donuts** for sorted bars.
7. **Write a short definitions panel** for each metric: source, window and calculation. Reconcile at least the headline numbers against the source system, such as Zendesk or Salesforce, and say so on the page. This is what rebuilds trust.

**Rebuilding trust** also takes a bit of process. Ask 3–4 of the people who say they don't trust it which number they got wrong or which one disagreed with their own view. I'd bet it's the monthly tile, the red lights and the CSAT counts. Then show them what you changed and why.

For Monday, I'd present it as: "Here's what was misleading, here's what I fixed, and here's what I recommend next." That's more credible than a redesign nobody has had a chance to test.

I can mock up a revised layout or write the corrected metric definitions, if you want. If you tell me what the dashboard is built in (Looker, Tableau, Power BI, Zendesk Explore or something custom), I can be more specific about how to make these changes.
