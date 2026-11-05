```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Notification settings</title>
<style>
  :root {
    --bg: #faf7f2; --card: #fff; --ink: #2b2623; --muted: #5f5750;
    --line: #8a8178; --hair: #e6e0d8; --accent: #2f6b4f; --accent-ink: #fff;
    --error: #b3261e; --error-bg: #fdecea; --ok-bg: #e8f3ed;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--ink);
         font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; }
  main { max-width: 34rem; margin: 0 auto; padding: 1.5rem 1rem 3rem; }
  h1 { font-size: 1.5rem; margin: 0 0 .25rem; }
  .lede { margin: 0 0 1.5rem; color: var(--muted); }
  form { background: var(--card); border: 1px solid var(--hair); border-radius: 12px; padding: 1.25rem; }
  fieldset { border: 0; margin: 0 0 1.5rem; padding: 0; min-width: 0; }
  legend { font-weight: 600; padding: 0; margin-bottom: .5rem; }

  .toggle { display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem;
            padding: .75rem 0; border-top: 1px solid var(--hair); }
  .toggle:first-of-type { border-top: 0; }
  .toggle label { flex: 1; min-width: 0; overflow-wrap: anywhere; }
  .toggle .name { display: block; font-weight: 500; }
  .toggle .hint { display: block; color: var(--muted); font-size: .875rem; }
  .switch { appearance: none; flex: none; width: 3rem; height: 1.75rem; margin: 0;
            border-radius: 999px; background: var(--line); position: relative; cursor: pointer;
            transition: background .15s; }
  .switch::after { content: ""; position: absolute; top: .2rem; left: .2rem; width: 1.35rem; height: 1.35rem;
                   border-radius: 50%; background: #fff; transition: transform .15s; }
  .switch:checked { background: var(--accent); }
  .switch:checked::after { transform: translateX(1.25rem); }
  .switch:disabled { opacity: .5; cursor: not-allowed; }
  .switch:focus-visible, input[type=text]:focus-visible, select:focus-visible, button:focus-visible {
    outline: 3px solid #1a5fd0; outline-offset: 2px; }
  .toggle:has(.switch:disabled) label { color: var(--muted); }
  .note { margin: .25rem 0 0; font-size: .875rem; color: var(--muted); }

  .field { margin-bottom: 1.25rem; }
  .field > label { display: block; font-weight: 600; margin-bottom: .25rem; }
  input[type=text], select { width: 100%; min-height: 2.75rem; padding: .5rem .75rem; font: inherit; color: inherit;
         background: #fff; border: 1.5px solid var(--line); border-radius: 8px; }
  input[aria-invalid=true] { border-color: var(--error); }
  .error { display: none; margin: .375rem 0 0; color: var(--error); font-size: .9375rem; }
  .error::before { content: "⚠ "; }
  input[aria-invalid=true] ~ .error { display: block; }

  .actions { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }
  button { min-height: 2.75rem; padding: .5rem 1.5rem; font: inherit; font-weight: 600; border: 0;
           border-radius: 8px; background: var(--accent); color: var(--accent-ink); cursor: pointer; }
  button[aria-busy=true] { opacity: .7; cursor: progress; }
  .status { margin: 0; padding: .5rem .75rem; border-radius: 8px; flex: 1 1 14rem; }
  .status:empty { display: none; }
  .status.ok { background: var(--ok-bg); }
  .status.fail { background: var(--error-bg); color: var(--error); }

  @media (max-width: 360px) { form { padding: 1rem; } button { width: 100%; } }
  @media (prefers-reduced-motion: reduce) { .switch, .switch::after { transition: none; } }
</style>
</head>
<body>
<main>
  <h1>Notification settings</h1>
  <p class="lede">Choose how you hear about your dog's day.</p>

  <form id="form" novalidate>
    <fieldset>
      <legend>What to send</legend>

      <div class="toggle">
        <label for="all"><span class="name">Send me notifications</span>
          <span class="hint">Turn off to pause everything below.</span></label>
        <input class="switch" type="checkbox" role="switch" id="all" checked>
      </div>
      <div class="toggle">
        <label for="photos"><span class="name">Photo updates</span>
          <span class="hint">Pictures from your dog's day.</span></label>
        <input class="switch topic" type="checkbox" role="switch" id="photos">
      </div>
      <div class="toggle">
        <label for="pickup"><span class="name">Pickup reminders</span>
          <span class="hint">A heads-up before it's time to collect your dog.</span></label>
        <input class="switch topic" type="checkbox" role="switch" id="pickup">
      </div>
      <div class="toggle">
        <label for="incidents"><span class="name">Incident notes</span>
          <span class="hint">Anything staff need you to know about, like a scrape or a skipped meal.</span></label>
        <input class="switch topic" type="checkbox" role="switch" id="incidents">
      </div>
      <p class="note" id="paused" hidden>Notifications are paused. Turn on “Send me notifications” to choose what you get.</p>
    </fieldset>

    <div class="field">
      <label for="method">How should we reach you?</label>
      <select id="method">
        <option value="" selected disabled>Select a method</option>
        <option value="text">Text message</option>
        <option value="email">Email</option>
      </select>
    </div>

    <div class="field" id="phone-field">
      <label for="phone">Mobile number for texts</label>
      <input type="text" id="phone" inputmode="tel" autocomplete="tel" placeholder="Mobile number"
             aria-describedby="phone-error">
      <p class="error" id="phone-error">Enter a mobile number with area code, for example 555 123 4567.</p>
    </div>

    <div class="actions">
      <button type="submit" id="save">Save</button>
      <p class="status" id="status" role="status" aria-live="polite"></p>
    </div>
  </form>
</main>

<script>
  const $ = id => document.getElementById(id);
  const all = $('all'), topics = document.querySelectorAll('.topic'),
        method = $('method'), phone = $('phone'), status = $('status'), save = $('save');

  function syncPause() {
    topics.forEach(t => t.disabled = !all.checked);
    $('paused').hidden = all.checked;
  }
  function syncMethod() {
    $('phone-field').hidden = method.value === 'email';
    if (method.value === 'email') phone.removeAttribute('aria-invalid');
  }
  all.addEventListener('change', syncPause);
  method.addEventListener('change', syncMethod);
  phone.addEventListener('input', () => phone.removeAttribute('aria-invalid'));
  syncPause(); syncMethod();

  function say(text, cls) { status.textContent = text; status.className = 'status ' + (cls || ''); }

  $('form').addEventListener('submit', async e => {
    e.preventDefault();
    say('');
    if (!method.value) { say('Choose how we should reach you.', 'fail'); method.focus(); return; }
    if (method.value === 'text' && phone.value.replace(/\D/g, '').length < 10) {
      phone.setAttribute('aria-invalid', 'true'); phone.focus(); return;
    }
    save.setAttribute('aria-busy', 'true'); save.textContent = 'Saving…';
    try {
      await saveSettings();   // replace with your real request
      say('Saved. Your notification choices are updated.', 'ok');
    } catch {
      say('We couldn’t save your changes. Your choices are still here. Press Save to try again.', 'fail');
    } finally {
      save.removeAttribute('aria-busy'); save.textContent = 'Save';
    }
  });

  function saveSettings() { return new Promise(r => setTimeout(r, 600)); }  // placeholder
</script>
</body>
</html>
```

**What changed and why**
- **Placeholder copy replaced.** "Option 1", "Option 2", "Enable feature", "Choice A/B" and "Invalid input" are now your three topics (photo updates, pickup reminders, incident notes). The master toggle is "Send me notifications". The dropdown is Text message or Email. The error now says what to fix.
- **Master toggle.** When it's off, the three topic toggles are disabled and a line explains why.
- **Save button.** It shows a busy state, then a success or failure message in words. A failure keeps what the parent entered and tells them to press Save again.
- **Error handling.** The error shows under the phone field with a ⚠ icon and the message, so it doesn't rely on color alone. Focus moves to the field, and screen readers get the message through `aria-describedby`.
- **Accessibility and layout.** Controls are real switches and inputs with labels, and focus rings are visible. The layout holds at 320px, and reduced-motion is respected.
- **Defaults.** All three topics start off, so nobody is opted in without choosing.

**Open items**
- `saveSettings()` is a stand-in that always succeeds. Wire it to your API.
- I assumed 10-digit phone numbers and didn't add a policy on whether incident notes can be turned off. Both need your call.
- I haven't run this in a browser or with a screen reader.
