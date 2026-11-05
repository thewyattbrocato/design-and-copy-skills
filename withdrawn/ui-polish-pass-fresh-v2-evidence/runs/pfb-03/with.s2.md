No, it's not a good fix, and it doesn't work here anyway.

- **It's wrong now.** The tab order is email → password → postcode → street → town → button. On screen, `order` puts password fifth, after town. Keyboard users jump from email to password and then back up.
- **Positive `tabindex` is an anti-pattern.** Those fields get focus before everything else on the page, including the header and nav. Every new field means renumbering, and screen-reader users get an order that disagrees with the reading order.
- **The real problem is that the DOM order differs from the visual order.** Tab order follows the DOM, so the fix is to put the DOM in the order you want to see.

Reorder the markup (email, postcode, street, town, password, button). Then drop every `tabindex` and every `order` style:

```html
<form class="signup" style="display:flex;flex-direction:column">
  <label>Email <input name="email" type="email"></label>
  <label>Postcode <input name="postcode"></label>
  <label>Street <input name="street"></label>
  <label>Town <input name="town"></label>
  <label>Password <input name="pw" type="password"></label>
  <button>Create account</button>
</form>
```

If you have to keep the CSS reordering, use `tabindex="0"` or no `tabindex` and keep the DOM in logical order. Don't use positive values.
