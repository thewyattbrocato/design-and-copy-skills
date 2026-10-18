Here's the finished screen. I replaced the placeholder labels and options with real ones for parents, and kept the same set of controls.

**Labels I chose (change any of these):**
- "Option 1" → **Photo updates**, with a frequency dropdown
- "Option 2" → **Pickup reminders**, with a minutes-before-pickup field
- "Enable feature" → **Incident notes**
- Dropdown choices → **As they happen** / **Daily summary**
- "Invalid input" is unchanged. It only appears when the field has `is-invalid` set, so you can wire that to your validation.

## HTML

```html
<main class="settings">
  <h1 class="settings__title">Settings</h1>
  <p class="settings__intro">Choose how you hear about your dog's day.</p>

  <form class="settings__form" novalidate>

    <section class="card">
      <div class="row">
        <div class="row__text">
          <span class="row__title" id="photo-label">Photo updates</span>
          <p class="row__help" id="photo-help">Get photos of your dog during the day.</p>
        </div>
        <label class="switch">
          <input type="checkbox" role="switch" checked
                 aria-labelledby="photo-label" aria-describedby="photo-help">
          <span class="switch__track" aria-hidden="true"></span>
        </label>
      </div>

      <div class="field">
        <label class="field__label" for="photo-frequency">How often</label>
        <select class="field__control" id="photo-frequency">
          <option value="" disabled selected>Select...</option>
          <option value="as-they-happen">As they happen</option>
          <option value="daily-summary">Daily summary</option>
        </select>
      </div>
    </section>

    <section class="card">
      <div class="row">
        <div class="row__text">
          <span class="row__title" id="pickup-label">Pickup reminders</span>
          <p class="row__help" id="pickup-help">Get a reminder before pickup time.</p>
        </div>
        <label class="switch">
          <input type="checkbox" role="switch"
                 aria-labelledby="pickup-label" aria-describedby="pickup-help">
          <span class="switch__track" aria-hidden="true"></span>
        </label>
      </div>

      <div class="field" id="pickup-field">
        <label class="field__label" for="pickup-minutes">Minutes before pickup</label>
        <input class="field__control" id="pickup-minutes" type="text" inputmode="numeric"
               placeholder="Enter value" aria-describedby="pickup-error">
        <p class="field__error" id="pickup-error">Invalid input</p>
      </div>
    </section>

    <section class="card">
      <div class="row">
        <div class="row__text">
          <span class="row__title" id="incident-label">Incident notes</span>
          <p class="row__help" id="incident-help">Get notified when an incident note is added.</p>
        </div>
        <label class="switch">
          <input type="checkbox" role="switch"
                 aria-labelledby="incident-label" aria-describedby="incident-help">
          <span class="switch__track" aria-hidden="true"></span>
        </label>
      </div>
    </section>

    <div class="settings__actions">
      <button class="button" type="submit">Save</button>
    </div>
  </form>
</main>
```

## CSS

```css
:root {
  --bg: #f5f6f8;
  --surface: #ffffff;
  --text: #1c2233;
  --muted: #5b6275;
  --border: #d9dde6;
  --accent: #2563eb;
  --accent-text: #ffffff;
  --track-off: #c4cad6;
  --error: #b42318;
  --focus: #1d4ed8;
  --radius: 14px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  color: var(--text);
  background: var(--bg);
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
}

.settings {
  max-width: 560px;
  margin: 0 auto;
  padding: 32px 16px 48px;
}

.settings__title {
  margin: 0 0 4px;
  font-size: 28px;
  font-weight: 700;
}

.settings__intro {
  margin: 0 0 24px;
  color: var(--muted);
  font-size: 15px;
}

.settings__form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px 20px;
}

/* Toggle rows */
.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.row__title {
  font-size: 16px;
  font-weight: 600;
}

.row__help {
  margin: 4px 0 0;
  color: var(--muted);
  font-size: 14px;
}

/* Switch: visually hidden checkbox drives the track */
.switch {
  position: relative;
  flex-shrink: 0;
  width: 48px;
  height: 28px;
  cursor: pointer;
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

.switch__track {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: var(--track-off);
  transition: background-color 0.2s ease;
  pointer-events: none;
}

.switch__track::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 1px 2px rgb(0 0 0 / 0.2);
  transition: transform 0.2s ease;
}

.switch input:checked + .switch__track {
  background: var(--accent);
}

.switch input:checked + .switch__track::after {
  transform: translateX(20px);
}

.switch input:focus-visible + .switch__track {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .switch__track,
  .switch__track::after {
    transition: none;
  }
}

/* Fields */
.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid var(--border);
}

.field__label {
  font-size: 14px;
  font-weight: 600;
}

.field__control {
  width: 100%;
  min-height: 44px;
  padding: 10px 12px;
  font: inherit;
  color: var(--text);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
}

.field__control:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 1px;
  border-color: var(--focus);
}

.field.is-invalid .field__control {
  border-color: var(--error);
}

.field__error {
  display: none;
  margin: 0;
  color: var(--error);
  font-size: 13px;
}

.field.is-invalid .field__error {
  display: block;
}

/* Save */
.settings__actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 8px;
}

.button {
  min-width: 120px;
  min-height: 44px;
  padding: 10px 20px;
  font: inherit;
  font-weight: 600;
  color: var(--accent-text);
  background: var(--accent);
  border: 0;
  border-radius: 10px;
  cursor: pointer;
}

.button:hover {
  filter: brightness(1.08);
}

.button:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

@media (max-width: 420px) {
  .settings__actions .button {
    width: 100%;
  }
}
```

## Notes

- **Toggles** are real checkboxes with `role="switch"`, so screen readers announce them as on/off switches and the whole row is labeled.
- **Error state:** add `is-invalid` to the `.field` wrapper and set `aria-invalid="true"` on the input to show "Invalid input." The error is linked to the input through `aria-describedby`.
- **Touch targets** are at least 44px, which matters for parents using phones.
- I did not run this in a browser. I checked it by reading the code.
