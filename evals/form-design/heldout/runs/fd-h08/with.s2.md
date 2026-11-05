Your form is already in good shape. It has visible labels, the right input types and autofill tokens, "optional" marked in words, and a specific button label. I left the structure and copy alone and only fixed how it looks and feels on a phone:

```html
<form action="/contact" method="post" style="max-width:420px;font-family:system-ui,sans-serif">
  <h2>Get in touch</h2>
  <p>Questions about a repair or a quote? We reply within two business days.</p>
  <label for="name">Your name</label>
  <input id="name" name="name" autocomplete="name" required style="display:block;width:100%;box-sizing:border-box;margin:4px 0 20px;padding:10px;font:inherit;font-size:16px">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" autocomplete="email" required style="display:block;width:100%;box-sizing:border-box;margin:4px 0 20px;padding:10px;font:inherit;font-size:16px">
  <label for="phone">Phone (optional)</label>
  <input id="phone" name="phone" type="tel" autocomplete="tel" style="display:block;width:100%;box-sizing:border-box;margin:4px 0 20px;padding:10px;font:inherit;font-size:16px">
  <label for="msg">What can we help with?</label>
  <textarea id="msg" name="msg" rows="5" required style="display:block;width:100%;box-sizing:border-box;margin:4px 0 20px;padding:10px;font:inherit;font-size:16px"></textarea>
  <button type="submit" style="min-height:44px;padding:0 24px;font:inherit;font-size:16px">Send message</button>
</form>
```

What changed:
- **Text size:** the inputs are now 16px, so iPhones don't zoom in when someone taps a field. They also have padding and `box-sizing:border-box`, so they fit the 420px width.
- **Spacing and button:** there's slightly more space between fields. The button is at least 44px tall, so it's easy to tap.

Two things to check on your side:
- **Phone field:** it would be stronger with a short reason beside it, such as "Only if you'd like a call back". I didn't add one because I don't know how you use phone numbers.
- **Error handling:** the browser's built-in validation messages are fine to ship. If your partner wants it to feel more custom, the next step would be inline error messages written for the form. That needs a bit of JavaScript, and I can add it if you want.
