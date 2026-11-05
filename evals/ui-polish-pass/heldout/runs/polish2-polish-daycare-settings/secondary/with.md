Here's the finished screen. It's split into `index.html` and `settings.css`, with a few lines of script for validation and the save state.

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
  <a class="skip-link" href="#settings-form">Skip to settings</a>

  <main class="page">
    <h1>Settings</h1>

    <form id="settings-form" novalidate>

      <fieldset class="group">
        <legend>How you hear about your dog's day</legend>

        <div class="row">
          <div class="row-text">
            <span class="row-label" id="photo-label">Photo updates</span>
            <span class="row-hint" id="photo-hint">Pictures of your dog during the day</span>
          </div>
          <label class="switch">
            <input type="checkbox" role="switch" name="photo_updates"
                   aria-labelledby="photo-label" aria-describedby="photo-hint">
            <span class="track" aria-hidden="true"></span>
          </label>
        </div>

        <div class="row">
          <div class="row-text">
            <span class="row-label" id="pickup-label">Pickup reminders</span>
            <span class="row-hint" id="pickup-hint">A heads-up before pickup time</span>
          </div>
          <label class="switch">
            <input type="checkbox" role="switch" name="pickup_reminders"
                   aria-labelledby="pickup-label" aria-describedby="pickup-hint">
            <span class="track" aria-hidden="true"></span>
          </label>
        </div>

        <div class="row">
          <div class="row-text">
            <span class="row-label" id="incident-label">Incident notes</span>
            <span class="row-hint" id="incident-hint">Notes about any incident involving your dog</span>
          </div>
          <label class="switch">
            <input type="checkbox" role="switch" name="incident_notes"
                   aria-labelledby="incident-label" aria-describedby="incident-hint">
            <span class="track" aria-hidden="true"></span>
          </label>
        </div>
      </fieldset>

      <div class="field">
        <label for="delivery">Send updates by</label>
        <div class="select-wrap">
          <select id="delivery" name="delivery" required>
            <option value="">Select...</option>
            <option value="a">Choice A</option>
            <option value="b">Choice B</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label for="value">Value</label>
        <input id="value" name="value" type="text" placeholder="Enter value"
               autocomplete="off" aria-describedby="value-error">
        <p id="value-error" class="field-error" hidden>Invalid input</p>
      </div>

      <div class="actions">
        <button type="submit" class="btn-primary" id="save-btn">Save</button>
        <p id="status" class="status" role="status" aria-live="polite"></p>
      </div>
    </form>
  </main>

  <script>
    const form = document.getElementById('settings-form');
    const value = document.getElementById('value');
    const error = document.getElementById('value-error');
    const saveBtn = document.getElementById('save-btn');
    const status = document.getElementById('status');

    // Placeholder rule: the field must not be empty. Replace with the real rule.
    function validate() {
      const ok = value.value.trim() !== '';
      value.setAttribute('aria-invalid', String(!ok));
      error.hidden = ok;
      return ok;
    }

    value.addEventListener('input', () => { if (error.hidden === false) validate(); });

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      status.textContent = '';
      if (!validate()) { value.focus(); return; }

      saveBtn.disabled = true;
      saveBtn.textContent = 'Saving…';
      try {
        // Replace with the real save request. It should reject on failure.
        await new Promise((resolve) => setTimeout(resolve, 600));
        status.textContent = 'Settings saved.';
      } catch {
        status.textContent = "Couldn't save. Your changes are still here. Try again.";
      } finally {
        saveBtn.disabled = false;
        saveBtn.textContent = 'Save';
      }
    });
  </script>
</body>
</html>
```

**settings.css**

```css
:root {
  --bg: #f6f7f9;
  --surface: #ffffff;
  --text: #1d2330;
  --muted: #5b6373;
  --border: #b8bfcc;
  --accent: #1f6feb;
  --accent-text: #ffffff;
  --error: #b42318;
  --focus: #1f6feb;
  --track-off: #7a8290;
  --track-on: #1f6feb;
  --thumb: #ffffff;
  --radius: 10px;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #15171c;
    --surface: #1e2127;
    --text: #f2f4f8;
    --muted: #b3bac6;
    --border: #6b7382;
    --accent: #6aa7ff;
    --accent-text: #0b1220;
    --error: #ff9a8f;
    --focus: #8ab8ff;
    --track-off: #6b7382;
    --track-on: #6aa7ff;
    --thumb: #0b1220;
  }
}

*, *::before, *::after { box-sizing: border-box; }

html { -webkit-text-size-adjust: 100%; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 16px/1.5 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}

/* Keyboard focus, never removed */
:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.skip-link {
  position: absolute;
  left: 1rem;
  top: -4rem;
  padding: 0.5rem 1rem;
  background: var(--surface);
  color: var(--text);
  border-radius: 6px;
  z-index: 10;
}
.skip-link:focus { top: 1rem; }

