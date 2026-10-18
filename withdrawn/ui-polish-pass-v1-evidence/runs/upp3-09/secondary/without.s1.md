Here's a tidied version. The behavior is the same: the toggle flips, and Save posts the state to `/api/prefs`.

```html
<div class="setting">
  <label for="delay-alert">Email me when a ferry is delayed</label>
  <button type="button" role="switch" id="delay-alert" class="switch" aria-checked="false"></button>
</div>
<div class="actions">
  <button type="button" id="save" class="save">Save</button>
  <span id="msg" role="status"></span>
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
  color: #1a1a1a;
}
.switch {
  position: relative;
  flex: none;
  width: 44px;
  height: 24px;
  padding: 0;
  border: 0;
  border-radius: 12px;
  background: #c9ced6;
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
.switch:focus-visible,
.save:focus-visible {
  outline: 2px solid #2a7;
  outline-offset: 2px;
}
.actions {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 8px;
  font: 14px system-ui, sans-serif;
}
.save {
  padding: 8px 16px;
  border: 0;
  border-radius: 6px;
  background: #2a7;
  color: #fff;
  font: inherit;
  cursor: pointer;
}
.save:disabled { opacity: 0.6; cursor: default; }
#msg { color: #555; }
</style>

<script>
const toggle = document.getElementById('delay-alert');
const save = document.getElementById('save');
const msg = document.getElementById('msg');

toggle.addEventListener('click', () => {
  const on = toggle.getAttribute('aria-checked') !== 'true';
  toggle.setAttribute('aria-checked', String(on));
});

save.addEventListener('click', async () => {
  save.disabled = true;
  msg.textContent = 'Saving…';
  try {
    const res = await fetch('/api/prefs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ delay: toggle.getAttribute('aria-checked') === 'true' }),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    msg.textContent = 'Saved';
  } catch (err) {
    msg.textContent = 'Could not save. Try again.';
  } finally {
    save.disabled = false;
  }
});
</script>
```

What changed:

- **Switch is a real control.** It's now a `<button role="switch">` with `aria-checked`, so keyboard and screen-reader users can operate it. The label is tied to it with `for`, so clicking the text also toggles it.
- **Visual polish.** The layout is vertically centered, the knob has a subtle shadow, the toggle animates, and there's a focus ring. The Save button is styled to match the accent color.
- **Save feedback.** The button disables while saving, and a status message shows "Saved" or an error. Previously the save gave no indication of success or failure.
- **Request fixes.** The fetch now sends a `Content-Type: application/json` header and checks the response status. If your server already ignores or handles those differently, the only functional change is the error message.

I haven't run this in a browser, so check the spacing and colors against the rest of the Orchard Bay Ferries page.
