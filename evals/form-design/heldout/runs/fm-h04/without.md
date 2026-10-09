Here's the complete file.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contact us</title>
<style>
  :root {
    color-scheme: light dark;
    --bg: #f5f6f8;
    --card: #ffffff;
    --text: #1c1e21;
    --muted: #5f6672;
    --border: #c3c8d0;
    --accent: #2457d6;
    --accent-text: #ffffff;
    --error: #b42318;
    --error-bg: #fef3f2;
    --ok: #067647;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #121417;
      --card: #1b1e23;
      --text: #eceef1;
      --muted: #a0a7b2;
      --border: #3a404a;
      --accent: #7aa2ff;
      --accent-text: #0b1220;
      --error: #ff8a80;
      --error-bg: #2a1716;
      --ok: #4ade80;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    min-height: 100vh;
    display: grid;
    place-items: center;
    padding: 1rem;
    background: var(--bg);
    color: var(--text);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  form {
    width: 100%;
    max-width: 28rem;
    background: var(--card);
    padding: 1.75rem;
    border-radius: 12px;
    border: 1px solid var(--border);
  }
  h1 { margin: 0 0 .25rem; font-size: 1.4rem; }
  .lead { margin: 0 0 1.25rem; color: var(--muted); font-size: .95rem; }
  .field { margin-bottom: 1rem; }
  label { display: block; margin-bottom: .3rem; font-weight: 600; font-size: .9rem; }
  input, textarea {
    width: 100%;
    padding: .65rem .75rem;
    font: inherit;
    color: inherit;
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 8px;
  }
  textarea { min-height: 8rem; resize: vertical; }
  input:focus-visible, textarea:focus-visible, button:focus-visible {
    outline: 3px solid var(--accent);
    outline-offset: 2px;
  }
  input[aria-invalid="true"] {
    border-color: var(--error);
    background: var(--error-bg);
  }
  .error {
    margin: .35rem 0 0;
    color: var(--error);
    font-size: .875rem;
  }
  .error[hidden] { display: none; }
  button {
    width: 100%;
    padding: .75rem 1rem;
    font: inherit;
    font-weight: 600;
    color: var(--accent-text);
    background: var(--accent);
    border: 0;
    border-radius: 8px;
    cursor: pointer;
  }
  button:hover { filter: brightness(1.08); }
  button:disabled { opacity: .6; cursor: not-allowed; }
  .status { margin: 1rem 0 0; min-height: 1.5rem; color: var(--ok); font-weight: 600; }
  @media (prefers-reduced-motion: no-preference) {
    input, textarea, button { transition: border-color .15s, background-color .15s, filter .15s; }
  }
</style>
</head>
<body>
  <form id="contact" action="#" method="post" novalidate>
    <h1>Contact us</h1>
    <p class="lead">We'll reply within two business days. All fields are required.</p>

    <div class="field">
      <label for="name">Name</label>
      <input id="name" name="name" type="text" placeholder="Your name" autocomplete="name" required>
    </div>

    <div class="field">
      <label for="email">Email</label>
      <input id="email" name="email" type="email" placeholder="you@example.com"
             autocomplete="email" inputmode="email" required aria-describedby="email-error">
      <p class="error" id="email-error" hidden></p>
    </div>

    <div class="field">
      <label for="message">Message</label>
      <textarea id="message" name="message" placeholder="How can we help?" required></textarea>
    </div>

    <button type="submit" id="send">Send</button>
    <p class="status" id="status" role="status" aria-live="polite"></p>
  </form>

<script>
  const form = document.getElementById('contact');
  const email = document.getElementById('email');
  const emailError = document.getElementById('email-error');
  const status = document.getElementById('status');
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  function validateEmail() {
    const value = email.value.trim();
    let message = '';
    if (!value) message = 'Please enter your email address.';
    else if (!emailPattern.test(value)) message = 'Enter a valid email address, like name@example.com.';
    email.setAttribute('aria-invalid', message ? 'true' : 'false');
    emailError.textContent = message;
    emailError.hidden = !message;
    return !message;
  }

  email.addEventListener('blur', () => { if (email.value) validateEmail(); });
  email.addEventListener('input', () => {
    if (email.getAttribute('aria-invalid') === 'true') validateEmail();
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    status.textContent = '';
    const emailOk = validateEmail();
    const firstInvalid = [...form.elements].find(
      (el) => el.willValidate && (el === email ? !emailOk : !el.value.trim())
    );
    if (firstInvalid) {
      firstInvalid.focus();
      if (firstInvalid !== email) status.textContent = '';
      return;
    }
    // Replace with a real submission (fetch/POST) here.
    form.reset();
    email.setAttribute('aria-invalid', 'false');
    status.textContent = 'Thanks! Your message has been sent.';
  });
</script>
</body>
</html>
```

**What I fixed**
- **Disabled button:** the original `disabled` button could never be clicked. It's now an enabled `type="submit"` button, and the form validates on submit.
- **Email input:** it was `type='text'`. It's now `type="email"` with `autocomplete`, `inputmode` and a custom validator.
- **Labels:** the inputs only had placeholders. Each field now has a visible `<label>` linked by `for`/`id`.
- **Form attributes:** I added `name` attributes, `required`, `autocomplete` hints and `lang`, charset and viewport meta tags.

**Invalid email error state**
- The field gets a red border and tint, plus a message such as "Enter a valid email address, like name@example.com."
- `aria-invalid` and `aria-describedby` link the message to the field for screen readers. The message also doesn't rely on colour alone.
- It validates on blur and on submit, then re-validates as the user types. Focus moves to the first invalid field.

**Styling**
- It uses a system font stack, visible focus rings, a light/dark theme, and no external assets.

The submit handler only shows a success message. Replace the `// Replace with a real submission` line with your `fetch` call or form action.
