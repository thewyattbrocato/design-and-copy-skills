## What's going on

The stylesheet has no shared source of values. Each rule was written with its own hand-picked numbers, so the same role gets a slightly different value every time. The differences are small enough that nobody notices any one of them, but together they read as inconsistency.

- **Near-duplicate colors:** the primary button is `#2f6fed` in `.btn` and `#2e6dea` in `.btn-big`. Three muted greys (`#8a8f98`, `#8d929b`, `#858a93`) do the same job. Two borders (`#e3e5e8`, `#e1e4e8`) and two green pairs (`#e6f6ea`/`#e4f5e8` backgrounds, `#1f7a3a`/`#217c3d` text) are the same story. Two blues that look identical on screen usually means someone picked a color by eye.
- **Seven radii with no scale:** 4, 5, 6, 7, 9, 10, 12px. `.btn` (5) and `.btn-big` (7) are the same component at two sizes but don't share a radius.
- **Off-grid spacing:** padding 9, 13, 17, 18, 22, 26; margins 14, 19, 34. None follow a 4px or 8px grid, so nothing lines up predictably.
- **Form controls that don't match:** `.input` is 38px tall and `.select` is 40px. Put them side by side in a form and they're visibly misaligned.
- **Duplicate components:** `.card` and `.panel` are nearly the same (border, radius, similar shadow, different padding). `.muted`, `.hint`, and `.caption` are three names for one style.
- **Four unrelated shadows:** card (`.12`, 2px/7px), panel (`.10`, 3px/9px), modal (`.28`, 12px/40px), with no defined elevation levels.
- **Irregular type scale:** 31, 23, 19, 17. The steps are uneven (the 19→17 step is tiny), and `h4` at 17px collides with `.btn-big`'s font size by coincidence.

I can only see this snippet, so I can't count how often each value appears across the app. That count is the first thing to get.

## What I'd do, in order

1. **Inventory before changing anything.** Grep the app's templates and CSS for every color, radius, shadow, and spacing value and count them. The most-used value in each family is the one to keep. This avoids arguing about which blue is "right" from the file alone.

2. **Define a small set of tokens** in one file, using the most-used values where possible:
   - **Color roles, not hues:** `--color-primary`, `--color-text-muted`, `--color-border`, `--color-success-bg`, `--color-success-fg`. One value each.
   - **Spacing:** 4, 8, 12, 16, 24, 32.
   - **Radius:** 4, 8, 12 (plus a pill value if you have one).
   - **Shadow:** `sm` (card), `md` (panel, if it survives), `lg` (modal).
   - **Type:** one scale for headings, for example 32/24/20/16. Use one line-height and one body size.

3. **Fix the most visible things first: primary color, buttons, and form controls.** Merge the two blues into one `--color-primary`. Make `.btn` and `.btn-big` one base class with a size modifier that changes only padding, font size, and radius. Give `.input` and `.select` the same height token so they align.

4. **Snap the rest to the scale.** Map each off-scale value to the nearest token (for example 9→8, 17→16, 22→24, 34→32, 5/6/7→8, 9/10→8 or 12). Snapping will make small visual changes, so check the result with whoever owns the design.

5. **Collapse duplicates.** Decide whether `.card` and `.panel` should be one component. Pick one name for the muted-text style.

6. **Add a guardrail** so the drift doesn't come back. A stylelint rule that rejects raw hex colors and off-scale px values outside the token file is the usual choice. Write one line of documentation per token saying what it's for.

Steps 1 and 2 take the most judgment and the least code. Step 3 is where users will notice the change, so it's a good place to get early feedback. If you want, I can start with the inventory: give me the stylesheet or templates for the rest of the app and I'll produce the value counts and a proposed token file.
