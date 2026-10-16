I'm working from your list only, not the code. Import counts show reach, not how the props are used, so check the few spots flagged below before committing.

## Merge

| Now | Becomes | Notes |
|---|---|---|
| Button, PrimaryButton, DangerButton | **Button** with `variant="primary｜secondary｜danger"` | These are the same behavior with different looks. Alias the old names, then codemod them. |
| LinkButton | `Button variant="link"` | It should render an `<a>` when given `href`. Check that it isn't doing anything special. |
| TextInput (35) into TextField (60) | **TextField** | TextInput is the 2021 legacy one. Deprecate it and migrate its 35 files. |
| Tag, StatusPill | One read-only **Badge** with `tone="neutral｜info｜success｜warning｜danger"` | Tag is the neutral tone. Both are read-only labels. Make StatusPill's tones carry an icon or text, not color alone, since "out of stock" and "ready for pickup" matter in a pharmacy. |
| Modal, ConfirmDialog | One dialog implementation | Keep ConfirmDialog as a thin preset (title, message, confirm and cancel buttons) built on Modal. Its 23 call sites don't change. |

## Keep separate

- **Chip** stays apart from Badge. It's interactive and removable, so it needs keyboard handling and remove semantics that a read-only label shouldn't carry.
- **IconButton** stays a thin wrapper over Button. It should require an accessible label and have a fixed square tap target, which matters on the kiosk.
- **SearchField and PasswordInput** stay as wrappers around TextField. Their behaviors (clear and submit, show and hide) aren't props that every field needs.
- **Drawer** stays separate from Modal, but they should share one focus-trap and scroll-lock primitive.
- **Toast** stays separate. It's non-modal and uses a live region.
- **Spinner and Skeleton** stay separate. They signal different things: unknown duration versus known layout.
- **LoadingOverlay** should compose Spinner. Don't merge them.
- **ProductCard and RefillCard** stay separate. They're domain components with different data. A refill involves Rx status, dates and actions, and shouldn't become a Card variant.

## Doing too much: Card

Card, with 23 props and flags like `showImage`, `showPrice`, `showRefillButton` and `showStockWarning`, is a product card, a refill card and a generic container all at once. Every new flag multiplies the states you'd have to design and test.

1. Reduce **Card** to a plain surface: padding, an optional media slot, and children.
2. Build **ProductCard** and **RefillCard** from it with explicit content, not `show*` flags.
3. Turn `showX` flags into slots or children. Turn `layout` into a small set of named layouts, or drop it if the kiosk and online layouts only differ in size.
4. Before the split, count how many of Card's 73 importers pass any `show*` prop: `[count from your repo]`. If most don't, the split is cheap. If most do, those files are really product or refill cards and will move to those components.

## Suggested order

1. Dialog primitive sharing and the Button variants. These are low risk and high count.
2. TextInput into TextField.
3. Badge, after you check that Tag has no links or other extras.
4. The Card split, which is the biggest job. Do it before the redesign so the redesign doesn't inherit 23 props.

The merges take your 29 listed components down to about 17 (or 14 if you count the thin wrappers as variants).
