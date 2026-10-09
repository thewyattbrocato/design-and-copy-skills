The core scale is solid. Before handing it off, I'd fix a few gaps: one contrast problem, a few missing roles, and the handoff contract.

**Fix before handoff**

1. **Border fails non-text contrast in both themes.** `--color-border` is about 1.4:1 on the light background and about 1.5:1 on the dark one. WCAG 1.4.11 requires 3:1 for input outlines and other UI boundaries. If borders only decorate (dividers, cards), that's fine. If they outline inputs, checkboxes, or table cells that carry meaning, add something like `--color-border-strong` at 3:1 or better and keep `--color-border` for decoration.

2. **No focus token.** There's no focus ring color or width. Add `--color-focus` (both themes) and probably `--focus-ring-width`. This is a common accessibility gap in v1 token sets.

3. **No font family or weight tokens.** This is a big gap for a handoff. For an inventory tool, add `--font-sans`, `--font-mono` or `--font-numeric` (with `font-variant-numeric: tabular-nums` for SKUs and quantities), and weight tokens such as `--font-weight-medium` and `--font-weight-semibold`.

4. **No `color-scheme`.** Add `color-scheme: light` on `:root` and `color-scheme: dark` on `[data-theme="dark"]`. Otherwise native inputs, scrollbars, and selects stay light in dark mode.

5. **No status backgrounds.** Danger, success, and warning are foreground-only. Badges and alerts need tinted backgrounds like `--color-danger-bg`, plus text tokens that pass on them. Check each pair; text on a tint is often the weakest contrast.

6. **No reduced-motion handling.** Either document that the motion tokens are overridden to `0ms` under `prefers-reduced-motion: reduce`, or define that override in the tokens file.

**Should fix or document**

- **Dark shadows barely register.** Black shadows at these opacities are nearly invisible on `#15140f`. Either rely on surface lightness and borders for elevation in dark mode, or document that shadows are subtle by design.
- **Hover moves in opposite directions.** Light hover darkens and dark hover lightens. That's correct for contrast, but document it so nobody "fixes" one theme to match the other.
- **Spacing has gaps at 20px and 40px.** That's fine if intentional, but add `--space-5` and `--space-10` if the other team will need them.
- **Type scale has no `xs`.** If labels or dense table cells ever need 12px, adding it now is cheaper than retrofitting it later.
- **Theme default is undefined.** `[data-theme="dark"]` won't follow `prefers-color-scheme`. Decide whether light is the default and whether the app should respect the OS setting.
- **Naming is slightly mixed.** Spacing uses numeric indices, type uses t-shirt sizes, and leading uses `tight`/`body`. That's defensible, but list it in the naming rules so new tokens follow one pattern.

**Handoff package**

Ship a short doc with the v1 token list, which tokens are public and which are internal, the theme contract, the contrast results for each text and UI pair, and a changelog policy. Without the contrast results, the other team will have to re-derive them.

I checked the contrast ratios by hand from the WCAG formula, so run them through a checker before you sign off. Text pairs I checked (muted text, action on white, danger, warning, and the dark-mode text pairs) all pass AA.

I can draft the revised token block with these additions if you want it.
