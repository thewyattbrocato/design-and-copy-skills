For a flat, blunt brand, the shape, depth, and motion systems should be small. Most tokens should resolve to zero or near-zero, so the real content is the few rules about what's allowed.

## Shape

Define one radius scale step, plus an explicit exception for circles.

```css
--radius-none: 0;      /* default for everything: buttons, cards, inputs, images, tags */
--radius-round: 50%;   /* exception: avatars, radio dots, status pips only */
```

Don't define `radius-sm`, `radius-md`, and so on. Those invite soft corners back in.

## Depth (elevation)

Use hard, offset, solid shadows with no blur, or use no shadow at all. Use the ink color so the depth reads as a printed rule, not a glow.

```css
--ink: #111;                        /* same value as your rule/text black */

--elevation-0: none;                /* default */
--elevation-1: 0 4px 0 var(--ink);  /* raised: card or button at rest, if needed */
--elevation-2: 0 8px 0 var(--ink);  /* overlays: menus, dialogs */

--z-base: 0;
--z-sticky: 100;
--z-overlay: 200;
--z-modal: 300;
```

The rules that go with these:

- **No blur shadows, ever.** Keep `blur` at 0 and `spread` at 0 in all shadow tokens.
- **Pressed state** is a `translate(4px, 4px)` with the shadow removed, so the element appears to press into the page. It can be instant.
- **Hover** swaps color (for example, to the tomato accent or inverts the rule color), not elevation.
- **Structure comes from thick rules** (`--rule-thick: 3px solid var(--ink)`) and `--rule-thin: 1px solid var(--ink)`, not shadows. Put these in the depth set because they do the separation work.

## Motion

Keep durations short and the list of allowed effects tiny.

```css
--duration-instant: 0ms;
--duration-fast: 80ms;     /* hover color swap, pressed state */
--duration-base: 120ms;    /* the longest transition you should use */

--ease-standard: cubic-bezier(0.2, 0, 0, 1);
--ease-snap: steps(2, end); /* optional: a stepped, print-like change for toggles */
```

Rules for motion:

- **Animate only `color`, `background-color`, and `transform`.** Don't animate layout, size, or blur.
- **Cap at 120ms** for UI feedback. Anything longer needs a specific reason in the spec.
- **No looping, no entrance animations, no parallax, no scroll-linked effects.**
- **Respect `prefers-reduced-motion`** by setting all durations to `0ms` in a media query. With this little motion, the cost is nearly zero.

```css
@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast: 0ms;
    --duration-base: 0ms;
  }
}
```

## What to document with the tokens

Write the reasons next to the values, because the restrictions are the point. A short line like "no blur shadows: brand is printed-rule flat" stops a future contributor from adding a soft shadow "just for this one card."

If you want, I can write these into your design-system token files and add a lint rule that flags `border-radius` values other than 0 or 50%, and `box-shadow` values containing blur. Let me know where the tokens live (I don't see a repo in the current directory).
