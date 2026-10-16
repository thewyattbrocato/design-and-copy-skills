I kept the `action`, `method`, field names, `id`s, `autocomplete`, and `required` attributes as they were, so your backend and anything reading the submissions won't notice a change. The polish is all in the presentation.

```html
<style>
  .kbr-form {
    max-width: 420px;
    padding: 28px;
    font-family: system-ui, sans-serif;
    color: #1f2933;
    background: #fff;
    border: 1px solid #e1e5ea;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgb(0 0 0 / 0.06);
  }
  .kbr-form h2 { margin: 0 0 8px; font-size: 1.5rem; }
  .kbr-form p  { margin: 0 0 24px; color: #52606d; line-height: 1.5; }
  .kbr-form label {
    display: block;
    margin-bottom: 6px;
    font-size: 0.875rem;
    font-weight: 600;
  }
  .kbr-form input,
  .kbr-form textarea {
    display: block;
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 18px;
    padding: 10px 12px;
    font: inherit;
    color: inherit;
    border: 1px solid #b8c1cc;
    border-radius: 8px;
    background: #fff;
  }
  .kbr-form textarea { resize: vertical; min-height: 120px; }
  .kbr-form input:focus,
  .kbr-form textarea:focus {
    outline: 2px solid #1d6fd8;
    outline-offset: 1px;
    border-color: #1d6fd8;
  }
  .kbr-form input:user-invalid,
  .kbr-form textarea:user-invalid { border-color: #c0392b; }
  .kbr-form button {
    width: 100%;
    padding: 12px 16px;
    font: inherit;
    font-weight: 600;
    color: #fff;
    background: #1d6fd8;
    border: 0;
    border-radius: 8px;
    cursor: pointer;
  }
  .kbr-form button:hover { background: #165bb3; }
  .kbr-form button:focus-visible { outline: 2px solid #1d6fd8; outline-offset: 2px; }
</style>

<form class="kbr-form" action="/contact" method="post">
  <h2>Get in touch</h2>
  <p>Questions about a repair or a quote? We reply within two business days.</p>

  <label for="name">Your name</label>
  <input id="name" name="name" autocomplete="name" required>

  <label for="email">Email</label>
  <input id="email" name="email" type="email" autocomplete="email" required>

  <label for="phone">Phone (optional)</label>
  <input id="phone" name="phone" type="tel" autocomplete="tel">

  <label for="msg">What can we help with?</label>
  <textarea id="msg" name="msg" rows="5" required></textarea>

  <button type="submit">Send message</button>
</form>
```

**What changed**
- **Layout:** the form now sits in a card with padding, a subtle border, and rounded corners. Spacing and type sizes are consistent.
- **Styles:** the repeated inline styles moved into one scoped `<style>` block under `.kbr-form`, so they won't affect the rest of your site.
- **Inputs:** `box-sizing: border-box` fixes the width overflow that `width:100%` plus padding would otherwise cause. The inputs inherit the font and have clear borders.
- **Focus and errors:** keyboard focus shows a visible blue ring. Invalid fields get a red border, but only after the user has interacted with them (`:user-invalid`).
- **Button:** it's full width, in your accent color, with hover and focus states.

**Things to adjust**
- I picked the blue (`#1d6fd8`) as a placeholder. Swap in Kestrel's brand color, and keep enough contrast with the white button text.
- Browsers that predate `:user-invalid` simply won't show the red border. Nothing breaks.

If your partner has something specific in mind, like a logo, a success message after sending, or a spam honeypot, I can add it. The success message and honeypot would need a small change on the `/contact` handler too.
