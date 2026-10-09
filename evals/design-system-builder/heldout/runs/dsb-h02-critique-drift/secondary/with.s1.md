## What's going on

The stylesheet has no shared vocabulary. Each rule picked its own values by eye, so the app ends up with near-duplicates that look almost the same and differ just enough to feel off:

- **Same color, two hex values.** `.btn` is `#2f6fed` and `.btn-big` is `#2e6dea`. Three near-identical muted greys (`#8a8f98`, `#8d929b`, `#858a93`), and two greens for the same success meaning (`#e6f6ea`/`#1f7a3a` and `#e4f5e8`/`#217c3d`).
- **Borders and shadows that almost match.** `.card` and `.panel` both have a 1px light grey border, but `#e3e5e8` vs `#e1e4e8`. Their shadows differ too (`0 2px 7px .12` vs `0 3px 9px .10`). Two surfaces that should be the same thing look slightly different.
- **Radii with no scale.** 4, 5, 6, 7, 9, 10, 12. Small buttons get 5px and big buttons 7px, so they look like different families.
- **Spacing with no scale.** Padding and margins are 9, 11, 13, 14, 17, 18, 19, 22, 26, 34. There's no 4px or 8px grid, so nothing lines up.
- **Type sizes that don't step.** Headings go 31, 23, 19, 17 (gaps of 8, 4, 2), and button text is 14 or 17. Nothing ties them to a ratio.
- **Form controls that don't match.** `.input` is 38px tall with a 6px radius, and `.select` is 40px with a 4px radius. Placed in the same form row, they're visibly misaligned.
- **Four shadow recipes** for what is really three elevation levels (card, panel, modal).
- **Variants copy instead of extend.** `.btn-big` repeats the button properties rather than building on `.btn`, which is how the color drifted.

Individually none of these is a bug. Side by side they read as "almost the same," and that's the inconsistency people feel without being able to name it.

## What I'd do, in order

1. **Make color tokens and collapse the near-duplicates.** Define `--color-brand`, `--color-text-muted`, `--color-success-bg`, `--color-success-text`, and so on. Map `#2e6dea` onto `#2f6fed`, the three greys onto one muted grey, and the two greens onto one pair. This is the cheapest change and the most visible improvement, and it's mostly find-and-replace.

2. **Define a spacing scale and a radius scale.** For example, spacing at 4, 8, 12, 16, 24, 32, and radius at 4, 8, 12. Snap each existing value to the nearest step. Expect small visual shifts, and check the main screens after each batch.

3. **Define elevation as three levels.** `--shadow-sm` for cards, `--shadow-md` for panels, `--shadow-lg` for modals. Use one border token for all surfaces. Merge `.card` and `.panel` into one surface component with size modifiers if they're really the same thing.

4. **Restructure components on the tokens.** Make `.btn` the base and have `.btn-sm`/`.btn-lg` change only padding and font size. Give `.input` and `.select` the same height and radius so they align in forms. Apply the type scale to `h1`–`h4`, and check that the body and button sizes sit on it too.

5. **Keep it from drifting back.** Add a stylelint rule that flags raw hex values and off-scale values outside the token file, or at minimum a review checklist item. Without this, the same drift will return in six months.

## Things to decide before step 2

- **Which value wins when two are close.** Someone should own the canonical brand blue and the canonical muted grey. I'd pick one from the more-used value.
- **Some differences may be intentional.** A modal shadow is supposed to be heavier than a card's. Confirm with whoever designed the screens before snapping them all to one value.

If you want, I can draft the token file from this stylesheet, with the mapping from each old value to its new token, and run the design-system-builder skill for the broader token and component structure.
