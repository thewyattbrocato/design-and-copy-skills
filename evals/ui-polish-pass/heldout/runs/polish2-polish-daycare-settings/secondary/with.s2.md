The screen is below. I replaced the placeholder labels with the three things parents choose (photo updates, pickup reminders, incident notes), made the switches real checkboxes with `role="switch"`, and added the error, busy and saved states. Layout, palette and type are new since there was no existing design to keep.

**index.html**
```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Notification settings</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to settings</a>

  <main id="main" class="screen">
    <h1>Settings</h1>

    <form id="settings-form" novalidate>
      <fieldset class="group">
        <legend>How you hear about your dog's day</legend>

        <label class="switch-row">
          <span class="switch-text">Photo updates</span>
          <input class="switch" type="checkbox" role="switch" name="photo_updates" checked>
        </label>

        <label class="switch-row">
          <span class="switch-text">Pickup reminders</span>
          <input class="switch" type="checkbox" role="switch" name="pickup_reminders">
        </label>

        <label class="switch-row">
          <span class="switch-text">Incident notes</span>
          <input class="switch" type="checkbox" role="switch" name="incident_notes">
        </label>
      </fieldset>

      <div class="field">
        <label for="details">Additional details</label>
        <input id="details" name="details" type="text" placeholder="Enter value"
               aria-describedby="details-error">
        <p id="details-error" class="error" hidden>
          <span class="error-icon" aria-hidden="true">!</span> Invalid input
        </p>
      </div>

      <div class="field">
        <label for="choice">Send updates by</label>
        <select id="choice" name="choice">
          <option value="" disabled selected>Select...</option>
          <option value="a">Choice A</option>
          <option value="b">Choice B</option>
        </select>
      </div>

      <button type="submit" id="save" class="save">Save</button>
      <p id="status" class="status" role="status" aria-live="polite"></p>
    </form>
  </main>

  <script>
    const form = document.getElementById('settings-form');
    const saveBtn = document.getElementById('save');
    const status = document.getElementById('status');
    const details = document.getElementById('details');
    const detailsError = document.getElementById('details-error');

    // Replace with the real request. Throw on failure.
    async function saveSettings(data) {
      await new Promise(resolve => setTimeout(resolve, 600));
    }

    // Replace with the real rule for the field. Returns true when valid.
    function isDetailsValid() {
      return true;
    }

    function showDetailsError(show) {
      detailsError.hidden = !show;
      details.setAttribute('aria-invalid', String(show));
    }

    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      status.textContent = '';

      if (!isDetailsValid()) {
        showDetailsError(true);
        details.focus();
        return;
      }
      showDetailsError(false);

      saveBtn.disabled = true;
      saveBtn.setAttribute('aria-busy', 'true');
      saveBtn.textContent = 'Saving…';

      try {
        await saveSettings(new FormData(form));
        status.textContent = 'Settings saved.';
      } catch (err) {
        status.textContent = "Couldn't save. Your changes are still here. Try again.";
      } finally {
        saveBtn.disabled = false;
        saveBtn.removeAttribute('aria-busy');
        saveBtn.textContent = 'Save';
      }
    });

    details.addEventListener('input', () => {
      if (!detailsError.hidden && isDetailsValid()) showDetailsError(false);
    });
  </script>
</body>
</html>
```

