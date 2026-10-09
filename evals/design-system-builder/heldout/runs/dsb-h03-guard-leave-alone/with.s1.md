The base is sound. The names are role-based, the scales are short, and dark mode remaps roles instead of inverting them. Dark surfaces also get lighter as they rise. The main gaps are tokens a warehouse UI will need on day one. If they're missing, the other team will invent their own values, which defeats the handoff.

I assumed a web product with one brand and a small team. I estimated contrast by eye and didn't compute it. The text, action and status pairs look comfortably above 4.5:1 in both themes, but run a checker before you ship.

## Fix before handoff

1. **Add a stronger border for form controls.** `--color-border: #d9d5cc` on white is roughly 1.4:1. That's fine for dividers, but input, checkbox and select edges need about 3:1 to be visible. Add `--color-border-strong` for both themes. Scanner and tablet users in bright aisles will notice this first.
2. **Add a focus ring token.** For example `--color-focus` plus a width and offset. Without it, every component will pick its own focus style.
3. **Add status backgrounds and "on" colors.** `danger`, `success` and `warning` work as text or icon colors, but low-stock and out-of-stock badges and alerts need fills. Add `--color-danger-subtle` (and the same for success and warning), and `--color-on-danger` for filled buttons. Decide whether you need `info`, since receiving and in-transit states often do.
4. **Add disabled and scrim tokens.** Add `--color-text-disabled` and `--color-scrim` for modal backdrops. `--shadow-overlay` alone is weak in dark mode, where shadows barely show. Either add `--color-surface-overlay` (lighter than surface in dark) or accept the weak shadow and say so.
5. **Fill in the type tokens.** You have sizes and leadings but no `--font-sans`, no weights, and no tabular figures. Quantities and SKUs in table columns need `font-variant-numeric: tabular-nums`, so give that a token or a utility. Consider a `--text-xs` (0.75rem) as well. Dense tables will want something under 14px, and if it isn't there people will hard-code it.
6. **Add a touch-target token.** For example `--size-target-min: 44px`. Warehouse use means gloves, handhelds and rushed taps, so this is your most product-specific token.
7. **Declare `color-scheme`.** Add `color-scheme: light` on `:root` and `color-scheme: dark` on `[data-theme="dark"]`, so native controls and scrollbars follow the theme. Also decide whether you honor `prefers-color-scheme` by default, with `data-theme` as the override. Say which in the docs.

## Smaller changes

- **Mixed units.** Type is in rem and spacing is in px, so users who scale their font won't get proportional spacing. Pick this on purpose and document it, or move spacing to rem.
- **Spacing names.** `space-1/2/3/4/6/8/12` are 4px multiples with gaps in the numbering. That's fine, but state the rule in a comment. Consider `--space-16: 64px` for page-level gutters.
- **Hover without pressed.** You have `action-hover` but no pressed state. Either add it or document that pressed reuses hover.
- **Reduced motion.** Add a rule for `prefers-reduced-motion`, such as setting the durations to near 0 in a media query. It's cheap to do now and awkward to retrofit.
- **Easing.** One easing is enough for v1. Say that `--ease-out` is the default so people don't add more.
- **Raw tier.** Going straight to semantic values is fine for one brand and two themes. Note that a raw ramp layer gets introduced only if you add a brand or a high-contrast theme.

## Handoff package

The CSS block alone isn't enough. Add these:

- A single source file, such as JSON exported to CSS and the design tool, so the two can't drift.
- A version tag and a changelog.
- A named owner for token changes.
- A deprecation rule: announce the change, provide a migration, then remove.
- One line on how the other team requests a new token. The default should be "reuse an existing one, or ask".

I can write the revised CSS with these additions. The new hex values would be proposals until contrast is verified.
