**Pick: Dev A's 4px base, with a 1.2 type scale rounded to whole pixels.** Dev B's 8px base is too coarse for dense tables, and Dev C's Tailwind reference only half-applies: Tailwind uses a 4px spacing base but hand-picked type sizes, not a ratio.

Why not 8px: an 8px grid has no 4px or 12px step, so table cell padding snaps to 8 or 16 and the tables get either cramped or loose. A 4px base gives you finer control and still stays on a clean grid.

Why 1.2 and not 1.333: a 1.333 scale from a 16px base produces 21, 28, 37px, which are too large for a data UI. Hierarchy in dense tables should come from weight and color more than size, so a tighter ratio is right.

## Spacing (4px base)

| Token | px | Typical use |
|---|---|---|
| `space-1` | 4 | Icon-to-label gap, tight cell padding |
| `space-2` | 8 | Cell padding (desktop), button inner gap |
| `space-3` | 12 | Form field gap (desktop) |
| `space-4` | 16 | Card padding, section gap |
| `space-5` | 20 | |
| `space-6` | 24 | Section separation |
| `space-8` | 32 | Page-level gaps |
| `space-10` | 40 | |
| `space-12` | 48 | |
| `space-16` | 64 | |

## Type (1.2 ratio, rounded, base 16px)

| Token | px | Line height | Use |
|---|---|---|---|
| `text-xs` | 12 | 16 | Column metadata, badges (desktop only) |
| `text-sm` | 14 | 20 | Desktop table body |
| `text-base` | 16 | 24 | Tablet body, default UI text |
| `text-lg` | 19 | 24 | Subheads |
| `text-xl` | 23 | 28 | Section headers |
| `text-2xl` | 28 | 32 | Page titles |
| `text-3xl` | 33 | 40 | Rarely used, dashboard figures |

Desktop tables can use `text-sm` (14px) as the body size. Keep tablet screens at `text-base` or larger, since warehouse staff read them at arm's length.

## Density and touch targets

Use two density tokens rather than one set of values, because gloves and mouse pointers need different sizes.

| Element | Tablet (touch, gloves) | Desktop (dense) |
|---|---|---|
| Minimum hit target | 56px | 32px |
| Table row height | 56px | 32px |
| Button height | 56px | 32px |
| Input height | 56px | 36px |
| Table cell padding (x / y) | 16 / 12 | 8 / 4 |

The 56px tablet target is above the 48px platform minimum, which is intentional for gloved use. Treat these as starting values and validate them with real gloves on a real 10-inch device before locking them in.

Next step: I can write these as design tokens (CSS custom properties or a Tailwind theme extension, whichever your stack uses) if you tell me which one.