**styles.css**
```css
:root {
  --text: #1d1b19;
  --muted: #5c5752;
  --bg: #ffffff;
  --line: #767676;
  --rule: #e3dfd9;
  --accent: #1f6f5c;
  --accent-ink: #ffffff;
  --error: #b3261e;
  --focus: #0b57d0;
  --radius: 10px;

  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: var(--text);
  background: var(--bg);
}

*, *::before, *::after { box-sizing: border-box; }

body { margin: 0; }

.skip-link {
  position: absolute;
  left: 8px;
  top: -48px;
  padding: 8px 12px;
  background: var(--text);
  color: #fff;
  border-radius: 6px;
}
.skip-link:focus { top: 8px; }

.screen {
  max-width: 480px;
  margin: 0 auto;
  padding: 24px 16px 32px;
}

h1 {
  font-size: 1.75rem;
  line-height: 1.2;
  margin: 0 0 16px;
}

.group {
  border: 0;
  padding: 0;
  margin: 0 0 24px;
}

legend {
  font-weight: 600;
  padding: 0;
  margin-bottom: 8px;
}

.switch-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 56px;
  padding: 12px 0;
  border-bottom: 1px solid var(--rule);
  cursor: pointer;
}
.switch-row:last-child { border-bottom: 0; }

.switch-text {
  flex: 1;
  min-width: 0;
  overflow-wrap: anywhere;
}

.switch {
  appearance: none;
  flex: none;
  position: relative;
  width: 52px;
  height: 32px;
  margin: 0;
  border-radius: 999px;
  background: var(--line);
  cursor: pointer;
  transition: background-color 0.2s ease;
}
.switch::before {
  content: "";
  position: absolute;
  top: 4px;
  left: 4px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  transition: transform 0.2s ease;
}
.switch:checked { background: var(--accent); }
.switch:checked::before { transform: translateX(20px); }
.switch:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.field {
  display: grid;
  gap: 6px;
  margin: 0 0 20px;
}
.field label { font-weight: 600; }

input[type="text"],
select {
  font: inherit;
  width: 100%;
  min-height: 48px;
  padding: 10px 12px;
  color: var(--text);
  background: #fff;
  border: 1px solid var(--line);
  border-radius: var(--radius);
}
input[type="text"][aria-invalid="true"] {
  border-color: var(--error);
  box-shadow: inset 0 0 0 1px var(--error);
}
input[type="text"]::placeholder { color: var(--muted); }

input[type="text"]:focus-visible,
select:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.error {
  display: flex;
  align-items: center;
  gap: 6px;
  margin: 0;
  font-size: 0.9rem;
  color: var(--error);
}
.error-icon {
  display: inline-grid;
  place-items: center;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--error);
  color: #fff;
  font-size: 0.75rem;
  font-weight: 700;
}

.save {
  font: inherit;
  font-weight: 600;
  width: 100%;
  min-height: 48px;
  margin-top: 8px;
  border: 0;
  border-radius: var(--radius);
  background: var(--accent);
  color: var(--accent-ink);
  cursor: pointer;
}
.save:hover { filter: brightness(0.92); }
.save:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}
.save:disabled {
  background: #d6d2cc;
  color: #3d3935;
  cursor: wait;
  filter: none;
}

.status {
  min-height: 1.5em;
  margin: 12px 0 0;
  color: var(--muted);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .switch,
  .switch::before { transition: none; }
}
```

What I changed and why:
- **Labels:** "Option 1", "Option 2" and "Enable feature" became photo updates, pickup reminders and incident notes, the three things you described. Confirm that mapping. "Enter value", "Select..." and "Choice A/B" are kept as given because the request doesn't say what they should be.
- **Error:** "Invalid input" is hidden until validation fails. It sits under the field, has a "!" icon as well as red text, and the field gets `aria-invalid` and focus. `isDetailsValid()` is a stub that always returns true, so you need to supply the real rule.
- **Save:** shows "Saving…" and is disabled while the request runs, so it can't be double-submitted. A failure keeps what was typed and says so. `saveSettings()` is a stub with a 600 ms delay; wire it to your API.
- **Access:** each switch has its own name, there's a visible focus ring on every control, a skip link, and the layout wraps at 320 px and at 200% text. Motion is removed under reduced-motion.

Not checked: I did not run this in a browser, test it with a screen reader, or measure contrast with a tool; the colors were chosen to meet WCAG AA by reasoning only. No dark theme was added because the project doesn't have one.
