## What's going on

The stylesheet doesn't have a design system. It has a pile of one-off values, and most of the inconsistency comes from near-misses that nobody chose on purpose:

- **Near-duplicate colors.** The primary button is `#2f6fed` in `.btn` and `#2e6dea` in `.btn-big`. Those look identical alone but not side by side. The card border `#e3e5e8` and panel border `#e1e4e8` are the same story.
- **Three greys for one role.** Secondary text is `#8a8f98`, `#8d929b`, and `#858a93`.
- **Two greens for one role.** `.alert-ok` and `.badge-ok` use different backgrounds and text colors for the same "success" meaning.
- **Radii with no scale.** 4, 5, 6, 7, 9, 10, and 12px. Cards are 9px, panels 12px, modals 10px, and buttons 5px or 7px depending on size.
- **Off-grid spacing.** Padding of 9, 11, 13, 17, 22, and 26px, and margins of 14, 19, and 34px. None sit on a 4px or 8px grid, so nothing lines up predictably.
- **Shadows that are almost the same.** `.card` and `.panel` use slightly different offsets, blurs, and opacities, so they read as "similar but wrong."
- **Type sizes with no ratio.** Headings are 31, 23, 19, and 17px. The h4 at 17px happens to match `.btn-big`, which is a coincidence, not a rule.
- **Inputs don't match.** `.input` is 38px tall and `.select` is 40px, with different horizontal padding and radius. Fields in the same form will look misaligned.
- **Accessibility risk.** `#8a8f98` on white is about 3.3:1, below the 4.5:1 WCAG AA minimum for body text. The other two greys are similar. Muted text may be hard to read, not just inconsistent.

Each rule is fine on its own. The problem is that nothing ties them together, so every new component picks a value by eye.

## What I'd do, in order

1. **Audit actual usage first.** Before changing any values, check which ones appear in templates and on which screens. Near-duplicates used on different pages are low-risk to merge. Ones used side by side are the visible bugs, so fix those first.

2. **Define tokens as CSS custom properties, without changing visuals yet.** Put every raw value behind a name:
   ```css
   :root {
     --color-primary: #2f6fed;
     --color-success-bg: #e6f6ea;
     --color-success-fg: #1f7a3a;
     --color-text-muted: #6b7079;   /* adjusted for contrast; check it */
     --color-border: #e1e4e8;
     --radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px;
     --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-6: 24px; --space-8: 32px;
     --shadow-1: 0 1px 3px rgba(0,0,0,.10);
     --shadow-2: 0 4px 12px rgba(0,0,0,.12);
     --shadow-3: 0 12px 40px rgba(0,0,0,.28);
   }
   ```
   Pick the scale values deliberately. The ones above are a starting point, not a final answer.

3. **Consolidate the near-duplicates onto those tokens.** Collapse the blues, borders, greys, and greens into one value each. Collapse radii to 2–3 steps and shadows to 2–3 elevations. Expect small visual shifts. Review them in the app, not just in the diff.

4. **Normalize the components.** Give buttons one size ladder (for example sm/md/lg built from the same tokens) instead of two unrelated rules. Merge `.card` and `.panel` into one surface component with a single radius and shadow, or a size modifier if they really differ. Make `.input` and `.select` share a height and padding. Note that `.btn-big` sets no `color`, so it only works when combined with `.btn`. Either make modifiers self-contained or document that they're meant to compose.

5. **Fix the type scale.** Choose one ratio (or a simple fixed list like 14/16/20/24/32) and map h1–h4 and body/caption to it. Consider classes for headings so page-specific headings aren't forced into element selectors.

6. **Prevent drift.** Add a stylelint rule that rejects raw hex colors and off-scale px values outside the token file. Without this, the same drift returns within a few months.

I'd start with steps 1–3 since they fix what people see and don't require touching components. Steps 4–6 are the durable part. I can do steps 2–3 directly in this file if you share the rest of the stylesheet and the templates that use these classes. The `design-system-builder` skill also covers this kind of work if you want a more structured pass.
