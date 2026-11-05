The set is in good shape: short scales, role-based names, and a dark theme that remaps roles instead of inverting. I'd fix the items below before handing it over, most important first. I checked contrast by hand-estimating luminance, not with a tool, so rerun the numbers in a checker before you quote them.

**Fix before handoff**

1. **Input borders are too faint.** `--color-border` (#d9d5cc) on white is about 1.5:1. That's fine for dividers, but form fields, checkboxes and similar controls need about 3:1 to be visible. Add a second border role:
   ```css
   --color-border-strong: #8a8576;  /* light, ~3.5:1 on bg/surface (my estimate) */
   /* dark */ --color-border-strong: #7a7566;  /* ~3.6:1 on surface (my estimate) */
   ```
2. **There's no focus token.** Warehouse staff use keyboards and scanner-style input a lot, so focus has to be consistent. Add `--focus-ring-width`, `--focus-ring-offset` and `--color-focus-ring: var(--color-action)`.
3. **Status colors have no background partners.** Stock states like low, out and received need badges, banners and row tints. Add `--color-danger-bg`, `--color-success-bg` and `--color-warning-bg`. Pick the values so each passes against its matching text color in both themes. Add `--color-on-danger` too if danger buttons are planned. Then add a rule to the guide that status never relies on color alone, so it always carries an icon or label.
4. **Theme mechanics are incomplete.**
   - Neither theme sets `color-scheme`. Add `color-scheme: light` in `:root` and `color-scheme: dark` in the dark block, so native scrollbars and form controls match.
   - Dark mode only works through `data-theme`. Honor `prefers-color-scheme` by default and let `data-theme` override it.
   - Add a `prefers-reduced-motion` rule that sets the motion durations to 0 or near it.
   - Test with forced-colors on.
5. **Type is only half specified.** There's no font family, no weights, and no monospace for SKUs and bin codes. Add `--font-sans`, `--font-mono` and `--weight-regular`, `--weight-strong`. Document `font-variant-numeric: tabular-nums` for quantity columns, because misaligned digits in inventory tables cause misreads. Also consider a size below 14px for dense tables, or state that 14px is the floor.

**Worth deciding now, but not blocking**

- **Interactive states.** There's a hover for action, but no pressed, disabled or selected-row tokens. Either add them or say in the handoff that components own those for now.
- **Touch targets.** For gloves and handhelds, add something like `--size-target-min: 44px`.
- **Layout and layering.** Spacing stops at 48px. Add 64px for page-level gaps and a small z-index scale (`--z-sticky`, `--z-overlay`, `--z-toast`), since you already have an overlay shadow. Breakpoints can't be custom properties in media queries, so document them separately.
- **Spacing names.** `space-N` means N×4px, which is why 5, 7 and 9–11 are missing. Say that in a comment so nobody reads it as an oversight.
- **Prefix.** Another team will consume these names, so a prefix like `--ty-` avoids collisions. It's cheap now and painful later.

**Governance for the handoff**
- Name one source of truth. If design files consume tokens too, export JSON as well as CSS.
- Add a version number and a changelog entry for v1.
- Name an owner, and write one line on how a token gets added or deprecated.

Everything else holds up. The radius, shadow and motion scales are sized right, and the light-theme text, action and status colors look comfortably above 4.5:1 on their grounds.

I can write the patched file with these additions if you'd like. I'd leave the status-background values for you to confirm.
