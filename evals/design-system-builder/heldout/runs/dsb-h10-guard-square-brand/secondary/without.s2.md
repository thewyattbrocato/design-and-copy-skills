Here's a token set that fits the brand. Depth comes from rule weight and stacking order, not blur. Motion is short and mechanical.

```css
:root {
  /* Shape */
  --radius-none: 0;            /* the only radius. Add nothing else. */

  /* Rules: borders carry the weight that shadows usually would */
  --rule-hairline: 1px;        /* table rows, footers, dividers */
  --rule-standard: 2px;        /* inputs, buttons, cards */
  --rule-heavy: 4px;           /* header bar, dialog edges */
  --ink: #111111;
  --paper: #F4F1EA;
  --accent: #E8442E;           /* tomato placeholder, tune against paper */

  /* Elevation: stacking order, plus one hard offset for floating surfaces */
  --elevation-0: none;
  --elevation-float: 6px 6px 0 0 var(--ink);   /* menus, popovers, dialogs only */
  --z-base: 0;
  --z-raised: 10;
  --z-overlay: 100;
  --z-modal: 1000;

  /* Motion: state feedback only */
  --duration-instant: 0ms;
  --duration-fast: 120ms;
  --duration-base: 200ms;      /* ceiling. Nothing longer. */
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast: 0ms;
    --duration-base: 0ms;
  }
}
```

**Rules for using them:**

- **Radius:** `--radius-none` is the only radius. If something needs a circle (avatars), make it a named exception token so it's visible in review, not an ad-hoc `border-radius: 50%`.
- **Elevation:** Cards and inputs stay flat and use `--rule-standard` borders. Only floating surfaces (menus, popovers, dialogs) get `--elevation-float`.
- **Focus ring:** A square 2px ink outline with a 2px offset. Don't use a soft glow.
- **Transitions:** Only `color`, `background-color`, `border-color`, and `transform`, at `--duration-fast` by default. No entrance animations, scroll effects, or looping anything.
- **Press state:** Buttons translate 2px down and right and drop their float shadow. That reads as a physical press, which suits a print-derived brand better than a hover lift.

**Judgment calls to confirm:**

1. I kept one hard offset shadow (`--elevation-float`) so overlays separate from the page. It's a solid block, not a soft blur, and it's the only shadow in the system. If you want zero shadows, delete that token and give floating surfaces a `--rule-heavy` border instead.
2. The 200ms ceiling is my pick. If you want the site to feel almost static, drop `--duration-base` to 120ms and use only `--duration-fast`.
3. The hex values are placeholders. Check the red against the off-white paper for contrast before you lock it, since a loud red on light paper can fail AA for small text.
