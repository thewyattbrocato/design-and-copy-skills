No, it's a fragile fix, and here it's also wrong.

- **Positive `tabindex` is an anti-pattern.** It pulls those elements out of the natural tab sequence. Any new field, or any element without a tabindex like links, the header or the cookie banner, ends up in a different place. It's hard to maintain.
- **The root cause is that the DOM order doesn't match the visual order.** The `order:` values in the CSS cause that. Screen readers and keyboard users follow the DOM, so the fix is to put the DOM in the right order (Email, Postcode, Street, Town, Password, button). Then remove both `order` and `tabindex`.
- **The current values don't match the layout anyway.**
  - Password is shown 5th but is tabbed 2nd.
  - The button has no `order`, so it defaults to 0 and renders at the top of the form. It is tabbed last.

If you must keep a layout that differs from the source order, don't use positive tabindex. Reorder the markup instead.
