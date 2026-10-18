Here's the tidied version. I kept the look, layout and wording, and fixed what made it feel unfinished: the switch wasn't usable by keyboard or screen reader, and Save did nothing visible.

```html
<div class="setting">
  <span id="sw1-label">Email me when a ferry is delayed</span>
  <button type="button" class="sw" id="sw1" role="switch" aria-checked="false" aria-labelledby="sw1-label"></button>
</div>
<button id="save">Save</button>
<p id="status" role="status"></p>
<style>
.setting{display:flex;justify-content:space-between;align-items:center;gap:16px;width:320px;max-width:100%;padding:10px;box-sizing:border-box}
.sw{width:40px;height:22px;flex:none;padding:0;border:0;background:#8c8c8c;border-radius:11px;position:relative;cursor:pointer}
.sw[aria-checked="true"]{background:#2a7}
.sw::after{content:'';position:absolute;top:2px;left:2px;width:18px;height:18px;background:#fff;border-radius:50%}
.sw[aria-checked="true"]::after{left:20px}
.sw:focus-visible,#save:focus-visible{outline:2px solid #05c;outline-offset:2px}
#save:disabled{cursor:progress}
#status{padding:0 10px;min-height:1.2em}
#status.error{color:#b00020}
</style>
<script>
var sw = document.getElementById('sw1');
var save = document.getElementById('save');
var status = document.getElementById('status');

sw.onclick = function () {
  var on = sw.getAttribute('aria-checked') !== 'true';
  sw.setAttribute('aria-checked', on);
  status.textContent = '';
};

save.onclick = function () {
  save.disabled = true;
  save.textContent = 'Saving…';
  status.className = '';
  status.textContent = '';
  fetch('/api/prefs', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({delay: sw.getAttribute('aria-checked') === 'true'})
  }).then(function (res) {
    if (!res.ok) throw new Error(res.status);
    status.textContent = 'Saved.';
  }).catch(function () {
    status.className = 'error';
    status.textContent = "Couldn't save your setting. Your choice is still here, so try Save again.";
  }).finally(function () {
    save.disabled = false;
    save.textContent = 'Save';
  });
};
</script>
```

**What changed**
- **Switch:** it's now a `<button role="switch">` with `aria-checked`. It can be focused and toggled with Tab, Space and Enter, and it's announced with its label. The `div` was invisible to keyboards and screen readers.
- **Focus:** both controls get a visible focus ring.
- **Save:**
  - It shows "Saving…" and is disabled while the request runs, so it can't be double-submitted.
  - It says "Saved." on success.
  - On a failed request, it shows an error and keeps the toggle where the user left it, so they can retry. Before, a failure was silent.
  - It also sends a JSON `Content-Type` header. Drop that if your endpoint already works without it.
- **Contrast:** the off-state track went from `#ccc` to `#8c8c8c`. The old grey nearly vanished on white. The green and the layout are unchanged.
- **Narrow screens:** the row now wraps cleanly below 320px, and the switch stays vertically centered and doesn't shrink.

**Not checked:** I haven't run this in a browser or with a screen reader. The error text is a placeholder, so swap in your own wording or a [support link] if you want one.
