Your form is already in good shape. It has visible labels, the right input types, autofill tokens, "optional" marked in words, and a specific button label. I'd only fix a few small things that affect how it looks and works on phones.

```html
<style>
  .kestrel-form { max-width:420px; font-family:system-ui,sans-serif }
  .kestrel-form input, .kestrel-form textarea {
    display:block; width:100%; box-sizing:border-box;
    margin:4px 0 16px; padding:10px 12px;
    font:inherit; font-size:16px;
  }
  .kestrel-form .hint { margin:2px 0 0; font-size:14px; color:#555 }
  .kestrel-form .hint + input { margin-top:4px }
  .kestrel-form button {
    padding:12px 20px; font:inherit; font-size:16px; min-height:44px; cursor:pointer;
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
  <p class="hint" id="phone-hint">Only if you'd like us to call you back.</p>
  <input id="phone" name="phone" type="tel" autocomplete="tel" aria-describedby="phone-hint">

  <label for="msg">What can we help with?</label>
  <textarea id="msg" name="msg" rows="5" required></textarea>

  <button type="submit">Send message</button>
</form>
```

- **What changed:** Inputs and the button are now 16px, so iPhones won't zoom in on focus. I added `box-sizing` and padding so the fields don't overflow their container. The button is at least 44px tall, and the inline styles moved into one block.
- **Phone hint:** I wrote "Only if you'd like us to call you back" as a placeholder reason. Change it if you use the number differently.

I left the fields, labels and wording alone. They already work, and adding a logo, colors or extra fields wouldn't make the form more usable.
