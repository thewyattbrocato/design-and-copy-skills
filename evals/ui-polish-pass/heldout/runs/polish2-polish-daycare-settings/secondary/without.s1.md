Here's the finished screen as two files, `index.html` and `styles.css`. I built it from the element list you gave, so the labels are your placeholder text for now.

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Settings</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main class="settings">
    <h1 class="settings__heading">Settings</h1>

    <form class="settings__form" action="#" method="post" novalidate>

      <div class="setting-row">
        <label class="setting-row__label" for="option-1">Option 1</label>
        <label class="switch">
          <input class="switch__input" type="checkbox" id="option-1" name="option_1" role="switch">
          <span class="switch__track" aria-hidden="true"><span class="switch__thumb"></span></span>
        </label>
      </div>

      <div class="setting-row">
        <label class="setting-row__label" for="option-2">Option 2</label>
        <label class="switch">
          <input class="switch__input" type="checkbox" id="option-2" name="option_2" role="switch">
          <span class="switch__track" aria-hidden="true"><span class="switch__thumb"></span></span>
        </label>
      </div>

      <div class="setting-row">
        <label class="setting-row__label" for="enable-feature">Enable feature</label>
        <label class="switch">
          <input class="switch__input" type="checkbox" id="enable-feature" name="enable_feature" role="switch">
          <span class="switch__track" aria-hidden="true"><span class="switch__thumb"></span></span>
        </label>
      </div>

      <div class="field" data-field>
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
        <p class="field__error" id="value-error" role="alert" hidden>Invalid input</p>
      </div>

      <div class="field">
        <label class="field__label" for="choice">Choice</label>
        <div class="select">
          <select class="select__control" id="choice" name="choice">
            <option value="" selected disabled>Select...</option>
            <option value="a">Choice A</option>
            <option value="b">Choice B</option>
          </select>
        </div>
      </div>

      <div class="settings__actions">
        <button class="button" type="submit">Save</button>
      </div>

    </form>
  </main>
</body>
</html>
```

**styles.css**

```css
:root {
  --color-bg: #f5f6f8;
  --color-surface: #ffffff;
  --color-text: #1d2330;
  --color-muted: #5b6372;
  --color-border: #d3d8e0;
  --color-primary: #2563eb;
  --color-primary-hover: #1d4fd1;
  --color-track-off: #b8bfcb;
  --color-error: #c62828;
  --color-focus: #2563eb;
  --radius: 10px;
  --font: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-height: 100vh;
  background: var(--color-bg);
  color: var(--color-text);
  font-family: var(--font);
  font-size: 16px;
  line-height: 1.5;
}

.settings {
  max-width: 480px;
  margin: 0 auto;
  padding: 32px 20px;
}

.settings__heading {
  margin: 0 0 24px;
  font-size: 28px;
  font-weight: 700;
}

.settings__form {
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 20px;
}

/* Toggle rows */
.setting-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
}

.setting-row__label,
.field__label {
  font-weight: 500;
}

/* Switch */
.switch {
  position: relative;
  display: inline-flex;
  flex-shrink: 0;
  cursor: pointer;
}

.switch__input {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.switch__track {
  position: relative;
  width: 48px;
  height: 28px;
  border-radius: 999px;
  background: var(--color-track-off);
  transition: background-color 0.2s ease;
}

.switch__thumb {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
  transition: transform 0.2s ease;
}

.switch__input:checked + .switch__track {
  background: var(--color-primary);
}

.switch__input:checked + .switch__track .switch__thumb {
  transform: translateX(20px);
}

.switch__input:focus-visible + .switch__track {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}

/* Text field and select */
.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-top: 8px;
}

.field__input,
.select__control {
  width: 100%;
  min-height: 44px;
  padding: 10px 12px;
  border: 1px solid var(--color-border);
  border-radius: 8px;
  background: var(--color-surface);
  color: var(--color-text);
  font: inherit;
}

.field__input::placeholder {
  color: var(--color-muted);
}

.field__input:focus-visible,
.select__control:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 1px;
  border-color: transparent;
}

.field__input[aria-invalid="true"] {
  border-color: var(--color-error);
}

.field__error {
  margin: 0;
  color: var(--color-error);
  font-size: 14px;
}

.field__error[hidden] {
  display: none;
}

.select {
  position: relative;
}

.select__control {
  appearance: none;
  padding-right: 40px;
  cursor: pointer;
}

.select::after {
  content: "";
  position: absolute;
  top: 50%;
  right: 16px;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--color-muted);
  border-bottom: 2px solid var(--color-muted);
  transform: translateY(-70%) rotate(45deg);
  pointer-events: none;
}

/* Save button */
.settings__actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 12px;
}

.button {
  min-height: 44px;
  padding: 10px 24px;
  border: none;
  border-radius: 8px;
  background: var(--color-primary);
  color: #ffffff;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.button:hover {
  background: var(--color-primary-hover);
}

.button:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .switch__track,
  .switch__thumb,
  .button {
    transition: none;
  }
}
```

**Notes**

- **Error state:** The "Invalid input" message is hidden by default. To show it, set `hidden` to false on `#value-error` and set `aria-invalid="true"` on `#value`. The `role="alert"` makes screen readers announce it when it appears. I didn't write that script because you asked only for HTML and CSS.
- **Labels:** I used your exact strings. "Option 1," "Option 2," and "Value" are placeholders. You'll likely want to replace them with the real copy, such as "Photo updates," "Pickup reminders," and "Incident notes." The "Choice" field label is also my addition, since the spec had no label for the dropdown.
- **Accessibility:** The toggles are real checkboxes with `role="switch"`, so keyboard and screen reader users get the right behavior. Every control has a visible label and a 44px minimum touch target.
- **Not included:** I didn't add a save handler or a validation rule for the text field, since the spec doesn't define one.
