**Decision: 4px spacing base, with a hand-picked integer type scale instead of a ratio.** This is closest to Dev A's base and borrows Dev C's Tailwind-style spacing names. Dev B's 8px base is too coarse for dense tables, and neither ratio gives usable sizes.

**Why not the ratios:** A 1.2 or 1.333 ratio produces fractional pixel sizes (for example, 14 × 1.2 = 16.8, 16.8 × 1.2 = 20.16), which render blurry or uneven. Dense tables and gloved tablets need specific sizes, not mathematically derived ones. Tailwind's type scale is also hand-picked, not a ratio, so Dev C's suggestion doesn't settle it.

**Spacing tokens (px, 4px base, rem-based in CSS so OS text scaling still works):**

| Token | Value | Typical use |
|---|---|---|
| space-0 | 0 | |
| space-1 | 4 | Icon gaps, dense cell padding (Y) |
| space-2 | 8 | Dense cell padding (X), inline gaps |
| space-3 | 12 | Compact control padding |
| space-4 | 16 | Default card and section padding |
| space-5 | 20 | |
| space-6 | 24 | Section gaps |
| space-8 | 32 | Page margins (desktop) |
| space-10 | 40 | |
| space-12 | 48 | Page margins (tablet) |
| space-14 | 56 | Tablet control gaps |
| space-16 | 64 | |

**Type scale (px / line-height):**

| Token | Size / LH | Use |
|---|---|---|
| text-xs | 12 / 16 | Metadata, column captions (desktop only) |
| text-sm | 14 / 20 | Desktop table body, dense forms |
| text-base | 16 / 24 | Default UI text (desktop) |
| text-lg | 18 / 24 | **Tablet body and table text** |
| text-xl | 20 / 28 | Section headings |
| text-2xl | 24 / 32 | Page titles |
| text-3xl | 30 / 36 | Rare, large numeric KPIs |

Use `font-variant-numeric: tabular-nums` for quantities, SKUs, and prices so columns align.

**Density and touch targets:**

- Desktop table rows: **32px** compact, **40px** default. Cell padding is space-1 vertically and space-2 horizontally.
- Tablet (gloved): **56px minimum** control height. Primary actions are 64px. Table rows are 56px. Use text-lg for body text.
- Interactive hit areas can extend past the visual control with padding, but never go under 48px on tablet.

**Implementation:** Put these as tokens (`--space-1: 0.25rem;` and so on). Switch density with a `data-density="tablet|desktop"` attribute on the root that remaps row height, control height, and table text, so components don't branch on device.

Caveat: I picked these from the constraints you gave (gloves, dense tables, 10" screens) and general touch and typography guidance, not from measured testing. Check the 56px tablet target and the 14px desktop table text with real users on a warehouse tablet before locking them in.
