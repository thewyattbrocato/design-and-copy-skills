The core is sound and I'd ship it after a few additions. The scales are short, the names describe roles instead of colors, and dark mode remaps the roles instead of inverting them. I also estimated contrast by hand, so treat these as approximate and confirm them with a checker. The text, action, danger, success and warning colors all come out around 6:1 or better against their surfaces in both themes.

**Fix before handoff**

1. **Add a focus ring token.** There's no `--color-focus`, so each team will invent its own. Define it in both themes (about 3:1 against both bg and surface) and add `--focus-ring-width` and `--focus-ring-offset`.
2. **Add a stronger border for form controls.** `--color-border` (#d9d5cc) is about 1.4:1 on white. That's fine for dividers but too faint for input and checkbox edges, which need about 3:1. Add `--color-border-strong` in both themes.
3. **Add status tints.** Warehouse screens will have many status badges and banners, such as low stock, a failed scan or a received shipment. Right now you only have the saturated colors. Add `--color-danger-subtle`, `--color-success-subtle` and `--color-warning-subtle` backgrounds, and either `--color-on-danger` or a rule that status text uses the base color on the subtle background. Check those pairs in both themes. Also tell consumers never to use color alone to signal status.
4. **Add raised and overlay surfaces for dark mode.** Black shadows barely show on #1f1d17, so dark elevation has to come from lighter surfaces. Add `--color-surface-raised` and `--color-surface-overlay`, which can equal `--color-surface` in light mode. Keep the shadows.
5. **Declare `color-scheme`.** Add `color-scheme: light` on `:root` and `color-scheme: dark` in the dark block, so native scrollbars and form controls match. Also add an `@media (prefers-color-scheme: dark)` default, with `data-theme` as the override. Right now dark only works if someone sets the attribute.

**Add for Tallyard specifically**

- **Fonts.** There are no `--font-sans` or `--font-mono` tokens and no weights. Inventory screens are full of SKUs and quantities, so also document `font-variant-numeric: tabular-nums` for numeric columns, either as a token or a utility.
- **Line heights per size.** `--leading-tight` and `--leading-body` aren't tied to sizes. State which sizes use which (tight for xl and 2xl, body for the rest).
- **Hit targets and density.** Handheld scanners and gloved hands need larger targets. Add something like `--target-min: 44px` (or 48px for the floor app) and decide now whether tables get a compact density, because adding that later is a breaking change.
- **Disabled state.** Add `--color-text-disabled` or a documented opacity token. Disabled controls are currently undefined.
- **Motion.** Add a `prefers-reduced-motion` rule that zeroes the durations. A second easing for entrances and exits would also be useful, since you only have one now.
- **Forced-colors.** Test in forced-colors mode. Shadows and tinted backgrounds disappear there, so borders have to carry the structure.

**Minor**

- Spacing names are the pixel value divided by 4 (`--space-3` is 12px), so say that in a comment. The jump from 32 to 48 is fine, but you'll probably want a `--space-16` (64px) soon. Resist filling in the missing steps.
- `--radius-full: 999px` is fine. Consider `--radius-lg` only when a real component needs it.
- The tokens are a single tier (roles hold hex directly), which is right for v1. Don't add a raw color ramp until a third theme needs one.

**For the handoff itself**

- If the other team doesn't consume CSS directly, keep one source (a JSON token file that exports to this CSS) so the two don't drift.
- Name an owner, add a changelog, and set the rule that a token is deprecated for a release before it's removed. Version this as v1.0.0 so the first breaking rename is visible.

I can write out the revised token block with these additions if you'd like. I'd propose the new hex values and check their contrast properly.
