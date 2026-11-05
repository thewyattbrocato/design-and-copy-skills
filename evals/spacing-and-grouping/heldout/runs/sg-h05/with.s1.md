**Use a 1px line (hairline) between rows.** Add comfortable vertical padding inside each row. Make the line a quiet, low-contrast color.

**Why a line works for this list**
- Thirty tightly packed rows with three columns (date, merchant, amount) is the case where space alone stops working. Rows have to be close enough to scan, and the line shows where one transaction ends and the next begins.
- The eye tracks horizontally across each row from merchant to amount. A line gives it a guide for that.
- Pure spacing needs gaps big enough to read as separation. That cuts the number of rows per screen. If the gap is small, it blurs into the row's own internal padding.

**Why not the other two**
- **Alternating backgrounds (zebra stripes):**
  - They suit wide tables with many columns, where the eye can drift to the wrong row. With only three fields, they add visual noise.
  - They fight with other background states, such as pressed, selected, or pending rows, and with dark mode.
  - Contrast is a problem. Stripes need enough contrast to show, and that makes the screen busier.
  - If you ever group by date, the stripes work against the grouping.
- **Extra space between rows:**
  - This works for a short list. With 30 rows it means more scrolling.
  - It also weakens grouping. If the gap between rows is close to the gap between date groups or sections, the groups stop reading as groups.

**Details that make the line version work**
- Give each row about 12–16px of vertical padding, so the line has room on both sides. On mobile, keep the row height at 44px or more if the whole row is tappable.
- Use one rule weight in a low-contrast neutral. Don't use a full-strength border color.
- Inset the line to align with the text's left edge, or run it full-width. Pick one and use it throughout.
- Skip the line after the last row. Let the container own the separators rather than putting a border on every row.
- Align amounts to the right edge, with tabular figures so the digits line up.
- If the list spans many days, group rows under date headers. Put more space above each header than below it. Then you can drop the date column from the rows and use lines only within each day.

**One exception:** if the list is a dense, wide table with many columns (running balance, category, status, and so on), light zebra striping alongside or instead of lines can help. Three fields don't need it.
