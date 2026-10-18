I couldn't save this to a file because the Write tool is disabled in this session, so the full screen is below. Save it as `notification-settings.html`.

Your spec used placeholder copy ("Option 1", "Enable feature", "Choice A"), which would confuse parents if shipped. I replaced it with copy for photo updates, pickup reminders and incident notes, and kept the same components.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Notification settings</title>
<style>
  :root {
    --bg: #f6f3ee;
    --card: #ffffff;
    --text: #2b2622;
    --muted: #6b625a;
    --border: #d9d2c8;
    --accent: #1f6f5c;
    --accent-dark: #175647;
    --error: #b3261e;
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
    box-shadow: 0 1px 3px rgba(0,0,0,.08);
  }
  h1 { margin: 0 0 4px; font-size: 1.5rem; }
  .intro { margin: 0 0 20px; color: var(--muted); }
  fieldset { border: 0; padding: 0; margin: 0 0 24px; }
  legend { font-weight: 600; margin-bottom: 4px; padding: 0; }

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
  .toggle-text span { display: block; }
  .toggle-title { font-weight: 500; }
  .toggle-hint { font-size: .875rem; color: var(--muted); }

  .switch { position: relative; flex: none; width: 48px; height: 28px; }
  .switch input {
    position: absolute; inset: 0; width: 100%; height: 100%;
    margin: 0; opacity: 0; cursor: pointer;
  }
  .track {
    position: absolute; inset: 0;
    background: #9b928a;
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
  .switch input:focus-visible + .track { outline: 3px solid #7fb8ff; outline-offset: 2px; }

  .field { margin-bottom: 20px; }
  label.label { display: block; font-weight: 600; margin-bottom: 6px; }
  input[type="tel"], select {
    width: 100%;
    min-height: 44px;
    padding: 10px 12px;
    font: inherit;
    color: var(--text);
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 8px;
  }
  input[type="tel"]:focus-visible, select:focus-visible {
    outline: 3px solid #7fb8ff; outline-offset: 1px; border-color: var(--accent);
  }
  input[aria-invalid="true"] { border-color: var(--error); }
  .error { margin: 6px 0 0; font-size: .875rem; color: var(--error); }
  .error[hidden] { display: none; }

  button {
    width: 100%;
    min-height: 48px;
    font: inherit; font-weight: 600;
    color: #fff; background: var(--accent);
    border: 0; border-radius: 8px;
    cursor: pointer;
  }
  button:hover { background: var(--accent-dark); }
  button:focus-visible { outline: 3px solid #7fb8ff; outline-offset: 2px; }
  .status { margin: 12px 0 0; text-align: center; color: var(--accent-dark); font-weight: 500; }
  .status:empty { display: none; }
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
          <span class="toggle-hint">Pictures and videos from playtime and naps</span>
        </span>
        <span class="switch">
          <input type="checkbox" name="photos" checked>
          <span class="track"></span>
        </span>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Pickup reminders</span>
          <span class="toggle-hint">A heads-up before it's time to collect your dog</span>
        </span>
        <span class="switch">
          <input type="checkbox" name="pickup" checked>
          <span class="track"></span>
        </span>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Incident notes</span>
          <span class="toggle-hint">Alerts if staff need to tell you about an injury, illness or behavior concern</span>
        </span>
        <span class="switch">
          <input type="checkbox" name="incidents" checked>
          <span class="track"></span>
        </span>
      </label>
    </fieldset>

    <div class="field">
      <label class="label" for="phone">Mobile number for texts</label>
      <input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel"
             placeholder="(555) 123-4567" aria-describedby="phone-error">
      <p class="error" id="phone-error" role="alert" hidden>Enter a valid mobile number, like (555) 123-4567.</p>
    </div>

    <div class="field">
      <label class="label" for="timing">Send pickup reminder</label>
      <select id="timing" name="timing">
        <option value="" disabled selected>Choose a time</option>
        <option value="30">30 minutes before pickup</option>
        <option value="60">1 hour before pickup</option>
      </select>
    </div>

    <button type="submit">Save changes</button>
    <p class="status" id="status" role="status"></p>
  </form>
</main>

<script>
  const form = document.getElementById('form');
  const phone = document.getElementById('phone');
  const error = document.getElementById('phone-error');
  const status = document.getElementById('status');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    status.textContent = '';
    const digits = phone.value.replace(/\D/g, '');
    const valid = digits.length === 10 || (digits.length === 11 && digits[0] === '1');
    // Empty is allowed (no texts); only a non-empty bad number is an error.
    const bad = phone.value.trim() !== '' && !valid;
    error.hidden = !bad;
    phone.setAttribute('aria-invalid', bad ? 'true' : 'false');
    if (bad) { phone.focus(); return; }
    // TODO: send the form values to the API here.
    status.textContent = 'Your settings are saved.';
  });
</script>
</body>
</html>
```

**Copy changes I made, so please check them:**
- **Toggles:** "Option 1", "Option 2" and "Enable feature" became Photo updates, Pickup reminders and Incident notes. Each has a one-line hint, and all three default to on.
- **Text field:** "Enter value" became a "Mobile number for texts" field with the placeholder `(555) 123-4567`.
- **Error text:** "Invalid input" became "Enter a valid mobile number, like (555) 123-4567." It tells parents what to fix.
- **Dropdown:** "Select..." with Choice A and B became "Send pickup reminder" with "30 minutes before pickup" and "1 hour before pickup". I picked this because it fits the pickup toggle. If your dropdown is meant for something else, such as delivery method, swap the label and options.
- **Button:** "Save" became "Save changes".
- **Heading:** "Settings" became "Notification settings".

**Still to do before you ship:**
- Replace the `TODO` in the script with your real API call.
- Decide whether parents should be able to turn off incident notes. Right now they can.
- I haven't opened this in a browser.
