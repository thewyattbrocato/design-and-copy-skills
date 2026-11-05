Mostly solid. The palette values hold up, but I'd fix three things before handing this off, and a few gaps will cause questions from the other team.

**Fix before handoff**

1. **Border contrast is too low for input edges.** `--color-border` is about 1.5:1 against white in light mode and about 1.5:1 against `--color-bg` in dark mode. WCAG 1.4.11 asks for 3:1 on UI boundaries such as inputs, checkboxes, and focus-adjacent edges. Keep the current value for dividers and decorative lines, and add a stronger token for control boundaries (e.g. `--color-border-strong`, roughly `#8a8577` light / `#6b6657` dark, which I'd verify with a checker).

2. **No focus token.** Without `--color-focus` and a focus ring width/offset, every team will invent their own, and keyboard users get inconsistent focus. Add `--color-focus` (probably `--color-action`, with a dark-mode variant), plus `--focus-ring-width` and `--focus-ring-offset`.

3. **No tinted status backgrounds.** Warehouse UIs will need badges and banners for low stock, out of stock, received, and so on. Right now danger, success, and warning are foreground-only, so teams will hard-code tints. Add `--color-danger-subtle`, `--color-success-subtle`, and `--color-warning-subtle`, along with matching `--color-on-*` text colors if the status fills are ever solid.

**Gaps worth closing in v1**

- **Font family and weight tokens** are missing: `--font-sans`, `--font-mono` (SKUs and bin codes will want mono), and weights such as `--weight-regular`, `--weight-medium`, and `--weight-semibold`.
- **Type scale has no `--text-xs`**, and there is no `--leading-normal` between tight and body. Dense tables often need a smaller size than 14px.
- **Spacing jumps.** Adding `--space-5` (20px) will matter for form layouts. Document the rule (4px base, what the gaps are) so the other team knows whether `--space-5`, `--space-7`, and so on are intentionally absent.
- **Border widths, z-index, and opacity for disabled states** are unspecified. Small, but they are the first things people hard-code.
- **Motion:** consider `--motion-slow` and a `prefers-reduced-motion` override that sets the durations to 0.
- **Format and versioning:** ship a source of truth (JSON in the W3C DTCG format, or Style Dictionary) and generate the CSS from it, so non-web platforms can consume the same tokens. Add a version number and a changelog, since v1 will get changed.

**Things I'd decide on deliberately, not necessarily change**

- **Dark shadows.** Black shadows at these opacities are barely visible on `#15140f`. Depth in dark mode will come mostly from surface lightness and borders, so make sure the team knows that.
- **Theme selection.** The dark theme only applies via `[data-theme="dark"]`. If you want OS-level dark mode, add a `prefers-color-scheme` block or document that the app sets the attribute.
- **Units.** Spacing and shadows are in px, type is in rem. Using rem for spacing scales it with the user's font-size setting. It's a reasonable choice either way, but pick one and document it.
- **Status color alone.** Success green and danger red are both used as text and fill. Warehouse staff may be colorblind, so the components should pair color with an icon or label. This is a component rule, not a token change, but the docs should say it.

**Checked and fine**

I computed these by hand, so run them through a checker to confirm:
- Light text `#1d1b16` on bg: very high contrast.
- Light muted text `#5c574b` on bg: about 6.9:1.
- Light action `#1b5e8a` on white, and `--color-on-action` on action: about 7:1.
- Dark muted text on dark bg: about 7.3:1.
- Dark action on dark surface: about 7.3:1.
- Dark on-action on dark action: about 7.6:1.

The danger, success, and warning colors look well above 4.5:1 on their backgrounds, but I didn't compute those exactly.

If you want, I can draft the additional tokens (with light and dark values and a contrast check) as a v1.1 patch to this file.
