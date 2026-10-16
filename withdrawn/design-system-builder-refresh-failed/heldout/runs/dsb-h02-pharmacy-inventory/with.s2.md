I've only seen names and import counts, not the code, so check the two judgment calls (marked below) against the source before committing.

## Merge

| Now | Becomes | Why |
|---|---|---|
| Button, PrimaryButton, DangerButton, LinkButton | One `Button` with `variant` (primary, secondary, danger, link) | They behave the same and differ only in look. LinkButton should render an `<a>` when given `href`. |
| TextInput (35) into TextField (60) | `TextField` only | TextInput is the 2021 version and TextField wraps it with label and error text. Migrate the 35 files, then deprecate TextInput. Keep a bare input as an internal primitive, not a public component. |
| Tag, StatusPill | One read-only `Badge` with `tone` (neutral, success, warning, danger, info) | Both are read-only labels. **Check first:** if StatusPill carries an icon or a fixed status vocabulary that Tag doesn't, keep that vocabulary as a restricted set of tones. Don't let "ready for pickup" and "out of stock" become free-form colors. |

## Keep separate

- **Chip:** it's interactive (removable), so it needs keyboard handling and a remove label that Badge shouldn't carry.
- **IconButton:** build it on Button, but keep it separate so it requires an accessible label. On the kiosk it also needs a larger touch target.
- **ConfirmDialog:** keep it as a thin preset over Modal. It has a different role (alertdialog), fixed actions and a destructive-action pattern, and 23 files depend on it.
- **Drawer and Toast:** different placement and behavior (Toast is non-modal). Have Modal and Drawer share one focus-trap/overlay primitive.
- **SearchField and PasswordInput:** they add behavior (clear/submit, show/hide). Build both on TextField so label and error handling stay consistent.
- **Spinner, Skeleton, LoadingOverlay:** three different jobs (indeterminate wait, content placeholder, blocking wait). LoadingOverlay can just compose Spinner. Leave them alone, since they aren't worth redesign time.

## Doing too much: Card

Card has 23 props, and the `showImage`, `showPrice`, `showRefillButton` and `showStockWarning` flags show that ProductCard and RefillCard are hiding inside it. Fix it in the opposite direction from the others:

- **Card** becomes a plain surface: padding, elevation, `variant`, and a header/body/footer layout.
- **ProductCard** (14) and **RefillCard** (6) become composed components that use Card. They own their own data: price and stock for products, Rx and refill status for refills.
- Don't fold the other two into Card. That would make the 23 props worse.

Card has 73 importers, so migrate in steps. For each file, find which show-flag combination it uses, which tells you whether it's really a product or refill card. Keep the old props working with a deprecation warning during the move.

## Order of work

1. **Card split.** It carries the most risk and the most redesign value.
2. **TextInput into TextField.** It's a mechanical migration and makes error and label handling consistent.
3. **Button family.** It's the most imports (146 across the five), but the change is easy.
4. **Badge.** Do it last, after you've confirmed the StatusPill question.

Two notes:
- Because the kiosk is a touch surface, settle target sizes and a kiosk density setting as tokens during the Button and TextField work, not per component.
- I haven't checked whether a component is imported by both the online and kiosk apps. That could change the migration order.
