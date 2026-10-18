I couldn't save this as a file because the Write tool is disabled in this session. The full screen is below as one file. I haven't run it in a browser or tested it with a screen reader.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Notification settings</title>
<style>
  :root {
    --bg: #f6f7f9; --card: #fff; --text: #1d2433; --muted: #5b6475;
    --border: #7a8396; --line: #e3e6ec; --accent: #1f5fd1; --accent-text: #fff;
    --error: #b3261e; --ok: #1b6e3c; --focus: #1f5fd1;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 24px 16px; background: var(--bg); color: var(--text);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
  }
  main {
    max-width: 480px; margin: 0 auto; background: var(--card);
    border-radius: 12px; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,.12);
  }
  h1 { margin: 0 0 4px; font-size: 1.5rem; }
  .intro { margin: 0 0 20px; color: var(--muted); }
  fieldset { border: 0; margin: 0 0 20px; padding: 0; }
  legend { padding: 0; font-weight: 600; margin-bottom: 4px; }

  .toggle {
    display: flex; align-items: center; justify-content: space-between; gap: 16px;
    min-height: 56px; padding: 8px 0; border-bottom: 1px solid var(--line); cursor: pointer;
  }
  .toggle-text { min-width: 0; overflow-wrap: anywhere; }
  .toggle-title { display: block; font-weight: 500; }
  .toggle-hint { display: block; font-size: .875rem; color: var(--muted); }
  .toggle input {
    appearance: none; flex: none; position: relative; width: 48px; height: 28px; margin: 0;
    border-radius: 14px; background: #fff; border: 2px solid var(--border); cursor: pointer;
    transition: background .15s, border-color .15s;
  }
  .toggle input::after {
    content: ""; position: absolute; top: 3px; left: 3px; width: 18px; height: 18px;
    border-radius: 50%; background: var(--border); transition: transform .15s, background .15s;
  }
  .toggle input:checked { background: var(--accent); border-color: var(--accent); }
  .toggle input:checked::after { transform: translateX(20px); background: #fff; }

  .field { margin-bottom: 20px; }
  label.lbl { display: block; font-weight: 600; margin-bottom: 6px; }
  .help { margin: 4px 0 0; font-size: .875rem; color: var(--muted); }
  select, input[type="text"] {
    width: 100%; min-height: 44px; padding: 8px 12px; font: inherit; color: var(--text);
    background: #fff; border: 1px solid var(--border); border-radius: 8px;
  }
  input[aria-invalid="true"] { border: 2px solid var(--error); }
  .error { margin: 6px 0 0; font-size: .875rem; color: var(--error); }
  .error[hidden] { display: none; }

  :focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }

  button {
    min-height: 44px; padding: 8px 24px; font: inherit; font-weight: 600;
    color: var(--accent-text); background: var(--accent); border: 0; border-radius: 8px; cursor: pointer;
  }
  button:hover { filter: brightness(.92); }
  button[aria-disabled="true"] { opacity: .7; cursor: progress; }
  .status { margin: 16px 0 0; min-height: 1.5em; }
  .status.ok { color: var(--ok); }
  .status.fail { color: var(--error); }
  .status button {
    min-height: 44px; padding: 4px 8px; margin-left: 4px;
    background: none; color: var(--accent); text-decoration: underline;
  }

  @media (prefers-reduced-motion: reduce) { * { transition: none !important; } }
  @media (forced-colors: active) {
    .toggle input::after { background: ButtonText; }
    .toggle input:checked::after { background: HighlightText; }
  }
