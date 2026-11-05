No, it's a brittle fix, and the real problem is the CSS `order`.

- **Positive tabindex is an anti-pattern.** It pulls those fields out of the natural tab order and puts them ahead of everything else on the page, including the header, nav and skip links. Every new field means renumbering by hand.
- **The numbers are also wrong.** Visual order by `order` is Email, Postcode, Street, Town, Password, but the tabindex order is Email (1), Password (2), Postcode (3), Street (4), Town (5). So Password is tabbed to second even though it appears last. The button at 9 is fine only by luck.
- **Root cause:** `order` changes the visual position but not the DOM or tab order, which fails WCAG 2.4.3 (focus order) and 1.3.2 (meaningful sequence).

**Better fix:** put the DOM in the intended order (Email, Postcode, Street, Town, Password, Button), delete every `order` and `tabindex`, and let the browser's natural order do the work. If the screen layout really needs to differ from the source order, fix the layout rather than the focus order.
