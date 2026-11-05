**Decision: 4px base spacing, 1.2 type ratio, with the type steps rounded to whole pixels.** Dev A's choice fits both screens. Dev B's 8px grid can't express the 4px gaps that dense desktop tables need. Dev C's "Tailwind" is a 4px spacing scale, so it agrees with A on spacing. On type, Tailwind's scale is hand-picked, not a ratio, and its smallest default (12px) is too small for a gloved tablet.

## Spacing (4px base)

Every value is a multiple of 4. Multiples of 8 are a subset, so B's values remain valid.

| Token | px | Token | px |
|---|---|---|---|
| `space-0` | 0 | `space-6` | 24 |
| `space-1` | 4 | `space-8` | 32 |
| `space-2` | 8 | `space-10` | 40 |
| `space-3` | 12 | `space-12` | 48 |
| `space-4` | 16 | `space-14` | 56 |
| `space-5` | 20 | `space-16` | 64 |

## Type (base 16, ratio 1.2, snapped to whole px)

| Token | Size / line height | Use |
|---|---|---|
| `text-2xs` | 11 / 16 | Column captions only; never for input |
| `text-sm` | 13 / 16 | Desktop table cells, dense metadata |
| `text-base` | 16 / 24 | Body, form input, tablet table cells |
| `text-lg` | 19 / 24 | Section headings |
| `text-xl` | 23 / 28 | Page titles |
| `text-2xl` | 28 / 32 | Dashboard numbers |
| `text-3xl` | 33 / 40 | Hero figures (rare) |

Why 1.2 over 1.333: from 16px, 1.333 gives 12, 16, 21, 28. There's no step between 12 and 16 for table text, and the jump from body to heading is too large for a data-dense UI. 1.2 gives the close steps UI needs.

## Density and touch targets

Density is a token layer over the same scale, not a second system:

- **Desktop (dense):** control height 32, table row 32, cell padding `space-2`/`space-3`, table text `text-sm`.
- **Tablet (gloved):** minimum target 48, primary actions 56, table row 56, cell text `text-base`, at least `space-3` between adjacent targets.

Tablet components should set their own minimums, not rely on text size. Gloved use needs big hit areas more than big type.

## Rules to write down

- Components use tokens only. Raw px values in component code fail lint.
- Spacing must be a multiple of 4. Anything else needs a reason in review.
- Type sizes come only from the scale above, and each has a fixed line height.

I picked these values myself, so the numbers are open to challenge. The one I'd defend hardest is the 1.2 ratio, since it's the choice that actually matters for dense tables.
