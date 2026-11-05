```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Notification settings</title>
<style>
  :root {
    --bg: #f7f4ef;
    --card: #ffffff;
    --text: #231f1a;
    --muted: #5e564c;
    --border: #8a8174;
    --accent: #1f6f5c;
    --accent-text: #ffffff;
    --error: #b3261e;
    --focus: #1a4fd6;
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
    border-radius: 12px;
    padding: 24px;
  }
  h1 { margin: 0 0 4px; font-size: 1.5rem; line-height: 1.25; }
  .intro { margin: 0 0 24px; color: var(--muted); }
  fieldset { border: 0; margin: 0 0 24px; padding: 0; }
  legend { font-weight: 600; padding: 0; margin-bottom: 8px; }

  /* Toggle rows */
  .toggle {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 16px;
    padding: 12px 0;
    border-top: 1px solid #e4ded4;
    cursor: pointer;
  }
  .toggle-text { min-width: 0; overflow-wrap: anywhere; }
  .toggle-label { display: block; font-weight: 600; }
  .toggle-hint { display: block; color: var(--muted); font-size: 0.9rem; }
  .toggle input {
    appearance: none;
    flex: none;
    position: relative;
    width: 48px;
    height: 28px;
    margin: 2px 0 0;
    border-radius: 14px;
    background: var(--border);
    cursor: pointer;
    transition: background 0.15s;
  }
  .toggle input::after {
    content: "";
    position: absolute;
    top: 3px; left: 3px;
    width: 22px; height: 22px;
    border-radius: 50%;
    background: #fff;
    transition: transform 0.15s;
  }
  .toggle input:checked { background: var(--accent); }
  .toggle input:checked::after { transform: translateX(20px); }
  /* State is also readable without color: On/Off word */
  .toggle .state { flex: none; font-size: 0.85rem; color: var(--muted); min-width: 2ch; }

  /* Fields */
  .field { margin-bottom: 20px; }
  label.field-label { display: block; font-weight: 600; margin-bottom: 4px; }
  .help { color: var(--muted); font-size: 0.9rem; margin: 0 0 6px; }
  input[type="tel"], select {
    width: 100%;
    min-height: 44px;
    padding: 8px 12px;
    font: inherit;
    color: var(--text);
    background: #fff;
    border: 1.5px solid var(--border);
    border-radius: 8px;
  }
  input[aria-invalid="true"] { border-color: var(--error); }
  .error {
    display: none;
    margin: 6px 0 0;
    color: var(--error);
    font-size: 0.9rem;
  }
  .error.show { display: block; }
  .error::before { content: "\26A0\FE0E  "; }

  /* Button + status */
  button {
    min-height: 44px;
    padding: 8px 24px;
    font: inherit;
    font-weight: 600;
    color: var(--accent-text);
    background: var(--accent);
    border: 0;
    border-radius: 8px;
    cursor: pointer;
  }
  button[aria-disabled="true"] { opacity: 0.7; cursor: progress; }
  .status { margin: 12px 0 0; min-height: 1.5em; }
  .status.ok { color: #14573f; }
  .status.fail { color: var(--error); }

  :focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }

  @media (max-width: 360px) {
    main { padding: 16px; }
    button { width: 100%; }
  }
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
          <span class="toggle-label">Photo updates</span>
          <span class="toggle-hint">Pictures and videos from your dog's day.</span>
        </span>
        <span class="state" aria-hidden="true"></span>
        <input type="checkbox" role="switch" name="photos" checked>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-label">Pickup reminders</span>
          <span class="toggle-hint">A heads-up before it's time to collect your dog.</span>
        </span>
        <span class="state" aria-hidden="true"></span>
        <input type="checkbox" role="switch" name="pickup" checked>
      </label>

      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-label">Incident notes</span>
          <span class="toggle-hint">Notes from staff if something happens, such as a scrape or a scuffle.</span>
        </span>
        <span class="state" aria-hidden="true"></span>
        <input type="checkbox" role="switch" name="incidents" checked>
      </label>
    </fieldset>

    <div class="field">
      <label class="field-label" for="method">Send updates by</label>
      <select id="method" name="method">
        <option value="text">Text message</option>
        <option value="email">Email</option>
      </select>
    </div>

    <div class="field">
      <label class="field-label" for="phone">Phone number for texts</label>
      <p class="help" id="phone-help">Only used for your dog's updates.</p>
      <input id="phone" name="phone" type="tel" autocomplete="tel"
             aria-describedby="phone-help phone-error">
      <p class="error" id="phone-error">That phone number doesn't look right. Check the digits and try again.</p>
    </div>

    <button type="submit" id="save">Save</button>
    <p class="status" id="status" role="status"></p>
  </form>
</main>

<script>
  const form = document.getElementById('form');
  const phone = document.getElementById('phone');
  const err = document.getElementById('phone-error');
  const method = document.getElementById('method');
  const save = document.getElementById('save');
  const status = document.getElementById('status');

  // On/Off word beside each switch
  form.querySelectorAll('.toggle').forEach(row => {
    const box = row.querySelector('input');
    const word = row.querySelector('.state');
    const sync = () => word.textContent = box.checked ? 'On' : 'Off';
    box.addEventListener('change', sync);
    sync();
  });

  function phoneProblem() {
    if (method.value !== 'text') return false;
    const digits = phone.value.replace(/\D/g, '');
    return digits.length < 7 || digits.length > 15 || /[^\d\s()+.\-]/.test(phone.value);
  }
  function showError(on) {
    err.classList.toggle('show', on);
    phone.setAttribute('aria-invalid', on ? 'true' : 'false');
  }
  phone.addEventListener('input', () => { if (err.classList.contains('show')) showError(phoneProblem()); });
  method.addEventListener('change', () => showError(false));

  form.addEventListener('submit', async e => {
    e.preventDefault();
    if (save.getAttribute('aria-disabled') === 'true') return;
    status.className = 'status'; status.textContent = '';

    if (phoneProblem()) { showError(true); phone.focus(); return; }
    showError(false);

    save.setAttribute('aria-disabled', 'true');
    save.textContent = 'Saving…';
    try {
      // TODO: replace with the real request, e.g. await fetch('/api/notification-settings', {...})
      await new Promise(r => setTimeout(r, 400));
      status.className = 'status ok';
      status.textContent = 'Saved. Your notification choices are updated.';
    } catch (_) {
      status.className = 'status fail';
      status.textContent = "We couldn't save your changes. Your choices are still here. Press Save to try again.";
    } finally {
      save.removeAttribute('aria-disabled');
      save.textContent = 'Save';
    }
  });
</script>
</body>
</html>
```

**What changed**
- **Copy:** I replaced the placeholder labels with your product's own terms. "Option 1", "Option 2" and "Enable feature" are now **Photo updates**, **Pickup reminders** and **Incident notes**. The dropdown is **Send updates by** with Text message and Email. The text field is **Phone number for texts**. "Invalid input" now says what's wrong and what to do.
- **Errors:** The message sits under the field with a ⚠ icon, so it doesn't rely on color alone. Focus moves to the field, and the field is marked invalid for assistive tech.
- **Save:** The button shows "Saving…" and ignores a second press. The result is announced in words. A failure keeps the person's choices and says to press Save again.
- **Toggles:** The whole row is clickable. Each switch has an On/Off word next to it. Each has a visible focus ring and a 44px minimum target. Long text wraps.
- **Other:** The layout holds down to 320px, and motion is off under reduced-motion.

**Needs your decision**
- All three toggles default to on, and the phone number is only checked when "Text message" is selected. Please confirm both.
- The save call is a stub (`setTimeout`). Swap in your real endpoint.
- The phone check is loose (7–15 digits). Tighten it if you only serve one country.
- I haven't run this in a browser or tested it with a screen reader.
