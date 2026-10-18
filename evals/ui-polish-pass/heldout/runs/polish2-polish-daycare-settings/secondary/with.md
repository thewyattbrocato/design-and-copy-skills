Here is the finished screen. I renamed the placeholder toggles to the three update types you described, and added the labels, validation, focus and busy states the screen was missing.

**index.html**

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Settings</title>
  <link rel="stylesheet" href="settings.css">
</head>
<body>
  <main class="settings">
    <h1 class="settings-title">Settings</h1>

    <form class="settings-form" id="settings-form" novalidate>

      <fieldset class="settings-group">
        <legend>Daily updates</legend>

        <label class="setting-row">
          <span class="setting-label">Photo updates</span>
          <input type="checkbox" role="switch" class="switch" name="photo_updates" checked>
        </label>

        <label class="setting-row">
          <span class="setting-label">Pickup reminders</span>
          <input type="checkbox" role="switch" class="switch" name="pickup_reminders" checked>
        </label>

        <label class="setting-row">
          <span class="setting-label">Incident notes</span>
          <input type="checkbox" role="switch" class="switch" name="incident_notes" checked>
        </label>
      </fieldset>

      <fieldset class="settings-group">
        <legend>Features</legend>

        <label class="setting-row">
          <span class="setting-label">Enable feature</span>
          <input type="checkbox" role="switch" class="switch" name="enable_feature">
        </label>
      </fieldset>

      <div class="field">
        <label class="field-label" for="value">Value</label>
        <input
          class="field-input"
          id="value"
          name="value"
          type="text"
          placeholder="Enter value"
          aria-describedby="value-error"
          autocomplete="off"
        >
        <p class="field-error" id="value-error" hidden>Invalid input</p>
      </div>

      <div class="field">
        <label class="field-label" for="choice">Choice</label>
        <select class="field-input" id="choice" name="choice">
          <option value="" disabled selected>Select...</option>
          <option value="a">Choice A</option>
          <option value="b">Choice B</option>
        </select>
      </div>

      <div class="form-actions">
        <button type="submit" class="btn-primary" id="save-button">Save</button>
        <p class="save-status" id="save-status" role="status"></p>
      </div>

    </form>
  </main>

  <script>
    const form = document.getElementById('settings-form');
    const value = document.getElementById('value');
    const error = document.getElementById('value-error');
    const saveButton = document.getElementById('save-button');
    const status = document.getElementById('save-status');

    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      if (value.value.trim() === '') {
        value.setAttribute('aria-invalid', 'true');
        error.hidden = false;
        value.focus();
        return;
      }

      value.removeAttribute('aria-invalid');
      error.hidden = true;

      saveButton.disabled = true;
      saveButton.textContent = 'Saving…';
      status.textContent = '';

      try {
        // Replace with the real request, e.g. await fetch(...)
        await new Promise((resolve) => setTimeout(resolve, 600));
        status.textContent = 'Settings saved.';
      } catch (err) {
        status.textContent = 'Could not save. Your changes are still here. Try again.';
      } finally {
        saveButton.disabled = false;
        saveButton.textContent = 'Save';
      }
    });

    value.addEventListener('input', () => {
      if (value.value.trim() !== '') {
        value.removeAttribute('aria-invalid');
        error.hidden = true;
      }
    });
  </script>
</body>
</html>
```

**settings.css**

```css
:root {
  --color-text: #1d1d1f;
  --color-muted: #5b5f66;
  --color-border: #7a7f88;
  --color-surface: #ffffff;
  --color-primary: #1f5f4a;
  --color-primary-text: #ffffff;
  --color-error: #b42318;
  --color-focus: #1f5f4a;
  --color-track-off: #6b7079;

  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;

  --radius: 8px;
  --font-size-body: 1rem;
  --font-size-small: 0.875rem;
  --font-size-title: 1.5rem;
  --min-target: 44px;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: var(--font-size-body);
  line-height: 1.5;
  color: var(--color-text);
  background: var(--color-surface);
}

