Mostly solid. The palette is well considered and the dark theme overrides every color role. I'd fix the first three items before handing this off, since they're the ones the other team will hit immediately.

**Fix before shipping**

1. **Border contrast is too low for form controls.** `--color-border` is about 1.5:1 against white in light mode and about 1.5:1 against `--color-surface` in dark mode. WCAG 1.4.11 asks for 3:1 on UI component boundaries when the border is the only thing marking an input or button. Either darken the light border (around `#8f8a7c` reaches 3:1 on white) and lighten the dark one, or add a separate `--color-border-strong` / `--color-input-border` for controls and keep the current value for dividers.

2. **There's no focus token.** Add `--color-focus` (and ideally `--focus-ring-width`). Focus needs at least 3:1 against both the surface and the adjacent colors. Blue `--color-action` may work in light mode, but it should be checked on dark surfaces and given its own name so it can diverge.

3. **Status colors have no "on" pairs.** There's `--color-on-action`, but nothing for danger, success, or warning. Any filled danger button, or a badge that uses those colors as backgrounds, will have no defined text color. Add `--color-on-danger`, `--color-on-success`, and `--color-on-warning`. For a warehouse tool, also add tinted backgrounds (for example `--color-danger-subtle`) for low-stock and error badges. Those are usually where status colors actually show up.

**Worth adding before v1 if the other team will build on them**

- **Missing type tokens.** There's no `--font-sans` / `--font-mono` (SKUs and bin codes usually want mono), no font weights, and no `--text-xs`. Dense inventory tables often need 12px for metadata.
- **Motion needs a reduced-motion rule.** Either document that the team should wrap transitions in `@media (prefers-reduced-motion: reduce)`, or define the zeroed values in that block. Also, `--ease-out` breaks the `--motion-*` prefix. Consider `--motion-ease-out`.
- **Theme selection.** Dark mode only applies with `[data-theme="dark"]`. Decide whether the OS preference (`prefers-color-scheme`) should also apply, and whether the team should set the attribute before first paint to avoid a flash.
- **Density.** Inventory screens tend to need compact row heights and padding. A `--row-height` or `--control-height` token keeps tables from being hand-tuned.
- **Spacing gaps.** The scale jumps from 12 to 16 to 24 with no 20px step, and 40 and 64 are absent. That's fine if intentional, but say so in the docs.

**Smaller things**

- Hover runs in opposite directions by theme: light mode darkens `--color-action-hover`, dark mode lightens it. That's correct for contrast, but name it in the docs so nobody "fixes" it.
- Shadows are nearly invisible on dark surfaces. Elevation there usually comes from a surface step (`--color-surface-raised`), so you may want a token for that.
- Consider whether the other team needs more than CSS custom properties. If they work from JSON or Figma, a Style Dictionary or DTCG-format export would keep the sources in sync.

I computed the contrast ratios by hand from the hex values, so run them through a checker before you rely on the exact numbers. The text colors (`--color-text`, `--color-text-muted`, `--color-action`, and the status colors on their surfaces) all pass AA for normal text in both themes.
