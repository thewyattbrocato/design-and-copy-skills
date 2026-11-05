## What's going on

Nobody made a wrong decision here. The same decision was made many times, slightly differently each time. Every value in this chunk is a one-off, so nothing is shared and nothing can be wrong in a way anyone can point to. These are the specific symptoms (counts are from this chunk only, so rerun them on the full stylesheet):

| Area | What's in the chunk | Problem |
|---|---|---|
| Radius | 4, 5, 6, 7, 9, 10, 12 (7 values) | Neighbors are 1px apart, so the eye reads them as a mistake instead of a hierarchy. `.input` is 6px and `.select` is 4px, side by side in forms. |
| Blue | `#2f6fed` and `#2e6dea` | A near-identical pair. `.btn-big` is a slightly different blue than `.btn`. |
| Secondary text | `#8a8f98`, `#8d929b`, `#858a93` | Three names for one gray. It's also roughly 3.3:1 on white, which is probably below AA for body text. Verify that. |
| Border and success colors | `#e3e5e8` and `#e1e4e8`; two green pairs (`.alert-ok`, `.badge-ok`) | Same duplication as the blues and grays. |
| Card, panel | Padding 18 and 22, radius 9 and 12, shadows `.12` and `.10` with different blur | These are one component with two accidental settings. |
| Control heights | `.input` is 38px and `.select` is 40px | Misaligned in any row that contains both. |
| Spacing | Margins 14, 19, 34; paddings 9, 11, 12, 13, 17, 18, 22, 26 | There's no scale. |
| Type | 14, 17, 19, 23, 31 | `.btn-big` (17) equals `h4` (17), which is coincidence, not design. The heading steps are irregular. |

So the inconsistency is real, but no individual value is the cause. The cause is that there are no tokens, so every author picks values by eye.

## What I'd do, in order

**1. Inventory the whole stylesheet (first, before changing anything).** Count distinct colors, font sizes, spacings, radii and shadows. Group them by purpose. The numbers tell you how big the cleanup is. I'm only working from this chunk, so I'm not guessing the totals.

**2. Fix short scales and merge into them.** Proposed targets, to be adjusted against the full inventory:

- **Radius:** 4 (controls), 8 (surfaces), 12 (large surfaces and modals).
  - Mapping: 4, 5, 6 → 4; 7, 9, 10 → 8; 12 → 12.
- **Spacing:** 4, 8, 12, 16, 24, 32, 48.
  - Mapping: 9, 11, 12 → 8 or 12; 13, 14 → 12; 17, 18 → 16; 19, 22 → 24 (check by eye); 26 → 24; 34 → 32.
- **Type:** 14, 16, 20, 24, 32, which is five roles instead of five arbitrary sizes. The button sizes map to 14 and 16.
- **Shadow:** two or three elevations: raised (card and panel) and overlay (modal).
- **Control height:** one value, probably 40, with 32 as an optional compact size.
- **Colors:** one accent, one muted text color, one border color and one success pair.
  - Mapping: `#2f6fed` and `#2e6dea` → one accent. The three grays → one `text-secondary`, darkened until it passes 4.5:1 on your surfaces. Both greens → one pair.

**3. Name the values by role, not by color.** Define them as CSS custom properties in two tiers:

- Raw values: the scales above.
- Semantic roles: `--color-accent`, `--color-text-secondary`, `--color-border-subtle`, `--color-success-bg`, `--space-3`, `--radius-surface`, `--shadow-raised`.
- Components read only the semantic roles, never raw values.

```css
:root {
  --color-accent: #2f6fed;
  --color-text-secondary: #6b7079; /* proposal: verify contrast */
  --radius-control: 4px;
  --radius-surface: 8px;
  --shadow-raised: 0 2px 8px rgba(0,0,0,.10);
}
.card { padding: var(--space-4); border-radius: var(--radius-surface); box-shadow: var(--shadow-raised); }
```

**4. Collapse the duplicate components.**
- `.card` and `.panel` become one component, with a padding modifier only if you really need two.
- `.btn-big` becomes a size variant of `.btn`, not a separate class with its own color.
- `.alert-ok` and `.badge-ok` share the success tokens.
- Make `.input` and `.select` share height, radius and padding.

**5. Migrate in order of visibility and risk.** Start with the elements on every screen (buttons, inputs, text colors), then cards and panels, then spacing, which touches the most layout. Do each as its own small change and compare screenshots before and after. Expect small visible shifts, because that's the point of merging values.

**6. Lock it in.**
- Add a stylelint rule that rejects raw hex colors and off-scale pixel values outside the token file.
- Write one page that states who owns the tokens and how to add one. The rule is that a new value replaces or merges into an existing one.
- Document every state for buttons and inputs (hover, focus, disabled, error), not just the default. This chunk shows none of them, so check that they exist.

Do steps 1 to 3 first. They're cheap and they stop the problem from growing, and everything after them is mechanical.

My assumptions are a single-brand web app with a small team and no existing token system. If you already have a design system or component library, tell me, because then this becomes a theming job instead.
