Here's a tidied version. It does the same thing, but the toggle is now a real button, so keyboard and screen-reader users can operate it.

```html
<div class="setting">
  <label id="delay-label" for="delay-switch">Email me when a ferry is delayed</label>
  <button type="button" id="delay-switch" class="switch" role="switch"
          aria-checked="false" aria-labelledby="delay-label"></button>
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
    font: 16px/1.4 system-ui, sans-serif;
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
    transition: background 0.15s;
  }
  .switch[aria-checked="true"] { background: #2a7; }
  .switch:focus-visible { outline: 2px solid #1a5f45; outline-offset: 2px; }

  .switch::after {
    content: "";
    position: absolute;
    top: 2px;
    left: 2px;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #fff;
    transition: transform 0.15s;
  }
  .switch[aria-checked="true"]::after { transform: translateX(18px); }

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
  .save:disabled { opacity: 0.6; cursor: default; }

  @media (prefers-reduced-motion: reduce) {
    .switch, .switch::after { transition: none; }
  }
</style>

<script>
  const toggle = document.getElementById('delay-switch');
  const saveBtn = document.getElementById('save');
  const status = document.getElementById('status');

  toggle.addEventListener('click', () => {
    const on = toggle.getAttribute('aria-checked') === 'true';
    toggle.setAttribute('aria-checked', String(!on));
  });

  saveBtn.addEventListener('click', async () => {
    saveBtn.disabled = true;
    status.textContent = 'Saving…';
    try {
      const res = await fetch('/api/prefs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ delay: toggle.getAttribute('aria-checked') === 'true' }),
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

What changed:
- **Accessibility:** the `div` toggle is now a `<button role="switch">` with `aria-checked`. It works with Tab, Space and Enter, and it has a visible focus ring and a proper label.
- **Styling:** the switch knob slides smoothly (and respects reduced-motion settings). The row is vertically centered. The Save button is styled to match.
- **Save feedback:** Save now shows "Saving…", "Saved" or an error message, and is disabled while the request is in flight. Before, it did nothing visible.
- **Request:** it sends a `Content-Type: application/json` header. Your original didn't, and some servers will reject or mis-parse the body without it.
- **Code:** it uses `addEventListener` instead of `onclick`, and the switch state lives in one place (`aria-checked`) instead of a CSS class.

I haven't run this against your `/api/prefs` endpoint. It also still starts in the "off" state, so if the saved preference can be "on", you'll want to set the initial `aria-checked` from the server.
