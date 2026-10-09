**What's going on:** there's no design system, only values that were eyeballed one component at a time. Almost every value is a near-duplicate of another, so the UI is off by small amounts everywhere. Nobody can name the cause because each individual value looks reasonable.

**Evidence in the snippet**

- **Colors**
  - Two blues: `#2f6fed` and `#2e6dea`.
  - Three greys for secondary text: `#8a8f98`, `#8d929b`, `#858a93`.
  - Two greens for success: `#e6f6ea`/`#1f7a3a` and `#e4f5e8`/`#217c3d`.
  - Two border colors: `#e3e5e8` and `#e1e4e8`.
  - These are visually indistinguishable, so they're accidents, not choices.
- **Radii:** 4, 5, 6, 7, 9, 10 and 12px. The `.select` has 4px next to an `.input` with 6px, so adjacent form controls don't match.
- **Control heights:** `.input` is 38px and `.select` is 40px. They'll sit misaligned in any form row.
- **Padding:** 9/17, 13/22, 18, 22, 26 and 11/12. There's no scale.
- **Spacing:** 14, 19 and 34px. There's no rhythm.
- **Shadows:** `.card` and `.panel` are almost the same elevation but written differently. `.modal` is a one-off.
- **Type:** 14, 17, 19, 23 and 31px. The steps are irregular, and `h4` (17px) matches `.btn-big` by coincidence.
- **Semantic gaps:** `.muted`, `.hint` and `.caption` are the same concept under three names. `.card` and `.panel` are probably the same component. `.btn-big` redefines the color instead of being a size modifier.

**What I'd do, in order**

1. **Audit before changing anything (about half a day).** Grep every distinct color, radius, spacing, font-size and shadow value, and count usages. The counts tell you which near-duplicate is the real one. Usually one of each pair is dominant.
2. **Pick the scales (an hour or two of decisions).**
   - Spacing on a 4px base (4, 8, 12, 16, 24, 32, 48).
   - 3 radii (for example 4, 8, 12).
   - 3 shadows (sm, md, lg).
   - A type scale (14, 16, 20, 24, 32).
   - One blue, one muted grey, one border color, and one success pair.
   - Control heights shared across input, select and button (for example 32, 40, 48).
3. **Define them as CSS custom properties** in one `:root` block (`--space-2`, `--radius-md`, `--color-text-muted`, and so on). Name them by role, not value. Don't touch components yet.
4. **Migrate in order of visibility and shared usage.**
   - Start with form controls (`.input`, `.select`, `.btn`). They sit side by side, so mismatches show most there.
   - Then cards, panels and modals. Merge `.card` and `.panel` into one component with a size modifier.
   - Then typography and text colors. Collapse `.muted`, `.hint` and `.caption` into one class.
   - Then alerts and badges, and finally spacing utilities.
   - Make `.btn-big` a size modifier that only changes padding, font size and height.
5. **Snap each value to the nearest token**, and accept small visual shifts (1–3px). Review in screenshots, since the point is to remove the drift.
6. **Lock it in.** Add a stylelint rule (for example `declaration-property-value-allowed-list` or `stylelint-declaration-strict-value`) that rejects raw hex colors and pixel values for these properties. Without this, the drift comes back within a few months.

The risk is doing step 4 as one big-bang rewrite. Migrate component by component, with visual regression screenshots if you have them. Step 1 is the most valuable on its own, because it turns "it feels off" into a concrete list you can show the team.

If you share the full stylesheet or point me at the repo, I can run the audit in step 1 and propose the actual token values from real usage counts.
