```html
<div class="setting">
  <label id="sw1-label" for="sw1">Email me when a ferry is delayed</label>
  <button type="button" class="sw" id="sw1" role="switch" aria-checked="false"></button>
</div>
<div class="actions">
  <button id="save">Save</button>
  <span id="status" role="status"></span>
</div>
<style>
.setting{display:flex;justify-content:space-between;align-items:center;gap:12px;width:320px;max-width:100%;padding:10px}
.sw{width:40px;height:22px;flex:none;padding:0;border:0;background:#767676;border-radius:11px;position:relative;cursor:pointer}
.sw[aria-checked="true"]{background:#2a7}
.sw::after{content:'';position:absolute;top:2px;left:2px;width:18px;height:18px;background:#fff;border-radius:50%}
.sw[aria-checked="true"]::after{left:20px}
.sw:focus-visible,#save:focus-visible{outline:2px solid #05c;outline-offset:2px}
.actions{display:flex;align-items:center;gap:12px;padding:0 10px}
#save[aria-busy="true"]{opacity:.6;cursor:progress}
#status.error{color:#b00020}
</style>
<script>
var sw = document.getElementById('sw1');
var save = document.getElementById('save');
var status = document.getElementById('status');

sw.onclick = function () {
  this.setAttribute('aria-checked', this.getAttribute('aria-checked') !== 'true');
  status.textContent = '';
};

save.onclick = function () {
  if (save.getAttribute('aria-busy') === 'true') return;
  save.setAttribute('aria-busy', 'true');
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
    status.textContent = 'Couldn\u2019t save your preference. Your choice is kept; press Save to try again.';
  }).finally(function () {
    save.removeAttribute('aria-busy');
    save.textContent = 'Save';
  });
};
</script>
```

I kept the layout, colors, wording and size. What changed:

- **Switch:** it was a `div`, so keyboard and screen-reader users couldn't reach it. It's now a `<button role="switch">` with `aria-checked`, and the text is a real `<label>` for it. Space and Enter toggle it. The `.on` class is gone.
- **Focus:** both controls now show a visible focus ring.
- **Save:** it was a silent `fetch`. It now shows "Saving…" and ignores double clicks. It reports "Saved." on success and a retryable message on failure, including HTTP errors, which the old code treated as success. The toggle keeps its state on failure. The message sits in a `role="status"` region so it's announced.
- **Request:** I added the `Content-Type: application/json` header. Without it, some servers won't parse the body. Drop it if your endpoint expects something else.
- **Contrast:** the off-state track was `#ccc` on white, which is too faint. It's now `#767676`.
- **Layout:** the row aligns vertically, has a gap, and shrinks on narrow screens.

Still open:
- The switch always starts off, because the snippet doesn't load the saved preference. If `/api/prefs` has a GET, the initial state should come from it.
- I didn't run this in a browser or with a screen reader.
