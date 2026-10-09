The set is in good shape. Contrast is solid and the dark theme overrides only what needs to change. These are the changes I'd make before handing it over, most important first.

**Fix before shipping**

1. **Border contrast is too low for form controls.** `--color-border` (#d9d5cc on #fbfaf8) is about 1.4:1, and the dark border is about 1.5:1. That's fine for dividers, but if the other team uses it on inputs, checkboxes, or buttons, it fails WCAG 1.4.11, which needs 3:1. Add a `--color-border-strong` (around #8a8575 in light) for interactive controls and document which one is for what.
2. **No focus ring token.** Without `--color-focus` (and maybe `--focus-ring-width` and `--focus-ring-offset`), every consumer will invent their own. In a keyboard-heavy tool like yours this matters.
3. **Add `color-scheme`.** Set `color-scheme: light` on `:root` and `color-scheme: dark` on `[data-theme="dark"]`. Otherwise native scrollbars, date pickers, and form controls stay light in dark mode.
4. **No tinted backgrounds for status colors.** You have danger, success, and warning as foregrounds, but nothing for banners, badges, or table rows. For stock states like low, out, and received, you'll want `--color-danger-subtle`, `--color-success-subtle`, and `--color-warning-subtle`. Check that each pairs with its base color at 4.5:1 or better in both themes.

**Gaps I'd fill (the other team will hit these quickly)**

- **Type:** there's no `--text-xs` (dense tables usually need 12px), no font-family tokens, and no weight tokens. For SKUs and quantities, add a `--font-mono` and consider a note or token for `tabular-nums`. Also pair line-heights with sizes, because `--leading-tight` and `--leading-body` aren't tied to anything yet.
- **Touch targets:** if people use this on handhelds or with gloves, add something like `--size-touch-min: 44px` (or 48px). It's the most Tallyard-specific token you could add.
- **Interaction states:** there's no `--color-action-active` or disabled tokens. There's also nothing for row hover or selected, which a table-heavy product needs.
- **Reduced motion:** add a `prefers-reduced-motion` block that zeroes out `--motion-fast` and `--motion-base`. This is one small block and spares every consumer from handling it.
- **Missing scales:** there's no z-index scale (dropdown, modal, toast) and no `--radius-lg`. Both are cheap to add now and painful to retrofit.

**Minor notes**

- The spacing scale skips 5 and 7 (20px, 28px). That's fine if you do it on purpose, but say so in the comment, because people will ask.
- Dark mode only works through `data-theme`. If you want it to follow the OS by default, add a `prefers-color-scheme` fallback. Otherwise state that it's opt-in.
- Everything is semantic with no primitive palette underneath. That's fine for v1, but adding a brand color or a third theme later will mean touching every role.

I checked contrast for text, muted text, action, on-action, and the status colors against their surfaces in both themes. All of them pass AA, and I found nothing else to change in the color values. I estimated the ratios by hand rather than running a tool, so run a checker over the final values, especially the new subtle backgrounds.

I can draft the additions as a patch to the CSS if you'd like.
