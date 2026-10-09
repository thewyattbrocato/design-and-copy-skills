**Use a 1px hairline between rows.** Keep the rows themselves fairly tight and add a little vertical padding inside each one.

**Why a rule fits here**
- Thirty rows of the same kind is a dense list, and a hairline is the standard fix for that. Space alone would make the list long, so people scroll more, and it would blur the rows into one block of text.
- Each row has three fields (date, merchant, amount). A rule marks where one transaction ends and the next begins. The reader then scans across a row and doesn't pair a date with the wrong amount.
- Extra space between rows pushes the list toward a card layout, and these rows aren't separate objects. It also uses up the screen height you need to see many transactions at once.

**Why not the other two**
- **Alternating backgrounds** suit wide, many-column tables, where the eye has to travel across a row. Your row has only three fields. Zebra striping also adds visual noise on a phone. It can break accessibility contrast checks, and it behaves badly in dark mode and with selected or pressed states.
- **Extra space only** works for short lists. At 30 rows it costs too much scroll length. It also relies on the reader noticing small differences in gap size.

**Details that make it work**
- Use one quiet color for the rule. Make it low-contrast, such as a light gray at roughly 10–15% opacity.
- Pad each row about 12–16px above and below, so the rule has room on both sides. Touch targets should be at least 44px tall if rows are tappable.
- Inset the rule to align with the text's left edge, and skip the line after the last row. Let the container own the rule, for example `border-top` on every row except the first, so the last row doesn't get a double line.
- Group by day with a small date header, such as "Today" or "Oct 3". The date is then not repeated on every row, and the grouping reads as bigger breaks than the hairlines. This works well with 30 rows. Keep more space above each header than below it, so the header sits closer to its own rows.
- Right-align the amounts, preferably with tabular numerals, so the figures line up in a column.
