Here's the finished screen. I kept your structure and order: heading, three toggles, text field, dropdown, Save, and the error text. I replaced the placeholder wording with the daycare's own, and I added the states a shipped form needs.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Notification settings</title>
<style>
  :root {
    --bg: #f6f5f2;
    --card: #ffffff;
    --text: #1d2321;
    --muted: #5b6360;
    --border: #767f7b;          /* 3:1+ on white for control borders */
    --accent: #0b6b5c;
    --accent-text: #ffffff;
    --error: #b3261e;
    --focus: #1a56db;
    --radius: 10px;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 24px 16px;
    background: var(--bg); color: var(--text);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
  }
  main { max-width: 520px; margin: 0 auto; }
  form {
    background: var(--card); border-radius: var(--radius);
    padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,.12);
  }
  h1 { margin: 0 0 4px; font-size: 1.5rem; line-height: 1.25; }
  .intro { margin: 0 0 20px; color: var(--muted); }
  fieldset { border: 0; margin: 0 0 24px; padding: 0; }
  legend { padding: 0; font-weight: 600; margin-bottom: 4px; }

  /* Toggles */
  .toggle {
    display: flex; align-items: center; justify-content: space-between;
    gap: 16px; padding: 12px 0; min-height: 44px;
    border-top: 1px solid #e3e5e3; cursor: pointer;
  }
  .toggle:first-of-type { border-top: 0; }
  .toggle-text { overflow-wrap: anywhere; }
  .toggle-title { display: block; font-weight: 500; }
  .toggle-hint { display: block; font-size: .875rem; color: var(--muted); }
  .switch {
    appearance: none; -webkit-appearance: none; flex: none;
    width: 48px; height: 28px; margin: 0; border-radius: 14px;
    background: var(--border); position: relative; cursor: pointer;
    transition: background .15s;
  }
  .switch::after {
    content: ""; position: absolute; top: 3px; left: 3px;
    width: 22px; height: 22px; border-radius: 50%; background: #fff;
    transition: transform .15s;
  }
  .switch:checked { background: var(--accent); }
  .switch:checked::after { transform: translateX(20px); }

  /* Fields */
  .field { margin-bottom: 20px; }
  label.field-label { display: block; font-weight: 600; margin-bottom: 6px; }
  input[type="text"], select {
    width: 100%; min-height: 44px; padding: 8px 12px;
    font: inherit; color: var(--text); background: #fff;
    border: 1px solid var(--border); border-radius: 8px;
  }
  .field-hint { margin: 4px 0 0; font-size: .875rem; color: var(--muted); }
  .error {
    display: none; margin: 6px 0 0; font-size: .875rem; font-weight: 500;
    color: var(--error);
  }
  .error::before { content: "⚠ "; }   /* icon + words, not color alone */
  .field.invalid .error { display: block; }
  .field.invalid input, .field.invalid select {
    border-color: var(--error); border-width: 2px;
  }

  /* Focus */
  .switch:focus-visible, input:focus-visible, select:focus-visible,
  button:focus-visible {
    outline: 3px solid var(--focus); outline-offset: 2px;
  }

  /* Save */
  .actions { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; }
  button[type="submit"] {
    min-height: 44px; padding: 8px 28px; font: inherit; font-weight: 600;
    color: var(--accent-text); background: var(--accent);
    border: 0; border-radius: 8px; cursor: pointer;
  }
  button[type="submit"]:hover { filter: brightness(1.12); }
  button[type="submit"]:active { filter: brightness(.92); }
  button[type="submit"][aria-disabled="true"] { opacity: .7; cursor: progress; }
  .status { margin: 0; font-weight: 500; }
  .status.ok { color: var(--accent); }
  .status.fail { color: var(--error); }

  @media (max-width: 400px) {
    form { padding: 16px; }
    button[type="submit"] { width: 100%; }
  }
  @media (prefers-reduced-motion: reduce) {
    .switch, .switch::after { transition: none; }
  }
  @media (forced-colors: active) {
    .switch { border: 2px solid ButtonText; }
    .switch:checked { background: Highlight; }
  }
