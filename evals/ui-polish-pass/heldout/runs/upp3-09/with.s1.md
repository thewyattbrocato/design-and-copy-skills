Here's the tidied version. It keeps the look, layout and wording. The changes are to the switch, the Save feedback and a few edge cases.

```html
<div class="setting">
  <span id="sw1-label">Email me when a ferry is delayed</span>
  <button type="button" class="sw" id="sw1" role="switch" aria-checked="false" aria-labelledby="sw1-label"></button>
</div>
<button id="save" type="button">Save</button>
<p id="status" role="status"></p>
<style>
.setting{display:flex;justify-content:space-between;align-items:center;gap:12px;width:320px;max-width:100%;padding:10px}
.sw{flex:none;width:40px;height:22px;background:#767676;border:0;padding:0;border-radius:11px;position:relative;cursor:pointer}
.sw[aria-checked="true"]{background:#1a7a55}
.sw::after{content:'';position:absolute;top:2px;left:2px;width:18px;height:18px;background:#fff;border-radius:50%}
.sw[aria-checked="true"]::after{left:20px}
.sw:focus-visible,#save:focus-visible{outline:2px solid #05f;outline-offset:2px}
#save:disabled{cursor:progress}
#status{margin:0;padding:0 10px;max-width:320px}
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
    status.textContent = 'Saved. Your notification setting is up to date.';
  }).catch(function () {
    status.className = 'error';
    status.textContent = 'Your setting wasn\u2019t saved. Check your connection and try Save again.';
  }).finally(function () {
    save.disabled = false;
    save.textContent = 'Save';
  });
};
</script>
```

**What changed**
- **Switch:** it was a clickable `div`, so keyboard and screen-reader users couldn't use it. It's now a `<button role="switch">` with `aria-checked`, named by the label text. Space and Enter work, and the on/off state is announced.
- **Focus:** there's now a visible focus ring on the switch and Save.
- **Contrast:** the off track was `#ccc` on white, which is too faint. It's now `#767676`. The on color is slightly darker (`#1a7a55`) so the white thumb stands out.
- **Save:** it was silent. Now the button shows "Saving…" and is disabled while the request runs, so it can't be double-submitted. The result appears as text in a live region. On failure the toggle stays as the user set it, and they can press Save again.
- **Request:** it now sends a JSON `Content-Type` header, and HTTP errors count as failures. Before, a 500 looked like success.
- **Layout:** the fixed 320px width now shrinks on narrow screens, with a gap and vertical centering so a long label doesn't crowd the switch.

**Notes**
- The switch always starts off, because nothing loads the saved preference. Users who already opted in will see "off" and may overwrite it. Fixing this needs a read endpoint I don't know about, so I left it.
- I haven't run this in a browser or tested it with a screen reader.
