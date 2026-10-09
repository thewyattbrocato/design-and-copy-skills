# Compact vs. comfortable spacing

## Approach

Drive both modes from one density token set on a root attribute (`data-density="compact|comfortable"`). Components read CSS variables and never branch on mode. Keep a 4px base grid in both modes, so only the multipliers change.

Compact is not "comfortable scaled down." Reduce vertical spacing a lot, horizontal spacing a little, and leave type size and touch targets mostly alone. Power users want more rows on screen, not smaller text.

## Tokens

| Token | Compact | Comfortable | Notes |
|---|---|---|---|
| `--space-1` (hairline gaps, icon-to-label) | 2px | 4px | |
| `--space-2` (inline gaps, chip padding) | 4px | 8px | |
| `--space-3` (control internal padding) | 8px | 12px | |
| `--space-4` (between related elements) | 12px | 16px | |
| `--space-5` (card padding) | 12px | 24px | |
| `--space-6` (between sections) | 16px | 32px | |
| `--row-height` (tables, lists) | 28px | 44px | |
| `--control-height` (buttons, inputs, selects) | 28px | 40px | |
| `--table-cell-pad-x` | 8px | 16px | |
| `--table-cell-pad-y` | 4px | 12px | |
| `--page-gutter` | 16px | 32px | |
| `--sidebar-item-height` | 28px | 40px | |
| `--chart-padding` (inside plot area) | 8px | 16px | |
| `--card-gap` (dashboard grid) | 12px | 24px | |

## Rules

- **Type:** Body text stays at 13px in compact and 14px in comfortable. Don't go below 12px for any data text. Line-height is 1.35 compact and 1.5 comfortable. Row height should come from padding plus line-height, not a fixed pixel height, so text scaling still works.
- **Horizontal vs. vertical:** Compact cuts vertical spacing by about 50–60% and horizontal by about 30–50%. Columns need breathing room to stay scannable, especially with right-aligned numbers.
- **Tables:** This is where the modes matter most. At 28px rows, compact fits about 1.5× the rows of comfortable at 44px. Keep zebra striping or a 1px row divider in compact, since tight rows need a visual guide. Comfortable can rely on whitespace alone.
- **Charts:** Reduce the padding around the plot and between chart and legend (8px vs. 16px). Don't shrink tick labels or data marks. Hit targets for tooltips stay the same size; only the whitespace around them changes.
- **Dashboard grid:** Use a 12px gap in compact and 24px in comfortable. Card padding follows the same ratio. Compact cards can drop the header divider and put the title and actions on one 28px line.
- **Toolbars and filters:** In compact, collapse filter bars to a single row and show icon + label only for the primary actions. Comfortable can wrap filters and show labels everywhere.
- **Hit targets:** Compact controls can be 28px tall because the users are mouse-driven. Keep a minimum 24×24px target, and expand the clickable area with pseudo-element padding where the visuals are smaller. On touch devices, force comfortable regardless of the setting.
- **Focus rings:** Same 2px ring with 1px offset in both modes. Don't shrink it in compact.

## Implementation

```css
:root,
[data-density="comfortable"] {
  --space-1: 4px;  --space-2: 8px;  --space-3: 12px;
  --space-4: 16px; --space-5: 24px; --space-6: 32px;
  --row-height: 44px;     --control-height: 40px;
  --font-body: 14px;      --line-body: 1.5;
}
[data-density="compact"] {
  --space-1: 2px;  --space-2: 4px;  --space-3: 8px;
  --space-4: 12px; --space-5: 12px; --space-6: 16px;
  --row-height: 28px;     --control-height: 28px;
  --font-body: 13px;      --line-body: 1.35;
}
```

- **Default and persistence:** Default new users to comfortable. Store the choice per user (server-side, with localStorage as a cache) and apply it before first paint to avoid layout shift.
- **Toggle:** Put it in user settings and as a quick toggle in the table toolbar. Optionally offer "auto" that suggests compact after a user hits some usage threshold, but don't switch it on them silently.
- **Virtualized tables:** Row height must come from the token. Read it once via `getComputedStyle` and recompute the virtualizer's size when density changes.
- **Components with hardcoded pixel values:** Audit for these first. They are the usual reason a density mode looks half-applied.
- **Testing:** Add visual regression snapshots for both modes on the table, a card with a chart, and a form. Check that no text truncates differently between modes beyond what the tighter padding explains.
