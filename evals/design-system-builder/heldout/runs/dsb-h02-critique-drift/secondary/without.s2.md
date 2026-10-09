## What's going on

Nothing here is wrong on its own. The problem is that every value is hand-picked, with no shared scale, so the app is full of near-misses. Two things that are almost identical but not quite look like a mistake to the eye, and that's probably what people are reacting to.

- **Near-duplicate colors:** the primary button is `#2f6fed` in `.btn` and `#2e6dea` in `.btn-big`. The card border `#e3e5e8` and panel border `#e1e4e8` differ by one step. The success alert and badge greens are also close but not equal.
- **Three grays for one job:** `.muted`, `.hint`, and `.caption` are `#8a8f98`, `#8d929b`, and `#858a93`. They're the same role with three slightly different values.
- **Radii with no scale:** 4, 5, 6, 7, 9, 10, and 12px all appear. The button and input use 5 and 6, and the big button uses 7.
- **Shadows and padding that drift:** the card and panel share a shape but have different shadows (`0 2px 7px .12` vs `0 3px 9px .10`), paddings (18 vs 22), and radii (9 vs 12).
- **Controls that don't line up:** input is 38px tall and select is 40px. Their padding and radius also differ, so they sit side by side at different heights.
- **Irregular type and spacing:** headings go 31 / 23 / 19 / 17 with no consistent ratio. Margins are 14, 19, and 34, which don't come from one grid.
- **Muted text may fail contrast:** `#8a8f98` on white is roughly 3.2:1, below the 4.5:1 WCAG AA needs for body-size text. The other two grays are about the same.
- **Missing states:** nothing here defines hover, focus, or disabled styles, so interactive elements may feel inconsistent even when their base styles match.

## What I'd do, in order

1. **Define tokens before changing any values.** Put colors, radii, shadows, spacing, and type sizes into `:root` custom properties. Pick the scales on paper first. Suggested starting points:
   - Radius: 4 (small), 6 (controls), 8 (cards), 12 (panels and modals)
   - Spacing: 4px base, so 4 / 8 / 12 / 16 / 24 / 32
   - Type: 14 body, 16 / 20 / 24 / 32 headings
   - Shadow: three levels (sm, md, lg)

2. **Collapse the near-duplicates.** This has the most visible effect and the lowest risk. Use one primary blue, one border gray, one muted text color, and one success pair. Map each old value to the nearest token. Keep the old `.muted`, `.hint`, and `.caption` class names as aliases to a single token, so you don't need to edit markup yet.

3. **Fix the controls.** Make `.btn` a base with size modifiers (`--sm`, `--md`, `--lg`) instead of a separate `.btn-big` with its own values. Set input and select to one height (40px) with shared padding and radius. Also set `line-height` explicitly on buttons so their height doesn't depend on the browser default.

4. **Apply the type and spacing scales.** Replace the 14 / 19 / 34 margins and the 18 / 22 / 26 paddings with grid values. This is the most visible change, so review it page by page.

5. **Fix accessibility.** Raise the muted text color until it passes 4.5:1. `#6b7079` on white is about 5:1 and close to the current look. Add `:hover`, `:focus-visible`, and `:disabled` states for buttons and inputs.

6. **Add a guardrail.** Use stylelint to ban raw hex values and off-scale pixel values outside `:root`, so the drift doesn't come back.

I haven't changed any files. If you want, I can apply steps 1–3 to this stylesheet and show you the diff. I'd need to know whether the rest of the app uses these class names, so I don't break markup I can't see.