</style>
</head>
<body>
<main>
  <form id="settings" novalidate>
    <h1>Settings</h1>
    <p class="intro">Choose how you hear about your dog's day.</p>

    <fieldset>
      <legend>Notify me about</legend>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Photo updates</span>
          <span class="toggle-hint">Pictures from your dog's day</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="photos" checked>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Pickup reminders</span>
          <span class="toggle-hint">A heads-up before pickup time</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="pickup" checked>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Incident notes</span>
          <span class="toggle-hint">If something happens during the day</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="incidents" checked>
      </label>
    </fieldset>

    <div class="field" id="method-field">
      <label class="field-label" for="method">Send notifications by</label>
      <select id="method" name="method" aria-describedby="method-error" required>
        <option value="" selected disabled>Select…</option>
        <option value="sms">Text message</option>
        <option value="email">Email</option>
      </select>
      <p class="error" id="method-error">Choose how you'd like to be notified.</p>
    </div>

    <div class="field" id="contact-field">
      <label class="field-label" for="contact">Phone number or email</label>
      <input type="text" id="contact" name="contact" autocomplete="off"
             placeholder="e.g. name@example.com"
             aria-describedby="contact-hint contact-error">
      <p class="field-hint" id="contact-hint">Where we'll send them.</p>
      <p class="error" id="contact-error">Invalid input</p>
    </div>

    <div class="actions">
      <button type="submit" id="save">Save</button>
      <p class="status" id="status" role="status" aria-live="polite"></p>
    </div>
  </form>
</main>

<script>
  const form = document.getElementById('settings');
  const save = document.getElementById('save');
  const status = document.getElementById('status');
  const method = document.getElementById('method');
  const contact = document.getElementById('contact');

  function setInvalid(fieldId, input, on, message) {
    const field = document.getElementById(fieldId);
    field.classList.toggle('invalid', on);
    input.setAttribute('aria-invalid', on ? 'true' : 'false');
    if (on && message) field.querySelector('.error').textContent = message;
  }

  function validate() {
    const bad = [];
    const noMethod = !method.value;
    setInvalid('method-field', method, noMethod);
    if (noMethod) bad.push(method);

    const v = contact.value.trim();
    let msg = null;
    if (v) {
      const isEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
      const isPhone = /^\+?[\d\s().-]{7,}$/.test(v);
      if (method.value === 'email' && !isEmail) msg = 'Invalid input: enter a valid email address.';
      else if (method.value === 'sms' && !isPhone) msg = 'Invalid input: enter a valid phone number.';
      else if (!method.value && !isEmail && !isPhone) msg = 'Invalid input: enter a phone number or email.';
    } else {
      msg = 'Invalid input: enter a phone number or email.';
    }
    setInvalid('contact-field', contact, !!msg, msg);
    if (msg) bad.push(contact);
    return bad;
  }

  // Replace with the real request; throw on failure.
  async function saveSettings(data) {
    /* await fetch('[settings endpoint]', { method: 'POST', body: JSON.stringify(data) }); */
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (save.getAttribute('aria-disabled') === 'true') return;   // no double-submit
    status.className = 'status'; status.textContent = '';

    const bad = validate();
    if (bad.length) { bad[0].focus(); return; }

    save.setAttribute('aria-disabled', 'true');
    save.textContent = 'Saving…';
    try {
      await saveSettings(Object.fromEntries(new FormData(form)));
      status.className = 'status ok';
      status.textContent = 'Saved. Your notification settings are updated.';
    } catch (err) {
      status.className = 'status fail';
      status.textContent = "Couldn't save your settings. Your changes are still here. Try again.";
    } finally {
      save.removeAttribute('aria-disabled');
      save.textContent = 'Save';
    }
  });

  // Clear an error as soon as the person fixes the field.
  method.addEventListener('change', () => setInvalid('method-field', method, false));
  contact.addEventListener('input', () => setInvalid('contact-field', contact, false));
</script>
</body>
</html>
```

**What changed**
- **Copy:** "Option 1", "Option 2" and "Enable feature" became Photo updates, Pickup reminders and Incident notes. Each has a one-line hint.
- **Field and dropdown:** The dropdown is now "Send notifications by" (Text message or Email). The text field is "Phone number or email".
- **Labels and errors:** Both fields have real labels instead of placeholder-only text. "Invalid input" still leads the error, now followed by what to fix, and the error also has a ⚠ icon.
- **Save:** The button shows "Saving…" and ignores a second press while it works. A success message appears beside it. A failure keeps what was typed and tells the person to try again. Errors clear as soon as the field is fixed.
- **Accessibility:** The toggles are real switches you can reach and use by keyboard. Focus rings are visible. Targets are at least 44px tall. The layout works at 320px.

**Needs your call**
- I guessed the dropdown and field meanings, because "Choice A/B" and "Enter value" didn't say. If they mean something else, change the labels and the `validate()` rules.
- `saveSettings()` is a stub, so the success message always appears until you wire in the real endpoint.
- I didn't test with a screen reader or on a real device.
