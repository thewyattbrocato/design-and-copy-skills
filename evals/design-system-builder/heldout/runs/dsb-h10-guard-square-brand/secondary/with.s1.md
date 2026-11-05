Here's the shape, depth and motion set. Depth is carried by black rules, not shadows, so the elevation tokens are border weights.

## Radius

```css
--radius-none: 0;
```

One value. Everything is square, so there's no scale to tune. If a control ever needs a circle (a radio dot, an avatar), add it as a marked exception rather than a token.

## Elevation (rule weight)

```css
--color-ink: #141414;          /* proposed, not contrast-checked */

--elevation-flat: 0;           /* page, inline blocks, body surfaces */
--elevation-raised: 2px;       /* cards, product tiles, callouts */
--elevation-overlay: 4px;      /* menus, dialogs, anything that sits above the page */
```

Usage: `border: var(--elevation-raised) solid var(--color-ink);`

- Three tiers, each about double the last, so they read as different without needing a fourth.
- No `box-shadow` tokens. A raised surface gets its rule, and an overlay gets a heavier rule plus a surface color change if it needs to stand apart.
- If you need a hairline for table or list dividers, that's a separate `--rule-hairline: 1px` and should be justified, since it's a fourth weight.

## Motion

```css
--motion-duration-none: 0ms;     /* default for everything */
--motion-duration-short: 120ms;  /* hover, focus, pressed state change */
--motion-duration-medium: 240ms; /* disclosure, dialog open/close */

--motion-ease-out: cubic-bezier(0.2, 0, 0, 1);
--motion-ease-linear: linear;
```

Rules:

- Default is `none`. Motion has to earn its duration.
- Only state changes and overlays get `short` or `medium`. No motion on page load, scroll, or decorative loops.
- No bounce, spring, or parallax. Those aren't tokens.
- `prefers-reduced-motion` sets every duration to `0ms`. For this brand that's close to the default anyway, so it costs almost nothing.

## Checks

- Radius: one value, no neighbors to confuse.
- Elevation: three tiers, 2px and 4px are clearly different.
- Motion: three durations and two easings, all within the scale ranges.
- None of these tokens reference raw colors except `--color-ink`, which the components should read through a semantic role such as `color.border.default`.

**Assumption:** I'm treating the print material's black as the same ink used for web rules. **Trade-off:** pure zero-radius and zero-shadow is distinctive but makes dense interfaces (long forms, data tables) harder to scan. Watch for that when specifying those components.
