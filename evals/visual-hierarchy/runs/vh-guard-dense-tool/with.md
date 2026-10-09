**My advice is to push back on the fewer-rows part and accept most of the rest.**

**The blotter's job.** Traders use it to scan and compare numbers continuously, so the most important content is the data. Cutting 40 visible rows to, say, 25 means more scrolling and more chances to miss a fill, a reject, or a position change. A designer judging this as a landing page would call it airy. For a monitoring tool it's a loss, so don't trade visible rows for bigger headings unless there's a task reason.

**What to keep**
- **Row count.** Hold it at about 40, or whatever the traders have today. If you want to test a change, measure it with them. Look at time-to-find-an-order and missed-event rates, not at how the screen looks in a mockup.
- **Numeric columns.** Keep tabular (monospaced-digit) figures, right-aligned with consistent decimals. Those alignments let traders compare values at a glance.
- **Row height.** Keep it compact. Offer a density toggle (compact, default, comfortable) so each trader can choose.

**What to take from the designer**
- **Headings.** Column headers and section titles can be clearer without being bigger. Quiet them in size and value, and use weight and a little spacing to separate them from the data. Big headings spend space on the least important content, and the data should be the loudest thing on the screen.
- **Space.** Put it where it groups things: between the header and the table, between logical column groups, and around the toolbar. Padding between every row isn't needed. Use zebra striping or a faint hairline, not boxes, to guide the eye along a row.
- **Emphasis.** Spend it sparingly, on the few things that matter: status, side (buy or sell), and large or abnormal values. Pair color with a second cue such as weight, an icon, or text, because red and green alone fail for color-blind traders. If everything is bold or colored, nothing stands out.
- **Secondary columns.** Move rarely used columns (IDs, timestamps to the millisecond, venue codes) behind a column chooser or a row expand. This is the safe way to make the screen feel lighter without losing rows.

**A compromise to offer the designer**
Frame the goal as less noise, not fewer rows. That means fewer columns by default, calmer headers, consistent alignment, and emphasis only on exceptions. It also means a density setting for anyone who wants more air. You get most of the airy look and keep the working view intact.

**Quick test.** Blur the screen. What remains should be the rows that need attention (rejects, big fills, limit breaches), not the headings. If the headings are the strongest shapes left, the redesign has the hierarchy backwards.
