Assumptions: a web product, one brand, a small team, and no existing tokens. I haven't contrast-checked anything.

Your brand is mostly a decision to not use these categories. So the scales are deliberately tiny, and the main job is to make "no" the default so it doesn't erode.

## Radius: 1 value, plus 1 functional exception

| Token | Value | Use |
|---|---|---|
| `radius.none` | `0` | Everything: buttons, inputs, cards, images, modals, tags |
| `radius.round` | `50%` | Only where the shape is semantically a circle: radio buttons, status dots, avatars (if you use them) |

Components read `radius.none` through a semantic role (`radius.control`, `radius.surface`). That way, if the brand ever softens, you change two mappings instead of hunting through components.

## Elevation: depth through rules, not blur

Elevation is a combination of border weight and, for overlays only, a hard offset. There are no blurred shadows and no tinted surfaces.

| Token | Border | Offset shadow | Use |
|---|---|---|---|
| `elevation.flat` | none | none | Page, sections, body content |
| `elevation.raised` | `2px solid ink` | none | Cards, inputs, buttons, table frames |
| `elevation.overlay` | `4px solid ink` | `6px 6px 0 0 ink` (0 blur) | Menus, dialogs, toasts |

Supporting border-width scale (3 values): `border.hairline` 1px (table row dividers), `border.rule` 2px, `border.heavy` 4px (section dividers, overlays).

Overlays need the hard offset because a thick border on top of another thick border doesn't read as "above". The offset is the one print-style shadow I'd allow. If you want zero shadows, use `overlay` = 4px border plus a page scrim in `ink` at 60% opacity instead.

## Motion: nearly none

| Token | Value | Use |
|---|---|---|
| `motion.duration.instant` | `0ms` | Default. Focus rings, menus opening, dialogs, route changes, disclosure |
| `motion.duration.fast` | `100ms` | Hover and pressed color flips on controls |
| `motion.easing.standard` | `linear` | The only easing; at 100ms nothing else is visible |

That's two durations and one easing, which is below the usual three or four. It's intentional, and adding a third duration should need a reason.

Rules to document with the tokens:
- Transition `color`, `background-color` and `border-color` only. Never transform, opacity, size or position.
- No entrance, scroll or parallax animation, and no skeleton shimmer. Use static placeholder blocks.
- Under `prefers-reduced-motion: reduce`, `fast` remaps to `0ms`. The semantic layer handles this, so components don't need to.

## CSS

```css
:root {
  /* raw */
  --radius-0: 0;
  --radius-circle: 50%;
  --border-1: 1px; --border-2: 2px; --border-4: 4px;
  --duration-0: 0ms; --duration-100: 100ms;

  /* semantic */
  --radius-control: var(--radius-0);
  --radius-surface: var(--radius-0);
  --radius-indicator: var(--radius-circle);

  --elevation-flat: none;
  --elevation-raised-border: var(--border-2) solid var(--color-ink);
  --elevation-overlay-border: var(--border-4) solid var(--color-ink);
  --elevation-overlay-shadow: 6px 6px 0 0 var(--color-ink);

  --motion-duration-instant: var(--duration-0);
  --motion-duration-fast: var(--duration-100);
  --motion-easing-standard: linear;
}

@media (prefers-reduced-motion: reduce) {
  :root { --motion-duration-fast: var(--duration-0); }
}
```

`--color-ink` comes from your color tokens. Tomato red stays out of these categories: it's an accent color, not a depth cue, so don't use it for borders on elevated surfaces.

## Two things to settle

1. **Focus indicator:** I'd make it a 4px tomato (or ink) outline with a 2px offset, appearing instantly. That belongs in the component specs, but the border-width scale above already covers it.
2. **Dark theme:** if you ever add one, `ink` and `paper` swap through the semantic layer. The overlay offset then needs to use the light value, or it disappears.
