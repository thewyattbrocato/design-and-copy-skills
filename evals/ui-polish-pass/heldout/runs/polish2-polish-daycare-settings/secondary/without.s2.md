Here's the finished screen as a single HTML file with its CSS in a separate stylesheet. I kept your strings exactly as written, so the placeholder labels ("Option 1", "Choice A") will need real copy before shipping. See the notes at the end.

**`settings.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Settings</title>
  <link rel="stylesheet" href="settings.css">
</head>
<body>
  <main class="screen">
    <h1 class="screen__title">Settings</h1>

    <form class="settings" novalidate>
      <ul class="settings__list">
        <li>
          <label class="row">
            <span class="row__label">Option 1</span>
            <input class="switch" type="checkbox" role="switch" name="option1">
          </label>
        </li>
        <li>
          <label class="row">
            <span class="row__label">Option 2</span>
            <input class="switch" type="checkbox" role="switch" name="option2">
          </label>
        </li>
        <li>
          <label class="row">
            <span class="row__label">Enable feature</span>
            <input class="switch" type="checkbox" role="switch" name="enableFeature">
          </label>
        </li>
      </ul>

      <div class="field" id="value-field">
        <label class="field__label" for="value">Value</label>
        <input
          class="field__input"
          type="text"
          id="value"
          name="value"
          placeholder="Enter value"
          aria-describedby="value-error"
          aria-invalid="false"
        >
        <p class="field__error" id="value-error" aria-live="polite">Invalid input</p>
      </div>

      <div class="field">
        <label class="field__label" for="choice">Choice</label>
        <div class="select">
          <select class="field__input" id="choice" name="choice">
            <option value="" disabled selected>Select...</option>
            <option value="a">Choice A</option>
            <option value="b">Choice B</option>
          </select>
        </div>
      </div>

      <button class="button" type="submit">Save</button>
    </form>
  </main>
</body>
</html>
```

**`settings.css`**

```css
:root {
  --bg: #f7f7f5;
  --surface: #ffffff;
  --text: #1d1d1b;
  --text-muted: #5f6368;
  --border: #d4d4d0;
  --accent: #2b6cb0;
  --accent-hover: #245a92;
  --track-off: #9aa0a6;
  --error: #b42318;
  --focus: #1a73e8;
  --radius: 12px;
  --font: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: var(--font);
  font-size: 16px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

.screen {
  max-width: 480px;
  margin: 0 auto;
  padding: 24px 16px 40px;
}

.screen__title {
  margin: 0 0 16px;
  font-size: 28px;
  font-weight: 700;
  line-height: 1.2;
}

/* Settings list */

.settings {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.settings__list {
  list-style: none;
  margin: 0;
  padding: 0;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
}

.settings__list li + li {
  border-top: 1px solid var(--border);
}

/* Toggle rows: the whole row is the click target */

.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 56px;
  padding: 12px 16px;
  cursor: pointer;
}

.row__label {
  font-size: 16px;
}

.switch {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  flex: 0 0 auto;
  width: 48px;
  height: 28px;
  margin: 0;
  border-radius: 999px;
  background: var(--track-off);
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.switch::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  transition: transform 0.2s ease;
}

.switch:checked {
  background: var(--accent);
}

.switch:checked::after {
  transform: translateX(20px);
}

.switch:focus-visible,
.field__input:focus-visible,
.button:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

/* Fields */

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field__label {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-muted);
}

.field__input {
  width: 100%;
  min-height: 48px;
  padding: 12px 14px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface);
  color: var(--text);
  font: inherit;
}

.field__input::placeholder {
  color: var(--text-muted);
}

.field__input[aria-invalid="true"],
.field--error .field__input {
  border-color: var(--error);
}

.select {
  position: relative;
}

.select::after {
  content: "";
  position: absolute;
  right: 16px;
  top: 50%;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--text-muted);
  border-bottom: 2px solid var(--text-muted);
  transform: translateY(-70%) rotate(45deg);
  pointer-events: none;
}

select.field__input {
  appearance: none;
  -webkit-appearance: none;
  padding-right: 40px;
  cursor: pointer;
}

/* Error text: shown under the field when the field is in an error state */

.field__error {
  display: none;
  margin: 0;
  font-size: 14px;
  color: var(--error);
}

.field--error .field__error {
  display: block;
}

/* Save button */

.button {
  align-self: stretch;
  min-height: 48px;
  padding: 12px 24px;
  border: 0;
  border-radius: 999px;
  background: var(--accent);
  color: #ffffff;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.button:hover {
  background: var(--accent-hover);
}

/* Respect reduced-motion preferences */

@media (prefers-reduced-motion: reduce) {
  .switch,
  .switch::after,
  .button {
    transition: none;
  }
}

/* Dark mode */

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #161617;
    --surface: #222224;
    --text: #f1f1ef;
    --text-muted: #a8acb2;
    --border: #3a3a3d;
    --accent: #6ea8fe;
    --accent-hover: #8bb9ff;
    --track-off: #5f6368;
    --error: #ff8a80;
    --focus: #8ab4f8;
  }

  .button {
    color: #0b0b0c;
  }
}
```

**How the error state works:** the "Invalid input" text is hidden by default. To show it, add the `field--error` class to the `#value-field` wrapper and set `aria-invalid="true"` on the input. Both changes are needed: the class shows the message and turns the border red, and `aria-invalid` tells screen readers the field is in error.

**Decisions to review before shipping:**

- **Labels are placeholders.** I kept "Option 1", "Option 2", "Enable feature", "Choice A/B" as given. Since the screen is for photo updates, pickup reminders and incident notes, you'll probably want labels like "Photo updates", "Pickup reminders" and "Incident notes". Tell me the final copy and I'll swap it in.
- **Visible labels I added.** "Value" above the text field and "Choice" above the dropdown. The placeholder alone isn't a label, so screen readers would otherwise have nothing to announce. Rename these too if you have better wording.
- **No JavaScript.** I didn't wire up validation or saving. The Save button is a plain submit button, and nothing in the page decides when to show the error.
- **Not tested in a browser.** I checked the markup and CSS by reading them, not by rendering the page, so do a quick visual pass on a phone-width screen and in dark mode.
