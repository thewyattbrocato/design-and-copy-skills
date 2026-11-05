## Shape

```css
--radius-none: 0;
```

Define one radius and no others. The skill's scale guidance is 2 to 4 steps, but the brand is a single deliberate value, so a second radius would only invite use. Add a lint rule that `border-radius` must resolve to `--radius-none`. Circular avatars or images, if you ever need them, are an explicit exception, not a token.

## Depth

Three levels, all hard-edged, no blur. Depth is a rule, not a haze.

```css
--elevation-0: none;                          /* flat: the default for everything */
--elevation-1: 0 0 0 2px var(--color-ink);    /* ruled: hover, selected, current item */
--elevation-2: 4px 4px 0 var(--color-ink);    /* lifted: menus, popovers, featured card */
```

`--color-ink` is a semantic role from your color tokens, so it remaps in any theme. Pressing a control should sink it onto its shadow: `transform: translate(4px, 4px)` with `--elevation-0`. That is the one interaction pattern for depth, and it keeps the flat brand physical.

## Motion

Three durations and three easings, with the default being no motion.

```css
--duration-none: 0ms;          /* default, and what reduced motion resolves to */
--duration-quick: 120ms;       /* state change: hover, press, focus */
--duration-standard: 240ms;    /* open or close: menu, dialog, drawer */

--ease-standard: cubic-bezier(0.2, 0, 0, 1);  /* things arriving */
--ease-exit: cubic-bezier(0.4, 0, 1, 1);      /* things leaving */
--ease-snap: steps(2, end);                   /* one hard, print-like change */

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-quick: 0ms;
    --duration-standard: 0ms;
  }
}
```

Motion rules for the spec:
- Nothing animates on page load, and nothing is scroll-linked.
- Animate only state changes that the user caused, never decoration.
- `--ease-snap` is for a single deliberate reveal, such as a stamp-like confirmation. Drop it if you want no stepped motion at all.

## Counts

- Radius: 1 value (deliberate, below the 2 to 4 range)
- Elevation: 3 levels
- Duration: 3 values
- Easing: 3 values

No existing tokens or colors were provided, so there is no merge map yet. The ink color is referenced by name only, and I have not proposed any hex values here.

Two notes: I chose offset hard shadows for elevation-2 as the one place "depth" is more than a rule. If the brand wants strictly rules and no offset, delete `--elevation-2` and use `--elevation-1` for everything raised. I did not check the durations against a real component set, so tune them once the first menu and button are built.
