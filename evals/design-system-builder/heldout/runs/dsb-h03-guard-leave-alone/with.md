The set is small and consistent, and the scales are sensible. Here's what I'd change before handoff, most important first.

**Fix before shipping**
1. **Borders are too faint for form controls.** I estimated `--color-border` at roughly 1.4:1 against the background in both themes. That's fine for dividers but fails the 3:1 that input and checkbox edges need. Split it into `--color-border` (subtle, for dividers and cards) and `--color-border-strong` (for control edges, about 3:1 or more). Please run a real contrast tool on this one, since my numbers are by hand.
2. **There are no `on-*` pairs for status colors.** Only `--color-on-action` exists. In dark mode, `danger`, `success` and `warning` are light tints, so white text on a filled danger button would fail. Add `--color-on-danger`, and the same for the other two if you'll ever fill with them.
3. **Status colors have no tinted backgrounds.** Badges, banners and toasts need something like `--color-danger-subtle`, `--color-success-subtle` and `--color-warning-subtle`. Without them, each team will invent its own. Add `--color-info` too, since you have no neutral status.
4. **No focus ring token.** Add `--color-focus` plus a ring width and offset. Handoff is when teams start improvising these.
5. **Dark mode has no raised-surface role.** Dark shadows barely show, so overlays need a lighter surface. Add `--color-surface-raised` (or `-overlay`), lighter than `--color-surface` in dark. Add `--color-surface-sunken` too if you have table headers or wells.
6. **Missing `color-scheme`.** Set `color-scheme: light` on `:root` and `color-scheme: dark` on `[data-theme="dark"]`, so native scrollbars and form controls follow the theme. Also decide whether the default follows `prefers-color-scheme`. Right now dark is opt-in only, so say so in the handoff notes.

**Tallyard-specific gaps**
7. **Numerals.** Inventory screens are mostly columns of quantities. Ship a `--font-numeric` or a documented `font-variant-numeric: tabular-nums` rule so counts align.
8. **Type is sizes only.** Add `--font-sans` and `--font-mono` (for SKUs and bin IDs), plus weights (regular, medium, bold). Pair a line-height with each size role, because `--leading-tight` and `--leading-body` aren't tied to anything yet.
9. **There's no size below 14px.** Dense tables often want 12px. Either add `--text-xs` or state that 14px is the floor.
10. **Touch targets.** If anyone uses this on handhelds or with gloves, add `--size-target-min` (44px or 48px) and a compact/comfortable density note. Otherwise the other team will pick row heights ad hoc.
11. **Status isn't color-only.** Low, out and in stock map to warning, danger and success. The guide should say every status needs an icon or label as well, for color-blind users and glare.

**Smaller items**
- Spacing names are multiples of 4px (`space-3` = 12px), so `space-5` and `space-7` are intentionally missing. That's fine, but write it down so nobody "fills the gaps".
- Motion: add a `prefers-reduced-motion` rule (durations near 0). If overlays will animate, add one longer duration, around 320ms.
- Z-index and border-width tokens are missing. They're cheap to add now and painful to retrofit.
- Naming is mostly role-based, which is good. `--color-action` is both a fill and a text/link color, so check that it works as a link color on `--color-surface`. It looks fine by my estimate (about 7:1).

**Looks good**
- Text, muted text, action, danger, success and warning all come out at roughly 5.9 to 7:1 on light surfaces by my estimate.
- Dark mode remaps roles rather than inverting values, and the accents are re-tuned for the dark ground.
- The scales are short, with no near-duplicates.

I assumed a web product with one brand and a small team. I only estimated the contrast ratios, so confirm them with a checker before you tell the other team they're verified.

I can write these additions into the CSS as a v1.1 block if you want.
