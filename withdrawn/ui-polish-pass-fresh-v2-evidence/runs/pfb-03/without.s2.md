No, it's a workaround that creates new problems. Positive `tabindex` values are widely considered an anti-pattern.

- **Fragile:** Every new field means renumbering, and any element without a `tabindex` (links, other widgets) gets visited after all the numbered ones.
- **Mismatch persists:** Your DOM order is email, street, postcode, town, password, but the visual order is email, postcode, street, town, password. Screen readers and anything else that follows the DOM still get the "wrong" order. It also fails WCAG 2.4.3 (Focus Order) and 1.3.2 (Meaningful Sequence) in spirit.
- **Wrong as written:** Your tabindex values (email 1, password 2, postcode 3, street 4, town 5) don't match the visual order set by `order`, so tab order is email → password → postcode → street → town. That's neither the DOM order nor the on-screen one.

**Better fix:** Put the fields in the DOM in the order you want them displayed (email, postcode, street, town, password), drop the `order` styles and all `tabindex` attributes, and the native tab order will be correct. If the layout really requires reordering visually, use `tabindex="0"` or `-1` only where needed, and keep DOM and visual order aligned.
