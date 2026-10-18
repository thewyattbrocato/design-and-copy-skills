I couldn't save this as a file because the Write tool is disabled in this session. The full screen is below, so you can paste it into `index.html`. I haven't opened it in a browser.

The placeholder labels ("Option 1", "Enable feature", "Enter value", "Invalid input") wouldn't make sense to parents, so I wrote real copy for them. Check the wording against what you want to say.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Notification settings</title>
<style>
  :root {
    --bg: #faf6f1;
    --card: #ffffff;
    --text: #2b2118;
    --muted: #6b5d50;
    --border: #d9cfc3;
    --accent: #b5541c;
    --accent-dark: #8f4115;
    --error: #b3261e;
    --focus: #1a5fb4;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 24px 16px;
    background: var(--bg);
    color: var(--text);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
  }
  main {
    max-width: 480px;
    margin: 0 auto;
    background: var(--card);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 1px 3px rgba(43, 33, 24, .12);
  }
  h1 { margin: 0 0 4px; font-size: 1.5rem; }
  .intro { margin: 0 0 24px; color: var(--muted); }
  fieldset { border: 0; margin: 0 0 24px; padding: 0; }
  legend { padding: 0; margin-bottom: 8px; font-weight: 600; }

  .toggle {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 12px 0;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
  }
  .toggle:last-child { border-bottom: 0; }
  .toggle-text strong { display: block; font-weight: 600; }
  .toggle-text span { color: var(--muted); font-size: .875rem; }

  .switch { position: relative; flex: none; width: 48px; height: 28px; }
  .switch input {
    position: absolute; inset: 0; width: 100%; height: 100%;
    margin: 0; opacity: 0; cursor: pointer;
  }
  .track {
    position: absolute; inset: 0;
    background: #8a7d70;
    border-radius: 14px;
    transition: background .15s;
    pointer-events: none;
  }
  .track::after {
    content: "";
    position: absolute; top: 3px; left: 3px;
    width: 22px; height: 22px;
    background: #fff; border-radius: 50%;
    transition: transform .15s;
  }
  .switch input:checked + .track { background: var(--accent); }
  .switch input:checked + .track::after { transform: translateX(20px); }
  .switch input:focus-visible + .track { outline: 3px solid var(--focus); outline-offset: 2px; }

  .field { margin-bottom: 20px; }
  label.label { display: block; margin-bottom: 4px; font-weight: 600; }
  .hint { margin: 0 0 6px; color: var(--muted); font-size: .875rem; }
  input[type="tel"], select {
    width: 100%;
    min-height: 44px;
    padding: 10px 12px;
    font: inherit;
    color: var(--text);
    background: #fff;
    border: 1px solid #8a7d70;
    border-radius: 8px;
  }
  input[type="tel"]:focus-visible, select:focus-visible, button:focus-visible {
    outline: 3px solid var(--focus);
    outline-offset: 2px;
  }
  input[aria-invalid="true"] { border-color: var(--error); border-width: 2px; }
  .error { margin: 6px 0 0; color: var(--error); font-size: .875rem; }
  .error[hidden] { display: none; }

  button[type="submit"] {
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
  button[type="submit"]:hover { background: var(--accent-dark); }
  .status { margin: 12px 0 0; text-align: center; color: var(--muted); min-height: 1.5em; }
</style>
</head>
<body>
<main>
  <h1>Notification settings</h1>
  <p class="intro">Choose how you hear about your dog's day.</p>

  <form id="settings" novalidate>
    <fieldset>
      <legend>What to send me</legend>

      <label class="toggle">
        <span class="toggle-text">
          <strong>Photo updates</strong>
          <span>Pictures and videos from your dog's day.</span>
        </span>
        <span class="switch">
          <input type="checkbox" role="switch" name="photos" checked>
          <span class="track"></span>
        </span>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <strong>Pickup reminders</strong>
          <span>A heads-up before it's time to collect your dog.</span>
        </span>
        <span class="switch">
          <input type="checkbox" role="switch" name="pickup" checked>
          <span class="track"></span>
        </span>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <strong>Incident notes</strong>
          <span>Alerts if something happens, like a scrape or a missed meal.</span>
        </span>
        <span class="switch">
          <input type="checkbox" role="switch" name="incidents" checked>
          <span class="track"></span>
        </span>
      </label>
    </fieldset>

    <div class="field">
      <label class="label" for="reminder-timing">Pickup reminder timing</label>
      <select id="reminder-timing" name="reminder-timing">
        <option value="" selected disabled>Select a time…</option>
        <option value="30">30 minutes before pickup</option>
        <option value="60">1 hour before pickup</option>
      </select>
    </div>

    <div class="field">
      <label class="label" for="phone">Mobile number for text alerts</label>
      <p class="hint" id="phone-hint">We'll only text you about your dog.</p>
      <input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel"
             placeholder="(555) 123-4567" aria-describedby="phone-hint phone-error">
      <p class="error" id="phone-error" role="alert" hidden>Enter a valid phone number, like (555) 123-4567.</p>
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
    const digits = phone.value.replace(/\D/g, '');
    const ok = phone.value.trim() === '' || digits.length === 10;
    error.hidden = ok;
    phone.setAttribute('aria-invalid', String(!ok));
    if (!ok) { phone.focus(); return; }
    // TODO: send form data to the backend here.
    status.textContent = 'Settings saved.';
  });
</script>
</body>
</html>
```

**What I changed from your spec**
- **Heading:** "Settings" is now "Notification settings".
- **Toggles:** "Option 1", "Option 2" and "Enable feature" became **Photo updates**, **Pickup reminders** and **Incident notes**. Each has a one-line description and starts switched on.
- **Dropdown:** it now sets how early the pickup reminder arrives. The "Select…" prompt stays, and "Choice A" and "Choice B" became "30 minutes before pickup" and "1 hour before pickup".
- **Text field:** it now collects the mobile number for text alerts. The placeholder is an example number.
- **Error text:** "Invalid input" now reads "Enter a valid phone number, like (555) 123-4567." It stays hidden until Save is pressed with a bad number.
- **Button:** "Save" is now "Save changes". A "Settings saved." message appears after a successful save.

**Questions for you**
- **Dropdown and phone field:** I guessed what these two controls do, because your spec didn't say. If they're meant for something else, such as email versus text delivery, tell me and I'll rework them.
- **Incident notes:** should parents be able to turn them off? Many daycares keep them always on. If you want that, I can make it a fixed, non-toggle row.
- **Save:** the button validates the phone number but doesn't send anything yet. There's a `TODO` in the script where your backend call goes.
