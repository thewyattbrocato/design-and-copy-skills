**Pick Dev A's 4px base and 1.2 ratio, and implement them as Tailwind tokens.** Dev C's answer is mostly Dev A's answer anyway, because Tailwind's spacing is already 4px-based (`1` = 0.25rem). Dev B's 8px grid is a subset of a 4px grid, so you lose nothing by allowing 4px steps. An 8px base would take away the half-steps that dense tables need, like 4px and 12px cell padding.

## Spacing (4px base)
`0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64`

- Use 8px multiples for layout: page gutters, card padding and section gaps.
- Use the 4px steps inside components, such as cell padding and icon-to-label gaps.

## Type (1.2 ratio, two base sizes)
Use the same ratio with a different base per density mode, rounded to whole pixels:

| Step | Desktop (base 14) | Tablet (base 16) |
|---|---|---|
| xs | 12 / 16 | 13 / 20 |
| base | **14 / 20** | **16 / 24** |
| lg | 17 / 24 | 19 / 28 |
| xl | 20 / 28 | 23 / 32 |
| 2xl | 24 / 32 | 28 / 36 |
| 3xl | 29 / 36 | 33 / 40 |

Sizes are font-size / line-height, and every line-height sits on the 4px grid. Table cells use base, and column headers use xs with medium weight. On tablet, nothing the user has to read in a hurry should go below 16px.

## Density and touch targets
Make density a token set, not separate designs:

| | Desktop compact | Desktop default | Tablet (gloves) |
|---|---|---|---|
| Table row height | 32 | 40 | 56 |
| Cell padding (V/H) | 4 / 8 | 8 / 12 | 12 / 16 |
| Min tap target | n/a | 32 | **48, 56 for primary actions** |
| Gap between targets | 4 | 8 | **12** |

## Why not 8px with 1.333
- At a 14px base, 1.333 gives 14 → 19 → 25 → 33. That's too big a jump for tables, which need close steps like 12, 14 and 17.
- A coarse 8px grid forces rows to 32 or 40 with no room in between. It also can't express the tighter padding desktop users want.
- "Cleaner" is a weak reason when the cost is density.

## Tailwind specifics
- Keep Tailwind's default spacing scale, and trim it if you want to enforce the list above.
- Override `fontSize` with the table above, not Tailwind's default sizes. Tailwind's defaults (12, 14, 16, 18, 20, 24, 30, 36) aren't a ratio.
- Drive the tablet/desktop switch with CSS variables, for example `--font-base` and `--row-h` set on a `[data-density]` attribute. Components then don't need to know which device they're on.

The numbers to check on real hardware are the 56px tablet row and the 48px minimum target. Test them with actual gloves before you lock them in.
