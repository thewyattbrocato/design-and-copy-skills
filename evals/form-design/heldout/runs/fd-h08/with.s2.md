Your form already follows good practice: visible labels, correct input types and autofill tokens, "optional" marked in words, and a specific button label. I kept the structure and copy and fixed only the rendering details that look unpolished.

```html
<style>
  .kestrel-form { max-width: 420px; font-family: system-ui, sans-serif; }
  .kestrel-form label { display: block; }
  .kestrel-form input,
  .kestrel-form textarea {
    display: block; width: 100%; box-sizing: border-box;
    margin: 4px 0 16px; padding: 10px 12px;
    font: inherit; font-size: 16px;
    border: 1px solid #767676; border-radius: 6px;
  }
  .kestrel-form .hint { margin: 2px 0 0; font-size: 14px; color: #555; }
  .kestrel-form .hint + input { margin-top: 4px; }
  .kestrel-form button {
    min-height: 44px; padding: 0 24px;
    font: inherit; font-weight: 600;
    border: 0; border-radius: 6px; background: #1a56c4; color: #fff; cursor: pointer;
  }
</style>

<form class="kestrel-form" action="/contact" method="post">
  <h2>Get in touch</h2>
  <p>Questions about a repair or a quote? We reply within two business days.</p>
  <label for="name">Your name</label>
  <input id="name" name="name" autocomplete="name" required>
  <label for="email">Email</label>
  <input id="email" name="email" type="email" autocomplete="email" required>
  <label for="phone">Phone (optional)</label>
  <p class="hint" id="phone-hint">Only if you'd rather we call you back.</p>
  <input id="phone" name="phone" type="tel" autocomplete="tel" aria-describedby="phone-hint">
  <label for="msg">What can we help with?</label>
  <textarea id="msg" name="msg" rows="5" required></textarea>
  <button type="submit">Send message</button>
</form>
```

What changed:
- **Inputs:** they now use `box-sizing: border-box`, so 100% width no longer overflows the form. They also use `font: inherit` with a 16px size, so the textarea isn't monospace and iPhones don't zoom on focus. I added padding and a clear border.
- **Button:** it is now 44px tall and styled, with the same label.
- **Phone field:** I added a printed reason for asking. Change the hint wording if it doesn't match how you actually use phone numbers.

I left alone the labels, field order, required and optional marking, autofill tokens and the reply-time sentence.

I didn't add live validation or a confirmation screen. I can't see your `/contact` handler, so check that it shows a clear "thanks, we'll reply within two business days" message and keeps what people typed if something fails.
