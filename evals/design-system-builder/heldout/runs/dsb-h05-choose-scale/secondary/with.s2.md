**Pick: Dev A's 4px base, with a 1.2 ratio used only to derive the type steps and then rounded to whole pixels.** Tailwind's spacing scale is also 4px, so Dev C is close, but Tailwind's type sizes don't match gloved tablets or dense tables. The 8px base is too coarse for dense UI: it has no 4px or 12px step for icon padding and inline gaps. The 1.333 ratio makes big jumps that wreck hierarchy in tables, and its raw values (21.3, 37.9) fall off any grid.

**Spacing (4px base)**

| Token | px | Typical use |
|---|---|---|
| `space-0-5` | 2 | Hairline gaps, icon nudges |
| `space-1` | 4 | Cell padding (dense), icon-to-label |
| `space-2` | 8 | Cell padding (default), tight groups |
| `space-3` | 12 | Form row gaps, toolbar gaps |
| `space-4` | 16 | Card padding, section gaps |
| `space-5` | 20 | |
| `space-6` | 24 | Section padding on tablet |
| `space-8` | 32 | Page margins (desktop) |
| `space-10` | 40 | |
| `space-12` | 48 | |
| `space-16` | 64 | |

**Type (1.2 ratio from 16px, rounded to whole px)**

| Token | px | Line height | Use |
|---|---|---|---|
| `text-sm` | 13 | 1.35 | Dense desktop tables, meta text |
| `text-base` | 16 | 1.5 | Body; the **minimum** on tablets |
| `text-lg` | 19 | 1.4 | Subheads, list item primary text |
| `text-xl` | 23 | 1.3 | Section headings |
| `text-2xl` | 28 | 1.25 | Page titles |
| `text-3xl` | 33 | 1.2 | Rare: empty states, scan-result totals |

Don't go below 13px anywhere. Dense tables use `text-sm` on desktop only; tablets always use `text-base` or larger.

**Control and target sizes**

| Context | Height | Notes |
|---|---|---|
| Table row, desktop dense | 32 | Uses `space-1` / `space-2` padding |
| Table row, desktop default | 40 | |
| Input / button, desktop | 36 (default), 32 (compact) | |
| Touch target, tablet | 56 | Gloved use. Absolute floor 48. |
| Row, tablet list | 64 | Scan-and-tap rows |
| Icon sizes | 16 (desktop inline), 20 (desktop controls), 24 (tablet) | |

**Radii:** 4 (inputs, table cells), 8 (buttons, cards), 12 (sheets).

**Density rule:** the same tokens everywhere, but a `density` context switches row height and control height. Tablet is `comfortable`, desktop defaults to `dense`. Don't invent per-screen values.

I haven't written any files, since this directory isn't a repo. I can generate this as a tokens file (CSS custom properties plus a JSON source) if you want it in the codebase.
