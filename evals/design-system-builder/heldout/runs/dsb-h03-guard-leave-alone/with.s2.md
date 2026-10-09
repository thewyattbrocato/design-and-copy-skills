The set is small and coherent. The spacing, radius and shadow scales are well-sized and the role names are good. I'd fix a few things before handing it over, because they're expensive to change once the other team has built on them.

I haven't seen your components or screens, so this review covers only the token file. My contrast numbers are rough estimates, so run them through a checker before relying on them.

## Change before shipping

1. **Input borders are too faint.** `--color-border` (#d9d5cc) on white is about 1.5:1. That's fine for dividers but fails the 3:1 that WCAG 1.4.11 asks for on input and control boundaries. Split the token:
   - `--color-border` for dividers and card edges.
   - `--color-border-strong` for inputs, checkboxes and anything interactive.
   - Light value: about `#8a8474`. Dark value: about `#6b6757`. Verify both.

2. **There are no status backgrounds or `on-` pairs.** Danger, success and warning exist only as text-weight colors. Banners, badges and table-row states need tinted fills, and a warehouse tool will show stock alerts everywhere. Add:
   - `--color-danger-bg`, `--color-success-bg` and `--color-warning-bg`, in both themes.
   - `--color-on-danger`, if you plan a solid danger button.
   - `--color-danger-hover`, since action has a hover state and danger doesn't.
   - Without these, each team will invent its own tints.

3. **There's no focus ring token.** Add `--color-focus` (it can point at the action color) plus a ring width and offset. This is the token teams most often skip, and then each component ends up with a different focus style.

4. **Dark mode has no way to show elevation.** There's one `--color-surface`, and shadows are nearly invisible on dark grounds. In dark themes, raised things should get lighter. Add `--color-surface-raised` and `--color-surface-overlay` for popovers, menus and modals. Light can map all three to #fff or close to it.

5. **Theme switching misses system preference and native controls.** Add:
   - `color-scheme: light` on `:root` and `color-scheme: dark` on `[data-theme="dark"]`, so scrollbars and native inputs match.
   - A `@media (prefers-color-scheme: dark)` block for `:root:not([data-theme="light"])`. Otherwise users who haven't picked a theme get light mode regardless of their OS setting.
   - Put the dark values in one shared block, not two copies.

6. **The type scale has no families or weights.** `--text-*` sizes alone leave the other team to guess. Add:
   - `--font-sans`, `--font-mono`, and weights for regular, medium and bold.
   - Pair each size with a line-height. `--leading-tight` and `--leading-body` are unattached right now, so say which sizes use which. For example, `xl` and `2xl` use tight, and the rest use body.
   - For an inventory tool, document `font-variant-numeric: tabular-nums` as the default for quantities and table numbers, so columns align.

## Should add (can ship as v1.1, but plan for it)

- **Touch target and density.** I'm assuming warehouse use on tablets or handhelds, possibly with gloves. If so, add `--size-target-min: 44px`, and consider a compact-density variant for dense tables. Say in the docs which one is the default.
- **Motion.** You have 2 durations and 1 easing. Add a `--motion-slow` (about 320ms) for overlays and an `--ease-in` for exits. Document a `prefers-reduced-motion` rule too: durations drop to about 0 or fall back to opacity-only.
- **Spacing ends at 48px.** Page-level layout usually wants a 64px step (`--space-16`). The numbering follows a 4px multiplier, which is fine, but say so in a comment. Otherwise the gaps (no 5, 7, 9–11) look like omissions.
- **Z-index and border width.** A short `--z-dropdown`, `--z-overlay`, `--z-toast` scale, plus `--border-width: 1px`, prevents `z-index: 9999` arms races.
- **Namespace.** If the other team's CSS may collide with yours, consider a prefix such as `--ty-`. Changing this later breaks every consumer.

## What I'd leave alone

- The radius scale (4, 8, full) and the two shadow levels are the right size.
- Role-based names (`--color-action`, `--color-on-action`, `--color-text-muted`) are good. Don't rename them to color names.
- The dark action color is re-tuned, not inverted. That's correct.
- By my estimate the text, action and status colors all clear 4.5:1 on their grounds in both themes. The only failing pair I found is the border above.

## Starter patch

```css
:root {
  color-scheme: light;
  --color-border-strong: #8a8474;
  --color-focus: var(--color-action);
  --color-surface-raised: #ffffff;
  --color-surface-overlay: #ffffff;
  --color-danger-hover: #8f1e18;
  --color-on-danger: #ffffff;
  /* tinted fills: pick and contrast-check against --color-text */
  --color-danger-bg: #fbeae8; --color-success-bg: #e6f3ea; --color-warning-bg: #fbf1dc;
  --font-sans: system-ui, sans-serif; --font-mono: ui-monospace, monospace;
  --weight-regular: 400; --weight-medium: 500; --weight-bold: 700;
  --size-target-min: 44px;
  --motion-slow: 320ms; --ease-in: cubic-bezier(.4,0,1,1);
}
[data-theme="dark"] {
  color-scheme: dark;
  --color-border-strong: #6b6757;
  --color-surface-raised: #26241d;
  --color-surface-overlay: #2d2b23;
  --color-danger-hover: #f6a39d;
  --color-on-danger: #2a0c0a;
  --color-danger-bg: #3a1f1c; --color-success-bg: #1b2f23; --color-warning-bg: #35290f;
}
```

All hex values in the patch are proposals. I haven't contrast-checked them.

Before you hand over, decide who owns changes after v1 and how deprecations will be announced. Even a one-page changelog is enough.
