Mostly solid. The palette is well-tuned and the muted text and action colors pass contrast in both themes. I'd fix these before handing off, since v1 names become a contract:

**Fix before v1**

1. **Borders fail non-text contrast.** `--color-border` (#d9d5cc) is about 1.4:1 against `--color-bg`, and the dark border is about 1.5:1. WCAG 1.4.11 asks for 3:1 on borders that are the only cue for a control, such as inputs, checkboxes, and table dividers in a warehouse form-heavy UI. Keep `--color-border` for decorative dividers and add something like `--color-border-strong` (3:1) for input and control outlines.

2. **No focus token.** Keyboard focus is a requirement, and there's nothing for it. Add `--color-focus` (and maybe `--focus-ring-width`). Dark focus will need its own value.

3. **Status colors have no backgrounds or on-colors.** `--color-danger`, `--color-success`, and `--color-warning` are text/icon colors only. Badges, alerts, and row highlights need `*-subtle` backgrounds and an on-color for each. Right now every team will invent these, which is the drift you're trying to prevent. Only `--color-on-action` exists, so the set is incomplete.

4. **No font tokens.** There's no family, weight, or mono face. For inventory data (SKUs, bin IDs, quantities), add `--font-sans`, `--font-mono`, and ideally tabular-numeric guidance. Also consider `--text-xs` (12px) for dense table metadata. 14px is the floor right now.

5. **Dark theme isn't fully declared.** Add `color-scheme: dark` to `[data-theme="dark"]` so native form controls and scrollbars match. Decide whether dark also follows `prefers-color-scheme` or only the attribute, and document it.

**Should fix, low effort**

6. **Hover direction flips between themes.** Light hover darkens the action color, and dark hover lightens it. That's correct for contrast, but it's non-obvious. Document it so nobody assumes "hover = darker."

7. **Spacing gaps.** The scale jumps from 16 to 24, with no 20px step, and nothing above 48. Add `--space-5: 20px`, and consider `--space-16: 64px` for page-level layout.

8. **Naming consistency.** `--motion-fast`/`--motion-base` and `--ease-out` use different prefixes. Pick one (`--duration-fast` / `--ease-out` is a common pairing). Also `--space-N` is an index, not a pixel value; that's fine if the team knows it, but say so in the docs.

9. **Shadows on dark.** Black shadows at these opacities are barely visible on `#15140f`. Surface elevation in dark usually relies on a lighter surface tone or a border instead. Check this visually.

10. **Raw hex in the semantic layer.** Adding a primitive tier (`--blue-600: #1b5e8a`, etc.) makes dark-mode overrides and future brands cheaper. Not required for v1, but it's easier to add now than later.

**Process, before handoff**

- Add a version header and a short changelog, and mark which names are stable.
- Add a reduced-motion rule to the docs, even if it isn't a token. The motion tokens need it.

Contrast figures above are my hand calculations, so run them through a checker before you publish them. I haven't changed any files. If you want, I can apply items 1–8 to the file and draft the docs, or run the design-system-builder skill for a fuller pass.
