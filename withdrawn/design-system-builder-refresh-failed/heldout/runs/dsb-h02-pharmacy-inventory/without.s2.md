Here's my read from the list alone. I haven't looked at the code, so check the prop APIs before committing.

## Merge

- **Buttons:** Make `PrimaryButton`, `DangerButton` and `LinkButton` variants of `Button` (`variant="primary" | "danger" | "link"`). They're almost certainly styling differences, and 62 imports would move to one component. Keep `IconButton` as its own component built on `Button`. It should require an `aria-label`, which is worth enforcing.
- **Text inputs:** Migrate `TextInput` (the 2021 one, 35 imports) to `TextField`, then deprecate it. Two inputs with different label and error behavior is a real accessibility risk on a pharmacy form.
- **Tag and StatusPill:** Merge them into one badge-style primitive with a `tone`. Keep `StatusPill` as a thin wrapper with a fixed status enum (ready, out of stock, and so on), so the status vocabulary stays consistent. Make sure status never relies on color alone.

## Keep separate, but build on shared bases

- **Chip:** It's interactive and removable, with keyboard and focus behavior that Tag doesn't have. Don't fold it into Tag.
- **Modal, ConfirmDialog and Drawer:** `ConfirmDialog` should stay a thin preset on `Modal`. It has 23 users and a consistent pattern. `Drawer` can share the overlay and focus-trap logic with `Modal`.
- **Toast:** It's non-blocking and has a different ARIA role, so it stays its own component.
- **SearchField and PasswordInput:** Keep them as specializations of `TextField`. They have real behavior (clear and submit, show/hide).
- **Spinner, Skeleton and LoadingOverlay:** They serve different purposes. Just have `LoadingOverlay` compose `Spinner`.
- **ProductCard and RefillCard:** Keep them. See below.

## Doing too much: `Card`

A 23-prop `Card` with `showPrice`, `showRefillButton` and `showStockWarning` is a god component. It has product and refill logic baked into a generic container, and `ProductCard` and `RefillCard` already exist for those cases. The `show*` booleans also create combinations nobody tests.

I'd split it:
1. `Card` becomes a plain container (header, body and footer slots, plus a few layout and variant props).
2. `ProductCard` and `RefillCard` compose it.
3. Audit the 73 `Card` importers. Most are probably using it as a product or refill card, and those should move to the specific components.

This is the biggest piece of work and the one the redesign will hit hardest, so do it first.

## Caveats

- Import counts show reach, not how each component is used. Before merging, check how many distinct prop combinations each of `Button`'s variants and `Card` actually see.
- The in-store kiosk probably needs larger touch targets. Make sure the consolidated `Button` and `TextField` have a size prop that covers that, rather than the kiosk forking them again.

## Suggested order

1. `Card` split
2. `TextInput` → `TextField`
3. Button variants
4. Tag and StatusPill
5. Shared overlay base for `Modal` and `Drawer`

If you export the prop definitions for `Card` and `Button`, I can draft the new APIs and a migration plan.
