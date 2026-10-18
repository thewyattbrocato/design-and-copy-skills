I found two real bugs in the submit handler:

- **False success:** `fetch` only rejects on network failure. A 400 or 500 from the server would still show "Reserved."
- **Missing data:** the POST has no body, so the tool and date never reach the server.

I also added a check for the pickup rule your own help text states (Tuesday to Saturday), and blocked past dates.

Replace the `<script>` with this. The markup and CSS are unchanged.

```html
<script>
const f = document.getElementById('reserve'), go = document.getElementById('go');
const pickup = document.getElementById('pickup');
const iso = d => new Date(d.getTime() - d.getTimezoneOffset() * 60000).toISOString().slice(0, 10);
pickup.min = iso(new Date());

f.addEventListener('input', e => e.target.removeAttribute('aria-invalid'));

f.addEventListener('submit', async e => {
  e.preventDefault();
  if (go.disabled) return;
  const err = document.getElementById('err'), ok = document.getElementById('ok');
  err.hidden = ok.hidden = true;
  const tool = document.getElementById('tool');

  let bad = null, msg = '';
  if (!tool.value && !pickup.value) { bad = tool; msg = 'Choose a tool and a pickup date.'; }
  else if (!tool.value) { bad = tool; msg = 'Choose a tool.'; }
  else if (!pickup.value) { bad = pickup; msg = 'Choose a pickup date.'; }
  else {
    const day = new Date(pickup.value + 'T00:00').getDay();
    if (pickup.value < pickup.min) { bad = pickup; msg = 'Pick a date that is today or later.'; }
    else if (day === 0 || day === 1) { bad = pickup; msg = "We're closed Sunday and Monday. Pick a day from Tuesday to Saturday."; }
  }
  [tool, pickup].forEach(x => x.setAttribute('aria-invalid', !x.value || x === bad));
  if (bad) { err.textContent = msg; err.hidden = false; bad.focus(); return; }

  go.disabled = true; go.textContent = 'Reserving...';
  try {
    const res = await fetch('/api/reserve', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({tool: tool.value, pickup: pickup.value})
    });
    if (!res.ok) throw new Error(res.status);
    f.reset();
    ok.hidden = false;
  } catch (x) {
    err.textContent = "That didn't go through. Check your connection and try again.";
    err.hidden = false;
  }
  go.disabled = false; go.textContent = 'Reserve';
});
</script>
```

What changed:
- **Request body:** the tool and date are now sent as JSON. I guessed the field names `tool` and `pickup` and the JSON format, so match them to your API.
- **Response check:** a non-2xx response now shows the error message instead of a false "Reserved."
- **Error messages:** each one names what's missing or wrong, and focus goes to the first problem field. Only fields that are actually empty or invalid get the red border.
- **Success reset:** on success the form resets, so a second click can't re-submit the same booking.
- **Stale red border:** the red border clears as soon as the person edits the field.
- **Past dates:** `min` is set to today in local time.
- **Double submit:** a guard stops Enter from re-submitting while a request is in flight.

Open items:
- **Server validation:** the server should still enforce the closed days. The check here is client-side only.
- **Error text:** the error copy for a server rejection is still the generic connection message. If your API returns a reason, such as "that tool is already booked," show it instead.
- **Testing:** I didn't run this in a browser or test it with a screen reader.
