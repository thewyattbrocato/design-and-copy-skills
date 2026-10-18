```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Notification settings</title>
<style>
  :root {
    --ink: #1f2933;
    --muted: #52606d;
    --line: #8896a4;
    --soft-line: #d9e0e6;
    --bg: #f5f7f9;
    --card: #ffffff;
    --accent: #1d6fb8;
    --accent-ink: #ffffff;
    --error: #b42318;
    --ok: #17663a;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 24px 16px;
    background: var(--bg);
    color: var(--ink);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
  }
  main {
    max-width: 520px;
    margin: 0 auto;
    background: var(--card);
    border: 1px solid var(--soft-line);
    border-radius: 12px;
    padding: 24px;
  }
  h1 { margin: 0 0 4px; font-size: 1.5rem; line-height: 1.25; }
  .intro { margin: 0 0 20px; color: var(--muted); }
  fieldset { border: 0; margin: 0 0 24px; padding: 0; }
  legend { padding: 0; font-weight: 600; margin-bottom: 4px; }

  /* Toggles */
  .toggle {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 16px;
    padding: 12px 0;
    border-bottom: 1px solid var(--soft-line);
    cursor: pointer;
  }
  .toggle:last-child { border-bottom: 0; }
  .toggle-text { min-width: 0; overflow-wrap: anywhere; }
  .toggle-title { display: block; font-weight: 500; }
  .toggle-hint { display: block; color: var(--muted); font-size: .875rem; }
  .toggle input {
    appearance: none;
    flex: none;
    position: relative;
    width: 48px;
    height: 28px;
    margin: 2px 0 0;
    border-radius: 14px;
    background: var(--line);
    cursor: pointer;
    transition: background .15s;
  }
  .toggle input::after {
    content: "";
    position: absolute;
    top: 3px; left: 3px;
    width: 22px; height: 22px;
    border-radius: 50%;
    background: #fff;
    transition: transform .15s;
  }
  .toggle input:checked { background: var(--accent); }
  .toggle input:checked::after { transform: translateX(20px); }
  .toggle input:focus-visible,
  select:focus-visible, input[type="text"]:focus-visible, input[type="tel"]:focus-visible,
  input[type="email"]:focus-visible, button:focus-visible {
    outline: 3px solid var(--accent);
    outline-offset: 2px;
  }

  /* Fields */
  .field { margin-bottom: 20px; }
  label.field-label { display: block; font-weight: 600; margin-bottom: 6px; }
  select, .field input {
    width: 100%;
    min-height: 44px;
    padding: 8px 12px;
    font: inherit;
    color: var(--ink);
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 8px;
  }
  .field input::placeholder { color: var(--muted); }
  .field.invalid input, .field.invalid select { border: 2px solid var(--error); }
  .error {
    display: none;
    margin: 6px 0 0;
    color: var(--error);
    font-size: .875rem;
  }
  .field.invalid .error { display: block; }

  /* Save */
  .actions { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
  button {
    min-height: 44px;
    padding: 8px 24px;
    font: inherit;
    font-weight: 600;
    color: var(--accent-ink);
    background: var(--accent);
    border: 0;
    border-radius: 8px;
    cursor: pointer;
  }
  button[aria-disabled="true"] { opacity: .7; cursor: progress; }
  #status { margin: 0; font-size: .9375rem; }
  #status.ok { color: var(--ok); }
  #status.fail { color: var(--error); }

  @media (prefers-reduced-motion: reduce) {
    .toggle input, .toggle input::after { transition: none; }
  }
</style>
</head>
<body>
<main>
  <h1>Notification settings</h1>
  <p class="intro">Choose how you hear about your dog's day.</p>

  <form id="form" novalidate>
    <fieldset>
      <legend>What to send me</legend>
      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Photo updates</span>
          <span class="toggle-hint">Pictures of your dog during the day.</span>
        </span>
        <input type="checkbox" role="switch" name="photos">
      </label>
      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Pickup reminders</span>
          <span class="toggle-hint">A heads-up before it's time to collect your dog.</span>
        </span>
        <input type="checkbox" role="switch" name="pickup">
      </label>
      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Incident notes</span>
          <span class="toggle-hint">Notes from staff if something happens during the day.</span>
        </span>
        <input type="checkbox" role="switch" name="incidents">
      </label>
    </fieldset>

    <div class="field" id="method-field">
      <label class="field-label" for="method">How should we reach you?</label>
      <select id="method" name="method" required aria-describedby="method-error">
        <option value="" selected disabled>Select a method</option>
        <option value="text">Text message</option>
        <option value="email">Email</option>
      </select>
      <p class="error" id="method-error">Choose text message or email.</p>
    </div>

    <div class="field" id="contact-field">
      <label class="field-label" for="contact" id="contact-label">Phone number or email</label>
      <input id="contact" name="contact" type="text" autocomplete="off"
             placeholder="Choose a method first" aria-describedby="contact-error" disabled>
      <p class="error" id="contact-error"></p>
    </div>

    <div class="actions">
      <button type="submit" id="save">Save</button>
      <p id="status" role="status" aria-live="polite"></p>
    </div>
  </form>
</main>

<script>
  const form = document.getElementById('form');
  const method = document.getElementById('method');
  const contact = document.getElementById('contact');
  const contactLabel = document.getElementById('contact-label');
  const contactError = document.getElementById('contact-error');
  const save = document.getElementById('save');
  const status = document.getElementById('status');

  const kinds = {
    text:  { label: 'Mobile number', placeholder: '(555) 123-4567', type: 'tel',
             ok: v => v.replace(/\D/g, '').length >= 10,
             msg: 'Enter a mobile number with area code, like (555) 123-4567.' },
    email: { label: 'Email address', placeholder: 'name@example.com', type: 'email',
             ok: v => /^\S+@\S+\.\S+$/.test(v),
             msg: 'Enter an email address like name@example.com.' }
  };

  function setInvalid(field, input, on) {
    field.classList.toggle('invalid', on);
    input.setAttribute('aria-invalid', on ? 'true' : 'false');
  }

  method.addEventListener('change', () => {
    const k = kinds[method.value];
    contact.disabled = false;
    contact.type = k.type;
    contact.placeholder = k.placeholder;
    contactLabel.textContent = k.label;
    setInvalid(document.getElementById('method-field'), method, false);
    setInvalid(document.getElementById('contact-field'), contact, false);
  });
  contact.addEventListener('input', () => {
    setInvalid(document.getElementById('contact-field'), contact, false);
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (save.getAttribute('aria-disabled') === 'true') return; // no double-submit
    status.className = '';
    status.textContent = '';

    const k = kinds[method.value];
    const methodBad = !k;
    const contactBad = !!k && !k.ok(contact.value.trim());
    setInvalid(document.getElementById('method-field'), method, methodBad);
    setInvalid(document.getElementById('contact-field'), contact, contactBad);
    if (contactBad) contactError.textContent = k.msg;
    if (methodBad) return method.focus();
    if (contactBad) return contact.focus();

    save.setAttribute('aria-disabled', 'true');
    save.textContent = 'Saving…';
    try {
      // Replace with the real request. Input stays in place if it fails.
      await saveSettings(new FormData(form));
      status.className = 'ok';
      status.textContent = 'Saved. We\'ll use these settings from now on.';
    } catch (err) {
      status.className = 'fail';
      status.textContent = 'Your settings weren\'t saved. Check your connection and press Save to try again.';
    } finally {
      save.removeAttribute('aria-disabled');
      save.textContent = 'Save';
    }
  });

  // Stub: swap for the app's real save call.
  function saveSettings(data) { return new Promise(r => setTimeout(r, 400)); }
</script>
</body>
</html>
```

**What I changed beyond the literal spec**
- **Copy:** I replaced the placeholder labels with this app's own. "Option 1", "Option 2" and "Enable feature" became Photo updates, Pickup reminders and Incident notes. "Select..." and "Choice A/B" became "How should we reach you?" with Text message or Email. The text field is now the phone number or email, and its label follows the method you pick. The heading is "Notification settings". If you'd mapped those controls differently, tell me and I'll swap them.
- **Error text:** "Invalid input" now says what to fix, for example "Enter a mobile number with area code…". It shows under the field, is marked `aria-invalid`, and focus moves to the first problem.
- **Save:** the button shows "Saving…" and blocks double-submits. A saved message and a failure message appear in a live region. A failed save keeps what was typed.
- **Accessibility:** the toggles are real switches with visible focus rings and hints. Inputs are at least 44px tall. The layout is single-column, so it holds on narrow screens. Reduced-motion turns off the toggle animation.
- **Toggles start off:** nothing is pre-selected, so parents opt in themselves.

**Still needed**
- `saveSettings()` is a stub, so wire it to your real endpoint. I didn't invent any retry or timeout behavior.
- I haven't run this in a browser or tested it with a screen reader. I only read through the code.
