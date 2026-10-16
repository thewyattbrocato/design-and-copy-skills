Here's a polished version. I kept the `action`, `method`, field `name`s, `id`s, `required` attributes and `autocomplete` values the same, so your `/contact` handler needs no changes.

```html
<style>
  .kestrel-contact {
    max-width: 440px;
    padding: 28px;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    color: #1f2933;
    background: #fff;
    border: 1px solid #e1e5ea;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, .06);
  }
  .kestrel-contact h2 { margin: 0 0 8px; font-size: 1.5rem; line-height: 1.2; }
  .kestrel-contact .intro { margin: 0 0 24px; color: #52606d; line-height: 1.5; }
  .kestrel-contact label { display: block; margin-bottom: 6px; font-size: .9rem; font-weight: 600; }
  .kestrel-contact .field { margin-bottom: 18px; }
  .kestrel-contact input,
  .kestrel-contact textarea {
    display: block;
    width: 100%;
    box-sizing: border-box;
    padding: 10px 12px;
    font: inherit;
    color: inherit;
    background: #fff;
    border: 1px solid #b8c0cc;
    border-radius: 8px;
    transition: border-color .15s, box-shadow .15s;
  }
  .kestrel-contact textarea { resize: vertical; min-height: 120px; }
  .kestrel-contact input:focus-visible,
  .kestrel-contact textarea:focus-visible {
    outline: none;
    border-color: #1d6fd1;
    box-shadow: 0 0 0 3px rgba(29, 111, 209, .25);
  }
  .kestrel-contact input:user-invalid,
  .kestrel-contact textarea:user-invalid { border-color: #c0392b; }
  .kestrel-contact button {
    width: 100%;
    padding: 12px 16px;
    font: inherit;
    font-weight: 600;
    color: #fff;
    background: #1d6fd1;
    border: 0;
    border-radius: 8px;
    cursor: pointer;
    transition: background .15s;
  }
  .kestrel-contact button:hover { background: #1859a8; }
  .kestrel-contact button:focus-visible { outline: 3px solid rgba(29, 111, 209, .4); outline-offset: 2px; }
</style>

<form class="kestrel-contact" action="/contact" method="post">
  <h2>Get in touch</h2>
  <p class="intro">Questions about a repair or a quote? We reply within two business days.</p>

  <div class="field">
    <label for="name">Your name</label>
    <input id="name" name="name" autocomplete="name" required>
  </div>

  <div class="field">
    <label for="email">Email</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
  </div>

  <div class="field">
    <label for="phone">Phone <span style="font-weight:400;color:#52606d">(optional)</span></label>
    <input id="phone" name="phone" type="tel" autocomplete="tel">
  </div>

  <div class="field">
    <label for="msg">What can we help with?</label>
    <textarea id="msg" name="msg" rows="5" required></textarea>
  </div>

  <button type="submit">Send message</button>
</form>
```

What changed:
- **Layout:** The inline styles moved into one scoped `<style>` block. The card has padding, a border, rounded corners and a light shadow. `box-sizing: border-box` stops the 100%-wide fields from overflowing once padding is added.
- **Inputs:** They now have padding, rounded corners, and inherit the form's font. The textarea can only be resized vertically.
- **Button:** It's full width and styled, with hover and keyboard-focus states. Before, it was the browser default.
- **Accessibility:** Fields have clear focus rings. Invalid fields get a red border only after the user has interacted with them (`:user-invalid`). The blue and gray text colors have enough contrast against white.

Two things to adjust:
- **Brand color:** `#1d6fd1` is a placeholder. Swap in Kestrel's brand color, and check that white text on it is still readable.
- **Page styles:** If your site's CSS already styles `input` or `button`, the `.kestrel-contact` selectors should win. If something looks off, that's the first place to check.

One suggestion, which I haven't included because it needs backend work: after submitting, show the user a confirmation message or a "thanks" page. That tends to make a contact form feel more professional than any styling.
