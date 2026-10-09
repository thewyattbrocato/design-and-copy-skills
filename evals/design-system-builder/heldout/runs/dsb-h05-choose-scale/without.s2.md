**Pick Dev A: a 4px spacing base and a 1.2 type ratio.** Dev C's answer is mostly the same as A's on spacing, and I'd drop it on type.

**Why**
- **4px base:** Dense desktop tables need 4, 12 and 20px steps for cell padding, icon gaps and row heights. An 8px base can't make those, and people end up adding off-grid values anyway. Use 8px as the default rhythm for layout, and keep 4px for fine adjustments.
- **1.2 ratio:** A 1.333 ratio jumps too far between steps (16 → 21 → 28 → 38). That suits marketing pages, not tables and forms where most text sits in 2–3 adjacent sizes.
- **Tailwind:** Its spacing is already a 4px base (`1` = 0.25rem), so adopting it costs nothing there. Its type sizes are hand-picked and follow no ratio, so define your own type tokens. You can still use Tailwind as the tool.

**Spacing scale (px)**

| Token | 1 | 2 | 3 | 4 | 6 | 8 | 12 | 16 |
|---|---|---|---|---|---|---|---|---|
| px | 4 | 8 | 12 | 16 | 24 | 32 | 48 | 64 |

**Type scale (1.2 from a 16px base, rounded, with line-heights on the 4px grid)**

| Step | Size | Line height | Use |
|---|---|---|---|
| xs | 11 | 16 | Captions, badges only |
| sm | 13 | 20 | Compact table cells, secondary text |
| base | 16 | 24 | Body text, touch-mode tables, inputs |
| lg | 19 | 28 | Section headers |
| xl | 23 | 32 | Page titles |
| 2xl | 28 | 36 | Key numbers and dashboards |
| 3xl | 33 | 40 | Rare |

Use tabular numerals (`font-variant-numeric: tabular-nums`) everywhere quantities appear. Keep body text at 13px or larger, and don't use 11px for anything a user has to act on.

**Two density modes from the same tokens**

| | Touch (warehouse tablet) | Compact (office desktop) |
|---|---|---|
| Table row height | 56 | 32 |
| Table text | 16 | 13 |
| Cell padding (vertical / horizontal) | 16 / 16 | 4 / 12 |
| Min tap target | 48 (56 for primary actions) | 24 (pointer only) |
| Gap between adjacent targets | 8 minimum, 12 preferred | 4–8 |
| Button height | 56 | 32 |

Gloves are why touch mode uses 48px minimum targets with 56px for primary actions. That is above the usual 44px (Apple) and 48px (Material) guidance. The gaps between targets matter as much as the target size, because gloved fingers mis-hit neighbours.

Implement density as a single data attribute (`data-density="touch|compact"`) that swaps CSS variables. Don't build separate components. Choose the default by device (`pointer: coarse`) with a user override.

These numbers are a sensible starting point, not tested values. Check the 56px row height and 13px compact text on a real tablet with gloves and on a real desktop table of about 50 rows before you lock them in.
