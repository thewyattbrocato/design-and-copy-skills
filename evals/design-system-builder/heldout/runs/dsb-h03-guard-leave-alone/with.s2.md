The tokens are a solid base. The values are coherent, the scales are short, and the names are by role. The gaps below are mostly missing tokens that the other team will otherwise invent on their own, so I'd close them before handoff.

I did the contrast math by hand, so treat the ratios as approximate. Text, muted text, action, danger, success and warning all pass 4.5:1 against their surfaces in both themes. `on-action` on action passes in both too.

## Fix before handoff

1. **No `color-scheme`.** Without `color-scheme: light` on `:root` and `color-scheme: dark` on the dark theme, native inputs, scrollbars and select menus stay light in dark mode.
2. **Dark mode only works via the attribute.** A user whose OS is set to dark gets light mode unless the app sets `data-theme`. Either document that the app owns this, or add a `prefers-color-scheme` fallback.
3. **No input-grade border.** `--color-border` (#d9d5cc) is about 1.4:1 on white. That's fine for dividers, but form fields and checkboxes need about 3:1 or they fail WCAG 1.4.11. Add `--color-border-strong`.
4. **No focus token.** Scanner-adjacent and keyboard-heavy screens need a visible focus ring. Add `--color-focus` plus a ring width and offset.
5. **No surface elevation in dark mode.** Dark `--shadow-overlay` at .6 alpha is nearly invisible on #1f1d17. Dark surfaces should get lighter as they rise, so add `--color-surface-raised` (and overlay). In light mode it can equal surface.
6. **Status colors are incomplete.** There's no `on-danger`, so a destructive button has no defined text color. There are also no subtle tints for banners and table-row states, and no info role. Tallyard will show low stock, out of stock and discrepancies constantly, so give these a defined pairing. Also state that status must never rely on color alone, so pair it with an icon or label.
7. **Type has sizes but no family, weight or numeric style.** Add `--font-sans`, `--font-mono` and weights (regular, medium, bold). For an inventory tool, document `font-variant-numeric: tabular-nums` for quantities, SKUs and table columns, or the digits won't line up.

## Should fix

- **Naming collision.** `--text-sm` is a size and `--color-text` is a color, and both start with `text`. Rename sizes to `--font-size-sm` and so on, while it's still cheap.
- **Spacing has no -5 or -7.** That's fine because the steps are well separated, but say so in the docs or people will add them. A 64px step for page-level layout is probably worth having.
- **Touch target token.** If this runs on handheld scanners or tablets with gloves, add `--size-target-min: 44px` (or larger) so the other team doesn't guess.
- **Motion.** Add a `prefers-reduced-motion` rule that zeroes the durations. Two durations and one easing is fine for v1.
- **Hover but no pressed state.** Add `--color-action-active`, or document that pressed reuses hover.
- **No raw tier.** Semantic-only is fine for one brand. Note that a second brand or a high-contrast theme would mean adding a raw ramp underneath.

## Fine as is

- The spacing scale (4px base, 7 steps).
- Two radii plus full, and two shadows.
- The warm neutrals and the restrained palette.
- The dark accents, which are re-tuned for the dark ground rather than inverted.

## Suggested additions

```css
:root {
  color-scheme: light;
  --color-border-strong: #8a8576;   /* ~3.5:1 on bg/surface */
  --color-focus: #1b5e8a;
  --focus-ring: 2px; --focus-offset: 2px;
  --color-surface-raised: #ffffff;
  --color-on-danger: #ffffff;
  --color-danger-subtle: #fbe9e7; --color-success-subtle: #e6f3ea; --color-warning-subtle: #fbf0d9;
  --font-sans: system-ui, sans-serif; --font-mono: ui-monospace, monospace;
  --weight-regular: 400; --weight-medium: 500; --weight-bold: 700;
  --size-target-min: 44px;
}
[data-theme="dark"] {
  color-scheme: dark;
  --color-border-strong: #7d7868;
  --color-focus: #6fb1de;
  --color-surface-raised: #27251e;
  --color-on-danger: #1f0a08;
  --color-danger-subtle: #3a1f1c; --color-success-subtle: #1b2e22; --color-warning-subtle: #33280f;
}
@media (prefers-reduced-motion: reduce) { :root { --motion-fast: 0ms; --motion-base: 0ms; } }
```

The subtle tints and `on-danger` values are proposals. I haven't checked them for contrast, so run the text-on-tint pairs before you ship.

**Assumptions:**
- I assumed a web product with one brand.
- I haven't seen how the components use these tokens, so some of the gaps above may already be handled locally.

Before handoff, also name an owner and a change process for the tokens (add, modify, deprecate). A one-page changelog is enough at v1.
