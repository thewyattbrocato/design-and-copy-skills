**Pick: Dev A's 4px spacing base, with a type ratio of about 1.2 applied to a short set of roles. Don't use Dev B's 1.333.**

**Why not the others**
- **8px base (B):** Dense tables need 4, 12 and 20px steps. An 8px grid forces you to pick 8 or 16, so rows end up too loose or too tight. You'd end up adding half-steps later anyway.
- **1.333 ratio (B):** Each step is 33% larger. From a 14px body size you get 14, 19, 25, 33, and the jump from body to the next size is too big for table headers and labels. It suits marketing pages, not tools.
- **Tailwind defaults (C):** The spacing is a 4px base, so that part already agrees with A. The type sizes (12, 14, 16, 18, 20, 24, …) aren't a ratio, and nothing is tuned for gloved touch targets. Take Tailwind's 4px spacing as a starting point, but define your own tokens and don't inherit the whole preset.

**Spacing (4px base, 10 steps)**

| Token | px |
|---|---|
| space-1 | 4 |
| space-2 | 8 |
| space-3 | 12 |
| space-4 | 16 |
| space-5 | 24 |
| space-6 | 32 |
| space-7 | 48 |
| space-8 | 64 |
| space-9 | 96 |
| space-10 | 128 |

**Type (1.2 ratio, 6 roles, rounded to whole pixels)**

| Role | Size / line height | Notes |
|---|---|---|
| caption | 12 / 16 | Metadata only. Not used for anything a gloved user must read. |
| body-sm | 14 / 20 | Dense tables on desktop |
| body | 16 / 24 | Default, and the tablet table size |
| subhead | 19 / 28 | |
| title | 23 / 32 | |
| display | 28 / 36 | Counts and totals, scan values |

**Density modes.** This is how one scale serves both devices:
- **Compact (desktop):** table rows are 32px tall (`space-6`), cell padding is 8×12 (`space-2` and `space-3`), and body text is 14px.
- **Comfortable (tablet):** the minimum touch target is 48px (`space-7`), at least 8px apart. Rows are 56px (the 48px step plus `space-2` of padding). Body text is 16px, and the primary action buttons are 56px tall.

Switch density with a token remap (`row-height`, `cell-padding`, `body-size` point to different steps). Don't build two scales.

**Two caveats**
- 48px is a common minimum target size. Gloved use often needs more, so check 56px against real gloves on your tablets before you lock the comfortable-mode values.
- The type sizes are proposals, not measured on your hardware. Check legibility at arm's length on the actual tablets.
