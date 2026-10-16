The form is in good shape: the labels, help text, focus ring, 44px targets, busy state and plain-language error all work. A few real problems remain, and the first two matter before this goes to a client.

**1. The request sends nothing, and any response counts as success.** `fetch('/api/reserve', {method: 'POST'})` has no body, so the server never learns the tool or date. A 400 or 500 also shows "Reserved." because `fetch` only rejects on network failure.

**2. The "Tuesday to Saturday" rule isn't enforced.** Someone can pick a Sunday or a past date and get a confirmation.

**3. Input borders are too faint.** `#c9d3cf` on white is about 1.5:1, and field boundaries need 3:1. The card border can stay as it is.

**4. Smaller issues.** The error message is the same whichever field is missing, and the invalid fields aren't linked to it. `.ok` has no top margin.

Replace the script with this:

```html
<script>
const f = document.getElementById('reserve'), go = document.getElementById('go');
const pickup = document.getElementById('pickup');
const today = new Date(); today.setMinutes(today.getMinutes() - today.getTimezoneOffset());
pickup.min = today.toISOString().slice(0, 10);

f.addEventListener('submit', async e => {
  e.preventDefault();
  const err = document.getElementById('err'), ok = document.getElementById('ok');
  err.hidden = ok.hidden = true;
  const tool = document.getElementById('tool');
  const day = pickup.value && new Date(pickup.value + 'T00:00:00').getDay();
  let msg = '', bad = [];
  if (!tool.value && !pickup.value) { msg = 'Choose a tool and a pickup date.'; bad = [tool, pickup]; }
  else if (!tool.value) { msg = 'Choose a tool.'; bad = [tool]; }
  else if (!pickup.value) { msg = 'Choose a pickup date.'; bad = [pickup]; }
  else if (pickup.value < pickup.min) { msg = 'Pick a date that is today or later.'; bad = [pickup]; }
  else if (day < 2 || day > 6) { msg = "We're closed Sunday and Monday. Pick a day from Tuesday to Saturday."; bad = [pickup]; }
  [tool, pickup].forEach(x => {
    x.setAttribute('aria-invalid', bad.includes(x));
    x.setAttribute('aria-describedby', (x === pickup ? 'pickup-help ' : '') + (bad.includes(x) ? 'err' : '').trim());
  });
  if (bad.length) { err.textContent = msg; err.hidden = false; bad[0].focus(); return; }
  go.disabled = true; go.textContent = 'Reserving...';
  try {
    const r = await fetch('/api/reserve', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({tool: tool.value, pickup: pickup.value})
    });
    if (!r.ok) throw new Error(r.status);
    ok.hidden = false;
  } catch (x) {
    err.textContent = "That didn't go through. Check your connection and try again.";
    err.hidden = false;
  }
  go.disabled = false; go.textContent = 'Reserve';
});
</script>
```

Two CSS changes:

```css
select,input{/* …existing… */border:1px solid #6f817c}
.ok{color:var(--accent);font-weight:600;margin:12px 0 0}
```

I wrote `border:1px solid #6f817c` as a replacement for the border in the existing `select,input` rule, with the rest unchanged.

- **Decision for you:** I assumed the `/api/reserve` body is `{tool, pickup}` as JSON. Match that to whatever your backend expects. The server should also re-check the open days, because client checks can be bypassed.
- **Not checked:** I haven't run this in a browser or with a screen reader, and I haven't tested the reply a real server sends back.
