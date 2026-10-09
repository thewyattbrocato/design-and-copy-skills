I'm assuming a web product with one brand and a small team. The brand is so flat that these three scales come out much shorter than the usual 2–4 steps.

## Radius

| Token | Value | Use |
|---|---|---|
| `radius.none` | `0` | Everything: buttons, inputs, cards, images, tags, modals |
| `radius.round` | `50%` | Only where the shape is semantically round: radio buttons and avatars, if you have them |

Don't add `sm/md/lg`. A mid-size radius would break the brand, and one missing step isn't worth a scale. If nobody has radios or avatars yet, ship only `radius.none`.

## Elevation (depth by rule, not shadow)

Depth comes from border weight and a scrim, with no blur anywhere. First define the rule weights:

| Token | Value | Use |
|---|---|---|
| `border.width.rule` | `2px` | Default outline for inputs, cards and dividers |
| `border.width.heavy` | `4px` | Section breaks, overlays, emphasis |

Then the elevation roles, which components read:

| Token | Treatment | Use |
|---|---|---|
| `elevation.flat` | No border, no shadow | Content on the page |
| `elevation.raised` | `rule` width, `color.border.strong` (black) | Cards, inputs, menus |
| `elevation.overlay` | `heavy` width, black, plus `color.scrim` behind | Modals, drawers, popovers |

Three levels is enough. Tomato never carries depth. It stays an accent (`color.accent`) and is not an elevation color.

## Motion

| Token | Value | Use |
|---|---|---|
| `motion.duration.none` | `0ms` | Default. Layout, reveals, page changes: no animation |
| `motion.duration.fast` | `100ms` | Hover and pressed color or fill changes only |
| `motion.easing.standard` | `linear` | The only easing |

I used two durations and one easing instead of the usual 3–4 and 3, because the brand is "basically no animation". There is no entrance, slide, fade or scale token on purpose. Anyone who needs one has to argue for it as a new addition.

Under `prefers-reduced-motion: reduce`, remap `fast` to `0ms`. Themes and preferences change what a role points to, not the component.

## CSS

```css
:root {
  /* shape */
  --radius-none: 0;
  --radius-round: 50%;

  /* depth */
  --border-width-rule: 2px;
  --border-width-heavy: 4px;
  --elevation-flat: none;
  --elevation-raised: var(--border-width-rule) solid var(--color-border-strong);
  --elevation-overlay: var(--border-width-heavy) solid var(--color-border-strong);

  /* motion */
  --motion-duration-none: 0ms;
  --motion-duration-fast: 100ms;
  --motion-easing-standard: linear;
}

@media (prefers-reduced-motion: reduce) {
  :root { --motion-duration-fast: 0ms; }
}
```

Elevation is a border shorthand, so use it as `border: var(--elevation-raised)`. Don't mix it with `box-shadow`, and lint for `box-shadow` and `border-radius` values other than these tokens.

**Notes**
- These tokens depend on `color.border.strong` (black), `color.scrim` and `color.accent` (tomato) existing in your color roles. I haven't defined or contrast-checked those here.
- Thick rules add layout size. Decide whether components use `box-sizing: border-box` so a 4px overlay border doesn't shift spacing.
