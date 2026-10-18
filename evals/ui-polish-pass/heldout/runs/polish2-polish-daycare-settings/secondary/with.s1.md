Here's the finished screen. I changed the placeholder labels to the three categories you named, added the missing states (error linked to its field, busy save, a status message), and made it work at narrow widths and under keyboard, forced-colors and reduced-motion settings.

**index.html**

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Settings</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main class="settings">
    <h1>Settings</h1>
    <p class="intro">Choose how you hear about your dog's day.</p>

    <form id="settings-form" novalidate>
      <fieldset class="group">
        <legend>Updates</legend>

        <label class="row">
          <span class="row-text">
            <span class="row-title">Photo updates</span>
            <span class="row-hint">Photos from your dog's day</span>
          </span>
          <span class="switch">
            <input type="checkbox" name="photo_updates" role="switch" checked>
            <span class="track" aria-hidden="true"></span>
          </span>
        </label>

        <label class="row">
          <span class="row-text">
            <span class="row-title">Pickup reminders</span>
            <span class="row-hint">A reminder before pickup time</span>
          </span>
          <span class="switch">
            <input type="checkbox" name="pickup_reminders" role="switch">
            <span class="track" aria-hidden="true"></span>
          </span>
        </label>

        <label class="row">
          <span class="row-text">
            <span class="row-title">Incident notes</span>
            <span class="row-hint">Notes about anything that happened during the day</span>
          </span>
          <span class="switch">
            <input type="checkbox" name="incident_notes" role="switch" checked>
            <span class="track" aria-hidden="true"></span>
          </span>
        </label>
      </fieldset>

      <div class="field">
        <label for="custom-value">[Field label]</label>
        <input
          id="custom-value"
          name="custom_value"
          type="text"
          placeholder="Enter value"
          aria-describedby="custom-value-error"
          autocomplete="off"
        >
        <p id="custom-value-error" class="error" hidden>
          <span aria-hidden="true">!</span> Invalid input
        </p>
      </div>

      <div class="field">
        <label for="custom-choice">[Dropdown label]</label>
        <select id="custom-choice" name="custom_choice">
          <option value="">Select...</option>
          <option value="a">Choice A</option>
          <option value="b">Choice B</option>
        </select>
      </div>

      <div class="actions">
        <button type="submit" class="primary">Save</button>
        <p id="save-status" class="status" role="status" aria-live="polite"></p>
      </div>
    </form>
  </main>

  <script>
    const form = document.getElementById('settings-form');
    const input = document.getElementById('custom-value');
    const error = document.getElementById('custom-value-error');
    const status = document.getElementById('save-status');
    const saveButton = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (saveButton.disabled) return;

      if (!input.value.trim()) {
        input.setAttribute('aria-invalid', 'true');
        error.hidden = false;
        status.textContent = '';
        input.focus();
        return;
      }

      input.removeAttribute('aria-invalid');
      error.hidden = true;

      saveButton.disabled = true;
      saveButton.textContent = 'Saving…';
      status.textContent = '';

      try {
        // Replace with the real request, e.g. await fetch('/api/notification-settings', {...})
        await new Promise((resolve) => setTimeout(resolve, 600));
        status.textContent = 'Settings saved.';
      } catch (err) {
        status.textContent = "Your settings weren't saved. Check your connection and try again.";
      } finally {
        saveButton.disabled = false;
        saveButton.textContent = 'Save';
      }
    });
  </script>
</body>
</html>
```

**styles.css**

```css
:root {
  --text: #1d1d1f;
  --muted: #55595f;
  --surface: #ffffff;
  --line: #d0d4da;
  --field-border: #767676;
  --accent: #1f5f4a;
  --accent-text: #ffffff;
  --error: #b42318;
  --focus: #1a56db;
  --radius: 0.5rem;
  --font: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font: 1rem/1.5 var(--font);
  color: var(--text);
  background: var(--surface);
}

.settings {
  max-width: 32rem;
  margin: 0 auto;
  padding: 1.5rem 1rem 2rem;
}

