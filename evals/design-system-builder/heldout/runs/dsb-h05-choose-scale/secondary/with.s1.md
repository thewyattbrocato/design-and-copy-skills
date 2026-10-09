**Decision: 4px base for spacing, with hand-set type steps instead of a generated ratio scale.** Dev A's base is the right grid for dense UI, and Tailwind's spacing already uses it, so Dev C gets most of what they want.

**Why not 8px:** Dense tables need 4px steps for cell padding and tight gaps. An 8px-only grid forces 16px where 12px is needed or 24px where 20px would do.

**Why not 1.333:** The steps are too large for desktop tables. Going from 16 to 21 to 28 skips the 14–16 range that dense UI relies on.

**Why not a generated ratio:** Pixel rounding makes generated sizes awkward, and tablet and desktop need different sizes anyway. Fixed tokens are easier to review and override.

## Spacing (4px base)

| Token | px | Typical use |
|---|---|---|
| `space-0` | 0 | |
| `space-1` | 4 | Cell padding (y), icon gap |
| `space-2` | 8 | Cell padding (x), tight gaps |
| `space-3` | 12 | Between related fields |
| `space-4` | 16 | Card/panel padding (desktop) |
| `space-5` | 20 | |
| `space-6` | 24 | Section gaps |
| `space-8` | 32 | Page-level gaps |
| `space-10` | 40 | |
| `space-12` | 48 | |
| `space-16` | 64 | |

## Type

| Token | Size / line-height | Use |
|---|---|---|
| `text-xs` | 12 / 16 | Desktop metadata only, never on tablet |
| `text-sm` | 14 / 20 | Desktop dense table body |
| `text-base` | 16 / 24 | Tablet body, desktop forms |
| `text-lg` | 19 / 24 | Section labels |
| `text-xl` | 23 / 28 | Subheads |
| `text-2xl` | 28 / 32 | Page titles |
| `text-3xl` | 33 / 40 | Hero numbers (rare) |

Step ratios are about 1.2, so the design intent holds, but the values are fixed tokens. Tablet UI uses `text-base` as its minimum.

## Density and touch

Density is a token pair, so components don't hard-code sizes:

| Token | Desktop (dense) | Tablet (gloved) |
|---|---|---|
| `row-h` | 32 | 56 |
| `control-h` (inputs, buttons) | 32 | 48 |
| `hit-min` (minimum tap target) | 24 | 48 |
| `hit-gap` (between targets) | 8 | 12 |

Gloves need larger targets than WCAG's 44px minimum, so 48px is the tablet floor.

If you want, I can write these as a tokens file (CSS custom properties plus a JSON source) in the project.
