Here's a token set that matches the brand: square corners, hard black rules, and depth built from offsets instead of blur. Values are starting points, so adjust them once you see them on the page.

```css
:root {
  /* Radius: the brand is square everywhere. Define the scale so it's explicit, then enforce 0. */
  --radius-none: 0;
  --radius-full: 50%; /* only for true circles, e.g. avatars or status dots. Remove if none exist. */

  /* Rules: borders do the work that shadows do in other systems. */
  --rule-hairline: 1px;  /* table rows, internal dividers */
  --rule-base: 2px;      /* inputs, cards, default component outline */
  --rule-heavy: 4px;     /* headers, section breaks, emphasis */
  --rule-color: #141414; /* off-black ink, not pure #000 */

  /* Elevation: hard, unblurred offset "block" shadows in the ink color. No blur ever. */
  --elevation-0: none;
  --elevation-1: 3px 3px 0 0 var(--rule-color);  /* cards, menus */
  --elevation-2: 6px 6px 0 0 var(--rule-color);  /* popovers, modals, sticky elements */

  /* Focus: accessibility can't be flat. Make it loud and in the accent. */
  --focus-ring: 3px solid var(--accent);
  --focus-offset: 3px;

  /* Motion: barely any. Two durations, one easing, and a hard off switch. */
  --duration-instant: 0ms;
  --duration-fast: 120ms;  /* hover, focus, color changes */
  --duration-base: 200ms;  /* menus, drawers, disclosure. Use sparingly. */
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --ease-linear: linear;   /* for color-only transitions */
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast: 0ms;
    --duration-base: 0ms;
  }
}
```

**Decisions behind these:**

- **Radius is zero on purpose.** Defining `--radius-none` as the only real radius means someone has to break the system to round a corner. Keep `--radius-full` only if you have circular elements.
- **Elevation is a hard offset, not a blur.** `6px 6px 0 0 ink` reads as a slab lifted off the page, which is the flat, blunt look you want. Going from `elevation-1` to `elevation-2` makes things feel like they're rising. If you'd rather have no shadows at all, drop the elevation tokens and use `--rule-heavy` for hierarchy.
- **Pressed buttons collapse their shadow.** A button with `elevation-1` can move 3px down and right on `:active` and drop its offset. That gives you a physical press without any easing curve or animation.
- **Motion stays short and mostly color-based.** Hovers and focus changes should be around 120ms, and nothing should loop, bounce, or slide large distances. Dialogs and menus can appear with an opacity or position change at 200ms, and nothing else needs motion.
- **Reduced motion is handled at the token level.** Components reference the duration tokens, so the media query turns off all motion without touching components.
- **Focus is always visible.** The accent-colored ring is the one place the brand gets loud on purpose, and it shouldn't be removed for aesthetics.

**Still to decide:** what `--accent` resolves to (your tomato red), and whether the `--radius-full` exception is worth keeping. If you tell me which components the site needs first, I can map these tokens onto buttons, cards, inputs, and nav.
