Mostly solid. The palette is restrained and the scales are clean. I'd fix the accessibility gaps and a few missing tokens before handing this off, because the other team will build against whatever ships in v1.

**Fix before handoff**

1. **Border contrast fails in both themes.** `--color-border` (#d9d5cc) against white is about 1.5:1, and `--color-border` in dark (#3a372d) against `--color-bg` is about 1.5:1. WCAG 1.4.11 asks for 3:1 on UI boundaries such as input outlines, checkbox edges, and card edges when the border is the only cue. Either darken the light border (roughly #8a8576 or darker) and lighten the dark one, or split the token: keep `--color-border` decorative and add `--color-border-strong` (3:1) for inputs and controls.

2. **No focus token.** Keyboard focus is a core requirement and nothing here defines it. Add something like `--color-focus` (per theme, at least 3:1 against both bg and surface) and `--focus-ring-width`, and say in the docs whether focus is an outline or a box-shadow.

3. **No on-color tokens for status colors.** `--color-on-action` exists, but `--color-danger`, `--color-success`, and `--color-warning` have no matching foreground. If anyone puts text on a filled danger or success button or badge, they'll pick ad hoc colors. Add `--color-on-danger`, `--color-on-success`, `--color-on-warning`, or decide now that those are text-only and document that.

4. **Missing `color-scheme`.** Dark mode needs `color-scheme: dark` on the `[data-theme="dark"]` selector (and `light` on `:root`). Without it, native form controls, scrollbars, and the default select menus stay light. Also decide whether `prefers-color-scheme` should set the theme when no attribute is present. Right now the default is light with no OS fallback.

**Should add for v1**

5. **Font family and weight tokens.** There are sizes and leading but no `--font-sans`, `--font-mono` (SKUs, bin codes, and quantities usually want tabular numerals), or `--font-weight-*`. Add `font-variant-numeric: tabular-nums` as a utility or token note for numeric columns.

6. **Reduced motion.** Add a `@media (prefers-reduced-motion: reduce)` block that sets the motion durations to 0ms, or document that the components must honor it.

7. **Status tints.** Low-stock, overdue, and received badges usually need a background tint plus text. Right now status is only foreground color. Add `--color-danger-subtle`, `--color-success-subtle`, and `--color-warning-subtle`. Also make sure status is never color-only, since the other team will need icons or labels for it.

8. **Touch and density sizes.** Tallyard is likely used on handhelds, tablets, and gloves. A `--size-target-min: 44px` (or 48px) and a dense row height for tables would prevent the other team from inventing these per component.

**Smaller things to consider**

9. **Mixed units.** Type uses `rem` and spacing uses `px`. If a user raises their browser font size, text grows and spacing doesn't. Switching spacing to `rem` (`0.25rem` base) is the common fix. If you keep `px`, say so explicitly.

10. **Naming inconsistency.** `--ease-out` doesn't follow the `--motion-*` prefix. Rename it to `--motion-ease-out` or move it under a consistent group.

11. **Type scale floor.** `--text-sm` at 14px is the smallest step. Dense tables and labels often want 12px, so consider `--text-xs`.

12. **Dark shadows.** `rgba(0,0,0,.5)` barely shows on `#15140f`. Elevation in dark mode usually comes from a lighter surface step, so add a `--color-surface-raised` token or document that shadows are weak in dark.

13. **Spacing gaps.** The scale jumps from 12 to 16 to 24 with no 20px step. That's fine if intentional, but the comment should say the scale is a multiplier of 4 and the gaps are deliberate.

**Checked and fine:** text, muted text, action, on-action, danger, success, and warning all meet 4.5:1 on their light and dark backgrounds, and the light-mode `--color-warning` (about 5.9:1 on white) passes AA for normal text.

I haven't edited any files since you didn't point me at one. If you want, I can write a revised `:root` and dark block with the additions above.