h1 {
  margin: 0 0 0.25rem;
  font-size: 1.75rem;
  line-height: 1.2;
}

.intro {
  margin: 0 0 1.5rem;
  color: var(--muted);
}

/* Groups */
fieldset {
  margin: 0 0 1.5rem;
  padding: 0;
  border: 0;
}

legend {
  padding: 0;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.group {
  border-top: 1px solid var(--line);
}

/* Toggle rows */
.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  min-height: 3.25rem;
  padding: 0.75rem 0;
  border-bottom: 1px solid var(--line);
  cursor: pointer;
}

.row-text {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.row-title {
  font-weight: 500;
}

.row-hint {
  font-size: 0.875rem;
  color: var(--muted);
  overflow-wrap: anywhere;
}

/* Switch: native checkbox stays focusable and announced; the track is the visual */
.switch {
  position: relative;
  flex: none;
  width: 2.75rem;
  height: 1.5rem;
}

.switch input {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.track {
  position: absolute;
  inset: 0;
  border: 1px solid var(--field-border);
  border-radius: 999px;
  background: #e9ecef;
  transition: background-color 150ms ease;
  pointer-events: none;
}

.track::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 0.2rem;
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
  background: #ffffff;
  border: 1px solid var(--field-border);
  transform: translateY(-50%);
  transition: transform 150ms ease;
}

.switch input:checked + .track {
  background: var(--accent);
  border-color: var(--accent);
}

.switch input:checked + .track::after {
  transform: translate(1.25rem, -50%);
  border-color: var(--accent);
}

.switch input:focus-visible + .track {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

/* Fields */
.field {
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
  margin-bottom: 1.25rem;
}

.field label {
  font-weight: 500;
}

input[type="text"],
select {
  width: 100%;
  min-height: 2.75rem;
  padding: 0.5rem 0.75rem;
  font: inherit;
  color: var(--text);
  background: var(--surface);
  border: 1px solid var(--field-border);
  border-radius: var(--radius);
}

input[type="text"]::placeholder {
  color: var(--muted);
}

input[aria-invalid="true"] {
  border: 2px solid var(--error);
  padding: calc(0.5rem - 1px) calc(0.75rem - 1px);
}

input:focus-visible,
select:focus-visible,
button:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.error {
  margin: 0;
  font-size: 0.875rem;
  color: var(--error);
  font-weight: 500;
}

/* Actions */
.actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1rem;
}

button {
  min-height: 2.75rem;
  padding: 0.5rem 1.25rem;
  font: inherit;
  font-weight: 600;
  border-radius: var(--radius);
  cursor: pointer;
}

.primary {
  color: var(--accent-text);
  background: var(--accent);
  border: 1px solid var(--accent);
}

.primary:hover {
  background: #184c3b;
}

.primary:disabled {
  cursor: progress;
  opacity: 0.7;
}

.status {
  margin: 0;
  color: var(--muted);
}

/* Narrow screens: full-width save button */
@media (max-width: 26rem) {
  .actions button {
    flex: 1 1 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .track,
  .track::after {
    transition: none;
  }
}

@media (forced-colors: active) {
  .track,
  .track::after,
  input[type="text"],
  select,
  button {
    border: 1px solid ButtonText;
  }

  .switch input:checked + .track {
    background: Highlight;
    border-color: Highlight;
  }

  .error {
    color: CanvasText;
  }
}
```

**Notes**

- **Placeholder copy:** I mapped "Option 1", "Option 2" and "Enable feature" to Photo updates, Pickup reminders and Incident notes, based on your description. The text field and dropdown have no stated purpose, so their labels are `[Field label]` and `[Dropdown label]`. Replace them before shipping.
- **Not checked:** I haven't rendered this in a browser, run it with a screen reader or tested it at 200% zoom. The save call is a 600 ms stub that always succeeds, so the failure path only shows if you swap in a real request. I also assumed "Invalid input" means the field is empty; if your rule is different, change the check in the script.
