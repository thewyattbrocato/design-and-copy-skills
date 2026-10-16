**Use a 1px line between rows.** Make it a hairline in a quiet color, and inset it to align with the text edge, not full-bleed.

**Why a line works best here**
- **Density:** 30 rows is a long scan. The rows are all peers and tightly packed, and that's the case where space alone stops separating them. A hairline does it without costing rows per screen.
- **Scanning:** Each row has the same date, merchant and amount layout. A thin rule gives the eye a clear horizontal track from the merchant on the left to the amount on the right.
- **Cost:** The line takes almost no room. Extra space gets expensive over 30 rows, and a separate gap makes the list read as 30 separate cards.

**Why not the others**
- **Alternating backgrounds (zebra stripes):** These suit wide tables with many columns, where the eye has to travel far. A row with three fields doesn't need them. They also add visual noise and can clash with selected, pressed or pending states. They get worse in dark mode, where low-contrast tints are hard to tune.
- **Extra space only:** This works for a short list. With 30 rows, the spacing has to be large enough to group by itself, and that costs scroll length. It also gets ambiguous when you add day headers.

**Details that matter**
- **Row height and padding:** Keep rows around 56–64px tall, with equal padding above and below the text. This gives a comfortable touch target. The tap area is the whole row, so you don't need extra gap between rows.
- **Line style:** Use one weight and a low-contrast color. Skip the line after the last row in a group so it doesn't double up with the group's edge.
- **Group by date:** Put date section headers like "Today" or "Oct 12" above groups of rows. Give each header more space above than below, so it sits closer to its own rows. Then the date doesn't need to repeat on every row, and the rows can show just merchant and amount. This does more for readability than the choice of separator.
- **Alignment:** Right-align the amounts, and use tabular (monospaced) digits so the decimals line up down the list.

If you add a selected or highlighted state, use a subtle background tint on that one row instead of persistent stripes.
