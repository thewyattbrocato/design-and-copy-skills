Overall the structure is sound: the roles are semantic, every dark-theme override has a light counterpart, and the names are consistent. Before you hand this off, I'd fix the first two items, which are accessibility gaps the other team would otherwise have to rediscover.

## Fix before handoff

**1. `--color-border` fails non-text contrast.** WCAG 1.4.11 requires 3:1 for input boundaries and other UI components that carry meaning. By my hand calculation, `#d9d5cc` on `#fbfaf8` is about 1.4:1, and dark `#3a372d` on `#1f1d17` is about 1.4:1. Keep `--color-border` as a decorative divider, and add a control token such as `--color-border-control` at 3:1 or better in both themes. Check the exact values with a contrast tool, since I did these by hand.

**2. No focus token.** A warehouse tool will have keyboard and scanner-heavy workflows, so focus visibility matters. Add `--color-focus` (3:1 against both `--color-bg` and `--color-surface`, in both themes) and `--focus-ring-width`, or a `--focus-ring` shorthand.

## Should fix

3. **Dark mode elevation is nearly invisible.** Black shadows on near-black backgrounds do almost nothing, and the surface-to-bg step is small. Either lift surfaces further or pair `--shadow-raised` with a border in dark mode. Also set `color-scheme: light` on `:root` and `color-scheme: dark` on `[data-theme="dark"]`, or native inputs, scrollbars, and date pickers will stay light.
4. **Status colors need tints and an info role.** `danger`, `success`, and `warning` are text/icon colors only. Badges and banners need background tints (for example `--color-danger-subtle`) with matching text. Inventory states such as low stock, in transit, and on hold will likely need an `--color-info` role. Also state that status should never be color-only.
5. **Missing roles:** a scrim/backdrop color for modals (`--shadow-overlay` doesn't cover it), a disabled text/background pair, and a selection color if you have selectable table rows.
6. **Motion.** Document `prefers-reduced-motion` behavior, either by setting durations to 0 in a media query or by stating that the other team handles it. Also decide whether `--motion-slow` is needed for drawers and similar patterns.
7. **Theme mechanism.** The file defines only `[data-theme="dark"]`. Tell the other team whether they should also honor `prefers-color-scheme` as a default, and what sets the attribute.
8. **Typography gaps.** Add font families and weights, or document that they're owned elsewhere. Dense inventory tables often need a size below `--text-sm`, such as 12px, for captions and metadata. Each size also needs a paired line height, not just two global leading values.

## Nice to know

- **Spacing scale is non-linear** (1, 2, 3, 4, 6, 8, 12). That's fine, but the scale should be documented as intentional, including the missing 5, 7, 10, and 16. Otherwise someone will ask for `--space-5` and expect it to exist.
- **Units are mixed:** spacing is in px and type in rem. That's defensible, but it means spacing won't scale with user font-size preferences. Say so in the docs.
- **Hover direction flips between themes:** light hover darkens and dark hover lightens. That's the usual pattern, but make sure the other team doesn't assume a single direction.
- **Versioning:** before v1, add a short contract listing which names are stable and how you'll handle renames and deprecations.

If you want, I can write a revised version of the file with the border, focus, and status-tint tokens added and the dark-mode fixes applied, with contrast values verified in the file's comments.
