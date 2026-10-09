I assumed a web product, one brand and a small team. I haven't checked any colors for contrast. These three scales are deliberately shorter than the usual ranges, because the brand has little depth or motion to express.

## Shape

| Token | Value | Use |
|---|---|---|
| `radius.none` | `0` | Every surface, control, image, tag, and focus ring. |

- Define one token, not a scale. Components still reference it, so a future change happens in one place.
- Round things such as radio buttons and status dots are the only exceptions. Keep them local and marked as exceptions, not as a `radius.full` token.

## Depth

Depth comes from rule weight and hard offsets, never blur.

| Token | Value | Use |
|---|---|---|
| `border.width.thin` | `1px` | Table rows, dividers inside a panel. |
| `border.width.base` | `2px` | Default outline for cards, inputs, and buttons. |
| `border.width.heavy` | `4px` | Section rules, masthead, and emphasis. |
| `elevation.flat` | `none` | The page and most content. |
| `elevation.raised` | `border.width.base` solid `color.border.strong` | Cards and inputs. |
| `elevation.overlay` | `raised` plus `4px 4px 0 0 color.border.strong` | Menus, dialogs, and toasts. |

- **Hard shadow:** the zero-blur offset on `elevation.overlay` is a proposal. It is the only "shadow" in the system. If you want no shadows at all, make overlay a `heavy` border on a paper ground.
- **Focus:** use a 3px `color.border.strong` outline with a 2px offset, so it is visible on both paper and tomato. Don't rely on the accent for focus until you've checked its contrast.

## Motion

| Token | Value | Use |
|---|---|---|
| `motion.duration.none` | `0ms` | Default for hover and pressed (hard color flips). |
| `motion.duration.fast` | `100ms` | Focus, disclosure toggles, and input state changes. |
| `motion.duration.base` | `200ms` | Menus, dialogs, and toasts appearing. |
| `motion.easing.standard` | `cubic-bezier(0, 0, 0.2, 1)` | The only easing. |

- Animate only `color`, `background-color`, and `opacity`. Nothing slides, scales, bounces, or parallaxes.
- No loops or decorative motion. A loading state is static text or a stepped indicator.
- Under `prefers-reduced-motion: reduce`, every duration becomes `0ms`.
- There is no `slow` duration and no second easing. Asking for one is a sign the brand is drifting.

## CSS

```css
:root {
  --radius-none: 0;

  --border-width-thin: 1px;
  --border-width-base: 2px;
  --border-width-heavy: 4px;

  --elevation-flat: none;
  --elevation-raised: 0 0 0 var(--border-width-base) var(--color-border-strong);
  --elevation-overlay: var(--elevation-raised), 4px 4px 0 0 var(--color-border-strong);

  --motion-duration-none: 0ms;
  --motion-duration-fast: 100ms;
  --motion-duration-base: 200ms;
  --motion-easing-standard: cubic-bezier(0, 0, 0.2, 1);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-duration-fast: 0ms;
    --motion-duration-base: 0ms;
  }
}
```

`--color-border-strong` is a semantic color role (black) that your color tokens need to define. Components read these tokens and never raw values like `2px` or `#000`.
