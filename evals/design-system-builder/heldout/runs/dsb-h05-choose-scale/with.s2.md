**Pick Dev A's 4px base and 1.2 type ratio.** Dev C's Tailwind spacing is also 4px-based, so A and C agree on spacing. The only real disagreement is with B.

I assumed a web product with one brand and a small team. The sizes below are proposals, and I haven't checked contrast.

## Spacing (4px base, 8 steps)

| Token | px | Tailwind key |
|---|---|---|
| `space-1` | 4 | `1` |
| `space-2` | 8 | `2` |
| `space-3` | 12 | `3` |
| `space-4` | 16 | `4` |
| `space-6` | 24 | `6` |
| `space-8` | 32 | `8` |
| `space-12` | 48 | `12` |
| `space-16` | 64 | `16` |

The token numbers match Tailwind's keys, so utilities like `p-4` still mean 16px. Override the theme to remove the other steps (5, 7, 9, 10 and so on).

## Type (16px anchor, 1.2 ratio, 5 roles, rounded to whole px)

| Role | Size / line height | Use |
|---|---|---|
| `text-label` | 13 / 20 | Table cells and captions on desktop |
| `text-body` | 16 / 24 | Default body text |
| `text-title` | 19 / 28 | Section titles |
| `text-heading` | 23 / 32 | Page headings |
| `text-display` | 28 / 36 | Large numbers and dashboard figures |

Every line height falls on the 4px grid. Use tabular numerals in all tables.

## Density modes

The roles stay the same and only the values change.

| | Desktop (compact) | Tablet (touch) |
|---|---|---|
| Table cell text | `text-label` 13 | `text-body` 16 |
| Table row height | 32 | 56 |
| Min tap target | 32 | 48 (56 for primary actions) |
| Gap between targets | `space-2` (8) | `space-3` (12) |
| Cell padding | `space-2` × `space-3` | `space-3` × `space-4` |

## Why not B

- **Row heights:** an 8px base can't produce the 36 or 44px row heights and 20px line heights that dense desktop tables depend on. You'd end up with 32 (too loose) or 40 (too tall), or you'd break the grid.
- **Type jumps:** at 1.333 from 16, the steps are 12, 16, 21, 28, 38 and 51. Those jumps are too coarse for a UI that is mostly 13 to 19px text. The 38 and 51 sizes would almost never be used, and the gap between 16 and 21 pushes people into one-off sizes.
- **"Cleaner":** the clean look comes from using a short scale consistently. The 4px base is still a multiple of 8, so you can use only the 8s where it matters.

## Why not Tailwind defaults

Tailwind's type sizes (12, 14, 16, 18, 20, 24, 30…) aren't a ratio, and its spacing has about 30 steps. That is the near-duplicate sprawl a short scale prevents. Keep Tailwind as the tooling and trim its theme to the values above.

## Trade-off

The 1.2 ratio gives 13px table text on desktop. That's fine for dense tables with a good typeface, but if the team finds it too small, raise `text-label` to 14. That breaks the ratio slightly but doesn't affect the other roles.
