**Pick Dev A's 4px base and 1.2 type ratio. Apply them through two density modes, not one set of sizes.** Dev C's answer is nearly the same as Dev A's anyway, because Tailwind's spacing is already 4px-based (`1 = 0.25rem`).

**Why not 8px / 1.333**
- An 8px grid can't make the row heights dense tables need. 28 and 36px rows don't exist on it, so you'd get 24 or 32 and nothing between.
- A 1.333 ratio jumps too fast. From a 14px base you get 14, 18.7, 24.9, 33. That leaves no small sizes for table cells, captions, and labels, which is where office users spend their day.

**Why not "whatever Tailwind does"**
- Take its spacing, since that's the 4px scale above.
- Its type scale is hand-picked (12, 14, 16, 18, 20, 24, 30…), not a ratio. It also has no concept of a glove-friendly density.

**Spacing tokens (4px base)**
4, 8, 12, 16, 20, 24, 32, 40, 48, 64. Use 8 and 16 as the defaults and the 4 steps for tight table internals.

**Type scale (1.2 ratio, rounded)**

| Step | Desktop (base 14) | Tablet (base 16) |
|---|---|---|
| xs | 12 / 16 | 13 / 20 |
| base | 14 / 20 | 16 / 24 |
| lg | 17 / 24 | 19 / 28 |
| xl | 20 / 28 | 23 / 32 |
| 2xl | 24 / 32 | 28 / 36 |
| 3xl | 29 / 36 | 33 / 40 |

Sizes are px / line-height. Define them in rem and switch the root size per density mode.

**Density-dependent sizes**

| | Desktop | Tablet (gloves) |
|---|---|---|
| Table row height | 32 (28 for compact) | 56 |
| Min touch target | 32 | 48, with 56 for primary actions |
| Gap between adjacent targets | 4–8 | 12–16 |
| Cell padding (horizontal) | 8–12 | 16 |

**Rules to adopt with it**
- Use tabular (monospaced) numerals in every table and quantity field so columns align.
- Don't go below 12px on desktop or 13px on tablet.
- Pick the mode with `pointer: coarse` or an explicit device setting, not just viewport width. A 10-inch tablet and a small desktop window can be the same width.

The 4px base gives desktop the fine row heights it needs. The 1.2 ratio keeps text sizes close together, and the tablet mode gets its glove-friendly size from a bigger base and bigger targets.
