The core structure is sound: a 4px spacing base, a clean semantic color layer, and dark mode done by overriding only the theme-sensitive values. Here's what I'd change before handing it over, most important first.

**Fix before shipping**

1. **Border color fails non-text contrast.** `--color-border` (#d9d5cc) is about 1.5:1 against white, and the dark border (#3a372d) is similarly faint against the dark background. WCAG 1.4.11 asks for 3:1 on UI component boundaries such as inputs, checkboxes, and button outlines. Keep the current value for decorative dividers, and add a stronger token, for example `--color-border-strong` at roughly 3:1 (#8a8476-ish in light, something similar in dark), for form controls. Verify the exact values with a checker.

2. **No focus token.** Warehouse staff will be on keyboards and scanners, and focus visibility matters here. Add `--color-focus` (and optionally `--focus-ring-width`). Light and dark need different values, and `--color-action` may not be distinct enough from the surrounding surfaces.

3. **Status colors have no "on" pairs.** `--color-on-action` exists, but there's nothing for danger, success, or warning. If those ever become fills (badges, pills, toasts), the text color is undefined. This matters most in dark mode: #f2877f or #6fcf92 as a background with white text fails contrast badly. Add `--color-on-danger`, `--color-on-success`, and `--color-on-warning` for both themes.

**Gaps the other team will hit**

4. **Typography is only sizes.** There's no font family, font weight, or letter-spacing. If they're going to set type from these tokens, add `--font-sans` (and `--font-mono` if SKUs or bin codes will be shown in monospace, which is common in inventory UIs), plus a few weights.

5. **Missing surface and state roles.** Table row striping or hover, selected rows, disabled text and disabled backgrounds, and an input background are all common in an inventory tool. Right now they'd have to reach for `--color-surface` or `--color-text-muted` and improvise.

6. **Border width and z-index are absent.** Probably fine for v1, but if the other team is building overlays and tables, they'll want `--z-*` and a `--border-width` token so they aren't hardcoding `1px`.

**Consistency and polish**

7. **Motion naming is inconsistent.** `--motion-fast` and `--motion-base` have a prefix, but `--ease-out` doesn't. Rename it to `--motion-ease-out` so everything motion-related sorts together.

8. **Set `color-scheme` on each theme.** Add `color-scheme: light` to `:root` and `color-scheme: dark` to the dark block. This makes native form controls and scrollbars match the theme. Also decide how the system preference is handled. As written, the dark theme only applies when `data-theme="dark"` is set. If you want to respect `prefers-color-scheme`, you'll need either a media query or a JS default, and the docs should say which.

9. **Dark-mode elevation is weak.** Black shadows at these opacities barely register on a near-black background. Consider leaning on surface lightness or the border for elevation in dark mode, and treat the shadow as secondary.

10. **Spacing has gaps and no documented intent.** The scale jumps from 16 to 24 and has no 20. That's probably intentional, but say so in the docs. Also add a short note on when to use which step.

**Things I'd leave alone**

- The text, action, danger, and success colors pass AA on their intended backgrounds in both themes, and the muted text does too (roughly 6.9:1 light, 7.3:1 dark). These are good.
- Dark hover moving lighter while light hover moves darker is the usual dark-mode convention, so that's fine.

The contrast figures above are my hand estimates, so run the final palette through a real checker before you publish the values. If you want, I can draft the additional tokens (`--color-border-strong`, `--color-focus`, the on-status pairs, and the font and surface roles) with values for both themes.
