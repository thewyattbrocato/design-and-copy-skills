Here's the tidied version. The toggle is now a real button with switch semantics, so it works with a keyboard and screen readers. Save shows a busy state and a visible result, and a failed save keeps the toggle as the person left it.

```html
<div class="setting">
  <span id="delay-label">Email me when a ferry is delayed</span>
  <button type="button" class="sw" id="sw1" role="switch" aria-checked="false" aria-labelledby="delay-label"></button>
</div>
<div class="actions">
  <button type="button" id="save">Save</button>
  <p id="status" role="status" aria-live="polite"></p>
</div>
<style>
.setting{display:flex;align-items:center;justify-content:space-between;gap:16px;width:100%;max-width:320px;padding:10px 0}
.sw{position:relative;flex:none;width:40px;height:22px;padding:0;border:0;border-radius:11px;background:#ccc;cursor:pointer;transition:background .2s}
.sw:focus-visible{outline:2px solid #2a7;outline-offset:2px}
.sw.on{background:#2a7}
.sw::after{content:'';position:absolute;top:2px;left:2px;width:18px;height:18px;background:#fff;border-radius:50%;transition:left .2s}
.sw.on::after{left:20px}
.actions{display:flex;align-items:center;gap:12px;margin-top:12px}
#status{margin:0;font-size:14px}
#status.error{color:#b00020}
@media (prefers-reduced-motion:reduce){.sw,.sw::after{transition:none}}
</style>
<script>
const sw = document.getElementById('sw1');
const save = document.getElementById('save');
const status = document.getElementById('status');

function setOn(on) {
  sw.classList.toggle('on', on);
  sw.setAttribute('aria-checked', String(on));
}

sw.onclick = function () { setOn(!sw.classList.contains('on')); };

save.onclick = async function () {
  save.disabled = true;
  status.className = '';
  status.textContent = 'Saving…';
  try {
    const res = await fetch('/api/prefs', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({delay: sw.classList.contains('on')})
    });
    if (!res.ok) throw new Error('HTTP ' + res.status);
    status.textContent = 'Saved.';
  } catch (err) {
    status.className = 'error';
    status.textContent = "Couldn't save your preference. Check your connection and try again.";
  } finally {
    save.disabled = false;
  }
};
</script>
```

What changed and why:
- **Toggle is a `<button role="switch">`** instead of a `div`. It's focusable, toggles with Space/Enter, announces its on/off state via `aria-checked`, and is named by the label.
- **Focus ring** is restored with `:focus-visible`, not removed.
- **Save gives feedback:** "Saving…", then "Saved." or a plain-language error that the person can act on. The button is disabled while saving to prevent double-submits.
- **Failure is handled:** non-2xx responses and network errors now reach the error message. The original fired and forgot.
- **Layout:** `max-width` instead of a fixed `width`, so it wraps and doesn't clip at narrow widths or large text sizes.
- **Motion:** a short transition, removed under `prefers-reduced-motion`.

Two things to check:
- I added a `Content-Type: application/json` header. Your server must accept JSON for this to be parsed as you expect. If it already reads the body as text, the header is harmless.
- The "Saved." message assumes a 2xx response means the preference was stored. I haven't run this against your server, and I didn't test it in a browser or with a screen reader.
