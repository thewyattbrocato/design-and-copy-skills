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
    --line: #8896a5;
    --soft: #e4e7eb;
    --bg: #f7f5f2;
    --card: #fff;
    --accent: #1d6b57;
    --error: #b42318;
    --error-bg: #fef3f2;
    --ok-bg: #ecf8f3;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 24px 16px;
    font: 1rem/1.5 system-ui, sans-serif;
    color: var(--ink); background: var(--bg);
  }
  main { max-width: 32rem; margin: 0 auto; }
  h1 { font-size: 1.5rem; margin: 0 0 4px; }
  .intro { margin: 0 0 24px; color: var(--muted); }
  form { background: var(--card); border-radius: 12px; padding: 8px 20px 24px; }
  fieldset { border: 0; margin: 0; padding: 0; min-width: 0; }
  legend { font-weight: 600; padding: 16px 0 4px; }

  /* Toggle rows */
  .toggle {
    display: flex; align-items: center; justify-content: space-between; gap: 16px;
    min-height: 56px; padding: 10px 0; border-bottom: 1px solid var(--soft);
  }
  .toggle .text { min-width: 0; overflow-wrap: anywhere; }
  .toggle .label { display: block; font-weight: 500; }
  .toggle .hint { display: block; font-size: .875rem; color: var(--muted); }
  .switch {
    appearance: none; flex: none; margin: 0; cursor: pointer;
    width: 48px; height: 28px; border-radius: 14px;
    background: var(--line); position: relative; transition: background .15s;
  }
  .switch::after {
    content: ""; position: absolute; top: 3px; left: 3px;
    width: 22px; height: 22px; border-radius: 50%; background: #fff;
    transition: transform .15s;
  }
  .switch:checked { background: var(--accent); }
  .switch:checked::after { transform: translateX(20px); }

  :focus-visible { outline: 3px solid #1a56db; outline-offset: 2px; }

  /* Fields */
  .field { margin-top: 20px; }
  .field label { display: block; font-weight: 600; margin-bottom: 4px; }
  .field .hint { display: block; font-size: .875rem; color: var(--muted); margin-bottom: 6px; }
  input[type=text], select {
    width: 100%; min-height: 44px; padding: 8px 12px;
    font: inherit; color: var(--ink); background: #fff;
    border: 1px solid var(--line); border-radius: 8px;
  }
  input[aria-invalid=true] { border-color: var(--error); border-width: 2px; }
  .error {
    display: flex; gap: 6px; margin: 6px 0 0;
    color: var(--error); font-size: .875rem; font-weight: 500;
  }
  .error[hidden] { display: none; }

  /* Actions */
  .actions { margin-top: 24px; display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
  button {
    min-height: 44px; padding: 8px 28px; font: inherit; font-weight: 600;
    color: #fff; background: var(--accent); border: 0; border-radius: 8px; cursor: pointer;
  }
  button[aria-disabled=true] { opacity: .7; cursor: progress; }
  .status { margin-top: 16px; padding: 10px 12px; border-radius: 8px; }
  .status:empty { display: none; }
  .status.ok { background: var(--ok-bg); color: #14513f; }
  .status.fail { background: var(--error-bg); color: var(--error); }
  .status button {
    min-height: 0; padding: 0; margin-left: 8px; background: none;
    color: inherit; text-decoration: underline; font-weight: 600;
  }

  @media (prefers-reduced-motion: reduce) {
    .switch, .switch::after { transition: none; }
  }
</style>
</head>
<body>
<main>
  <h1>Notification settings</h1>
  <p class="intro">Choose how you hear about your dog’s day.</p>

  <form id="form" novalidate>
    <fieldset>
      <legend>What to send me</legend>

      <label class="toggle">
        <span class="text">
          <span class="label">Photo updates</span>
          <span class="hint">Pictures from your dog’s day</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="photos">
      </label>

      <label class="toggle">
        <span class="text">
          <span class="label">Pickup reminders</span>
          <span class="hint">A heads-up before pickup time</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="pickup">
      </label>

      <label class="toggle">
        <span class="text">
          <span class="label">Incident notes</span>
          <span class="hint">Anything staff need you to know about, such as an injury or a change in behavior</span>
        </span>
        <input class="switch" type="checkbox" role="switch" name="incidents" checked>
      </label>
    </fieldset>

    <div class="field">
      <label for="method">Send notifications by</label>
      <select id="method" name="method">
        <option value="" selected disabled>Select…</option>
        <option value="text">Text message</option>
        <option value="email">Email</option>
      </select>
    </div>

    <div class="field">
      <label for="contact">Phone number or email</label>
      <input type="text" id="contact" name="contact" autocomplete="off"
             placeholder="Enter value" aria-describedby="contact-error">
      <p class="error" id="contact-error" hidden>
        <span aria-hidden="true">⚠</span>
        <span>Invalid input</span>
      </p>
    </div>

    <div class="actions">
      <button type="submit" id="save">Save</button>
    </div>
    <div class="status" id="status" role="status"></div>
  </form>
</main>

<script>
  const form = document.getElementById('form');
  const contact = document.getElementById('contact');
  const err = document.getElementById('contact-error');
  const save = document.getElementById('save');
  const status = document.getElementById('status');
  let saving = false;

  const valid = v => /^\S+@\S+\.\S+$/.test(v) || /^[+\d][\d\s().-]{6,}$/.test(v);

  function setInvalid(bad) {
    err.hidden = !bad;
    contact.setAttribute('aria-invalid', bad ? 'true' : 'false');
  }
  contact.addEventListener('input', () => { if (valid(contact.value.trim())) setInvalid(false); });

  async function submit() {
    if (saving) return;
    status.className = 'status'; status.textContent = '';
    if (!valid(contact.value.trim())) {
      setInvalid(true); contact.focus(); return;
    }
    saving = true;
    save.setAttribute('aria-disabled', 'true'); save.textContent = 'Saving…';
    try {
      // TODO: replace with the real save request, sending the form values.
      await new Promise(r => setTimeout(r, 400));
      status.className = 'status ok';
      status.textContent = 'Saved. Your notification settings are updated.';
    } catch (e) {
      status.className = 'status fail';
      status.innerHTML = 'Your settings weren’t saved. Your changes are still here. <button type="button" id="retry">Try again</button>';
      document.getElementById('retry').addEventListener('click', submit);
    } finally {
      saving = false;
      save.removeAttribute('aria-disabled'); save.textContent = 'Save';
    }
  }
  form.addEventListener('submit', e => { e.preventDefault(); submit(); });
</script>
</body>
</html>
```

**What I changed and why**
- **Placeholder labels became real ones.** "Option 1", "Option 2" and "Enable feature" are now Photo updates, Pickup reminders and Incident notes, each with a one-line hint. The dropdown is "Send notifications by" with Text message and Email as its two choices. The text field is labelled "Phone number or email".
- **Error state.** The "Invalid input" text sits under the field with a ⚠ icon, so it doesn't rely on color alone. The field also gets a thicker red border. On Save, focus moves to the field. Screen readers get the error through `aria-invalid` and `aria-describedby`.
- **Saving.** The button shows "Saving…" and ignores repeat clicks. A success message appears in words. A failure keeps what the parent typed and offers "Try again".
- **Access and layout.** Toggles are real checkboxes with `role="switch"` and a visible focus ring. Targets are at least 44px tall, and long text wraps. Reduced-motion is respected. I kept your structure and added no dark theme.

**Needs your call**
- Incident notes starts on, since parents will usually want those. Change it if that's not your policy.
- The save request is a stub (`TODO` in the script), so wire in your endpoint.
- The "Invalid input" wording is as you gave it. Something more specific, like "Enter a phone number or email we can reach you at", would help parents more.
- The validation regexes are loose, so swap in your own rules.
- I haven't run this in a browser or tested it with a screen reader.
