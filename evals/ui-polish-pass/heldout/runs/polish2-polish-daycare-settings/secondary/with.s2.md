Here's the finished screen as one file. Save it as `notification-settings.html` and open it in a browser.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Settings</title>
<style>
  :root {
    --ink: #1f2328;
    --muted: #57606a;
    --line: #d0d7de;
    --surface: #ffffff;
    --page: #f6f8fa;
    --accent: #1d5c4a;
    --accent-ink: #ffffff;
    --error: #b42318;
    --focus: #1d5c4a;
    --radius: 10px;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    background: var(--page);
    color: var(--ink);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }

  .settings {
    max-width: 36rem;
    margin: 0 auto;
    padding: 2rem 1rem 3rem;
  }

  h1 {
    font-size: 1.75rem;
    line-height: 1.2;
    margin: 0 0 0.25rem;
  }

  .intro {
    color: var(--muted);
    margin: 0 0 1.5rem;
  }

  .group {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 0.25rem 1.25rem;
    margin: 0 0 1.25rem;
    min-width: 0;
  }

  legend {
    font-weight: 600;
    padding: 1rem 0 0.25rem;
  }

  /* Toggle rows */
  .toggle-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.875rem 0;
    border-top: 1px solid var(--line);
    cursor: pointer;
  }

  .toggle-row:first-of-type { border-top: 0; }

  .toggle-name { display: block; font-weight: 500; }
  .toggle-desc { display: block; color: var(--muted); font-size: 0.9375rem; }

  .switch {
    appearance: none;
    flex: none;
    width: 2.75rem;
    height: 1.5rem;
    margin: 0;
    border-radius: 999px;
    background: #8c959f;
    position: relative;
    cursor: pointer;
    transition: background-color 150ms ease;
  }

  .switch::after {
    content: "";
    position: absolute;
    top: 0.1875rem;
    left: 0.1875rem;
    width: 1.125rem;
    height: 1.125rem;
    border-radius: 50%;
    background: #fff;
    transition: transform 150ms ease;
  }

  .switch:checked { background: var(--accent); }
  .switch:checked::after { transform: translateX(1.25rem); }

  @media (prefers-reduced-motion: reduce) {
    .switch, .switch::after { transition: none; }
  }

  /* Fields */
  .field {
    padding: 0.875rem 0;
    border-top: 1px solid var(--line);
  }

  .field label,
  .field-label {
    display: block;
    font-weight: 500;
    margin-bottom: 0.375rem;
  }

  .hint {
    color: var(--muted);
    font-size: 0.9375rem;
    margin: 0 0 0.5rem;
  }

  input[type="email"],
  select {
    width: 100%;
    min-height: 2.75rem;
    padding: 0.5rem 0.75rem;
    font: inherit;
    color: var(--ink);
    background: var(--surface);
    border: 1px solid #6e7781;
    border-radius: 8px;
  }

  input[aria-invalid="true"] {
    border: 2px solid var(--error);
  }

  .error {
    color: var(--error);
    font-size: 0.9375rem;
    margin: 0.375rem 0 0;
  }

  .error[hidden] { display: none; }

  :focus-visible {
    outline: 3px solid var(--focus);
    outline-offset: 2px;
  }

  /* Actions */
  .actions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.75rem 1rem;
    margin-top: 1.5rem;
  }

  .btn {
    min-height: 2.75rem;
    padding: 0.5rem 1.25rem;
    font: inherit;
    font-weight: 600;
    color: var(--accent-ink);
    background: var(--accent);
    border: 0;
    border-radius: 8px;
    cursor: pointer;
  }

  .btn:disabled {
    cursor: progress;
    opacity: 0.7;
  }

  .status {
    margin: 0;
    color: var(--muted);
  }

  .status.is-error { color: var(--error); }

  @media (max-width: 320px) {
    .settings { padding: 1.25rem 0.75rem 2rem; }
  }
