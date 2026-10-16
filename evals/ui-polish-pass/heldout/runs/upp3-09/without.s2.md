Here's a cleaned-up version. It has the same behavior, plus an accessible switch and basic save feedback.

```html
<div class="setting">
  <span id="delay-label">Email me when a ferry is delayed</span>
  <button type="button" class="switch" id="delay-switch"
          role="switch" aria-checked="false" aria-labelledby="delay-label"></button>
</div>

<div class="actions">
  <button type="button" id="save" class="save">Save</button>
  <span id="status" role="status" aria-live="polite"></span>
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
  }

  .switch {
    flex: none;
    position: relative;
    width: 40px;
    height: 22px;
    padding: 0;
    border: 0;
    border-radius: 11px;
    background: #ccc;
    cursor: pointer;
    transition: background .15s;
  }
  .switch::after {
    content: "";
    position: absolute;
    top: 2px;
    left: 2px;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #fff;
    transition: transform .15s;
  }
  .switch[aria-checked="true"] { background: #2a7; }
  .switch[aria-checked="true"]::after { transform: translateX(18px); }
  .switch:focus-visible,
  .save:focus-visible { outline: 2px solid #05c; outline-offset: 2px; }

  .actions {
    display: flex;
    align-items: center;
    gap: 12px;
    font: 14px system-ui, sans-serif;
  }
  .save {
    padding: 8px 18px;
    border: 0;
    border-radius: 6px;
    background: #2a7;
    color: #fff;
    font: inherit;
    cursor: pointer;
  }
  .save:disabled { opacity: .6; cursor: default; }

  @media (prefers-reduced-motion: reduce) {
    .switch, .switch::after { transition: none; }
  }
</style>

<script>
  const delaySwitch = document.getElementById('delay-switch');
  const saveBtn = document.getElementById('save');
  const status = document.getElementById('status');

  delaySwitch.addEventListener('click', () => {
    const on = delaySwitch.getAttribute('aria-checked') === 'true';
    delaySwitch.setAttribute('aria-checked', String(!on));
  });

  saveBtn.addEventListener('click', async () => {
    saveBtn.disabled = true;
    status.textContent = 'Saving…';
    try {
      const res = await fetch('/api/prefs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ delay: delaySwitch.getAttribute('aria-checked') === 'true' }),
      });
      if (!res.ok) throw new Error(res.status);
      status.textContent = 'Saved';
    } catch {
      status.textContent = 'Couldn’t save. Please try again.';
    } finally {
      saveBtn.disabled = false;
    }
  });
</script>
```

**What changed**
- **Switch:** it's now a real `<button role="switch">` with `aria-checked`. It works with the keyboard (Tab, Space, Enter) and screen readers, and the label is tied to it. The `.on` class is gone, because `aria-checked` drives both the state and the styling.
- **Styling:** the knob slides with a short transition (disabled for reduced-motion users), there's a visible focus ring, and items are vertically centered with a gap. The Save button is styled to match.
- **Save feedback (new):** the button disables while saving, and a status message shows "Saving…", "Saved" or an error. Before, a failed save was silent.
- **Request:** it now sends a `Content-Type: application/json` header. Your original sent the JSON without one, so it went out as `text/plain`. If your server only parses JSON when that header is present, this fixes a latent bug. If it was reading the raw body, it's still fine.

The page still doesn't load the saved preference when it opens, so the switch always starts off. If `/api/prefs` has a GET, I can wire that up.
