Keep these tokens few and literal. The brand is flat, so most of the scale is zero, and the depth and motion tokens should describe hard edges and short, plain transitions.

**Shape (radius)**

```css
--radius-none: 0;      /* default for everything: buttons, cards, inputs, images, tags */
--radius-round: 50%;   /* only for true circles, such as a status dot or avatar, if you need one */
```

Don't add `--radius-sm/md/lg`. If you later need a soft radius, it will be a deliberate exception, and a named token makes that visible.

**Depth (elevation)**

Use borders and hard offsets instead of blur. Nothing should have a blurred shadow.

```css
--ink: #111;            /* the thick black rule color */
--paper: #F4F1EA;       /* off-white background, adjust to taste */
--accent: #FF6347;      /* tomato red, the single loud color */

--border-rule: 2px solid var(--ink);   /* standard panel, card, input edge */
--border-heavy: 4px solid var(--ink);  /* emphasis, masthead, featured book */

--elevation-0: none;                             /* flat, sits on the paper */
--elevation-1: 4px 4px 0 0 var(--ink);           /* raised card or button, hard offset */
--elevation-2: 8px 8px 0 0 var(--ink);           /* overlay, menu, modal */
--elevation-pressed: 0 0 0 0 var(--ink);         /* pressed state: shadow collapses, element moves into it */
```

Also define a z-index scale (`--z-base`, `--z-raised`, `--z-overlay`, `--z-modal`). That is layering, not depth, but it usually goes in the same file.

**Motion (animation)**

Keep it to a few tokens and make reduced motion the default behavior.

```css
--duration-instant: 0ms;
--duration-fast: 100ms;    /* hover and press feedback */
--duration-base: 160ms;    /* menus, drawers, color changes */

--ease-standard: cubic-bezier(0.2, 0, 0, 1);  /* plain ease-out, no overshoot */
--ease-linear: linear;

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast: 0ms;
    --duration-base: 0ms;
  }
}
```

Rules to write down next to the tokens:

- No bounce, spring, or overshoot easing.
- Animate only color, the offset in `--elevation-*`, and opacity. Avoid animating layout.
- The hover and press pattern is the main interaction: on hover, step the elevation or color; on press, go to `--elevation-pressed` and translate by the same offset. This gives the tactile, blunt feel without decorative motion.
- Anything that moves more than a few pixels should be justified, since most of the site should not move at all.

The answer depends on a few brand decisions. Confirm whether the focus ring should be a thick accent outline (I'd suggest `--border-heavy` in `--accent`, not a soft glow), and whether the offset shadow should be solid black or the accent color. I'd keep it black, because the accent is reserved for one thing per screen.
