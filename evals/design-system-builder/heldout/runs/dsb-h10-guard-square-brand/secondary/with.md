Here are the three scales, in CSS custom properties. They're short on purpose: the brand's flatness means most of the decisions are "none."

```css
:root {
  /* Shape: square everywhere. One exception, for circular marks only. */
  --radius-none: 0;
  --radius-round: 50%;   /* status dots, radio marks, avatars only */

  /* Depth: rules, not blur. No soft shadows exist in this system. */
  --elevation-0: none;                             /* flat on the paper */
  --elevation-1: 0 0 0 2px var(--color-border-strong);  /* ruled edge: cards, inputs */
  --elevation-2: 4px 4px 0 0 var(--color-border-strong); /* hard offset block: raised, menus, hover */

  /* Motion: state changes only. Nothing decorative. */
  --duration-none: 0ms;     /* reduced motion, and the default for decorative anything */
  --duration-fast: 120ms;   /* hover, focus, press */
  --duration-moderate: 240ms; /* menus, drawers, dialogs opening */

  --ease-standard: cubic-bezier(0.2, 0, 0, 1);  /* default for state changes */
  --ease-enter: cubic-bezier(0, 0, 0, 1);       /* things arriving */
  --ease-exit: cubic-bezier(0.4, 0, 1, 1);      /* things leaving */
}
```

**How they're used**

- **Radius:** components use `--radius-none`. `--radius-round` is limited to the listed circular marks, so it stays an exception rather than a second corner style.
- **Elevation:** `elevation-1` is the resting rule for cards and inputs. `elevation-2` is for things that sit above the page. Pressing a raised element moves it down to `elevation-0` with a 4px translate, so the block looks pushed in rather than faded. That gives press feedback with no easing curve.
- **Motion:** only state changes get `fast` or `moderate`. Anything that doesn't answer a user action uses `none`. Under `prefers-reduced-motion`, all durations resolve to `none`, and the press translate becomes instant.
- **Naming:** `--color-border-strong` is a semantic role pointing at the near-black ink. Components should reference the role, not the raw black.

**Notes**

- The hard offset in `elevation-2` is technically a shadow, just unblurred. If the team reads "no shadows" literally, use a 4px outline ring or a second border instead. The visual result is nearly the same.
- I didn't propose any new colors, so there are no contrast claims to check here. The `border-strong` role still needs a contrast check against the paper background when the palette is set.
