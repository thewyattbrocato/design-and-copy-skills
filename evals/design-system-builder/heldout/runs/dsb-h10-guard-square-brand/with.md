Your brand uses very few values here, so the sets below are deliberately small and well under the usual scale sizes.

## Radius: 1 token

| Token | Value |
|---|---|
| `radius.none` | `0` |

Every component reads this one token, so a rounded corner can't appear by accident. If you ever soften the brand, you change one value. I'd leave out `sm`, `md` and `lg`. Unused scale steps invite exceptions.

## Elevation: 3 levels, built from rules instead of shadows

Depth comes from rule weight, not blur. First define the rule widths:

| Token | Value | Use |
|---|---|---|
| `border.width.thin` | `1px` | Table rows, list dividers |
| `border.width.medium` | `2px` | Inputs, cards, buttons |
| `border.width.thick` | `4px` | Section rules, overlays, masthead |

Then the elevation roles. Components use these, not the raw widths:

| Token | Value | Use |
|---|---|---|
| `elevation.flat` | no border, no shadow | Content on the page |
| `elevation.raised` | `2px` solid ink | Cards, inputs, buttons |
| `elevation.overlay` | `4px` solid ink | Menus, dialogs, toasts |

- **Overlays:** A thick rule over off-white may not separate an overlay from busy content behind it. If it doesn't, add one hard offset shadow, `4px 4px 0 ink`, with zero blur, to `elevation.overlay` only. That is a proposal. I'd test it on a real page first.
- **Scrim:** If dialogs need one, use a solid ink at about 60% opacity, not a blur.
- **Focus:** Use a `3px` ink outline with a `2px` offset, so it stays visible against the tomato accent. Don't use tomato for focus.

## Motion: 2 durations, 1 easing

| Token | Value | Use |
|---|---|---|
| `duration.instant` | `0ms` | The default. Hover, press and selection are hard cuts. |
| `duration.fast` | `120ms` | Only for things that appear or disappear: menus, dialogs, toasts, disclosure. |
| `easing.standard` | `cubic-bezier(0, 0, 0.2, 1)` | Used with `fast`. |

- **Rules:** Animate opacity only. Don't animate position, scale or size. No springs, no bounce, no page-load choreography.
- **Reduced motion:** `prefers-reduced-motion: reduce` sets `duration.fast` to `0ms`. Nothing else needs to change, because the default is already no motion.

## CSS

```css
:root {
  /* raw */
  --rule-1: 1px;
  --rule-2: 2px;
  --rule-4: 4px;

  /* semantic: components read these */
  --radius-none: 0;
  --border-width-thin: var(--rule-1);
  --border-width-medium: var(--rule-2);
  --border-width-thick: var(--rule-4);

  --elevation-flat: none;
  --elevation-raised: var(--border-width-medium) solid var(--color-border-strong);
  --elevation-overlay: var(--border-width-thick) solid var(--color-border-strong);

  --focus-ring: 3px solid var(--color-border-strong);
  --focus-offset: 2px;

  --duration-instant: 0ms;
  --duration-fast: 120ms;
  --easing-standard: cubic-bezier(0, 0, 0.2, 1);
}

@media (prefers-reduced-motion: reduce) {
  :root { --duration-fast: 0ms; }
}
```

`--color-border-strong` is your ink black. It belongs to the color tokens, not this set.

## Decisions for you

- **Circles:** Radio buttons and avatars are the one place "square everywhere" gets tested. I'd keep radios square-ish too, such as a filled square, and make any circle a named exception, not a second radius token.
- **Dark theme:** If you add one, the rules remap to the light ink. Elevation tokens keep their names and widths.

I assumed a web product with one brand and a small team. I haven't contrast-checked anything, because these tokens don't set any colors.
