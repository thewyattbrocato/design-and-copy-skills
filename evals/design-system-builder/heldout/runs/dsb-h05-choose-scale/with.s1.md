**Pick Dev A: a 4px base with a 1.2 type ratio, rounded to whole pixels.** Run it in two density modes, because the tablet and the desktop need different sizes.

**Spacing** (8 steps, `space-1` to `space-8`)

| Token | px | rem |
|---|---|---|
| 1 | 4 | 0.25 |
| 2 | 8 | 0.5 |
| 3 | 12 | 0.75 |
| 4 | 16 | 1 |
| 5 | 24 | 1.5 |
| 6 | 32 | 2 |
| 7 | 48 | 3 |
| 8 | 64 | 4 |

**Type** (1.2 ladder from 16px, rounded: 12, 14, 16, 20, 24, 28). Line heights are multiples of 4.

| Role | Compact (desktop) | Touch (tablet) | Line height (compact / touch) |
|---|---|---|---|
| caption | 12 | 14 | 16 / 20 |
| body, table cell | 14 | 16 | 20 / 24 |
| heading-sm | 16 | 20 | 24 / 28 |
| heading | 20 | 24 | 28 / 32 |
| title | 24 | 28 | 32 / 36 |

Touch mode shifts every role up one step on the same ladder. Use weight 600 for emphasis instead of adding sizes.

**Density** (these are proposals, so test them on a real tablet with gloves)

| | Compact | Touch |
|---|---|---|
| Table row height | 32 | 56 |
| Cell padding (x / y) | 12 / 6 | 16 / 16 |
| Min tap target | 32 | 48 |
| Primary action height | 36 | 56 |
| Gap between adjacent targets | 4 | 8 |

**Why not the other two**
- **Dev B (8px, 1.333):** An 8px base has no 4 or 12, and dense tables need those for cell padding and icon gaps. A 1.333 ratio also jumps too far between sizes (16, 21, 28, 38). That leaves no room for a 14px table cell next to 16px body text.
- **Dev C (Tailwind):** Tailwind's spacing is already a 4px base, so C and A agree there. Its default type scale has about 13 sizes with no rationale. Use Tailwind as the tooling, but override the theme with only the values above so nobody can reach for `text-lg` or `p-5`.

**Assumptions:** This is a web product, and density is a mode that switches per device or user setting, not something chosen per component.
