The palette is in good shape: the text and action colors pass WCAG AA in both themes, and the dark theme's muted text is readable. Most of what I'd change is missing coverage that the other team will hit right away. I estimated the contrast ratios by hand, so run the pairs through a checker before you ship.

**Fix before handoff**

1. **`--color-border` fails non-text contrast in light mode.** `#d9d5cc` on white is about 1.5:1. WCAG 1.4.11 asks for 3:1 on any border that identifies a control, such as an input or checkbox. Keep this value for dividers and add a stronger token for control borders, e.g. `--color-border-strong` at roughly `#8a8478` or darker.
2. **No focus token.** Keyboard focus is unspecified, and the other team will improvise it. Add `--color-focus` and `--focus-ring-width` (2px is typical). Make sure focus is visible against both `--color-bg` and `--color-surface`.
3. **Hover direction flips between themes.** In light mode `--color-action-hover` is darker than the action color. In dark mode it is lighter. That is a reasonable choice, but state it in the docs so nobody "fixes" one side.
4. **Mixed units with no base.** Spacing is px and type is rem. This works, but document that type scales with the user's browser font size and spacing does not. Otherwise someone will try to convert one to the other.

**Gaps for a warehouse tool**

- **Touch target size.** Handheld scanners and tablets on the floor need a minimum hit size, usually 44px or more. Add `--size-touch-target`.
- **Tabular numerals for counts.** Quantities and SKUs in tables should align. Add a `--font-numeric` token or a utility with `font-variant-numeric: tabular-nums`.
- **Surface variants for tables.** You have no muted surface for row striping, header rows, or disabled inputs. Add something like `--color-surface-muted` and `--color-surface-sunken`.
- **Status colors on fills.** `--color-on-action` exists, but there is no matching `--color-on-danger`, `--color-on-success`, or `--color-on-warning`. Any badge or alert that uses those colors as a background will need them. Check both themes for these pairs too.
- **Status is not color-only.** Tokens can't enforce this, but the docs should say that danger, warning, and success always pair with an icon or label, since warehouse lighting and color vision both vary.
- **Font family and weights.** Neither exists. Add `--font-sans`, `--font-mono` if SKUs or codes use monospace, and a short weight set.
- **Reduced motion.** Add a `@media (prefers-reduced-motion: reduce)` block that sets the motion durations to 0ms or near it.
- **Dark theme and OS preference.** Dark only applies under `[data-theme="dark"]`. Decide whether to also honor `prefers-color-scheme` when no attribute is set, and document which one wins.

**Structure**

- **Two-tier naming.** There are no primitives, so the dark block repeats hex values and raw colors are scattered across roles. Consider a primitive ramp (`--blue-600`, etc.) that roles reference. This is easier to maintain now than after the other team has built on the role names.
- **Dark shadows barely register.** A `rgba(0,0,0,.5)` shadow on `#15140f` is nearly invisible. Lean on the surface step and border for elevation in dark mode, or accept flat cards there.
- **Z-index and overlay scrim.** A `--z-*` scale and a scrim color (`--color-scrim`) prevent conflicts when modals, toasts, and dropdowns stack.

**Minor**

- `--text-md` is a confusing name for body text. If `--text-md` stays, document it as the body size. Renaming it to `--text-base` before v1 is cheaper than after.
- The spacing scale skips 20px and 40px. That's fine if intentional; say so in the docs so nobody asks for `--space-5` later.

If you want, I can write the additions as a diff against this file, with the focus, border, and touch-target tokens included.
