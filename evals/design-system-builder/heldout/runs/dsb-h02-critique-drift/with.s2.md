## What's going on

Nobody made an inconsistent choice. There are no shared choices, so every rule picked its own value, and the values are close enough that the differences look like mistakes. In your chunk:

| Property | Distinct values | Examples |
|---|---|---|
| Radii | 7 | 4, 5, 6, 7, 9, 10, 12 |
| Muted text grays | 3 | `#8a8f98`, `#8d929b`, `#858a93` |
| Brand blue | 2 | `#2f6fed`, `#2e6dea` |
| Card/panel border | 2 | `#e3e5e8`, `#e1e4e8` |
| Success green background | 2 | `#e6f6ea`, `#e4f5e8` |
| Success green text | 2 | `#1f7a3a`, `#217c3d` |
| Container padding | 3 | 18, 22, 26 |
| Vertical margins | 3 | 14, 19, 34 |
| Control heights | 2 | input 38, select 40 |
| Control horizontal padding | 2 | input 11, select 12 |
| Card/panel shadows | 2 near-twins | `0 2 7 .12` and `0 3 9 .10` |

Four things are going wrong:

1. **Near-duplicates.** These are the real culprits. A 38px input next to a 40px select, or a 4px radius next to a 6px one, is too small a difference to look intentional, so it reads as sloppiness. Three grays within a few hex steps of each other do the same.
2. **Parallel components.** `.card` and `.panel` are the same idea with slightly different numbers. `.btn` and `.btn-big` differ in every property, not just size. `.muted`, `.hint` and `.caption` are one color under three names, and `.alert-ok` and `.badge-ok` are one success color under two.
3. **Off-grid numbers.** Values like 9, 13, 17, 19 and 34 don't come from any scale. They look like values copied from mockups or eyeballed in the browser.
4. **Heading sizes collide with other sizes.** `h4` and `.btn-big` are both 17px, which looks accidental. Meanwhile 31, 23 and 19 aren't on a consistent ratio.

All of this comes from only 6 lines of heading, color and spacing rules, so I expect the full stylesheet to be worse. I haven't seen the rest, so the counts above cover this chunk only.

## What I'd do, in order

**1. Inventory the whole stylesheet** (an hour or so). Count every distinct color, font size, spacing, radius and shadow `[count from your repo]`, grouped by purpose. This tells you how big the problem is and gives you the list you'll merge from.

**2. Pick short scales and merge into them.** Don't add new values. Here is a starting proposal for your chunk:

| Scale | Proposed values | Merge map |
|---|---|---|
| Radius | 4 / 8 / 12 | 4,5,6 → 4 (controls); 7,9,10 → 8 (cards, modals); 12 stays |
| Spacing | 4, 8, 12, 16, 24, 32, 48 | 9→8, 11,12,13,14→12, 17,18,19→16, 22,26→24, 34→32 |
| Control height | one value (40) | 38 and 40 → 40 |
| Elevation | 3 levels: raised, overlay, modal | card and panel shadows → raised; modal stays |
| Type | 5 or 6 roles on a fixed ratio | Decide after the inventory, since your 14/17/19/23/31 is only a partial view |
| Muted text | 1 | The three grays → one |
| Blue, border, success green | 1 each | Each pair → one |

I haven't contrast-checked any of these. Before settling the muted text and success colors, check them against their backgrounds. `#8a8f98` on white is about 3.2:1 by my estimate, which would fail AA for body text.

**3. Add semantic tokens, and have components read only those.** Use role names such as `text-secondary`, `surface-raised`, `border-subtle`, `accent`, `success-bg` and `success-text`. Don't use `gray-500` or `blue-2`. This is where `.muted`, `.hint` and `.caption` collapse into one role, and where `.alert-ok` and `.badge-ok` share one success pair.

**4. Consolidate components, one at a time.** Start with the most-used ones:
- **Button:** one component with a size variant (`.btn` and `.btn-big` currently differ in every property).
- **Input and select:** shared height, padding and radius.
- **Card and panel:** merge them into one surface with a padding variant, unless they behave differently in ways this chunk doesn't show.

Migrate each component fully, then delete the old rules. Don't leave both versions in place.

**5. Lock it in.**
- Keep a single token file, as CSS custom properties, that both design and code use.
- Add a stylelint rule that flags raw hex colors and off-scale px values.
- Name an owner who can reject a new value.
- Write a one-page guide showing what each token is for.

Do this before the first migrations land, or the stylesheet will drift again within a quarter.

**Why this order:** the inventory and scales (steps 1 and 2) are cheap and make every later decision mechanical. The migration (step 4) is the expensive part, and it only stays done if the lint rule and owner (step 5) exist.

Two assumptions: this is a single-brand web app with a small team, and the scales above are proposals to adjust after the inventory. If you can share the full stylesheet, I can turn this into an actual token file and a complete merge map.
