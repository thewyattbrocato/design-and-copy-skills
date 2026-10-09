## What's going on

Nothing here is one bug. Each component's values were picked separately, with no shared tokens, so the stylesheet has drifted:

- **Near-duplicate colors that look identical but aren't.** The primary blue is `#2f6fed` in `.btn` and `#2e6dea` in `.btn-big`. There are three muted grays (`#8a8f98`, `#8d929b`, `#858a93`), two card borders (`#e3e5e8`, `#e1e4e8`), and two success greens. Side by side, these read as "slightly off," which is the inconsistency people feel.
- **Too many radii:** 4, 5, 6, 7, 9, 10, and 12px, with no scale.
- **Three near-identical elevations.** `.card`, `.panel`, and `.modal` have different shadows, and `.card` and `.panel` are nearly the same component.
- **Off-grid spacing.** Paddings like 9, 11, 13, 17, 18, 22, and 26 and margins like 14, 19, and 34 don't follow a 4px or 8px grid.
- **Type scale with no ratio.** The steps are 31, 23, 19, 17, and 14, and the gaps shrink as you go down. `.btn-big`'s 17px is the same size as `h4` by coincidence.
- **Real mismatches, not just drift:**
  - `.btn-big` doesn't set `color: #fff`, so its text inherits whatever color the parent has. That can render dark text on blue.
  - `.input` is 38px tall with 6px radius, and `.select` is 40px with 4px radius. In a form row, they won't line up.
  - Buttons have no fixed height, so they're sized by padding and line-height. They won't match the inputs either.
- **Muted text fails contrast.** `#8a8f98` on white is roughly 3.2–3.5:1, below the 4.5:1 AA minimum for small text. The other two grays are about the same.

## What I'd do, in order

1. **Fix the actual bugs first.** Add `color: #fff` to `.btn-big`. Make `.input` and `.select` the same height and radius. Both are small, safe changes.
2. **Add color tokens and collapse the duplicates.** Keep one primary, one primary-hover, one border, one muted text, and one success pair. Pick one muted gray that passes AA, such as `#6b7079` (about 5:1 on white, my estimate). Then update the selectors to use the tokens.
3. **Set a radius scale.** For example `--radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px`. Map buttons and inputs to `sm`/`md`, cards and panels to `lg`, and the modal to `lg`.
4. **Merge the surfaces and set two elevations.** Make `.panel` a variant of `.card`, or remove it. Use one `--shadow-sm` for cards and one `--shadow-lg` for modals.
5. **Put spacing on a 4px grid.** Something like 4, 8, 12, 16, 24, 32. Snap the outliers (9→8, 17→16, 19→20, 34→32, and so on), then check the screens visually, since these shifts are noticeable.
6. **Pick a type scale and apply it to headings.** For example 14 body, 16, 20, 24, 32. Move the heading rules to classes if they need to be overridden per page, rather than element selectors.
7. **Put it all in custom properties** on `:root`, so new components use the tokens by default and the drift doesn't come back.

Steps 1 and 2 would probably resolve most of what people are noticing. Steps 3–6 are cleanup that tightens things further.

I only saw this excerpt. There may be other overrides elsewhere that affect the result. If you share the rest of the stylesheet, or the app's repo, I can make these changes directly and check the result in the running app.
