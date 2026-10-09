The inconsistency comes from values chosen one at a time with no shared scale, so near-duplicates pile up. Each one looks fine alone, but they show up side by side: a button next to an input, a card next to a panel, two headings in a row.

**What's going on**

- **Near-duplicate colors.** The primary button is `#2f6fed` in `.btn` and `#2e6dea` in `.btn-big`. The borders are `#e3e5e8` and `#e1e4e8`. Three grays (`#8a8f98`, `#8d929b`, `#858a93`) all mean "muted text." The success alert and badge are almost the same green with different values.
- **No radius scale.** Seven values (4, 5, 6, 7, 9, 10, 12px) with no step pattern.
- **No spacing scale.** Paddings of 9, 11, 12, 13, 17, 18, 22, and 26px, and margins of 14, 19, and 34px. None sit on a base grid.
- **Mismatched control heights.** Inputs are 38px and selects are 40px, so they won't line up in a form row.
- **Type scale with no ratio.** The steps are 31, 23, 19, 17, which shrink by 1.35×, 1.21×, then 1.12×. `h4` and `.btn-big` are both 17px, so they're tied by accident, not by design.
- **Three shadows for two elevations.** `.card` and `.panel` are the same thing (a bordered surface) with different shadows and paddings. `.modal` is the only real elevation step.
- **Components that are variants of each other but not built that way.** `.btn-big` only overrides size and color, and it has no text color, so it depends on `.btn` being applied too.
- **Raw values everywhere.** Nothing uses custom properties, so nothing can be changed in one place.

**What I'd do, in order**

1. **Inventory before changing anything.** Pull every color, radius, padding, margin, font size, and shadow the app actually uses, not just this slice. Count them and group by role. This tells you the real target set and which differences are accidents.

2. **Define a small set of tokens and snap to them.** Pick roughly:
   - Colors: one primary, one primary-hover, one muted text, one border, one success pair.
   - Radius: `4 / 8 / 12px`.
   - Space: a 4px base (`4, 8, 12, 16, 24, 32`).
   - Type: one ratio and a few steps.
   - Elevation: two shadows.

   Snap each existing value to the nearest token. The blue and gray snaps are invisible. Radius and spacing snaps are visible, so get design sign-off on those.

   ```css
   :root {
     --color-primary: #2f6fed;
     --color-text-muted: #8a8f98;
     --color-border: #e1e4e8;
     --color-success-bg: #e6f6ea;
     --color-success-text: #1f7a3a;
     --radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px;
     --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-6: 24px;
     --shadow-1: 0 2px 8px rgba(0,0,0,.12);
     --shadow-2: 0 12px 40px rgba(0,0,0,.28);
   }
   ```

3. **Consolidate components.** Merge `.card` and `.panel` into one surface with a padding modifier if needed. Make `.btn` the base and have `.btn--lg` change only size. Set one control height for inputs, selects, and buttons so they align.

4. **Lock it down.** Add a stylelint rule that rejects raw hex colors and off-scale values outside the token file, so drift can't come back. Put this in early, not last, so the migration doesn't keep adding new one-offs.

5. **Verify visually.** Take before and after screenshots of the key screens and diff them. Expect small shifts, and review them as a set rather than one at a time.

Steps 1 and 2 are where most of the value is. Steps 3 and 4 are mostly mechanical once the tokens exist. I've only judged this from the one chunk you pasted, so the full inventory in step 1 may turn up more.
