**Use the 1px line.** Add a little vertical padding to each row, but don't add gaps between rows.

**Why a line works best here**
- The rows are uniform (date, merchant, amount) and there are 30 of them. The user scans down and across to compare amounts and dates, so a hairline marks where each row ends without breaking the scan.
- A line costs almost no vertical space, so more rows fit on screen. Extra gaps between rows use up space on a list this long.
- A line separates rows without adding a second visual signal. Space and a line together would be redundant.

**Why not the other two**
- **Extra space between rows:** the gaps would be too big. If you make them small enough to fit many rows, they are too small to group anything. The rows would also start to look like separate cards, and these are entries in one ledger, not objects. Space also gives weak separation when every row has the same three fields.
- **Alternating backgrounds (zebra stripes):** these suit wide tables where the eye has to travel far across a row. Here the amount is a short distance from the merchant, so they add little. They also cause trouble in dark mode and with accessibility settings, because the contrast between stripes is hard to get right. Tapping a row would also clash with the stripes (pressed, selected or highlighted states). Finally, banking lists often have date-group headers ("Today", "Yesterday"), and stripes collide with those.

**How to set it up**
- **Row height:** use about 56–64 px with roughly 12–16 px of vertical padding inside each row. That keeps a comfortable 44 px or larger tap target without needing gaps between rows.
- **Line style:** use one quiet color, such as a low-contrast gray, and the same weight everywhere. Put it only *between* rows, not after the last one. Let the container or the following row own it, so you don't get a doubled line at the end.
- **Line inset:** start the line at the left text edge, not the screen edge. This is a common mobile pattern and it keeps the list from looking like a stack of boxes.
- **Grouping by day:** if you group by date, use extra space above each group header and less below it. That is the one place where space should do the grouping work.
- **Alignment:** right-align the amounts and use tabular (monospaced) figures so the digits line up in a column.

If you later offer a "compact" mode for power users, you can drop the vertical padding and keep the lines. The lines still separate the rows even when the list is dense.
