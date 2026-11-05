**Pick: a 4px base for spacing, with a hand-picked type scale of about 1.2. Don't use a strict ratio, and don't copy Tailwind wholesale.**

Dev A is closest. Here is why each option wins or loses for Tallyard:

- **8px base (Dev B):** Too coarse for dense desktop tables. Row padding of 4, 12 and 20px falls between the steps, so people end up inventing off-grid values. 8px is a good *touch target* unit, but you can get that from a 4px base by using the larger steps.
- **1.333 ratio (Dev B):** It grows too fast. Going from 14px body text to 18.7px, then 24.9px, leaves no useful sizes for table cells, labels and captions. You'd skip over the sizes dense UI needs most.
- **Tailwind defaults (Dev C):** Tailwind's spacing is a 4px base, so Dev C and Dev A agree on spacing. Its type scale is a hand-picked list from 12 to 96px, built for marketing pages, so most of it goes unused here. Take the spacing and skip the type scale.

## Spacing (4px base, 9 steps)

| Token | px |
|---|---|
| `space-1` | 4 |
| `space-2` | 8 |
| `space-3` | 12 |
| `space-4` | 16 |
| `space-5` | 24 |
| `space-6` | 32 |
| `space-7` | 48 |
| `space-8` | 64 |
| `space-9` | 96 |

Steps below 16px are 4px apart. Above that they widen, so no two neighbors can be mistaken for each other. Don't add 20px or 28px. Use the nearest step.

## Type (about 1.2 ratio, 6 roles, rounded to whole pixels)

| Role | Size / line height | Use |
|---|---|---|
| `text-caption` | 12 / 16 | Metadata, badges |
| `text-body-sm` | 14 / 20 | **Dense table cells (desktop default)** |
| `text-body` | 16 / 24 | **Body and form inputs (tablet default)** |
| `text-title-sm` | 19 / 28 | Section headings |
| `text-title` | 23 / 32 | Page titles |
| `text-display` | 28 / 36 | Totals and counts shown at a glance |

Every line height lands on the 4px grid. Keep 16px as the minimum for inputs on tablets, because smaller text is hard to read and tap with gloves.

## Density: one system, two modes

Use the same tokens and let a density setting choose which ones apply. Keep it to two modes, set by context, with a user override.

| | Compact (desktop) | Comfortable (tablet) |
|---|---|---|
| Control and row height | 32 | 48 |
| Table cell text | `body-sm` (14) | `body` (16) |
| Table cell padding (vertical / horizontal) | `space-1` / `space-3` (4 / 12) | `space-3` / `space-4` (12 / 16) |
| Gap between tappable targets | `space-1` (4) | `space-2` (8) |
| Minimum touch target | n/a | 48 × 48 |

Glove use is the reason for the 48px floor, and it's above the usual 44 to 48px guidance for touch. For the warehouse, I'd use 56px for primary actions such as Confirm count and Receive.

## Assumptions and trade-offs

- I assumed a web product with one brand and a small team. Tell me if the tablets run a native app, because that changes the type sizes.
- A hand-rounded scale gives up the mathematical purity Dev B likes. In exchange you get sizes that sit on the line-height grid and suit tables.
- I haven't tested any of this on real hardware. Before you lock the values, try the comfortable mode with gloves on a real warehouse tablet. I'd expect the touch targets to need the most adjustment.