</style>
</head>
<body>
<main class="settings">
  <h1>Settings</h1>
  <p class="intro">Choose how you hear about your dog's day.</p>

  <form id="settings-form" novalidate>
    <fieldset class="group">
      <legend>Updates about your dog</legend>

      <label class="toggle-row">
        <span>
          <span class="toggle-name">Photo updates</span>
          <span class="toggle-desc">Pictures taken during the day</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="photo_updates" checked>
      </label>

      <label class="toggle-row">
        <span>
          <span class="toggle-name">Pickup reminders</span>
          <span class="toggle-desc">A reminder before pickup time</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="pickup_reminders" checked>
      </label>

      <label class="toggle-row">
        <span>
          <span class="toggle-name">Incident notes</span>
          <span class="toggle-desc">Notes if anything happens during the day</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="incident_notes" checked>
      </label>
    </fieldset>

    <fieldset class="group">
      <legend>Delivery</legend>

      <div class="field">
        <label for="contact-email">Notification email</label>
        <p class="hint" id="contact-email-hint">Optional. Leave blank to use your account email.</p>
        <input id="contact-email" name="contact_email" type="email" autocomplete="email"
               placeholder="name@example.com" aria-describedby="contact-email-hint contact-email-error"
               aria-invalid="false">
        <p class="error" id="contact-email-error" role="alert" hidden>
          Enter an email address like name@example.com, or leave this blank.
        </p>
      </div>

      <div class="field">
        <label for="delivery-timing">Delivery timing</label>
        <select id="delivery-timing" name="delivery_timing">
          <option value="" disabled selected>Select...</option>
          <option value="a">Choice A</option>
          <option value="b">Choice B</option>
        </select>
      </div>
    </fieldset>

    <div class="actions">
      <button class="btn" type="submit">Save</button>
      <p class="status" id="save-status" role="status" aria-live="polite"></p>
    </div>
  </form>
</main>

<script>
  const SAVE_URL = '/api/notification-settings'; // replace with your endpoint

  const form = document.getElementById('settings-form');
  const saveBtn = form.querySelector('button[type="submit"]');
  const status = document.getElementById('save-status');
  const email = document.getElementById('contact-email');
  const emailError = document.getElementById('contact-email-error');

  function validateEmail() {
    const ok = email.value.trim() === '' || email.checkValidity();
    email.setAttribute('aria-invalid', String(!ok));
    emailError.hidden = ok;
    return ok;
  }

  email.addEventListener('input', () => {
    if (email.getAttribute('aria-invalid') === 'true') validateEmail();
  });

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    status.textContent = '';
    status.classList.remove('is-error');

    if (!validateEmail()) {
      email.focus();
      return;
    }

    saveBtn.disabled = true;
    saveBtn.textContent = 'Saving…';
    form.setAttribute('aria-busy', 'true');

    try {
      const response = await fetch(SAVE_URL, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(Object.fromEntries(new FormData(form))),
      });
      if (!response.ok) throw new Error(`Save failed: ${response.status}`);
      status.textContent = 'Settings saved.';
    } catch (err) {
      status.textContent = "Couldn't save. Your changes are still here. Try again.";
      status.classList.add('is-error');
    } finally {
      saveBtn.disabled = false;
      saveBtn.textContent = 'Save';
      form.removeAttribute('aria-busy');
    }
  });
</script>
</body>
</html>
```

**What changed and why**

- **Labels:** "Option 1 / Option 2 / Enable feature" became "Photo updates / Pickup reminders / Incident notes", the three things you described. Each toggle has a one-line description so parents know what they're switching on.
- **Error text:** "Invalid input" now says what to enter, and the field is marked `aria-invalid` and announced via `role="alert"`. It clears as soon as the value is fixed.
- **Save:** shows "Saving…" and disables itself to prevent double-submits. Success and failure both appear as text. A failure keeps everything the parent typed.
- **Access:** toggles are real switches with names, the whole row is clickable, focus rings are visible, and targets are at least 44px tall.
- **Layout:** the layout holds at 320px and wraps at 200% text.

**Needs a product decision**

- The email field, the "Select..." dropdown with Choice A/B, and "Delivery timing" are my guesses. The original screen didn't say what those controls set, so swap in the real purpose and options.
- Incident notes is on by default and can be turned off. You may want that locked on for safety.
- `SAVE_URL` is a placeholder, and the save call assumes a JSON `PUT` endpoint.

**Not checked:** I did not test this with a screen reader, on a real device, or against a live server.
