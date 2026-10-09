## What's going on

The stylesheet has no shared system. Each component has its own hand-picked values, and most of the differences are accidental rather than intentional. Each value looks reasonable alone, so no one notices the drift until you add them up:

- **Near-duplicate colors:** Primary blue is `#2f6fed` on `.btn` and `#2e6dea` on `.btn-big`. Borders are `#e3e5e8` and `#e1e4e8`. Success green is `#e6f6ea`/`#1f7a3a` on the alert and `#e4f5e8`/`#217c3d` on the badge. Three grays for muted text (`#8a8f98`, `#8d929b`, `#858a93`) differ by a few units each. You can't see these differences side by side, but they show up as slightly different colors across the app.
- **Radii with no scale:** 4, 5, 6, 7, 9, 10, 12. Seven values for corners.
- **Spacing off any grid:** Paddings include 9, 11, 12, 13, 17, 18, 22, 26, and margins include 14, 19, 34.
- **Mismatched form controls:** `.input` is 38px tall and `.select` is 40px. Side-by-side fields in a form will sit misaligned.
- **Uneven type scale:** Headings go 31 → 23 → 19 → 17. The steps shrink unevenly, so h3 and h4 are barely distinct. h4 (17px) also matches `.btn-big`.
- **Low-contrast muted text:** `#8a8f98` on white is about 3.2:1. That fails WCAG AA's 4.5:1 for body text, and the other two grays are about the same.
- **Fragile modifiers:** `.btn-big` sets a background but no text color. It only looks right if `.btn` is also applied, so it's a modifier in name only.

## What I'd do, in order

1. **Define tokens and snap existing values to them.** This comes first because every later step depends on it. Put them in custom properties:
   ```css
   :root {
     --color-primary: #2f6fed;
     --color-text-muted: #6b7079;   /* ~5:1 on white, passes AA */
     --color-success-bg: #e5f5e9;
     --color-success-text: #1f7a3a;
     --space-1: 4px; --space-2: 8px; --space-3: 12px;
     --space-4: 16px; --space-5: 24px; --space-6: 32px;
     --radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px;
     --shadow-sm: 0 2px 6px rgba(0,0,0,.10);
     --shadow-md: 0 4px 12px rgba(0,0,0,.12);
     --shadow-lg: 0 12px 40px rgba(0,0,0,.28);
   }
   ```
   Replace each raw value with the nearest token. This is a mostly invisible change, so it's low-risk. Check the screenshots to confirm nothing jumps.

2. **Fix the controls.** Buttons and inputs are the most used and most noticeable elements.
   - Make `.btn` the base with a size modifier: `.btn-sm`, `.btn` (default), `.btn-lg`. Put the background and text color on the base so no modifier depends on another class.
   - Give `.input` and `.select` the same height (40px), radius, and padding so form rows line up.

3. **Fix text.** Replace the three grays with `--color-text-muted`, which passes contrast. Rebuild the heading sizes on a fixed ratio, for example 14 body, 16 h4, 20 h3, 24 h2, 32 h1. Each level should be clearly distinct from the next.

4. **Unify the surfaces.** `.card`, `.panel`, and `.modal` are one concept with three paddings, three radii, and three shadows. Use one base container with `--radius-md` and `--shadow-sm` or `--shadow-md`, and add variants only where a design reason exists. Merge the two near-identical borders into one token.

5. **Add guardrails so it doesn't drift again.** Enable a stylelint rule that flags raw colors and off-scale values outside `:root` (for example, `stylelint-declaration-strict-value`). Then reject new raw values in review. Optionally add visual snapshot tests for buttons, forms, and cards.

Steps 1 and 2 would probably resolve most of what people are noticing. Step 3 is also a real accessibility fix, so don't defer it if you have an audit or compliance requirement.

I only saw this fragment, so other rules may override some of these values. Before changing anything, run a search for every class name to confirm where each one is used.
