## What's going on

There's no shared source of truth for values. Someone eyeballed or copy-pasted each rule, so near-duplicates piled up. No single rule is wrong, but together they produce the "something is off" feeling. Your snippet shows it in every category:

| Category | What's in the snippet |
|---|---|
| Colors | Primary blue is `#2f6fed` and `#2e6dea`. Muted gray is `#8a8f98`, `#8d929b` and `#858a93`. Border is `#e3e5e8` and `#e1e4e8`. Success green has two backgrounds and two text colors. |
| Radius | 4, 5, 6, 7, 9, 10 and 12px. There are seven values, with no rule for which to use. |
| Padding | 9/17, 13/22, 18, 22, 26. None of these follow a scale. |
| Shadows | Three elevations (`.12`/7px, `.10`/9px, `.28`/40px). The card and panel shadows are different for no reason. |
| Spacing | 14, 19 and 34px. This isn't a 4px or 8px grid. |
| Type | 31, 23, 19, 17 and 14px. The steps are irregular, and `h4` equals `.btn-big`'s font size. |
| Form controls | `.input` is 38px tall with a 6px radius. `.select` is 40px tall with a 4px radius. They sit side by side in forms. |
| Components | `.card` and `.panel` are the same concept at slightly different sizes. |

The near-identical values are the worst part. Differences of 1–3 hex digits or 1px can't be seen deliberately, so they read as sloppiness, and nobody can name the cause because no single rule is the culprit.

One side finding: the muted grays on a white background are around 3:1 contrast, which probably fails WCAG AA for body text. Measure it before you rely on that.

## What I'd do, in order

1. **Inventory the full stylesheet.** Grep every color, radius, shadow, font-size and spacing value and count the uses. Your snippet is only a sample, and the real counts tell you which value to treat as canonical. This takes an hour or two and changes nothing.
2. **Define tokens and snap to them.** Create CSS custom properties: about 1 primary color, 3 grays for text, 1–2 borders, 1 success color, a 4px-based spacing scale, 3–4 radii, 3 shadow elevations and 5–6 type sizes. Pick the most-used existing value for each, so visual change stays minimal. Then replace the raw values. Most of this is mechanical, and the near-duplicates collapse without anyone noticing.
3. **Merge duplicated components.** Fold `.card` and `.panel` into one component with a size modifier. Give `.input` and `.select` the same height and radius. Make `.btn-big` a size variant of `.btn` that differs only in size tokens, not in color.
4. **Lock it in with tooling.** Add a stylelint rule (for example `declaration-property-value-allowed-list` or a no-raw-hex plugin) so new code can't reintroduce raw values. Without this, the drift comes back within a few months.
5. **Check it visually.** Run screenshot or visual-regression tests around step 2 so you can confirm the changes are small and intentional. Then fix the contrast issue as a deliberate change, separate from the cleanup.

Steps 1–2 give most of the payoff. Step 4 is what stops the problem from returning. If you share the full stylesheet or the repo, I can run the inventory and propose the token set.
