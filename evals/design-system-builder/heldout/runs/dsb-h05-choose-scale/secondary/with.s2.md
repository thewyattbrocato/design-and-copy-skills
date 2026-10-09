**Decision: Dev A's 4px base with a 1.2 type ratio, plus Dev B's 8px multiples for touch-target sizes.** Tailwind's spacing scale is also 4px-based, so you can use its numbers for spacing, but its type scale is not a constant ratio.

**Why not 8px:** Dense tables need 28px and 32px rows and 12px gaps. An 8px grid gives you 24, 32, 40, which is too coarse for chips, badges, and inline padding. Touch targets are the one place where 8px multiples are natural, so they can stay on the 8px grid without the rest of the system being limited by it.

**Why not 1.333:** The steps are too large for a dense UI. From 16px you jump to 21, then 28, then 37, which wastes horizontal space in tables and leaves few usable sizes between labels and headings. 1.2 gives finer steps for the 12–20px range where most inventory UI lives.

## Spacing (4px base)

| Token | px | Typical use |
|---|---|---|
| `space-0` | 0 | |
| `space-1` | 4 | Icon-to-label gap, tight cell padding |
| `space-2` | 8 | Cell padding (desktop), chip padding |
| `space-3` | 12 | Form field internal gaps |
| `space-4` | 16 | Card padding, section gaps |
| `space-5` | 20 | |
| `space-6` | 24 | Section separation |
| `space-8` | 32 | Page-level separation |
| `space-10` | 40 | |
| `space-12` | 48 | |
| `space-16` | 64 | |

## Type (1.2 ratio, 16px base)

Values are rounded to whole pixels.

| Token | px | Line height | Use |
|---|---|---|---|
| `text-caption` | 12 | 16 | Metadata only. Don't use for data on tablets. |
| `text-sm` | 13 | 18 | Desktop table body |
| `text-base` | 16 | 24 | Body, tablet table body, all gloved-use labels |
| `text-lg` | 19 | 24 | Section headers |
| `text-xl` | 23 | 28 | Page headers |
| `text-2xl` | 28 | 32 | Big numbers (counts, totals) |
| `text-3xl` | 33 | 40 | Rare, dashboard hero values |

Density rule: desktop dense tables use `text-sm`. Tablet uses `text-base` everywhere. Nothing on a tablet goes below `text-base` for data.

## Component sizing

| Element | Desktop (dense) | Tablet (gloved) |
|---|---|---|
| Table row height | 32 (compact 28) | 64 |
| Button / input height | 32 | 56 |
| Minimum hit target | 32 | 56 |
| Icon size | 16 / 20 | 24 |
| Radius | 4 (controls), 8 (cards) | Same |

The 56px tablet minimum is above the common 48px guideline on purpose, because gloves make taps less precise. Treat that number as a starting point and check it with real gloves on the actual tablets before you lock it.

## Tailwind comparison (for Dev C)

Tailwind's default spacing uses a 4px base, so its values match ours. Its type scale does not use a constant ratio: `text-xs` 12, `sm` 14, `base` 16, `lg` 18, `xl` 20, `2xl` 24, `3xl` 30, `4xl` 36. Use Tailwind's spacing if you like, but define the type tokens above in your theme so the names and values stay under your control.
