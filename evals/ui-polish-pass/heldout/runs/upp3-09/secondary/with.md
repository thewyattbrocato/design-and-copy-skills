Here's the snippet with the switch made keyboard- and screen-reader-accessible, Save given a busy state and a visible result, and the layout fixed for narrow screens. Colors and wording stay the same, apart from one track color for contrast.

```html
<div class="setting">
  <label id="delay-label" for="sw1">Email me when a ferry is delayed</label>
  <button type="button" role="switch" id="sw1" class="sw" aria-checked="false" aria-labelledby="delay-label"></button>
</div>
<button id="save" type="button">Save</button>
<p id="status" role="status" aria-live="polite"></p>
<style>
.setting{display:flex;align-items:center;justify-content:space-between;gap:16px;width:320px;max-width:100%;box-sizing:border-box;padding:10px}
.sw{position:relative;flex:none;width:40px;height:22px;padding:0;border:0;border-radius:11px;background:#767676;cursor:pointer;transition:background-color .2s}
.sw.on{background:#2a7}
.sw::after{content:'';position:absolute;top:2px;left:2px;width:18px;height:18px;background:#fff;border-radius:50%;transition:left .2s}
.sw.on::after{left:20px}
.sw:focus-visible,#save:focus-visible{outline:2px solid #2a7;outline-offset:2px}
#save[aria-busy="true"]{opacity:.6;cursor:progress}
#status{min-height:1.2em;margin:8px 0 0;padding:0 10px}
#status.error{color:#b00020}
@media (prefers-reduced-motion: reduce){.sw,.sw::after{transition:none}}
</style>
<script>
const sw = document.getElementById('sw1');
const save = document.getElementById('save');
const status = document.getElementById('status');
let saving = false;

function setOn(on) {
  sw.classList.toggle('on', on);
  sw.setAttribute('aria-checked', String(on));
}

sw.onclick = function () { setOn(!sw.classList.contains('on')); };

save.onclick = async function () {
  if (saving) return;
  saving = true;
  save.setAttribute('aria-busy', 'true');
  save.textContent = 'Saving…';
  status.className = '';
  status.textContent = '';
  try {
    const res = await fetch('/api/prefs', {method: 'POST', body: JSON.stringify({delay: sw.classList.contains('on')})});
    if (!res.ok) throw new Error('HTTP ' + res.status);
    status.textContent = 'Preferences saved.';
  } catch (err) {
    status.className = 'error';
    status.textContent = "Couldn't save your preference. Check your connection and try Save again.";
  } finally {
    saving = false;
    save.removeAttribute('aria-busy');
    save.textContent = 'Save';
  }
};
</script>
```

What changed and why, in order of harm:
- **Switch was unusable by keyboard and silent to screen readers.** It was a bare `div` with no role, name or focus. It's now a real `button` with `role="switch"`, `aria-checked` kept in sync, and a name from the row label.
- **Save failed silently and could double-submit.** It now ignores repeat presses while a save is in flight, shows "Saving…", and reports success or failure in a live region. A failed save keeps the switch state so the person doesn't have to set it again. The error gives no invented retry count.
- **Track was `#ccc` on white, about 1.6:1.** I darkened the off state to `#767676` (3:1) so the switch boundary is visible. The on-state green `#2a7` is about 3:1 against white, which is borderline; if you want margin, a darker green would be the next tweak.
- **Layout and polish:** the row no longer overflows at 320px, the label and switch are vertically centred, and the knob and track animate only when motion is allowed.

Not checked: I haven't run this in a browser, with a real `/api/prefs` endpoint, or with a screen reader or keyboard. The `fetch` is unchanged apart from the `res.ok` check, so if the endpoint returns a non-2xx status for success, that would now show as an error.
