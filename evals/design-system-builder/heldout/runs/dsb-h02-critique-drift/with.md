**What's going on:** there's no shared set of decisions. Each rule was written by eye, so every value is close to its neighbors but not equal to them. No single difference is visible, but together they make everything look slightly off. I've counted only this snippet. Run the same count on the whole stylesheet (`[count from your repo]`), because the real numbers will be worse.

**Evidence in the snippet**

| Property | Values in use | Problem |
|---|---|---|
| Primary blue | `#2f6fed`, `#2e6dea` | Same intent, different values. `.btn-big` doesn't even set `color`. |
| Muted text | `#8a8f98`, `#8d929b`, `#858a93` | Three class names for one role. All sit around 3:1 on white, so they probably fail AA for body text. Check this. |
| Success | `#e6f6ea`/`#1f7a3a` and `#e4f5e8`/`#217c3d` | One role, two pairs. |
| Border | `#e3e5e8`, `#e1e4e8` | Near-duplicates. |
| Radius | 4, 5, 6, 7, 9, 10, 12 | Seven values in 1–2px steps. Nobody can see the difference, but the sum looks unsettled. |
| Control height | input 38, select 40 | Placed side by side in a form, they misalign. |
| Control padding and radius | input `0 11px` / 6px, select `0 12px` / 4px | Same kind of control, different shape. |
| Card vs panel | 18/22 padding, 9/12 radius, 2 near-identical shadows | One component under two names, drifted apart. |
| Heading sizes | 31, 23, 19, 17 | `.btn-big` at 17px duplicates h4. There's no stated type scale. |
| Spacing | 14, 19, 34 margins, plus 9, 11, 13, 17, 18, 22, 26 padding | No rhythm. Each value was eyeballed. |

**What I'd do, in order**

1. **Finish the inventory.** Count every distinct color, font size, spacing, radius, shadow and control height across the whole codebase, grouped by purpose. This tells you how big the cleanup is and which values are used most. Those become the winners in the merge map.

2. **Fix the scales on paper.** Use short scales. These are proposals to adjust against your inventory:
   - Spacing: 4, 8, 12, 16, 24, 32, 48.
   - Radius: 4, 8, 12.
   - Elevation: 2 or 3 levels, such as raised and overlay.
   - Type: 5 or 6 roles (caption, body, body-large, h3, h2, h1).
   - Control height: 40 for all form controls.

3. **Define the tokens as CSS custom properties, in two tiers.** Raw values feed semantic roles. Components use only the roles, never raw values.
   - Names like `--color-accent`, `--color-text-secondary`, `--color-border-subtle`, `--color-success-surface`, `--radius-md` and `--space-4`.
   - Don't name tokens by color or page.
   - Pick a muted-text color that passes AA, and verify the contrast ratio.

4. **Migrate in order of least visible change first.**
   1. Colors. Merging the blues, grays, greens and borders is nearly invisible. Collapse `.muted`, `.hint` and `.caption` into one role.
   2. Radius, border and shadow.
   3. Spacing and type. These shift layouts, so go screen by screen.
   4. Merge `.card` and `.panel` into one component, and align `.input` and `.select` to one control spec. `.btn` and `.btn-big` become one button with a size variant.

   Write the merge map (old value → token) before you touch anything, so each change is mechanical and reviewable.

5. **Lock it in.** Add a stylelint rule that rejects raw hex colors and off-scale px values outside the token file. Without this, the drift comes back within a few sprints. Mark any one-off value as a labeled exception.

6. **Add light governance.** Name one owner for the token file. Tokens change only through add, modify or deprecate, with a changelog. A pattern joins the system when a second screen needs it. A one-squad team needs a single page for this, not a committee.

Later, if you want dark mode or a second brand, it will be a remap of the semantic roles. That's only possible after step 3.

**Assumptions:** a single-brand web app with a small team, and no existing design system or token file. If you already have one, I'd extend it instead of building this.
