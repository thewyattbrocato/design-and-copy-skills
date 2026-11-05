Your form is already in good shape: visible labels, correct input types, autofill tokens, "optional" marked in words, and a specific button label. I kept the structure and changed only the polish that was missing.

```html
<form action="/contact" method="post" style="max-width:420px;font-family:system-ui,sans-serif;font-size:16px;line-height:1.4">
  <h2>Get in touch</h2>
  <p>Questions about a repair or a quote? We reply within two business days.</p>
  <label for="name">Your name</label>
  <input id="name" name="name" autocomplete="name" required style="display:block;box-sizing:border-box;width:100%;min-height:44px;padding:8px 10px;font:inherit;margin:4px 0 20px">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" autocomplete="email" autocapitalize="off" spellcheck="false" required style="display:block;box-sizing:border-box;width:100%;min-height:44px;padding:8px 10px;font:inherit;margin:4px 0 20px">
  <label for="phone">Phone (optional)</label>
  <input id="phone" name="phone" type="tel" autocomplete="tel" style="display:block;box-sizing:border-box;width:100%;min-height:44px;padding:8px 10px;font:inherit;margin:4px 0 20px">
  <label for="msg">What can we help with?</label>
  <textarea id="msg" name="msg" rows="5" required style="display:block;box-sizing:border-box;width:100%;padding:8px 10px;font:inherit;margin:4px 0 20px"></textarea>
  <button type="submit" style="min-height:44px;padding:0 24px;font:inherit;font-weight:600">Send message</button>
</form>
```

What changed:
- **Text size:** Inputs and the button now use 16px text, so phones don't zoom in when a field is focused.
- **Touch targets:** Fields and the button are at least 44px tall, with inner padding.
- **Width fix:** `box-sizing:border-box` stops the 100%-wide fields from overflowing the form once they have padding.
- **Email field:** Auto-capitalize and spellcheck are off.
- **Spacing:** The gap between field groups is a bit larger than the gap between a label and its field.

Two notes:
- The phone field doesn't say why you ask for it. If you want it, add a short reason under the label, such as "Only if you'd like a call back". Otherwise drop the field. I didn't invent the wording for you.
- I left the browser's built-in `required` validation alone. If your partner wants custom error messages, tell me and I'll add them, with a message next to each field.
