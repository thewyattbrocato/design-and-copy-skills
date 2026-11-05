No, it's not a good fix.

- **Positive tabindex is an anti-pattern.** Those fields jump ahead of everything else on the page, such as the skip link, header and nav. Every new field also forces you to renumber.
- **The cause is the CSS `order`.** The DOM order doesn't match the visual order, so the fix belongs in the markup.
- **It's already wrong.** The tab order goes Gift Aid (5) after Newsletter (4), but on screen Gift Aid appears first.

**Fix:** Put the elements in the DOM in the order you want them shown (first name, last name, email, Gift Aid, newsletter, button). Then delete all the `order` styles and `tabindex` attributes. Natural tab order will then match the visual order, and screen readers will read the form in that order too.
