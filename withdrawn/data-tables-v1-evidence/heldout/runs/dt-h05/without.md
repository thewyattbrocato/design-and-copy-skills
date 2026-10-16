**Why right-align numbers:** Digits only compare at a glance when place values line up. Right-aligned (with a tabular-figure font, and the same decimal places in a column), units sit under units and tens under tens. Longer numbers visibly look bigger, so you can scan and compare magnitude without reading. Left-aligned or centered numbers have ragged place values, so 1,250 can look similar to 12.5.

**Mixed columns ('3 days', '12 days', 'Pending'):**

The question is whether the user will compare the values or just read them.

1. **Split the number from the unit.** Put "days" in the header ("Duration (days)") and make the cells `3` and `12`, right-aligned. This is the best fix whenever the unit is the same throughout.
2. **Treat the non-numeric state as a different kind of value.** "Pending" isn't a quantity. Either:
   - show an em dash or "–" right-aligned, with the status communicated elsewhere (a status column or a muted style), or
   - keep the word, but right-align it with the numbers and style it differently (muted gray, italic) so it reads as "no number yet."
3. **If you can't split the unit** (units vary, like "3 days" and "2 weeks"), left-align the whole column. Text is compared by reading, not by place value, so left alignment is correct.

**Rule of thumb for designers:**

> Align by how the reader uses the column. If they compare magnitudes, right-align, using tabular figures, consistent decimals, and units in the header. If they read each cell as a label, left-align. Never center data columns. In a mixed column, pull the numbers out so they can be right-aligned, and make the exceptions visually distinct. If the numbers can't be separated out, left-align the column.

**Corollary:** a column header should have the same alignment as its data, so a right-aligned numeric column gets a right-aligned header.
