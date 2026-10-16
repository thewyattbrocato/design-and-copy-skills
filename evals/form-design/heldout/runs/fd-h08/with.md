The form's structure is already sound, so I left it alone. It has visible labels, correct input types, autofill tokens, "optional" marked in words, and a specific button. The polish is visual: type size, spacing, a real button, and a reason for the phone field.

```html
<style>
  .kbr-form { max-width: 420px; font: 16px/1.5 system-ui, sans-serif; }
  .kbr-form label { display: block; font-weight: 600; }
  .kbr-form .hint { margin: 0; font-size: 14px; color: #555; }
  .kbr-form input, .kbr-form textarea {
    display: block; width: 100%; box-sizing: border-box;
    margin: 4px 0 20px; padding: 10px 12px;
    font: inherit; border: 1px solid #767676; border-radius: 6px;
  }
  .kbr-form input:focus, .kbr-form textarea:focus,
  .kbr-form button:focus-visible { outline: 3px solid #1a5fb4; outline-offset: 2px; }
  .kbr-form textarea { resize: vertical; }
  .kbr-form button {
    min-height: 44px; padding: 0 24px;
    font: inherit; font-weight: 600; color: #fff; background: #1a5fb4;
    border: 0; border-radius: 6px; cursor: pointer;
  }
  .kbr-form button:hover { background: #154c91; }
</style>

<form class="kbr-form" action="/contact" method="post">
  <h2>Get in touch</h2>
  <p>Questions about a repair or a quote? We reply within two business days.</p>

  <label for="name">Your name</label>
  <input id="name" name="name" autocomplete="name" required>

  <label for="email">Email</label>
  <input id="email" name="email" type="email" autocomplete="email" required>

  <label for="phone">Phone (optional)</label>
  <p class="hint" id="phone-hint">Only if you'd prefer a call back.</p>
  <input id="phone" name="phone" type="tel" autocomplete="tel" aria-describedby="phone-hint">

  <label for="msg">What can we help with?</label>
  <textarea id="msg" name="msg" rows="5" required></textarea>

  <button type="submit">Send message</button>
</form>
```

What changed:
- **Layout and type:** Inputs are 16px, so phones don't zoom on focus. `box-sizing` is fixed so padded fields don't overflow the 420px column. Spacing is a little more generous, and the button is a 44px-tall touch target in a solid color.
- **Focus:** There's a visible focus outline on the fields and the button.
- **Phone hint:** I added "Only if you'd prefer a call back" so the phone field has a printed reason. Edit it if you use phone numbers differently.

I didn't add custom validation or error styling. The browser's built-in checks work for a form this small. If you want styled error messages, tell me and I'll add them.
