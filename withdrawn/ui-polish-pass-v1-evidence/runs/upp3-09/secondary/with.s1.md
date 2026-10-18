Here's the tidied version. The switch is now a real button, the save has feedback, and the colors meet contrast.

```html
<div class="setting">
  <span id="delay-label">Email me when a ferry is delayed</span>
  <button type="button" class="sw" id="sw1" role="switch" aria-checked="false" aria-labelledby="delay-label"></button>
</div>
<div class="actions">
  <button id="save" type="button">Save</button>
  <span id="status" role="status"></span>
</div>
<style>
.setting{display:flex;align-items:center;justify-content:space-between;gap:16px;width:320px;max-width:100%;box-sizing:border-box;padding:10px}
.sw{position:relative;flex:none;width:40px;height:22px;padding:0;border:0;border-radius:11px;background:#767676;cursor:pointer;transition:background .2s}
.sw.on{background:#1e7a55}
.sw::after{content:'';position:absolute;top:2px;left:2px;width:18px;height:18px;background:#fff;border-radius:50%;transition:left .2s}
.sw.on::after{left:20px}
.sw:focus-visible,#save:focus-visible{outline:2px solid #1e7a55;outline-offset:2px}
#save:disabled{opacity:.6;cursor:progress}
.actions{display:flex;align-items:center;gap:10px;padding:10px}
@media (prefers-reduced-motion: reduce){.sw,.sw::after{transition:none}}
</style>
<script>
const sw = document.getElementById('sw1');
const save = document.getElementById('save');
const status = document.getElementById('status');

sw.onclick = function () {
  const on = this.classList.toggle('on');
  this.setAttribute('aria-checked', on);
  status.textContent = '';
};

save.onclick = async function () {
  save.disabled = true;
  save.textContent = 'Saving…';
  status.textContent = '';
  try {
    const res = await fetch('/api/prefs', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({delay: sw.classList.contains('on')})
    });
    if (!res.ok) throw new Error(res.status);
    status.textContent = 'Saved.';
  } catch (err) {
    status.textContent = "Couldn't save. Check your connection and try again.";
  } finally {
    save.disabled = false;
    save.textContent = 'Save';
  }
};
</script>
```

What changed, most harmful first:
- **Switch was unusable without a mouse.** It was a `div` with no name, role, or keyboard focus. It's now a `button` with `role="switch"`, `aria-checked`, and a label from the text. Focus is visible.
- **Save failed silently.** It now shows "Saved." or an error that says what to do, and it disables itself while the request runs so it can't be double-pressed. The toggle keeps its state on failure, so retrying is just pressing Save again.
- **Contrast.** The off track `#ccc` was too faint against white. It's now `#767676`, and the on green is darkened to `#1e7a55`. Both are the same hues as before.
- **Layout.** The fixed width no longer clips longer labels, and the label and switch are vertically centered.
- **Motion.** The knob animates, and reduced-motion users get no movement.

Two notes:
- I added a `Content-Type: application/json` header and a `res.ok` check. Confirm the server parses JSON bodies and returns non-2xx on failure, or the success and error messages won't match reality.
- Not tested in a browser, with a screen reader, or against your server.
