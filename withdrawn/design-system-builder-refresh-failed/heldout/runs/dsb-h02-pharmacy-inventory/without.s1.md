I'm working only from your names, counts, and descriptions. I haven't seen the code, so check the "verify" notes before committing. By my count this takes 22 components down to 17.

## Merge (5 components go away)

- **PrimaryButton, DangerButton, LinkButton → `Button` variants** (`primary`, `danger`, `link`). They're the same component with different styling, and a codemod can handle the 62 imports. Verify that LinkButton doesn't render an `<a>`. If it does, keep that as an `as`/`href` option on Button.
- **TextInput → TextField.** This is a migration, not a design decision. TextField is the newer wrapper, with label and error text. Deprecate TextInput (35 imports) and move those files over. Check whether SearchField and PasswordInput are built on the old TextInput, since they'd need to move too.
- **Tag + StatusPill → one `Badge` with a `tone` prop.** Both are read-only labels, so the only real difference is semantic color. This is the least certain merge. If StatusPill has status-specific logic like icons or mapping from order states, keep that logic as a thin wrapper over Badge. For a pharmacy, status such as "out of stock" should keep an icon or text cue, not rely on color alone.

## Keep separate

- **Chip.** It's interactive (removable), while Tag and StatusPill are read-only. Different behavior and accessibility needs.
- **IconButton.** It needs a required `aria-label` and square sizing. Build it on top of Button, but keep it as its own component.
- **Modal, ConfirmDialog, Drawer, Toast.** They look similar but behave differently. Toast is non-blocking, and Drawer has its own layout and focus handling. Verify that ConfirmDialog is built on Modal, and share a base dialog primitive with Drawer if they don't already.
- **SearchField and PasswordInput.** They add real behavior (clear and submit, show/hide). They should wrap TextField.
- **ProductCard and RefillCard.** They represent different domain objects.
- **Spinner, Skeleton, LoadingOverlay.** They solve different problems. LoadingOverlay should just compose Spinner.

## What's doing too much: Card

Card has 23 props, including `showPrice`, `showRefillButton` and `showStockWarning`. That means a generic container has absorbed what ProductCard and RefillCard are supposed to do. At 73 imports, it's the biggest risk in the redesign.

- Reduce Card to a plain surface: padding, variant, layout, and slots for children.
- Move the pharmacy-specific `show*` logic into ProductCard and RefillCard.
- Before you start, grep which `show*` combinations are actually used. I'd expect most of the 73 call sites to use two or three patterns, which would make the migration mostly mechanical.
- Check whether the kiosk relies on `layout` differently from the online site.

## Suggested order

1. Card split. It has the highest payoff and the most risk, so scope it first.
2. TextInput → TextField migration.
3. Button variant codemod.
4. Tag/StatusPill merge, once the designers confirm the tone set.

If you can export the Card call sites, or its prop usage counts, I can sort them into the patterns that will drive the split.
