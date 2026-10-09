**Recommendation: a 1px divider line, inset to align with the text and kept low-contrast.**

**Why it fits this case**
- **Scanning:** Each row is a short horizontal record (date, merchant, amount). A thin rule helps the eye track across the row without adding visual weight. Thirty rows will still read as a clean list.
- **Density:** A line costs 1px. Extra spacing across 30 rows adds a lot of scrolling and shows fewer transactions per screen. Users of a banking app often want to scan and compare.
- **Noise:** Zebra striping adds a repeating pattern across the whole screen. It also conflicts with other background states such as pending rows, selected rows, date group headers and dark mode. It works better in wide, many-column tables, where the eye has to travel far across a row. Here the row is short, so it isn't needed.

**Details that make it work**
- Inset the line to start at the left text edge, as iOS lists do. Don't run it full-bleed.
- Use a subtle color, about 8–12% contrast against the background, and check it in dark mode.
- Group by date with a sticky section header. Then the date doesn't repeat on every row, and the dividers only separate rows within a group.
- Right-align amounts and use tabular (monospaced) numerals so the digits line up down the column.
- Make rows at least 44–48px tall for touch targets. This gives enough built-in padding that you don't need extra gaps.

**When to choose something else**
- **Extra space:** Use it if each row grows to hold more content, such as a category icon, a status chip and a second line. Spacing alone can then group things well. Pair it with grouping, or the rows may blur together.
- **Alternating colors:** Consider these only for a wide, multi-column desktop table view.

If you can only test one option, test the inset hairline, and compare it against spacing-only on how quickly people find a specific transaction.
