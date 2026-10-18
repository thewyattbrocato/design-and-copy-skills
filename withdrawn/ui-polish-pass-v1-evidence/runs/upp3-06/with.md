Mostly solid. The labels, 44px targets, focus ring, busy state and live regions all work, and I've left them alone. These are the fixes, in order of harm:

1. **The request sends nothing.** `fetch('/api/reserve', {method:'POST'})` has no body, so the server never learns which tool or date was picked.
2. **A failed request shows as success.** `fetch` only throws on network errors. A 400 or 500 response still shows "Reserved."
3. **The date is never checked.** The help text says Tuesday to Saturday, but Sundays, Mondays and past dates go through.
4. **The missing-field message is vague.** It names both fields even when only one is empty.
5. **Input borders are too faint.** `#c9d3cf` on white is about 1.5:1, and form fields need 3:1.
6. **The form stays filled after success.** A second tap on Reserve books the same tool again.

Changed pieces only:

```css
:root{/* add */ --field:#6f7f7a}
select,input{/* change border color */ border:1px solid var(--field)}
.ok{color:var(--accent);font-weight:600;margin:12px 0 0}
```

```js
const f = document.getElementById('reserve'), go = document.getElementById('go');
const tool = document.getElementById('tool'), pickup = document.getElementById('pickup');
const today = new Date(); today.setMinutes(today.getMinutes() - today.getTimezoneOffset());
pickup.min = today.toISOString().slice(0, 10);

f.addEventListener('input', e => e.target.removeAttribute('aria-invalid'));

f.addEventListener('submit', async e => {
  e.preventDefault();
  const err = document.getElementById('err'), ok = document.getElementById('ok');
  err.hidden = ok.hidden = true;
  const fail = (msg, el) => { err.textContent = msg; err.hidden = false; el.focus(); };
  f.querySelectorAll('[required]').forEach(x => x.setAttribute('aria-invalid', !x.value));
  if (!tool.value && !pickup.value) return fail('Choose a tool and a pickup date.', tool);
  if (!tool.value) return fail('Choose a tool.', tool);
  if (!pickup.value) return fail('Choose a pickup date.', pickup);
  const day = new Date(pickup.value + 'T00:00').getDay();
  if (pickup.value < pickup.min || day < 2) {
    pickup.setAttribute('aria-invalid', true);
    return fail(pickup.value < pickup.min
      ? 'Pick today or a later date.'
      : "We're closed Sunday and Monday. Pick a date from Tuesday to Saturday.", pickup);
  }
  go.disabled = true; go.textContent = 'Reserving...';
  try {
    const r = await fetch('/api/reserve', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({tool: tool.value, pickup: pickup.value})
    });
    if (!r.ok) throw new Error(r.status);
    ok.hidden = false; f.reset();
  } catch (x) {
    err.textContent = "That didn't go through. Check your connection and try again."; err.hidden = false;
  }
  go.disabled = false; go.textContent = 'Reserve';
});
```

- **Needs your call:** I guessed the request shape (JSON with `tool` and `pickup`). Match it to what the backend expects. The 4xx/5xx case also shows the connection-problem message, which is wrong for a rejected request. If the API returns a reason, show that instead.
- **Not checked:** I haven't run this in a browser or with a screen reader. I didn't test a slow or hanging network either, since there's no timeout on the request.
