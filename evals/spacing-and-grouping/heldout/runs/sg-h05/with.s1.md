**Use a 1px hairline between rows.** Pair it with modest, consistent vertical padding inside each row. Don't use alternating backgrounds, and don't rely on extra space alone.

**Why a hairline fits this list**
- **Dense, uniform rows:** Thirty rows of date, merchant and amount are all the same kind of item. Space alone makes them blur into one mass, or it costs you rows per screen.
- **Scanning:** Users scan across a row to match a merchant with its amount. A thin rule guides the eye along the row without adding visual weight.
- **Rules need room on both sides:** Give each row about 12–16px of vertical padding above and below the text. That also keeps each row a comfortable touch target of 44px or more.

**Why not the others**
- **Alternating backgrounds (zebra stripes):**
  - They suit wide tables with many columns, where the eye can lose its row. A three-field row doesn't have that problem.
  - They add visual noise and can look like a selected or highlighted state.
  - They break in dark mode and with accessibility settings, and they fight with any real selected, pending or highlighted row states.
- **Extra space only:** This works with few items, or when rows are grouped. With 30 rows it cuts how many fit on screen, and the rows can still read as loose lines of text instead of a list.

**Details**
- Use one quiet color for the rule, such as a low-contrast gray, and keep the weight the same everywhere.
- Inset the rule to align with the text's left edge, as iOS does. This looks lighter than a full-bleed line.
- Skip the rule after the last row.
- Put the date in a smaller, secondary color. Right-align the amount, and use tabular figures so the digits line up.
- Group by day with a section header (like "Oct 14"), with more space above the header than below it. The date then doesn't have to repeat on every row, and the header does the grouping that space would otherwise do.
- Use space, not rules, to separate day groups. Rules inside groups and space between groups gives you two clearly different levels.
