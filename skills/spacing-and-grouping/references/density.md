# Density

Load this for dense tools, compact and comfortable modes, or any request to show more rows or controls on screen.

## Decide by the task

| Situation | Lean toward |
| --- | --- |
| Experts use it for hours, scanning many records (admin tables, trading views, logs, spreadsheets) | Compact |
| People visit now and then, or read and decide (settings, onboarding, checkout, articles, marketing) | Comfortable to generous |
| Touch-first screens | Comfortable, with touch-size targets |
| Mixed audiences | Comfortable by default, optional compact |

Offer a density setting only when a tool has both kinds of users and enough data to make the difference matter. A simple site does not need one.

## What compresses

- Vertical padding in rows and cells (for example 12 px down to 6 or 4 px).
- Gaps between small items and between rows.
- Section spacing, by one or two steps.
- Control height, down to about 28 to 32 px for pointer-only tools.

## What must not change

- **The within/between ratio.** If groups sat at 8 inside and 24 between, compact may be 4 and 12. The ratio holds, so groups still read.
- **The structure.** The same items, in the same order, in the same groups, in both modes.
- **A readable text size.** Keep body and table text at a legible size (around 13 to 14 px at the smallest for sustained reading; smaller only for secondary data). Make density come from tighter space, not tiny type.
- **Alignment.** Numbers stay right-aligned and columns keep their edges.
- **Row separation.** Subtle rules or shading keep tight rows from merging; space alone stops being enough as rows get close.
- **Touch targets** if the screen can be used with touch. A compact mode is usually for pointer use; do not let it ship to phones unchanged.
- **Focus rings and hover states** stay visible and not clipped by smaller padding.

## Building the two modes

Define the steps once and map them:

```css
:root              { --row-pad: var(--space-3); --group-gap: var(--space-5); }
[data-density="compact"] { --row-pad: var(--space-1); --group-gap: var(--space-4); }
```

Components read the density variables, not literal values. Check the compact mode with a full table of real data, not three rows.

## Fitting a number of rows in view

When a request names how many rows must be visible at once, work backward: the height left after the header and filters, divided by the row count, gives the row height. If that lands at or below the compact range for tables, use the compact row from the data-tables skill (if installed) and let the page scroll less rather than padding rows back out. Keep the rest of the density levers: smaller text, thin rules or light banding, and aligned numbers.

## Generous density

Reading and marketing pages gain from larger gaps between sections (48 to 96 px) and between paragraph blocks. Generous does not mean uniform: within-group space stays small so groups still read, and a few large, deliberate gaps give the page pace. Avoid large empty areas that cut a group in two.
