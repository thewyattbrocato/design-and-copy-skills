**What's going on:** Nothing here is broken in isolation. The inconsistency comes from the stylesheet having no shared scale. Each component picks its own numbers, and the numbers drift apart:

- **Near-duplicate colors that aren't the same:** the primary blue appears as `#2f6fed` and `#2e6dea`. The muted greys `#8a8f98`, `#8d929b`, and `#858a93` are three values for one role. The success greens `#e6f6ea`/`#1f7a3a` and `#e4f5e8`/`#217c3d` are two more near-matches. Borders are `#e3e5e8` and `#e1e4e8`.
- **Radii with no scale:** 4, 5, 6, 7, 9, 10, 12px. Buttons get 5 and 7, cards 9, panels 12, modals 10.
- **Spacing with no grid:** paddings of 9, 11, 12, 13, 17, 18, 22, 26. Margins of 14, 19, 34. Nothing is on a 4px or 8px step, so things almost line up but never quite do.
- **Type sizes that step irregularly:** 14, 17, 19, 23, 31. `.btn-big` and `h4` both use 17 by coincidence, not by design.
- **Controls that don't line up:** `.input` is 38px tall and `.select` is 40px. Placed side by side in a form, they visibly mismatch. The 14px `.btn` is roughly 35px tall, so it doesn't match either field (exact heights depend on line-height, which isn't in the sheet).
- **Variants as new magic numbers:** `.btn-big`, `.panel`, and `.card` are separate components with their own values, not modifiers on a base. Each one was probably written by copying a neighbor and tweaking it.
- **Three shadows and two surfaces for one job:** `.card` and `.panel` are both bordered containers with near-identical shadows, so it's unclear which to use.

Nobody can say why because each value is individually reasonable. The problem is that there are about 40 unique values where there should be 5 to 8 per category.

**What I'd do, in order:**

1. **Define tokens by snapping, not redesigning.** Pick a 4px spacing scale (4, 8, 12, 16, 24, 32), a radius scale (4, 8, 12), a type scale, one shadow per elevation level (card, modal), and named color roles (primary, text-muted, success). Map each existing value to its nearest token. Keep the change small so the app looks about the same. Doing this first gives every later step a target.

2. **Merge the duplicates.** Collapse the two blues, three greys, two greens, and two borders into one value each. This is low-risk and removes most of the "why does this look slightly off" effect, even before any layout changes.

3. **Fix the form controls.** Give buttons and inputs one shared control height token (for example 40px) and use it in `.btn`, `.btn-big`, `.input`, and `.select`. This is the most visible fix for users, since it's where mismatches show up on screen.

4. **Rebuild the components on tokens.** Make `.btn` a base with size modifiers (`--sm`, `--md`, `--lg`) instead of a separate `.btn-big`. Merge `.card` and `.panel` into one surface component with a padding variant, and have `.modal` reuse the same surface and elevation tokens.

5. **Tie the type scale to heading tokens.** The `h1`–`h4` element selectors are global, so changing one changes everything. Move sizes into tokens and consider classes for headings, so a heading's look and its semantic level can differ.

6. **Add a guardrail.** Use a stylelint rule to block raw hex values and off-scale spacing or radii outside the tokens file, so drift doesn't come back.

Before step 1, take screenshots of the main screens. Snapping values will shift things slightly, and you'll want to compare before and after. Also decide on the scale values with a designer or whoever owns the brand, since that's a judgment call.

If you want, I can do steps 1 and 2 in this file now. I can also draft the token file and the `.btn` size modifiers, using the design-system-builder workflow.
