I kept the `action`, `method`, and every field `id` and `name` the same, so your backend and anything that targets those fields won't break. The changes are all visual or accessibility improvements.

```html
<style>
  .kbr-form {
    max-width: 420px;
    padding: 24px;
    font-family: system-ui, sans-serif;
    color: #1f2933;
    background: #fff;
    border: 1px solid #e1e5ea;
    border-radius: 8px;
  }
  .kbr-form h2 { margin: 0 0 8px; font-size: 1.5rem; }
  .kbr-form p { margin: 0 0 24px; color: #52606d; line-height: 1.5; }
  .kbr-form label { display: block; font-size: 0.875rem; font-weight: 600; }
  .kbr-form .optional { font-weight: 400; color: #697586; }
  .kbr-form input,
  .kbr-form textarea {
    display: block;
    width: 100%;
    box-sizing: border-box;
    margin: 6px 0 18px;
    padding: 10px 12px;
    font: inherit;
    color: inherit;
    border: 1px solid #b8c0cc;
    border-radius: 6px;
  }
  .kbr-form textarea { resize: vertical; min-height: 120px; }
  .kbr-form input:focus,
  .kbr-form textarea:focus {
    outline: 2px solid #1d4ed8;
    outline-offset: 1px;
    border-color: #1d4ed8;
  }
  .kbr-form button {
    width: 100%;
    padding: 12px 16px;
    font: inherit;
    font-weight: 600;
    color: #fff;
    background: #1d4ed8;
    border: 0;
    border-radius: 6px;
    cursor: pointer;
  }
  .kbr-form button:hover { background: #1e40af; }
  .kbr-form button:focus-visible { outline: 2px solid #1d4ed8; outline-offset: 2px; }
</style>

<form class="kbr-form" action="/contact" method="post">
  <h2>Get in touch</h2>
  <p>Questions about a repair or a quote? We reply within two business days.</p>

  <label for="name">Your name</label>
  <input id="name" name="name" autocomplete="name" required>

  <label for="email">Email</label>
  <input id="email" name="email" type="email" autocomplete="email" required>

  <label for="phone">Phone <span class="optional">(optional)</span></label>
  <input id="phone" name="phone" type="tel" autocomplete="tel">

  <label for="msg">What can we help with?</label>
  <textarea id="msg" name="msg" rows="5" required></textarea>

  <button type="submit">Send message</button>
</form>
```

**What changed**
- **Layout:** Inline styles moved into one scoped stylesheet. The form now has a card with a border, rounded corners, and padding. `box-sizing: border-box` fixes the `width:100%` inputs overflowing their container once padding is added.
- **Inputs:** Roomier padding, visible borders, and fonts that inherit from the form instead of the browser's small default.
- **Focus states:** A clear blue outline on fields and the button, which helps keyboard users.
- **Button:** Full width, branded color, and a hover state.
- **Details:** "(optional)" is muted, and the textarea can only be resized vertically.

**Things to adjust**
- The blue (`#1d4ed8`) is a placeholder. Swap in your brand color, keeping enough contrast with white text.
- I didn't add a success or error message after submit. That depends on how `/contact` responds, so tell me what it returns if you want that.
