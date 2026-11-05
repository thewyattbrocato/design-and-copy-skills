No, it's not a good fix. It's a workaround for a problem that positive `tabindex` values create.

**Problems**
- Positive `tabindex` values pull those fields ahead of everything else on the page, including the header, nav and skip links. Keyboard users land in the form first, then jump back to the normal flow afterward.
- It's fragile. Any field added later without a `tabindex` goes to the end of the tab order, and any other form on the page with positive values will conflict with this one.
- The underlying issue is CSS `order` making the visual order differ from the DOM order. The `tabindex` values paper over that mismatch, and screen reader reading order still follows the DOM, which fails WCAG 2.4.3 (Focus Order) and 1.3.2 (Meaningful Sequence).

**Better fix**
1. Put the DOM in the order you want people to read and tab through: first name, last name, email, newsletter, Gift Aid, button.
2. Remove all `order` styles and all `tabindex` attributes.
3. Use `width:100%` or `flex-basis:100%` for layout where needed.

Native tab order then follows the source order with no extra attributes.

Your current `tabindex` values also don't match the visual order. Gift Aid is visually fourth (`order:4`) but has `tabindex='5'`, and the newsletter is visually fifth but has `tabindex='4'`. Keyboard focus therefore jumps between the two checkboxes in the opposite direction to what people see.
