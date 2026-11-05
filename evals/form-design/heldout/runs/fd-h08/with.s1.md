Your form is already sound. It has visible labels, the right input types and autofill tokens, "optional" marked in words, and a specific button. I left the structure and copy alone and polished the look:

- Text is 16px, so phones don't zoom on focus.
- Fields get padding, borders and a visible focus ring.
- The button is a proper 44px target.
- The phone field says why you ask for it.

```html
<style>
  .kestrel-form { max-width: 420px; font: 16px/1.5 system-ui, sans-serif; color: #1a1a1a; }
  .kestrel-form h2 { margin: 0 0 8px; font-size: 1.5rem; line-height: 1.25; }
  .kestrel-form p { margin: 0 0 24px; color: #444; }
  .kestrel-form label { display: block; font-weight: 600; }
  .kestrel-form .hint { margin: 0 0 4px; font-size: 0.875rem; font-weight: 400; color: #555; }
  .kestrel-form input,
  .kestrel-form textarea {
    display: block; box-sizing: border-box; width: 100%;
    margin: 4px 0 20px; padding: 10px 12px;
    font: inherit; color: inherit;
    border: 1px solid #767676; border-radius: 6px; background: #fff;
  }
  .kestrel-form textarea { resize: vertical; }
  .kestrel-form input:focus-visible,
  .kestrel-form textarea:focus-visible,
  .kestrel-form button:focus-visible { outline: 3px solid #1a5fb4; outline-offset: 2px; }
  .kestrel-form button {
    min-height: 44px; padding: 0 24px;
    font: inherit; font-weight: 600; color: #fff;
    background: #1a5fb4; border: 0; border-radius: 6px; cursor: pointer;
  }
  .kestrel-form button:hover { background: #154c91; }
</style>

<form class="kestrel-form" action="/contact" method="post">
  <h2>Get in touch</h2>
  <p>Questions about a repair or a quote? We reply within two business days.</p>

  <label for="name">Your name</label>
  <input id="name" name="name" autocomplete="name" required>

  <label for="email">Email</label>
  <input id="email" name="email" type="email" autocomplete="email" autocapitalize="off" spellcheck="false" required>

  <label for="phone">Phone (optional)</label>
  <div class="hint" id="phone-hint">Add it if you'd like a call back.</div>
  <input id="phone" name="phone" type="tel" autocomplete="tel" aria-describedby="phone-hint">

  <label for="msg">What can we help with?</label>
  <textarea id="msg" name="msg" rows="5" required></textarea>

  <button type="submit">Send message</button>
</form>
```

Two notes:
- I moved the inline styles into a scoped `<style>` block. If your site already has a stylesheet or button style, use that instead so the form matches the rest of the page.
- I picked the colors (`#1a5fb4` blue, grays) as placeholders, so swap in your brand color. If it's a light color, keep the button text dark enough to read.
