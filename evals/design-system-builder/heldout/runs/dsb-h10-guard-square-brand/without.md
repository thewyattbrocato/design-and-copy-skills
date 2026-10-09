# Boxcar Press shape, depth and motion tokens

The brand is flat, so these token sets should be small. A token that's always `0` still earns its place, because it gives you one place to change it and stops anyone from adding a rounded corner later.

## Radius

```css
--radius-none: 0;      /* default for everything */
--radius-round: 50%;   /* only for things that are circular by nature */
```

- Define `--radius-none` and use it on every component: buttons, inputs, cards, tags, modals, images.
- Don't build a sm/md/lg scale. Its absence tells people not to round things.
- `--radius-round` is only for radio buttons, and avatars if you have any. If you don't need those, leave it out.
- Don't add a pill radius.

## Elevation

With no soft shadows, depth comes from rule weight and layering. Define border widths as the elevation scale:

```css
--rule-thin: 1px;     /* table rows, dividers inside a component */
--rule-medium: 2px;   /* inputs, default card outline */
--rule-thick: 4px;    /* section breaks, emphasized or featured blocks */
--rule-color: #000;

--elevation-0: none;                                   /* flat on paper */
--elevation-1: var(--rule-medium) solid var(--rule-color);
--elevation-2: var(--rule-thick) solid var(--rule-color);
```

- Use `border` or `outline` for these. Don't use `box-shadow` for the rules.
- Overlays (modals, menus, popovers) are the one place where a rule alone may not separate a layer from the page. I'd allow one optional token:

  ```css
  --shadow-hard: 6px 6px 0 #000;  /* zero blur, overlays only */
  ```

  This is a hard offset print-style shadow, which still reads as flat. If you want to stay strict, skip it and give overlays a `--rule-thick` border on a paper background, plus a solid black scrim behind modals.
- Don't define blur-based shadows, glows, or translucent or backdrop-blur layers.
- Focus rings should be a thick, square outline in the accent red, for example `3px solid tomato` with a 2px offset. This is an elevation-adjacent decision and it needs to be loud and visible.

## Motion

"Basically no animation" still needs a few tokens, so any motion that does exist stays consistent:

```css
--duration-instant: 0ms;     /* default: state changes just happen */
--duration-fast: 100ms;      /* optional: color or invert on hover/press */
--easing-linear: linear;     /* the only easing */

@media (prefers-reduced-motion: reduce) {
  :root { --duration-fast: 0ms; }
}
```

- The default is no transition. Hover, active and selected states snap to the new state, for example by inverting black on paper to paper on black, or switching to tomato.
- Allow `--duration-fast` only for color or background changes, and use linear easing only.
- Don't define spring or ease-in-out curves, or any slide, fade, scale or parallax tokens. Don't define transform or position animation.
- Page transitions and scroll effects should be left out of the system entirely.

## Decisions for you

1. **Hard shadow for overlays:** allow it, or use rules only?
2. **100ms color transition:** keep it, or make everything strictly instant? Instant fits the brand better, and the fast token just gives you an escape hatch.
3. **Pressed-button feedback:** I'd use a snap inversion, with no translate-down effect.

I can write these out as a tokens file in your format (CSS variables, Tailwind config, or Style Dictionary JSON) if you tell me which one you're using.
