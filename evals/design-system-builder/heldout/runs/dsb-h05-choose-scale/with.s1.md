**Pick Dev A's 4px base and about a 1.2 type ratio.** Tailwind's spacing is already 4px, so Dev C's answer is mostly Dev A's. Use Tailwind as the implementation, but restrict it to the short scale below.

## Spacing (8 steps, 4px base)

| Token | px | Typical use |
|---|---|---|
| `space-1` | 4 | Icon-to-label gap, cell padding in compact tables |
| `space-2` | 8 | Minimum gap between touch targets, tight inset |
| `space-3` | 12 | Cell padding (comfortable), form gaps |
| `space-4` | 16 | Default inset, card padding |
| `space-5` | 24 | Section gaps |
| `space-6` | 32 | Group separation |
| `space-7` | 48 | Page-level gaps |
| `space-8` | 64 | Page margins on large screens |

I left out 20 and 40 on purpose. They sit too close to their neighbors and would end up as near-duplicates. In Tailwind, override `theme.spacing` with only these values so the other steps can't be used by accident.

## Type (6 roles, 1.2 ratio from 16px, rounded to whole pixels)

| Role | Size / line height | Notes |
|---|---|---|
| `text-caption` | 12 / 16 | Floor; never go smaller |
| `text-body-sm` | 14 / 20 | Table cells on desktop |
| `text-body` | 16 / 24 | Default on tablet |
| `text-title` | 20 / 28 | Section titles |
| `text-heading` | 24 / 32 | Page headings |
| `text-display` | 28 / 36 | Scan results, big counts; tablet only |

Every line height is a multiple of 4, so type sits on the spacing grid.

## Density modes

Density is a theme that remaps roles. It doesn't add new scales.

| | Desktop `compact` | Tablet `touch` |
|---|---|---|
| Table row height | 32 | 56 |
| Cell padding | `space-1` × `space-3` | `space-3` × `space-4` |
| Table text | `body-sm` (14) | `body` (16) |
| Min target size | 32 | 48 (primary actions 56) |
| Gap between targets | `space-1` | `space-2` minimum |

Gloves are why touch targets are 48px or larger and gaps are at least 8px. Use `pointer: coarse` or a user setting to switch modes, and let users override it.

## Why not 8px / 1.333

- **8px base:** dense tables need 28px rows and 4px or 12px padding. An 8px grid forces 32 or 40px rows and wastes the desktop users' screen space.
- **1.333 ratio:** from 16px it gives 21, 28, 38. That is too coarse for a UI that mostly lives between 12 and 20px, and it leaves no sensible size between table text and a title.

Assumptions: web product, one brand, and you'll size in `rem` (1rem = 16px) so browser font settings still work. I haven't checked these against your real screens. Build one inventory table and one scan screen first, and adjust only if something doesn't fit.
