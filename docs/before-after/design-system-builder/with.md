**What's going on:** there's no shared set of decisions. Each rule was written by eye, so every value is close to its neighbors but not equal to them. No single difference is visible, but together they make everything look slightly off.
[...]
2. **Fix the scales on paper.** Use short scales. These are proposals to adjust against your inventory:
   - Spacing: 4, 8, 12, 16, 24, 32, 48.
   - Radius: 4, 8, 12.
   - Elevation: 2 or 3 levels, such as raised and overlay.
   - Type: 5 or 6 roles (caption, body, body-large, h3, h2, h1).
   - Control height: 40 for all form controls.
[...]
4. **Migrate in order of least visible change first.**
   1. Colors. Merging the blues, grays, greens and borders is nearly invisible. Collapse `.muted`, `.hint` and `.caption` into one role.
   2. Radius, border and shadow.
   3. Spacing and type. These shift layouts, so go screen by screen.
   4. Merge `.card` and `.panel` into one component, and align `.input` and `.select` to one control spec. `.btn` and `.btn-big` become one button with a size variant.

   Write the merge map (old value → token) before you touch anything, so each change is mechanical and reviewable.
[...]
**Assumptions:** a single-brand web app with a small team, and no existing design system or token file. If you already have one, I'd extend it instead of building this.
