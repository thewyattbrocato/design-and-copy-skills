## What's going on

There's no design system underneath the stylesheet. Each component was styled by eye, so every value drifts slightly from its neighbors. Nothing is badly wrong, which is why nobody can point at the cause. The problem is dozens of values that are almost the same.

**Near-duplicates in this chunk**
- **Primary blue:** `.btn` uses `#2f6fed` and `.btn-big` uses `#2e6dea`. That's a visually identical color defined twice, so the two will diverge further over time.
- **Muted gray:** `.muted`, `.hint` and `.caption` use `#8a8f98`, `#8d929b` and `#858a93`. These are three values for one role.
- **Success green:** `.alert-ok` and `.badge-ok` use two slightly different backgrounds and two slightly different text colors.
- **Card borders:** `.card` uses `#e3e5e8` and `.panel` uses `#e1e4e8`.
- **Radii:** the values are 4, 5, 6, 7, 9, 10 and 12. That's seven radii, with no rule for which component gets which.
- **Spacing:** paddings include 9, 11, 12, 13, 17, 18, 22 and 26. Margins are 14, 19 and 34. None of these follow a scale.
- **Type sizes:** 14, 17, 19, 23 and 31 follow no consistent ratio. `.btn-big` at 17px also matches `h4` by coincidence rather than by design.

**Likely duplicate components**
- `.card` and `.panel` look like the same component with different padding (18 vs 22), radius (9 vs 12) and shadow.
- `.input` and `.select` sit next to each other in forms but have different heights (38 vs 40px) and radii (6 vs 4px). This is probably the most visible inconsistency, because users see them side by side.

**Accessibility**
- The grays near `#8a8f98` on white are roughly 3:1 contrast. That fails WCAG AA for body-size text, so `.muted`, `.hint` and `.caption` probably need darkening anyway.

I'm only seeing a chunk of the stylesheet. The real count of drifted values is probably much larger.

## What I'd do, in order

1. **Inventory the values.** Extract every distinct color, radius, font-size, spacing and shadow value, with a usage count. A quick script or a tool like `cssstats` is enough. This shows the real scale of the drift and which values are dominant.
2. **Define tokens with a small set per category.** Use CSS custom properties.
   - Colors: one primary, one neutral ramp, and semantic colors for success, danger and so on.
   - Radii: for example 4, 8 and 12.
   - Spacing: a 4px-based scale.
   - Type: about 5 sizes.
   - Shadows: about 3 elevations.

   Snap each existing value to its nearest token. Don't preserve the near-duplicates.
3. **Fix the most visible mismatches first.** These are form control height and radius, button variants, and the three grays. Fixing these gives most of the perceived improvement. Darken the muted gray to pass contrast at the same time.
4. **Merge duplicate components.** Fold `.card` and `.panel` into one component with a size or elevation modifier. Do the same for `.alert-ok` and `.badge-ok` as variants of a shared semantic color. `.btn-big` should become a size modifier of `.btn`, not a re-declaration.
5. **Normalize type and spacing.** This touches the most places and is the likeliest to cause layout shifts, so do it after the quick wins. Check it visually, ideally with screenshot diffs.
6. **Add guardrails.** Use stylelint with a rule such as `declaration-property-value-allowed-list`, or a plugin that bans raw hex and px values outside the token file. Without this, the drift will come back within a few months.

Steps 1 to 3 can be done in a day or two and will remove most of the "something feels off" effect. Steps 4 to 6 are what stop it recurring.

If you'd like, point me at the real stylesheet directory and I can run the inventory in step 1 and propose the token set from the actual numbers.
