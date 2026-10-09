**Pick: Dev A's 4px spacing grid, with a 1.2 type ratio, and two density modes.** Dev C is right that the spacing grid should match Tailwind's 4px unit, though Tailwind's type sizes are hand-picked rather than a ratio.

**Why not 8px:** Dense tables need 4px steps. Row padding of 4 or 12, 28px or 36px rows, and 12px cell padding are all off an 8px grid. Touch targets are the only thing 8px handles better, and 56px is already a multiple of 8.

**Why not 1.333:** It makes jumps too large for dense UIs. Hierarchy in a table should come from weight and color, not big size changes. 1.2 gives small, usable steps.

**Spacing (4px base, both modes):**
`0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64`

**Control heights:**
- Desktop (dense): 32px rows and inputs, 40px for standard buttons
- Tablet (gloved): 56px minimum for every tap target, 64px for primary actions. Don't go below 48px anywhere.

**Type, desktop (base 14px, ratio 1.2):**

| Token | px | Use |
|---|---|---|
| `text-caption` | 12 | Metadata, column hints |
| `text-body` | 14 | Table cells, forms |
| `text-lg` | 17 | Section labels |
| `text-h3` | 20 | Panel titles |
| `text-h2` | 24 | Page titles |
| `text-h1` | 29 | Rarely used |

**Type, tablet (base 16px, ratio 1.2):**

| Token | px | Use |
|---|---|---|
| `text-caption` | 13 | Metadata |
| `text-body` | 16 | Lists, forms, table cells |
| `text-lg` | 19 | Section labels |
| `text-h3` | 23 | Panel titles |
| `text-h2` | 28 | Page titles |
| `text-h1` | 33 | Rarely used |

Use the same token names in both modes so components don't need to know which device they're on. Only the values change.

**Rules to write down:**
- Spacing and control sizes are multiples of 4. Type sizes are whole pixels. Don't round type to the grid.
- Tablet data text is never below 16px, because gloved users are reading at arm's length.
- Mode is set per device or per screen at the app root, not per component.

These are proposed values. I didn't check any existing code or design files because there are none in this directory, so the numbers still need to be checked against your real screens on an actual warehouse tablet.
