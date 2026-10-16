**Extra space between rows, combined with a hairline divider if you need more structure.** If I had to pick one of your three, I'd pick the 1px line.

**Why the 1px line wins for this case**
- **Scanning:** The line gives each row a clear edge. Your eye can track from date to merchant to amount without drifting to the neighboring row, and this matters most when the amount is far from the date.
- **Density:** A line costs 1px. Extra spacing costs 8–16px per row, which over 30 rows means a lot more scrolling.
- **Scroll behavior:** Lines stay stable as rows move. Alternating colors can flicker or reshuffle when rows are filtered, deleted, or loaded in pages.
- **Accessibility:** A thin line doesn't depend on color contrast, which makes it easier to get right in both light and dark mode.

**Why not the other two**
- **Alternating backgrounds (zebra stripes):** These suit wide, multi-column tables where the eye has to travel far across a row. Your rows have only three fields and are narrow on mobile, so stripes add visual noise without much benefit. Stripes also clash with tap and selected states, and they're hard to keep accessible across themes.
- **Extra space only:** This works well for short lists or card-style items. At 30 rows it makes the list long and the grouping looser. Proximity alone is also a weaker separator when rows have uneven heights, for example when a merchant name wraps to two lines.

**Practical tips**
- Use a low-contrast divider, such as 8–12% opacity of the text color. It should be visible but not dominant.
- Inset the line to align with the text's left edge, as iOS does, instead of running it full width.
- Give rows about 12–16px of vertical padding, so you get breathing room as well as the line.
- Group by date with sticky section headers ("Today", "Yesterday"). This lets you drop the date from each row and cuts clutter more than any separator choice will.
- Right-align the amounts and use tabular (monospaced) figures so the digits line up down the column.
- Keep a clear pressed state for the row, since the whole row is typically tappable.
