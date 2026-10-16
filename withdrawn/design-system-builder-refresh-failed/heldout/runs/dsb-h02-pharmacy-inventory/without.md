I'm working from names, import counts and your notes only. I haven't read any of the code, so check each point below against the actual components.

## Merge

- **PrimaryButton, DangerButton and LinkButton go into Button as `variant="primary" | "danger" | "link"`.** These are the same element with different styling. That's 62 files to migrate, but the change is mostly mechanical, so a codemod should handle it.
- **TextInput goes into TextField (35 files).** TextInput is the 2021 version and TextField is its replacement. Migrate the callers, then delete the old component. If TextField wraps TextInput, keep the bare input as an internal, unexported primitive.

## Keep separate, but make sure they share internals

- **IconButton:** It could be a Button variant, but icon-only buttons need a required `aria-label` and square sizing. Keep it as a thin wrapper around Button.
- **ConfirmDialog:** This should be a preset built on Modal. If it has its own overlay and focus-trap code, fix that instead of merging.
- **Drawer:** Only 7 files use it, but it shares overlay, focus and escape-key behavior with Modal. Share those internals and keep the two components separate.
- **SearchField and PasswordInput:** These are specialized wrappers (clear icon, show/hide toggle). They should be built on TextField, not merged into it.
- **LoadingOverlay:** It should compose Spinner.

## Leave alone

- **Chip, Tag and StatusPill:** Chip is interactive and removable, so it stays separate. Tag and StatusPill look alike, but StatusPill carries meaning ("out of stock", "ready for pickup"). That meaning needs consistent tones and a text or icon cue, not color alone. Merging them would invite people to use Tag where a status belongs. At most, share a base style.
- **Toast:** It's non-modal and uses `aria-live`, which is a different job from Modal.
- **Spinner and Skeleton:** Inline activity and content placeholders are different jobs.
- **ProductCard and RefillCard:** They show different data (refill ones presumably carry Rx and due-date information). Don't merge them with each other.

## What's doing too much: Card

Card has 23 props, including `showRefillButton` and `showStockWarning`. That means a generic container has pharmacy business logic baked in. It's also the most widely used component after Button, at 73 imports.

1. Find which of the 73 usages pass any `show*` or `layout` props. I'd guess many are plain containers.
2. Reduce Card to a dumb container, with padding, elevation and slots for header, body and footer.
3. Move the product and refill behavior into ProductCard and RefillCard, which are presumably already wrappers. Callers that pass `showPrice` and similar props move to those components.
4. Keep `variant` only if it's purely visual.

## Suggested order

1. Card split. It carries the most risk, and the redesign will be much harder if you don't do it first.
2. The Button variants.
3. TextInput to TextField.
4. The shared-internals cleanup for Modal, ConfirmDialog and Drawer.

For the design lead, the headline is that this should remove about 5 components (PrimaryButton, DangerButton, LinkButton, TextInput and the bloated Card). The rest should stay, because merging them would hide real differences in behavior or accessibility.

If you give me the repo path, I can check how many Card usages pass the `show*` props and whether ConfirmDialog and LoadingOverlay actually build on Modal and Spinner.