.page {
  max-width: 36rem;
  margin: 0 auto;
  padding: 2rem 1rem 3rem;
}

h1 {
  font-size: 1.75rem;
  line-height: 1.2;
  margin: 0 0 1.5rem;
}

/* Groups */
.group {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--surface);
  padding: 0 1rem;
  margin: 0 0 1.5rem;
  min-width: 0;
}

.group legend {
  font-weight: 600;
  padding: 1rem 0 0.25rem;
  color: var(--muted);
  font-size: 0.9rem;
}

/* Toggle rows */
.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  min-height: 3.5rem;
  padding: 0.75rem 0;
  border-top: 1px solid var(--border);
}
.row:first-of-type { border-top: 0; }

.row-text { display: flex; flex-direction: column; min-width: 0; }
.row-label { font-weight: 600; overflow-wrap: anywhere; }
.row-hint { color: var(--muted); font-size: 0.9rem; overflow-wrap: anywhere; }

/* Switch: real checkbox for keyboard and screen readers */
.switch {
  position: relative;
  flex: 0 0 auto;
  width: 3rem;
  height: 3rem;          /* 48px touch target */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.switch input {
  position: absolute;
  inset: 0;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.track {
  position: relative;
  width: 2.75rem;
  height: 1.5rem;
  border-radius: 999px;
  background: var(--track-off);
  transition: background-color 150ms ease;
  pointer-events: none;
}

.track::after {
  content: "";
  position: absolute;
  top: 0.1875rem;
  left: 0.1875rem;
  width: 1.125rem;
  height: 1.125rem;
  border-radius: 50%;
  background: var(--thumb);
  transition: transform 150ms ease;
}

.switch input:checked + .track { background: var(--track-on); }
.switch input:checked + .track::after { transform: translateX(1.25rem); }

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

.field label { font-weight: 600; }

.field input,
.field select {
  width: 100%;
  min-height: 2.75rem;
  padding: 0.5rem 0.75rem;
  font: inherit;
  color: var(--text);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  appearance: none;
}

.select-wrap { position: relative; }
.select-wrap::after {
  content: "";
  position: absolute;
  right: 0.9rem;
  top: 50%;
  width: 0.5rem;
  height: 0.5rem;
  border-right: 2px solid var(--muted);
  border-bottom: 2px solid var(--muted);
  transform: translateY(-75%) rotate(45deg);
  pointer-events: none;
}
.select-wrap select { padding-right: 2.25rem; }

.field input::placeholder { color: var(--muted); opacity: 1; }

.field input[aria-invalid="true"] {
  border: 2px solid var(--error);
}

.field-error {
  margin: 0;
  color: var(--error);
  font-size: 0.9rem;
  font-weight: 600;
}

/* Actions */
.actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1rem;
}

.btn-primary {
  min-height: 2.75rem;
  padding: 0.5rem 1.5rem;
  font: inherit;
  font-weight: 600;
  color: var(--accent-text);
  background: var(--accent);
  border: 0;
  border-radius: 8px;
  cursor: pointer;
}

.btn-primary:hover { filter: brightness(1.05); }
.btn-primary:disabled {
  opacity: 0.6;
  cursor: progress;
}

.status {
  margin: 0;
  color: var(--muted);
  font-size: 0.95rem;
}

@media (prefers-reduced-motion: reduce) {
  .track,
  .track::after { transition: none; }
}

/* Narrow screens and large text */
@media (max-width: 22rem) {
  .page { padding-inline: 0.75rem; }
  .group { padding: 0 0.75rem; }
  .btn-primary { width: 100%; }
}
```

**What changed and why**
- Replaced "Option 1/2" and "Enable feature" with the three categories you described: photo updates, pickup reminders, incident notes. The mapping is my guess, so check that "Enable feature" was meant to be the incident notes toggle.
- Each toggle is a real checkbox with a visible label and hint. Focus rings are kept, and the touch targets are 48px.
- The text field gets a visible label. It had only a placeholder before.
- "Invalid input" appears under the field with `aria-invalid` and `aria-describedby`. It is hidden until the form is submitted with an error, and it clears as you type.
- Save shows "Saving…" and disables itself to prevent double submits. The result is announced in words, and a failed save keeps the person's input.
- Dark theme follows the system setting (`prefers-color-scheme`), since you asked for one. Reduced motion is respected.
- The layout works down to 320px, and the skip link is included.

**Decisions you need to make**
- The dropdown choices stay as "Choice A" and "Choice B", and its label "Send updates by" is my guess. Real options and a label are needed before shipping.
- The validation rule ("not empty") is a placeholder. Replace it with the real rule, and make "Invalid input" say what is wrong.
- The save call is a 600ms timer stub. Replace it with the real request.

**Not checked:** I have not run this in a browser, tested it with a screen reader, or checked contrast values with a tool.
