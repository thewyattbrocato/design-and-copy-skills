I couldn't write the files: the Write tool is disabled in this session, and I have no shell to save them. The finished HTML and CSS are below so you can paste them into `notification-settings.html` and `notification-settings.css`.

Three choices to check:
- **Toggle labels:** I mapped the three toggles to the topics you named: Option 1 → Photo updates, Option 2 → Pickup reminders, Enable feature → Incident notes.
- **Placeholder copy:** "Contact" (field label), "Preference" (dropdown label) and the Choice A/B options are placeholders. Replace them with the real labels and options.
- **Dark theme:** not included, since you didn't ask for one and the project doesn't have one.

**notification-settings.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Notification settings</title>
  <link rel="stylesheet" href="notification-settings.css">
</head>
<body>
  <main class="page">
    <h1>Settings</h1>

    <form id="settings-form" class="card" novalidate>
      <fieldset class="group">
        <legend>How you hear about your dog's day</legend>

        <label class="toggle">
          <span class="toggle-label">Photo updates</span>
          <input type="checkbox" role="switch" name="photo_updates">
          <span class="track" aria-hidden="true"></span>
        </label>

        <label class="toggle">
          <span class="toggle-label">Pickup reminders</span>
          <input type="checkbox" role="switch" name="pickup_reminders">
          <span class="track" aria-hidden="true"></span>
        </label>

        <label class="toggle">
          <span class="toggle-label">Incident notes</span>
          <input type="checkbox" role="switch" name="incident_notes">
          <span class="track" aria-hidden="true"></span>
        </label>
      </fieldset>

      <div class="field" id="contact-field">
        <label for="contact">Contact</label>
        <input id="contact" name="contact" type="text" placeholder="Enter value"
               aria-describedby="contact-error">
        <p id="contact-error" class="error" role="alert" hidden>Invalid input</p>
      </div>

      <div class="field">
        <label for="preference">Preference</label>
        <select id="preference" name="preference">
          <option value="" selected disabled>Select...</option>
          <option value="a">Choice A</option>
          <option value="b">Choice B</option>
        </select>
      </div>

      <div class="actions">
        <button type="submit" class="btn" id="save-btn">Save</button>
        <p id="status" class="status" role="status" aria-live="polite"></p>
      </div>
    </form>
  </main>

  <script>
    const form = document.getElementById('settings-form');
    const contact = document.getElementById('contact');
    const contactField = document.getElementById('contact-field');
    const contactError = document.getElementById('contact-error');
    const saveBtn = document.getElementById('save-btn');
    const status = document.getElementById('status');

    // Replace with the real request to your backend.
    async function saveSettings(data) {
      return Promise.resolve(data);
    }

    function showContactError(show) {
      contactField.classList.toggle('is-invalid', show);
      contact.setAttribute('aria-invalid', String(show));
      contactError.hidden = !show;
    }

    contact.addEventListener('input', () => {
      if (contact.value.trim() !== '') showContactError(false);
    });

    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      status.textContent = '';

      if (contact.value.trim() === '') {
        showContactError(true);
        contact.focus();
        return;
      }
      showContactError(false);

      const data = Object.fromEntries(new FormData(form));
      saveBtn.disabled = true;
      saveBtn.textContent = 'Saving…';
      status.textContent = 'Saving…';

      try {
        await saveSettings(data);
        status.textContent = 'Settings saved.';
      } catch (err) {
        status.textContent = "Couldn't save your settings. Your changes are still here. Try again.";
      } finally {
        saveBtn.disabled = false;
        saveBtn.textContent = 'Save';
      }
    });
  </script>
</body>
</html>
```

**notification-settings.css**

```css
:root {
  --bg: #f6f7f9;
  --surface: #ffffff;
  --text: #1d2330;
  --muted: #4a5365;
  --border: #8a93a3;
  --accent: #1f5fbf;
  --accent-text: #ffffff;
  --track-off: #6b7485;
  --error: #b42318;
  --focus: #1f5fbf;
  --radius: 10px;
  --space: 16px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: var(--text);
  background: var(--bg);
}

* { box-sizing: border-box; }

body {
  margin: 0;
  min-height: 100vh;
}

.page {
  max-width: 480px;
  margin: 0 auto;
  padding: 32px 16px;
}

h1 {
  font-size: 1.75rem;
  line-height: 1.2;
  margin: 0 0 var(--space);
}

.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  display: grid;
  gap: 24px;
}

/* Groups */
.group {
  border: 0;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 4px;
}

legend {
  font-weight: 600;
  padding: 0;
  margin-bottom: 8px;
}

/* Toggles: the whole row is the hit target (min 44px tall) */
.toggle {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  cursor: pointer;
  position: relative;
}

.toggle input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
  margin: 0;
}

.track {
  flex: 0 0 auto;
  width: 48px;
  height: 28px;
  border-radius: 999px;
  background: var(--track-off);
  position: relative;
  transition: background-color 150ms ease;
}

.track::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #ffffff;
  transition: transform 150ms ease;
}

.toggle input:checked + .track {
  background: var(--accent);
}

.toggle input:checked + .track::after {
  transform: translateX(20px);
}

/* Focus shows on the visual track, since the real input is hidden */
.toggle input:focus-visible + .track {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .track,
  .track::after {
    transition: none;
  }
}

/* Fields */
.field {
  display: grid;
  gap: 6px;
}

.field label {
  font-weight: 600;
}

input[type="text"],
select {
  font: inherit;
  width: 100%;
  min-height: 44px;
  padding: 8px 12px;
  color: var(--text);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
}

input[type="text"]::placeholder {
  color: var(--muted);
  opacity: 1;
}

input[type="text"]:focus-visible,
select:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.field.is-invalid input {
  border: 2px solid var(--error);
}

.error {
  margin: 0;
  color: var(--error);
  font-size: 0.9rem;
  font-weight: 600;
}

/* Actions */
.actions {
  display: grid;
  gap: 8px;
}

.btn {
  font: inherit;
  font-weight: 600;
  min-height: 44px;
  padding: 10px 20px;
  color: var(--accent-text);
  background: var(--accent);
  border: 0;
  border-radius: 8px;
  cursor: pointer;
  justify-self: start;
}

.btn:hover {
  filter: brightness(0.92);
}

.btn:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.btn:disabled {
  cursor: progress;
  opacity: 0.7;
}

.status {
  margin: 0;
  font-size: 0.95rem;
  color: var(--muted);
  min-height: 1.5em;
}

/* Narrow screens: tighter card padding so rows still fit at 320px */
@media (max-width: 360px) {
  .card {
    padding: 16px;
  }
}
```

**What the states do**
- **Error:** the contact field is required here, which I chose as the only rule because you gave none. Empty input shows "Invalid input" under the field, marks the field invalid, moves focus to it, and clears when the person types.
- **Save:** the button disables and reads "Saving…" while the request runs. Success says "Settings saved." On failure the message says the changes are still there and to try again, with no retry count.
- **Toggles:** each is a real switch with a visible focus ring and a 44px tap row. Reduced motion removes the slide.

**Not checked:** I did not run this in a browser or with a screen reader, and I did not test at 200% text size or 320px width beyond reading the CSS. The save call is a stub (`saveSettings`), so the real backend request and its failure path still need wiring up.