.settings {
  max-width: 32rem;
  margin: 0 auto;
  padding: var(--space-6) var(--space-4);
}

.settings-title {
  font-size: var(--font-size-title);
  font-weight: 600;
  margin: 0 0 var(--space-6);
}

.settings-form {
  display: grid;
  gap: var(--space-6);
}

/* Groups */
.settings-group {
  margin: 0;
  padding: 0;
  border: 0;
  display: grid;
  gap: var(--space-2);
}

.settings-group legend {
  padding: 0;
  margin-bottom: var(--space-2);
  font-size: var(--font-size-small);
  font-weight: 600;
  color: var(--color-muted);
}

/* Toggle rows: the whole row is the click target */
.setting-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  min-height: var(--min-target);
  padding: var(--space-2) 0;
  cursor: pointer;
}

.setting-label {
  overflow-wrap: anywhere;
}

/* Switch */
.switch {
  appearance: none;
  flex: 0 0 auto;
  position: relative;
  width: 48px;
  height: 28px;
  margin: 0;
  border-radius: 999px;
  background: var(--color-track-off);
  cursor: pointer;
  transition: background-color 150ms ease;
}

.switch::before {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--color-surface);
  transition: transform 150ms ease;
}

.switch:checked {
  background: var(--color-primary);
}

.switch:checked::before {
  transform: translateX(20px);
}

.switch:focus-visible,
.field-input:focus-visible,
.btn-primary:focus-visible {
  outline: 3px solid var(--color-focus);
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .switch {
    appearance: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .switch,
  .switch::before {
    transition: none;
  }
}

/* Fields */
.field {
  display: grid;
  gap: var(--space-2);
}

.field-label {
  font-weight: 600;
}

.field-input {
  width: 100%;
  min-height: var(--min-target);
  padding: var(--space-2) var(--space-3);
  font: inherit;
  color: var(--color-text);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
}

.field-input::placeholder {
  color: var(--color-muted);
}

.field-input[aria-invalid="true"] {
  border: 2px solid var(--color-error);
  padding: calc(var(--space-2) - 1px) calc(var(--space-3) - 1px);
}

.field-error {
  margin: 0;
  font-size: var(--font-size-small);
  font-weight: 600;
  color: var(--color-error);
  overflow-wrap: anywhere;
}

.field-error[hidden] {
  display: none;
}

/* Actions */
.form-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-3) var(--space-4);
}

.btn-primary {
  min-height: var(--min-target);
  padding: var(--space-2) var(--space-6);
  font: inherit;
  font-weight: 600;
  color: var(--color-primary-text);
  background: var(--color-primary);
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
}

.btn-primary:disabled {
  cursor: progress;
  opacity: 0.7;
}

.save-status {
  margin: 0;
  font-size: var(--font-size-small);
  color: var(--color-muted);
}

/* Narrow screens */
@media (max-width: 22rem) {
  .btn-primary {
    width: 100%;
  }
}
```

**What changed**

- Toggles are now labeled with the update types you named (photo updates, pickup reminders, incident notes). "Enable feature" stays as it was.
- Toggles use `role="switch"` and sit inside their labels, so the whole row is the click target and the name is announced.
- The text field has a visible label, since the placeholder alone is not a label. The error is hidden until the field is submitted empty, then it gets `aria-invalid`, `aria-describedby`, and focus.
- Save shows a busy state, blocks double-submit, and announces the result in a live region. A failed save should keep what the person typed (the script already does this).
- Focus rings are visible on every control, and nothing uses `outline: none`.
- Layout works at 320px and at 200% text size, and the Save button goes full width on very narrow screens.

**Needs your input**

- The "Value" field label, the "Choice" dropdown label and the "Daily updates" group heading are my placeholders. Tell me what those fields actually control and I'll replace them.
- "Invalid input" is shown as you specified. A message that names the problem and the fix would serve parents better once the field's rule is known.
- The save is simulated with a timer. Replace the marked line with your real request.

**Not checked**

- I did not test this with a screen reader, keyboard-only navigation, or a real device. Those checks are still needed before release.
