Here's a cleaned-up version. The markup and API call are unchanged: it still POSTs `{delay: true|false}` to `/api/prefs`.

```html
<div class="setting">
  <label for="delay-switch">Email me when a ferry is delayed</label>
  <button type="button" id="delay-switch" class="switch" role="switch" aria-checked="false"></button>
</div>
<div class="actions">
  <button type="button" id="save">Save</button>
  <span id="save-status" role="status" aria-live="polite"></span>
</div>

<style>
.setting {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  width: 320px;
  padding: 12px 0;
  font: 15px/1.4 system-ui, sans-serif;
  color: #222;
}

.switch {
  flex: none;
  position: relative;
  width: 44px;
  height: 24px;
  padding: 0;
  border: 0;
  border-radius: 12px;
  background: #ccc;
  cursor: pointer;
  transition: background 0.2s;
}
.switch::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  transition: transform 0.2s;
}
.switch[aria-checked="true"] {
  background: #2a7;
}
.switch[aria-checked="true"]::after {
  transform: translateX(20px);
}

.actions {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 8px;
  font: 15px/1.4 system-ui, sans-serif;
}
#save {
  padding: 8px 18px;
  border: 0;
  border-radius: 6px;
  background: #2a7;
  color: #fff;
  font: inherit;
  cursor: pointer;
}
#save:disabled {
  opacity: 0.6;
  cursor: wait;
}
.switch:focus-visible,
#save:focus-visible {
  outline: 2px solid #2a7;
  outline-offset: 2px;
}
#save-status {
  font-size: 14px;
  color: #555;
}
</style>

<script>
const delaySwitch = document.getElementById('delay-switch');
const saveButton = document.getElementById('save');
const saveStatus = document.getElementById('save-status');

delaySwitch.addEventListener('click', () => {
  const on = delaySwitch.getAttribute('aria-checked') !== 'true';
  delaySwitch.setAttribute('aria-checked', String(on));
  saveStatus.textContent = '';
});

saveButton.addEventListener('click', async () => {
  saveButton.disabled = true;
  saveStatus.textContent = 'Saving…';
  try {
    const res = await fetch('/api/prefs', {
      method: 'POST',
      body: JSON.stringify({ delay: delaySwitch.getAttribute('aria-checked') === 'true' })
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    saveStatus.textContent = 'Saved';
  } catch (err) {
    saveStatus.textContent = "Couldn't save. Try again.";
  } finally {
    saveButton.disabled = false;
  }
});
</script>
```

What changed:

- **Switch is a real button** with `role="switch"` and `aria-checked`, so screen readers announce its state and it's keyboard-focusable. The `<label for>` makes clicking the text toggle it too.
- **Layout:** vertically centered row, a bit more padding, a gap between label and switch, and a readable font stack.
- **Motion:** the thumb and track animate instead of snapping.
- **Save feedback:** the button disables while saving, and shows "Saved" or an error. The original gave no feedback at all.
- **Error handling:** the original ignored failed responses. Now a non-2xx status shows an error message.
- **Focus styles** for keyboard users, and the Save button is styled to match the switch's green.

I haven't run this in a browser, so check the spacing and the thumb position against your design.
