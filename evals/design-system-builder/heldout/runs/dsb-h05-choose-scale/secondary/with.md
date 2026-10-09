**Pick: Dev A's 4px base with a 1.2 type ratio, with the values below.** Tailwind's spacing is already a 4px scale, so Dev C agrees on spacing. Its type scale isn't a ratio and its defaults are too small for gloved tablet use, so take the mechanism from it, not the values.

**Why not 8px:** Dense desktop tables need 28px and 36px rows. An 8px grid forces 24, 32, or 40 and leaves no good middle step. 4px gives those values without custom tokens.

**Why not 1.333:** From a 14px body, 1.333 gives 18.7, 24.9, 33.2. Dense UI needs closer steps between table text, labels, and values, and 1.333 also pushes the caption size too small. 1.2 keeps the steps tight.

### Spacing (4px base)

| Token | px | Typical use |
|---|---|---|
| space-1 | 4 | Icon-to-label gap, cell padding (tight) |
| space-2 | 8 | Cell padding (desktop), inline gaps |
| space-3 | 12 | Control inner padding |
| space-4 | 16 | Card and panel padding |
| space-5 | 20 | Section gaps |
| space-6 | 24 | Between sections |
| space-8 | 32 | Page margins (desktop) |
| space-10 | 40 | Page margins (tablet) |
| space-12 | 48 | Large separators |
| space-14 | 56 | Tablet touch targets |

### Type (1.2 ratio, anchored at 14px)

| Token | px | Use |
|---|---|---|
| text-caption | 12 | Metadata, column hints (desktop only) |
| text-body-sm | 14 | Desktop body, table cells, labels |
| text-body | 17 | Tablet body (gloved, arm's length) |
| text-title | 20 | Section headings |
| text-heading | 24 | Page titles |
| text-display | 29 | Rare: totals, stock counts on tablet |

Body is 14 on desktop and 17 on tablet. Use a surface token that maps `text-body` to whichever applies, so components don't branch on device.

Line heights: 1.25 in tables and dense lists, 1.5 for forms and prose.

### Control sizes

- **Desktop dense table row:** 28px. Comfortable row: 36px.
- **Desktop controls (buttons, inputs):** 32px.
- **Tablet controls:** 56px minimum for anything tapped. Gloves need more than the 44–48px touch guidelines assume, so don't go below 56 on warehouse surfaces.
- **Tablet table rows:** 56px.

### Rules to put in the repo

1. All spacing and sizes come from these tokens. No raw px in components.
2. Surfaces (`tablet`, `desktop`) set density tokens. Components don't check device.
3. Changing a token value requires a review of both surfaces.

I haven't checked these against any existing Tallyard files, since the repo isn't a git repository and I didn't look for a token file. If you want, I can write these as a JSON or CSS token file.
