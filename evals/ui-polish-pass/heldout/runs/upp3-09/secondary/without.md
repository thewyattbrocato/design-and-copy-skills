Here's a cleaned-up version. The look is more polished, the toggle is keyboard and screen-reader accessible, and the save button gives feedback.

```html
<div class="setting">
  <label id="delay-label" for="delay-switch">Email me when a ferry is delayed</label>
  <button type="button" id="delay-switch" class="switch" role="switch"
          aria-checked="false" aria-labelledby="delay-label"></button>
</div>
<button type="button" id="save" class="save">Save</button>
<p id="status" class="status" role="status" aria-live="polite"></p>

<style>
.setting {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  width: 320px;
  padding: 12px 0;
  border-bottom: 1px solid #e5e5e5;
  font: 15px/1.4 system-ui, sans-serif;
  color: #222;
}
.switch {
  position: relative;
  flex: none;
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
.switch[aria-checked="true"] { background: #2a7; }
.switch[aria-checked="true"]::after { transform: translateX(20px); }

.save {
  margin-top: 12px;
  padding: 8px 18px;
  border: 0;
  border-radius: 6px;
  background: #2a7;
  color: #fff;
  font: 600 14px system-ui, sans-serif;
  cursor: pointer;
}
.save:disabled { opacity: 0.6; cursor: default; }
.switch:focus-visible,
.save:focus-visible { outline: 2px solid #2a7; outline-offset: 2px; }

.status { margin: 8px 0 0; font: 13px system-ui, sans-serif; color: #555; min-height: 1em; }
</style>

<script>
const toggle = document.getElementById('delay-switch');
const save = document.getElementById('save');
const status = document.getElementById('status');

toggle.addEventListener('click', () => {
  toggle.setAttribute('aria-checked', toggle.getAttribute('aria-checked') !== 'true');
});

save.addEventListener('click', async () => {
  save.disabled = true;
  status.textContent = 'Saving…';
  try {
    const res = await fetch('/api/prefs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ delay: toggle.getAttribute('aria-checked') === 'true' })
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    status.textContent = 'Saved';
  } catch (err) {
    status.textContent = "Couldn't save. Please try again.";
  } finally {
    save.disabled = false;
  }
});
</script>
```

What changed:

- **Layout and styling:** The row is vertically centered, has a divider, and uses a system font. The switch is a bit larger, with a soft knob shadow and a smooth slide and color transition. The Save button is styled to match.
- **Accessibility:** The label is tied to the switch, the switch uses `role="switch"` with `aria-checked`, and both controls are real `<button>`s, so they work with the keyboard and screen readers. There's a visible focus ring.
- **Feedback:** Save shows "Saving…", then "Saved" or an error message, and it's disabled while the request is in flight.
- **Request handling:** The fetch now checks the response status, so a failed save no longer fails silently. It also sends `Content-Type: application/json`. If your server only reads the raw body, that header is harmless, but check that the endpoint still parses the request correctly.

The switch state now lives in `aria-checked` instead of an `.on` class. If any other code reads `.sw.on`, it will need updating to `[aria-checked="true"]`.
