I'd make a few changes before handing it over. The core is solid. The text and action colors pass AA contrast in both themes, and the roles are named by purpose rather than by hue.

**Fix before shipping**

1. **Border contrast.** `--color-border` is about 1.4:1 against bg/surface in both themes. That's fine for dividers but fails the 3:1 WCAG minimum for input and checkbox edges. Keep it for dividers and add `--color-border-strong` (roughly `#8a8576` light, `#6b6757` dark) for form controls.
2. **No focus token.** Add `--color-focus-ring` and `--focus-ring-width`. Otherwise every team will invent its own, and they won't match.
3. **Missing status tints.** Danger, success, and warning exist only as foreground colors. Badges, banners, and table-row states need backgrounds, so add `--color-danger-bg`, `--color-success-bg`, and `--color-warning-bg`. For an inventory tool, "low stock" and "out of stock" will be your most common states. Also add an `--color-info`, or decide on purpose that action blue covers it.
4. **No `color-scheme`.** Add `color-scheme: light` to `:root` and `color-scheme: dark` to the dark block. Without it, native scrollbars, date pickers, and form controls stay light in dark mode.

**Worth adding for Tallyard**

5. **Control sizes.** If anyone uses this on handhelds or with gloves, tokens like `--size-control-md: 44px` and `--size-control-lg: 56px` will matter more than most of what's here.
6. **`--text-xs` (0.75rem).** Dense tables and SKU metadata usually need it, and teams will hardcode it if it's missing. Also add font-family tokens, including a mono one for SKUs and bin locations, and weight tokens. Document `font-variant-numeric: tabular-nums` for quantity columns.
7. **Scrim and z-index.** You have `--shadow-overlay` but no `--color-scrim` (for example `rgba(0,0,0,.5)`) and no z-index scale (dropdown, modal, toast). Stacking bugs show up between teams.
8. **Reduced motion.** Add a `@media (prefers-reduced-motion: reduce)` block that sets the motion durations to about 0ms, so consumers get it for free.

**Minor**

- **Spacing:** the scale jumps from 48 to nothing, so consider `--space-16: 64px`. Document that the number is the multiple of 4px, because `--space-6` = 24px surprises people who expect an ordinal scale.
- **Theme default:** dark only applies with `data-theme="dark"`. If you want it to follow the OS by default, add a `prefers-color-scheme` rule (e.g. `:root:not([data-theme="light"])`).
- **Missing states:** there's no `--color-action-active`, no disabled tokens, and no on-color for danger or success fills. Add them if you expect filled destructive buttons.
- **Breakpoints:** custom properties can't be used in `@media` queries, so ship breakpoints as documentation or in a JS/JSON export rather than in this CSS.
- **Docs:** a one-line note that status colors must be paired with an icon or text, never used alone, will save you accessibility bugs later.

I can draft the additions as a patch to the CSS if you want.
