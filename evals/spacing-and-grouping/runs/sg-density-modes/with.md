# Compact vs. comfortable spacing

## Principle

Change the size of the spacing steps. Keep the structure and the within/between ratio. In both modes the gap between groups should stay at about 2× the gap inside a group, so groups still read in compact mode. If you shrink every value by the same amount, groups merge. Compact mode should come from tighter space, not smaller type.

## What stays the same
- Items, order, and grouping are identical in both modes.
- Body and table text is 13–14 px in both. Compact mode doesn't shrink type.
- Numbers stay right-aligned and column edges stay put.
- Focus rings and hover states stay visible and aren't clipped by the smaller padding.

## Scale (4 px base)

| Token | Compact | Comfortable | Use |
|---|---|---|---|
| `--space-1` | 2 | 4 | icon to label, chips |
| `--space-2` | 4 | 8 | label to field, items in a small group |
| `--space-3` | 8 | 12 | related rows, cell padding |
| `--space-4` | 12 | 16 | default padding, gap between fields |
| `--space-5` | 16 | 24 | between groups, panel padding |
| `--space-6` | 24 | 32 | between larger groups |
| `--space-7` | 32 | 48 | between sections |

Compact mode is about one step tighter than comfortable. The relationships hold: inside a group it's 4 against 12 between groups (compact), and 8 against 24 (comfortable).

## Component values

| Element | Compact | Comfortable |
|---|---|---|
| Table row height | 28 px (6 px vertical padding) | 44–48 px (12–14 px vertical padding) |
| Cell horizontal padding | 8 px | 16 px |
| Control height (inputs, buttons, selects) | 28–30 px | 36–40 px |
| Button padding (vertical / horizontal) | 4 / 10 px | 8 / 16 px |
| Toolbar and filter bar height | 36–40 px | 56 px |
| Gap between filters or toolbar controls | 8 px | 12–16 px |
| Chart card or panel padding | 12–16 px | 24 px |
| Gap between panels on a dashboard | 12–16 px | 24 px |
| Section gap | 24–32 px | 48 px |
| Page margin | 16–24 px | 32–48 px |
| Sidebar nav item height | 28 px | 40 px |

Row height and control height matter most. At 1280×800, 28 px rows fit about 25 rows with a header and filters. 48 px rows fit about 12–14.

## Things that need more care in compact mode
- **Row separation.** Tight rows need a 1 px hairline or light zebra banding. Space alone stops working below about 32 px rows. Use the same rule weight and a quiet color in both modes.
- **Panel gap vs. padding.** The gap between panels should be at least the panel padding, so cards don't blur together. That's 12–16 against 12–16 in compact mode, and 24 against 24 in comfortable mode.
- **Touch.** Compact mode is for pointer use. On touch devices (`@media (pointer: coarse)`) or narrow viewports, force comfortable values. Targets should be 44 px or larger with about 8 px between neighbors.
- **Chart interactions.** Keep hit areas for hover and click on chart points and legend items at 24 px or larger, even if the visible marks are small.

## Implementation

Define the steps once and let the mode change what they map to. Components read tokens, never literals.

```css
:root {
  --space-1: 0.25rem; --space-2: 0.5rem;  --space-3: 0.75rem;
  --space-4: 1rem;    --space-5: 1.5rem;  --space-6: 2rem; --space-7: 3rem;

  --row-h: 2.75rem;      /* 44 */
  --control-h: 2.25rem;  /* 36 */
  --cell-px: var(--space-4);
  --panel-pad: var(--space-5);
  --panel-gap: var(--space-5);
  --section-gap: var(--space-7);
}

[data-density="compact"] {
  --space-1: 0.125rem; --space-2: 0.25rem; --space-3: 0.5rem;
  --space-4: 0.75rem;  --space-5: 1rem;    --space-6: 1.5rem; --space-7: 2rem;

  --row-h: 1.75rem;      /* 28 */
  --control-h: 1.75rem;  /* 28 */
  --cell-px: var(--space-3);
  --panel-pad: var(--space-4);
  --panel-gap: var(--space-4);
  --section-gap: var(--space-6);
}

@media (pointer: coarse) {
  [data-density="compact"] { /* restore comfortable touch values */ }
}
```

- Put `data-density` on `<html>` or the app root. Persist it per user in `localStorage` or the user profile. Set it before first paint to avoid a layout flash.
- Let parents own the gaps (`display: grid; gap: var(--panel-gap)`). Don't put margins on children.
- Use `rem` for spacing so it follows the user's text size. Use px for hairlines.

## Defaults and rollout
- Default to **comfortable**. Once-a-week users shouldn't have to find a setting, and power users will switch.
- Put the toggle in a visible place, such as the user menu or table toolbar. Don't bury it in settings.
- You could also apply compact to data tables only, and keep comfortable chrome around them. That's a cheaper first version if the full token swap is too big.

## QA
1. Test compact with a full table of real data, not three rows.
2. Squint at both modes. The same groups should be visible in each.
3. Grep for hard-coded `px` margins and paddings that bypass the tokens. These will stay at comfortable values in compact mode.
4. Check focus rings on 28 px controls to make sure nothing clips them.
