The main defect is that the form reports success for any server response, including errors. I fixed that and made the validation message name only the fields that are actually missing. Only the script changed; the markup and CSS are fine as they are.

Replace the `<script>` block with this:

```html
<script>
const f = document.getElementById('reserve'), go = document.getElementById('go');
const names = { tool: 'a tool', pickup: 'a pickup date' };
f.addEventListener('submit', async e => {
  e.preventDefault();
  const err = document.getElementById('err'), ok = document.getElementById('ok');
  err.hidden = ok.hidden = true;
  const fields = [...f.querySelectorAll('[required]')];
  const missing = fields.filter(x => !x.value);
  fields.forEach(x => x.setAttribute('aria-invalid', !x.value));
  if (missing.length) {
    err.textContent = 'Choose ' + missing.map(x => names[x.id]).join(' and ') + '.';
    err.hidden = false;
    missing[0].focus();
    return;
  }
  go.disabled = true; go.textContent = 'Reserving...';
  let msg = '';
  try {
    const res = await fetch('/api/reserve', {method: 'POST'});
    if (res.ok) ok.hidden = false;
    else msg = "That didn't go through. Please try again.";
  } catch (x) {
    msg = "That didn't go through. Check your connection and try again.";
  }
  if (msg) { err.textContent = msg; err.hidden = false; }
  go.disabled = false; go.textContent = 'Reserve';
});
</script>
```

What changed:
- **False success fixed:** a 4xx or 5xx response used to show "Reserved. We'll email a confirmation." Now only `res.ok` shows success, and other failures get the retry message. The connection message is kept only for real network failures.
- **Accurate validation message:** with only one field missing, it used to say "Choose a tool and a pickup date." It now names just the missing field.

Not changed, and worth a look before it goes out:
- **Past dates:** the date input accepts any date. If pickups can't be in the past, set `min` to today's date when the page loads.
- **Live regions:** `#err` and `#ok` are toggled with `hidden`, so some screen readers may skip the first announcement. Keeping them always in the DOM and filling in the text is more reliable. I left it alone because it changes the spacing.
- **Stale errors:** the red borders and the error text stay until the next submit, even after the person fixes the field.
- **Hanging requests:** a `fetch` that never resolves leaves the button on "Reserving..." indefinitely. A timeout with an `AbortController` would fix that.
- **Confirmation copy:** "We'll email a confirmation" is your claim. Make sure the backend actually sends that email.

I haven't run this, and I didn't test it with a screen reader or against the real `/api/reserve` endpoint. The checks were by reading the code.