</style>
</head>
<body>
<main>
  <h1>Settings</h1>
  <p class="intro">Choose how you hear about your dog’s day.</p>

  <form id="form" novalidate>
    <fieldset>
      <legend>What to send me</legend>
      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Photo updates</span>
          <span class="toggle-hint">Pictures from your dog’s day</span>
        </span>
        <input type="checkbox" role="switch" name="photos">
      </label>
      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Pickup reminders</span>
          <span class="toggle-hint">A heads-up before it’s time to collect your dog</span>
        </span>
        <input type="checkbox" role="switch" name="pickup">
      </label>
      <label class="toggle">
        <span class="toggle-text">
          <span class="toggle-title">Incident notes</span>
          <span class="toggle-hint">Notes from staff if something happens during the day</span>
        </span>
        <input type="checkbox" role="switch" name="incidents">
      </label>
    </fieldset>

    <div class="field">
      <label class="lbl" for="method">Send notifications by</label>
      <select id="method" name="method">
        <option value="" selected disabled>Select…</option>
        <option value="email">Email</option>
        <option value="sms">Text message</option>
      </select>
    </div>

    <div class="field">
      <label class="lbl" for="contact">Email address or mobile number</label>
      <input type="text" id="contact" name="contact" placeholder="Enter value"
             autocomplete="off" aria-describedby="contact-help contact-error">
      <p class="help" id="contact-help">We’ll only use this for the notifications you turn on.</p>
      <p class="error" id="contact-error" hidden></p>
    </div>

    <button type="submit" id="save">Save</button>
    <p class="status" id="status" role="status" aria-live="polite"></p>
  </form>
</main>

<script>
  const form = document.getElementById('form');
  const method = document.getElementById('method');
  const contact = document.getElementById('contact');
  const err = document.getElementById('contact-error');
  const status = document.getElementById('status');
  const save = document.getElementById('save');
  let busy = false;

  function setError(msg) {
    err.hidden = !msg;
    err.textContent = msg ? 'Invalid input: ' + msg : '';
    if (msg) contact.setAttribute('aria-invalid', 'true');
    else contact.removeAttribute('aria-invalid');
  }

  function validate() {
    const v = contact.value.trim();
    if (!method.value) return { el: method, msg: 'Choose how you’d like to be notified.' };
    if (!v) return { el: contact, msg: 'enter an email address or mobile number.' };
    if (method.value === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v))
      return { el: contact, msg: 'that doesn’t look like an email address, e.g. name@example.com.' };
    if (method.value === 'sms' && v.replace(/\D/g, '').length < 10)
      return { el: contact, msg: 'a mobile number needs at least 10 digits.' };
    return null;
  }

  // TODO: replace with the real endpoint; it must reject on failure.
  async function saveSettings(data) {
    if (!navigator.onLine) throw new Error('offline');
    return data;
  }

  async function submit() {
    if (busy) return;
    setError('');
    status.className = 'status';
    status.textContent = '';
    const problem = validate();
    if (problem) {
      if (problem.el === contact) setError(problem.msg);
      else { status.className = 'status fail'; status.textContent = problem.msg; }
      problem.el.focus();
      return;
    }
    busy = true;
    save.setAttribute('aria-disabled', 'true');
    save.textContent = 'Saving…';
    try {
      await saveSettings(Object.fromEntries(new FormData(form)));
      status.className = 'status ok';
      status.textContent = 'Saved. Your notification settings are updated.';
    } catch (e) {
      status.className = 'status fail';
      status.innerHTML = 'Couldn’t save your settings. Your choices are still here. <button type="button" id="retry">Try again</button>';
      document.getElementById('retry').addEventListener('click', submit);
    } finally {
      busy = false;
      save.removeAttribute('aria-disabled');
      save.textContent = 'Save';
    }
  }

  form.addEventListener('submit', e => { e.preventDefault(); submit(); });
  contact.addEventListener('input', () => setError(''));
</script>
</body>
</html>
```

**What changed**
- **Copy:** "Option 1", "Option 2" and "Enable feature" are now Photo updates, Pickup reminders and Incident notes, each with a one-line hint. The heading is still "Settings", with a short intro line added.
- **Dropdown and text field:** I couldn't tell what these controlled, so I assumed a delivery method (Email or Text message) and a matching contact field. Change the labels and options if that's wrong.
- **Error message:** "Invalid input" now leads the message and says what's wrong, for example "Invalid input: that doesn't look like an email address". It shows under the field, is linked to the field for screen readers, and focus moves to the first problem.
- **Save:** The button shows "Saving…" and ignores repeat presses. Success is confirmed in words. On failure, the form keeps what was entered and offers "Try again".
- **Access:** Toggles are real switches you can reach by keyboard, with visible focus. Targets are at least 44px, and the layout holds down to 320px. Transitions are turned off for reduced-motion users.

**Still open**
- `saveSettings` is a stub that only fails when offline. Connect it to your real endpoint.
- All three toggles start off, so no one is opted in by default. Decide whether Incident notes should start on.
- **Not checked:** I didn't run it in a browser or with a screen reader.
