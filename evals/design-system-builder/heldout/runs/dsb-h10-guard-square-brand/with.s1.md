Assumptions: web, one brand, small team, no existing site to inventory. The brand sets the scale sizes here, so some scales are shorter than usual.

## Radius: 1 token, 1 opt-in

| Token | Value | Use |
|---|---|---|
| `radius.none` | `0` | Everything: buttons, inputs, cards, images, tags, menus |
| `radius.full` | `9999px` | Opt-in exception for things that are circular by function (avatar, radio). Drop it if you'd rather make those square too. |

A radius scale exists to give you steps, and this brand has none. Set `radius.none` anyway and have components read it. Then "why is this rounded?" becomes a defect you can find, because a stray `border-radius` no longer looks normal.

## Elevation: rules instead of shadows

Depth comes from border weight, so first define the rule widths:

| Token | Value | Use |
|---|---|---|
| `border.width.thin` | `1px` | Table rows, list dividers |
| `border.width.medium` | `2px` | Controls, cards |
| `border.width.thick` | `4px` | Section rules, page header and footer rules |

Then three elevation levels built from them:

| Token | Recipe | Use |
|---|---|---|
| `elevation.flat` | no border, no shadow | Content on the page |
| `elevation.raised` | `2px solid ink` | Cards, inputs, buttons |
| `elevation.overlay` | `3px solid ink` plus a hard offset block, `4px 4px 0 ink`, zero blur | Menus, dialogs, toasts |

Overlays are the one place I'd go beyond the brief. A menu with only a border blends into a bordered card underneath it. A hard offset block fits the print look (it's a stamped edge, not a soft shadow) and separates the layers. If you want strictly rules only, drop the offset and make overlays `4px` bordered. The cost is weaker separation.

## Motion: 2 durations, 1 easing

| Token | Value | Use |
|---|---|---|
| `duration.instant` | `0ms` | Default. State changes just switch. |
| `duration.fast` | `100ms` | Optional: color change on hover or focus, and nothing else |
| `easing.standard` | `linear` | The only curve. At 100ms, easing is invisible. |

Nothing moves, fades, slides or scales. Hover and press are hard swaps (for example, ink background with paper text), which suits the print look. Under `prefers-reduced-motion`, `duration.fast` resolves to `0ms`. Add a longer duration only when a real component needs it and it passes the second-use rule.

## CSS

```css
:root {
  /* shape */
  --radius-none: 0;
  --radius-full: 9999px;

  /* rules */
  --border-width-thin: 1px;
  --border-width-medium: 2px;
  --border-width-thick: 4px;

  /* elevation (color comes from the semantic ink role) */
  --elevation-flat: none;
  --elevation-raised-border: var(--border-width-medium) solid var(--color-border-strong);
  --elevation-overlay-border: 3px solid var(--color-border-strong);
  --elevation-overlay-shadow: 4px 4px 0 var(--color-border-strong);

  /* motion */
  --duration-instant: 0ms;
  --duration-fast: 100ms;
  --easing-standard: linear;
}

@media (prefers-reduced-motion: reduce) {
  :root { --duration-fast: 0ms; }
}
```

`--color-border-strong` is your ink black. Define it in the color tokens, not here. The tomato red stays out of these tokens, because it's an accent for color and focus, not for depth.

- **Trade-off:** the scales are shorter than the usual 2–4 radii and 3–4 durations. That's deliberate, since the brand is the constraint.
- **Not checked:** I haven't looked at contrast or at a dark theme. If you want one, the overlay offset needs a paper-colored variant.
