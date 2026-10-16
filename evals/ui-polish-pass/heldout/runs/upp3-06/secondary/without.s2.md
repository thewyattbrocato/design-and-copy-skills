Two things in the current version would break in front of a client: the request doesn't send the selection, and a server error still shows "Reserved." I fixed those below along with a few smaller items.

```html
<form id="reserve" novalidate>
  <h2>Reserve a tool</h2>
  <label for="tool">Tool</label>
  <select id="tool" required>
    <option value="">Choose a tool</option>
    <option>Cordless drill</option>
    <option>Tile saw</option>
    <option>Step ladder</option>
  </select>
  <label for="pickup">Pickup date</label>
  <input id="pickup" type="date" required aria-describedby="pickup-help">
  <p id="pickup-help" class="help">We're open Tuesday to Saturday. Loans run 7 days.</p>
  <p id="err" class="err" role="alert" hidden></p>
  <button id="go" type="submit">Reserve</button>
  <p id="ok" class="ok" role="status" hidden>Reserved. We'll email a confirmation.</p>
</form>
<style>
:root{--ink:#1d2b2a;--muted:#55635f;--line:#c9d3cf;--accent:#1f6f5c;--bad:#a4271f}
body{font:16px/1.5 system-ui,sans-serif;color:var(--ink);margin:0;padding:24px;background:#f7faf8}
form{max-width:380px;margin:auto;background:#fff;border:1px solid var(--line);border-radius:10px;padding:24px}
h2{margin:0 0 16px;font-size:1.25rem}
label{display:block;font-weight:600;margin-top:14px}
select,input{width:100%;box-sizing:border-box;font:inherit;padding:10px 12px;border:1px solid var(--line);border-radius:6px;min-height:44px;margin-top:4px}
.help{color:var(--muted);font-size:.875rem;margin:4px 0 0}
.err{color:var(--bad);margin:12px 0 0}
.ok{color:var(--accent);font-weight:600}
button{margin-top:18px;width:100%;min-height:44px;font:inherit;font-weight:600;color:#fff;background:var(--accent);border:0;border-radius:6px;cursor:pointer}
button:hover{background:#185a4a}
button:disabled{background:#9db8b0;cursor:not-allowed}
:focus-visible{outline:3px solid #1b5fd1;outline-offset:2px}
[aria-invalid=true]{border-color:var(--bad)}
@media (prefers-reduced-motion:no-preference){button{transition:background .15s}}
</style>
<script>
const f = document.getElementById('reserve'), go = document.getElementById('go');
const err = document.getElementById('err'), ok = document.getElementById('ok');
const fields = [...f.querySelectorAll('[required]')];
const messages = { tool: 'Choose a tool.', pickup: 'Choose a pickup date.' };

f.addEventListener('submit', async e => {
  e.preventDefault();
  err.hidden = ok.hidden = true;

  const missing = fields.filter(x => !x.value);
  fields.forEach(x => missing.includes(x)
    ? x.setAttribute('aria-invalid', 'true')
    : x.removeAttribute('aria-invalid'));
  if (missing.length) {
    err.textContent = missing.map(x => messages[x.id]).join(' ');
    err.hidden = false;
    missing[0].focus();
    return;
  }

  go.disabled = true;
  go.textContent = 'Reserving...';
  try {
    const res = await fetch('/api/reserve', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tool: f.tool.value, pickup: f.pickup.value })
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    ok.hidden = false;
    f.reset();
  } catch (x) {
    err.textContent = "That didn't go through. Check your connection and try again.";
    err.hidden = false;
  } finally {
    go.disabled = false;
    go.textContent = 'Reserve';
  }
});
</script>
```

**What changed**

- **Request body:** `fetch` now sends the tool and pickup date as JSON. The original sent an empty POST, so the server had no idea what was being reserved.
- **Server errors:** `fetch` only rejects on network failures. The code now checks `res.ok`, so a 4xx or 5xx shows the error message instead of the success message.
- **Error text:** the message names only the missing field(s) instead of always saying "Choose a tool and a pickup date."
- **`aria-invalid`:** it is now removed when a field is valid instead of being set to `"false"`. The `[aria-invalid=true]` CSS only matches the `"true"` value anyway.
- **Reset after success:** the form clears so a second click can't submit the same booking by accident.
- **`finally`:** the button resets on every path, not just success and the catch.

The CSS is unchanged. I haven't run this in a browser, so please check it there before it goes out.

**Check before sending**

1. **Pickup days:** the help text says you're open Tuesday to Saturday, but nothing stops a Sunday or Monday pickup. If pickups are only on those days, add a weekday check. If the text is only about when staff are around, consider rewording it so it isn't read as a rule.
2. **Past dates:** the date input accepts any date. Setting `min` to today would stop bookings for days that have already passed.
3. **Confirmation email:** the success message promises one. Confirm the backend actually sends it.
4. **Server errors:** the generic failure message will be misleading if the API returns something specific, such as a tool already booked for that day. If it does, show the server's message.
