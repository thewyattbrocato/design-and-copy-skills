Here's the finished screen. The placeholder labels were generic, so I wrote dog-daycare copy and assumed what the text field and dropdown are for (see the notes below the code).

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Notification settings</title>
<style>
  :root {
    --bg: #f6f3ee;
    --card: #ffffff;
    --text: #25211c;
    --muted: #6b645b;
    --border: #d9d2c7;
    --accent: #2f6f5e;
    --accent-dark: #245649;
    --error: #b3261e;
    --focus: #1a5fb4;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 24px 16px;
    background: var(--bg);
    color: var(--text);
    font: 16px/1.45 system-ui, -apple-system, "Segoe UI", sans-serif;
  }
  main {
    max-width: 480px;
    margin: 0 auto;
    background: var(--card);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,.08);
  }
  h1 { margin: 0 0 4px; font-size: 1.5rem; }
  .intro { margin: 0 0 20px; color: var(--muted); }

  fieldset { border: 0; margin: 0 0 24px; padding: 0; }
  legend, label.field-label { font-weight: 600; }

  /* Toggle rows */
  .toggle {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 14px 0;
    border-top: 1px solid var(--border);
    cursor: pointer;
  }
  .toggle:last-child { border-bottom: 1px solid var(--border); }
  .toggle-text { display: flex; flex-direction: column; }
  .toggle-title { font-weight: 600; }
  .toggle-desc { font-size: .875rem; color: var(--muted); }

  .switch { position: relative; flex: none; width: 48px; height: 28px; }
  .switch input {
    position: absolute; inset: 0; width: 100%; height: 100%;
    margin: 0; opacity: 0; cursor: pointer;
  }
  .track {
    position: absolute; inset: 0;
    background: #8f877b;
    border-radius: 14px;
    transition: background .15s;
    pointer-events: none;
  }
  .track::after {
    content: "";
    position: absolute; top: 3px; left: 3px;
    width: 22px; height: 22px;
    background: #fff;
    border-radius: 50%;
    transition: transform .15s;
  }
  .switch input:checked + .track { background: var(--accent); }
  .switch input:checked + .track::after { transform: translateX(20px); }
  .switch input:focus-visible + .track { outline: 3px solid var(--focus); outline-offset: 2px; }

  /* Fields */
  .field { margin-bottom: 20px; }
  .field-label { display: block; margin-bottom: 6px; }
  .hint { margin: 0 0 6px; font-size: .875rem; color: var(--muted); }
  input[type="tel"], select {
    width: 100%;
    min-height: 44px;
    padding: 10px 12px;
    font: inherit;
    color: var(--text);
    background: #fff;
    border: 1px solid #8f877b;
    border-radius: 8px;
  }
  input[type="tel"]:focus-visible, select:focus-visible, button:focus-visible {
    outline: 3px solid var(--focus);
    outline-offset: 2px;
  }
  input[aria-invalid="true"] { border-color: var(--error); border-width: 2px; }
  .error { margin: 6px 0 0; font-size: .875rem; color: var(--error); font-weight: 600; }
  .error[hidden] { display: none; }

  button {
    width: 100%;
    min-height: 48px;
    font: inherit;
    font-weight: 600;
    color: #fff;
    background: var(--accent);
    border: 0;
    border-radius: 8px;
    cursor: pointer;
  }
  button:hover { background: var(--accent-dark); }
  .status { margin: 12px 0 0; text-align: center; color: var(--accent-dark); font-weight: 600; }

  @media (prefers-reduced-motion: reduce) {
    .track, .track::after { transition: none; }
  }
</style>
</head>
<body>
<main>
  <h1>Notification settings</h1>
  <p class="intro">Choose how you hear about your dog's day.</p>

  <form id="settings" novalidate>
    <fieldset>
      <legend class="visually-hidden" style="position:absolute;left:-9999px">Notification types</legend>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Photo updates</span>
          <span class="toggle-desc">Pictures and videos from playtime and naps</span>
        </span>
        <span class="switch">
          <input type="checkbox" role="switch" name="photos" checked>
          <span class="track"></span>
        </span>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Pickup reminders</span>
          <span class="toggle-desc">A heads-up before it's time to collect your dog</span>
        </span>
        <span class="switch">
          <input type="checkbox" role="switch" name="pickup" checked>
          <span class="track"></span>
        </span>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Incident notes</span>
          <span class="toggle-desc">Scuffles, scrapes, or anything the staff want you to know</span>
        </span>
        <span class="switch">
          <input type="checkbox" role="switch" name="incidents" checked>
          <span class="track"></span>
        </span>
      </label>
    </fieldset>

    <div class="field">
      <label class="field-label" for="reminder">Remind me before pickup</label>
      <select id="reminder" name="reminder">
        <option value="" disabled selected>Choose timing</option>
        <option value="15">15 minutes before</option>
        <option value="30">30 minutes before</option>
        <option value="60">1 hour before</option>
      </select>
    </div>

    <div class="field">
      <label class="field-label" for="phone">Mobile number for text alerts</label>
      <p class="hint" id="phone-hint">We'll only text you about the notifications you've turned on.</p>
      <input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel"
             placeholder="(555) 123-4567" aria-describedby="phone-hint phone-error">
      <p class="error" id="phone-error" role="alert" hidden>Enter a valid 10-digit mobile number.</p>
    </div>

    <button type="submit">Save changes</button>
    <p class="status" id="status" role="status"></p>
  </form>
</main>

<script>
  const form = document.getElementById('settings');
  const phone = document.getElementById('phone');
  const error = document.getElementById('phone-error');
  const status = document.getElementById('status');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    status.textContent = '';
    const value = phone.value.trim();
    // Phone is optional; only flag it if something was typed and it isn't 10 digits.
    const bad = value !== '' && value.replace(/\D/g, '').length !== 10;
    error.hidden = !bad;
    phone.setAttribute('aria-invalid', bad);
    if (bad) { phone.focus(); return; }
    // TODO: send form data to the backend here.
    status.textContent = 'Your settings are saved.';
  });
</script>
</body>
</html>
```

**What I assumed (change any of these if they're wrong):**
- **Toggles:** "Option 1", "Option 2" and "Enable feature" became Photo updates, Pickup reminders and Incident notes. All three default to on.
- **Dropdown:** It sets how far ahead the pickup reminder arrives. I added a 1-hour option, so there are three choices instead of two.
- **Text field:** It collects a mobile number for text alerts. It's optional, and the error only shows when the number isn't 10 digits.
- **Error text:** "Invalid input" now says what to fix: "Enter a valid 10-digit mobile number." It stays hidden until validation fails.
- **Button:** "Save" became "Save changes". After a successful save it shows "Your settings are saved."

**Things to know before you ship:**
- The small script is only there to show and hide the error and the confirmation. The `TODO` marks where your real save call goes.
- Incident notes are on by default. You may want to stop parents turning them off, or show a warning when they do.
- The toggles are keyboard-accessible, and the error is announced to screen readers.
