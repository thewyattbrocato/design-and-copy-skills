Here's my read from the names, counts, and your context. I haven't looked at the code, so I'm assuming the names match what the components do.

## Merge
- **Button, PrimaryButton, DangerButton, LinkButton** become one `Button` with `variant="primary | secondary | danger | link"`. These are the same element with different styling, and the split is probably why 84 files use plain Button. This is the biggest win.
- **TextInput (35) into TextField (60).** Migrate the 2021 component's callers to the newer one and delete it. If TextField wraps TextInput internally, keep the bare input as a private primitive but stop exporting it.
- **Tag and StatusPill** could become one `Badge` with a `tone` prop, where neutral is today's Tag. This is optional and lower priority. Both are read-only labels, so the visual difference is mostly color. If StatusPill carries behavior like icons or accessible status text, keep them separate and have Tag reuse its styles.

## Keep separate
- **Chip.** It's interactive (removable), so it has focus, keyboard, and remove-button behavior that the read-only labels don't.
- **IconButton.** It needs a required accessible label and square sizing. Build it on top of the new Button instead of folding it in.
- **SearchField and PasswordInput.** They have real behavior (clear/submit, show/hide). Build both on TextField so they share label and error handling.
- **Drawer, Toast, and Modal.** They differ in interaction. Toast is non-blocking and announced via a live region, and Drawer has a different layout. Share a base overlay or focus-trap if they don't already.
- **ConfirmDialog.** Keep it as a preset, but make sure it's built on Modal rather than reimplementing it.
- **Spinner, Skeleton, LoadingOverlay.** These cover different loading cases. Just make sure LoadingOverlay uses Spinner.

## Doing too much: Card
Card is the problem. With 23 props and flags like `showPrice`, `showRefillButton`, and `showStockWarning`, it's a product card and a refill card disguised as a generic container. It also puts pharmacy domain logic in a base component.

I'd split it three ways:
- **Card** becomes a plain surface with slots (header, media, body, footer) and maybe 3–5 props.
- **ProductCard** and **RefillCard** compose Card and own their domain flags.
- Callers that pass `showX` flags move to whichever domain card fits.

Before committing, check how the 73 Card importers use it. If most pass few props, the flags come from a small group of callers. In that case migrating those callers to ProductCard or RefillCard is cheap. If the 14 ProductCard and 6 RefillCard files just wrap Card with preset flags, the split is mostly done already.

## Suggested order
1. Button variants, which is high impact and mechanical to migrate.
2. TextInput into TextField.
3. Card split.
4. Tag and StatusPill, only if the redesign needs it.

One thing to check for the kiosk: StatusPill states like "out of stock" and "ready for pickup" should not rely on color alone. Also check that the merged Button's touch targets are big enough for kiosk use.

I can grep the repo for how Card's flags are used, or draft the migration plan, if you point me at it. This directory is empty right now.
