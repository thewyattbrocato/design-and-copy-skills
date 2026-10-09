The set is coherent and the colors are mostly in good shape. Here's what I'd change, most important first.

**Fix before handoff**

1. **Border contrast.** `--color-border` is about 1.4:1 against the background in light mode and about 1.5:1 in dark. That's fine for decorative dividers. It fails the WCAG 3:1 requirement for input and control boundaries. Split it into `--color-border` (subtle dividers) and `--color-border-strong` (inputs, checkboxes, table controls, around 3:1 or more).
2. **No focus token.** Add `--color-focus-ring` (and probably `--focus-ring-width` and `--focus-ring-offset`). Otherwise each team invents its own, and warehouse users on keyboards or scanners will feel it.
3. **Add `color-scheme`.** Set `color-scheme: light` on `:root` and `color-scheme: dark` in the dark block. Native scrollbars, form controls, and autofill will then match the theme.
4. **Dark theme only applies via `[data-theme]`.** If you want it to follow the OS by default, add a `prefers-color-scheme: dark` rule that targets `:root:not([data-theme="light"])`. Either way, document which behavior you intend.
5. **Status colors have no companions.** You have `danger`, `success` and `warning` as solid colors only. Inventory UIs use them constantly for low stock, out of stock, and sync errors. You'll need:
   - Tinted backgrounds, for example `--color-danger-bg` and `--color-danger-border`, for badges and banners.
   - `--color-on-danger`, if you ever use solid fills.
   - `--color-danger-hover`, if destructive buttons exist.
   - Possibly `--color-info`.

**Should do**

6. **Mixed units.** Type is in `rem` and spacing is in `px`, so spacing won't scale if users raise their browser font size. Consider `rem` for spacing (`0.25rem`, `0.5rem`, and so on) or document that it's intentional.
7. **Spacing and type gaps.** There's no `--space-5` (20px), `--space-10` or `--space-16`. Dense data tables also usually want a 2px step and a `--text-xs` (0.75rem). If the gaps are deliberate, say so in the docs. Teams tend to hardcode `20px` otherwise.
8. **Missing type basics.** There are no `--font-sans` or `--font-mono` tokens, no weights, and no `--leading-*` pairing guidance. For SKUs and quantities, I'd add a mono family and a note on `font-variant-numeric: tabular-nums` so columns of numbers align.
9. **Dark-mode shadows.** Black shadows on `#1f1d17` are nearly invisible. Elevation in dark mode usually reads better from a lighter surface plus a border. Consider `--color-surface-raised` and `--color-surface-overlay`, and use them for modals and menus.
10. **Missing structural tokens.** You'll likely get asked for:
    - A scrim, such as `--color-scrim`.
    - Disabled states (text and background).
    - A selected or hover row color for tables.
    - A z-index scale.
    - Breakpoints. Note that these can't be CSS custom properties in media queries, so document them.

**Smaller notes**

- Add `prefers-reduced-motion` guidance. At minimum, a rule that zeroes `--motion-fast` and `--motion-base` in that media query.
- Add an `--ease-in` and `--ease-in-out`, or say that `--ease-out` is the only curve on purpose.
- `--radius-full: 999px` works. Some teams prefer `9999px`, but it makes no practical difference.
- Add a short README that covers usage rules (semantic color roles only, never raw hex), a version number, and a changelog stub. The other team will want to know what counts as breaking once v1 ships.
- Status color alone shouldn't carry meaning, so note in the docs that status always pairs with an icon or label.

**What's already good**

Text, muted text, action, and the status colors all clear 4.5:1 on their light surfaces. I eyeballed these rather than measuring, so run them through a checker before you ship. The dark palette is well balanced, and `--color-on-action` is handled correctly in both themes. The role-based naming (`action`, `surface`, `text-muted`) will survive a rebrand.

I can write the revised CSS with these changes folded in, including computed contrast values for the new border and tint tokens, if you'd like.
