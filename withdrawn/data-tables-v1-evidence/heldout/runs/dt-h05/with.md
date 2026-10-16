**Why numbers go right-aligned**

- Digits compare by place value. If the ones, tens and hundreds line up in vertical stacks, you can see which number is bigger at a glance, without reading each one.
- Right-aligning does this for integers and money, because the last digit always sits in the same spot.
- It only works with tabular (fixed-width) figures. In CSS that's `font-variant-numeric: tabular-nums`.
- Every value in a column should have the same number of decimals, so the decimal points line up too. Pad with `.00` where needed.
- The header should take the same alignment as its column. A right-aligned header sits over the last digit.

**Mixed columns like "3 days", "12 days", "Pending"**

Right-aligning doesn't help here. The cells are text, and the numbers in them don't compare cleanly. Pick one of these, in this order of preference:

1. **Split it into a number column and a status column.** Put "Duration (days)" as bare numbers, right-aligned, with a dash for no value. Put "Status" in a separate column. This is the best option if people will sort or compare the values.
2. **Keep one column, but make "Pending" the missing value.** Move the unit to the header ("Wait (days)"), so the cells are `3`, `12` and `—`. Add a note if "—" isn't obvious. If "Pending" really matters, give it its own status column.
3. **If it has to stay mixed, treat it as text.** Left-align the column and its header. Don't right-align a column of words just because some cells have numbers in them.

**Rule of thumb for designers**

> Align by what the column *is*. Numbers that people compare go on the right, with matching decimals and tabular figures. Words, dates and mixed content go on the left. If one column is trying to be both, split it.

Three smaller rules go with it:
- Put the unit once in the header, not in every cell.
- Never center numbers.
- Never leave a cell blank. Use a dash or "n/a" with a note, and show 0 only when the value really is zero.
