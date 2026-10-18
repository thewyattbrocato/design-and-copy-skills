I read through it and found two real bugs plus a few smaller gaps. The form is otherwise in good shape: the labels, focus styles, 44px targets and reduced-motion handling are all solid.

**Bugs to fix before it goes out**
1. **The request sends no data.** `fetch('/api/reserve', {method: 'POST'})` has no body, so the server never learns which tool or date was chosen.
2. **Server errors show as success.** `fetch` only throws on network failure. A 400 or 500 response would still show "Reserved. We'll email a confirmation." You need to check `res.ok`.

**Smaller gaps**
- The help text says "Tuesday to Saturday", but nothing enforces it. Past dates and Sundays or Mondays go through.
- `aria-invalid` stays set after the user fixes a field, until the next submit.
- After a successful reservation the form keeps its values, so a second click books a duplicate.
- `.ok` has no top margin, so it sits tight against the button.

**Polished version**

```html
<form id="reserve" novalidate>
  <h2>Reserve a tool</h2>
  <label for="tool">Tool</label>
  <select id="tool" name="tool" required>
    <option value="">Choose a tool</option>
    <option>Cordless drill</option>
    <option>Tile saw</option>
    <option>Step ladder</option>
  </select>
  <label for="pickup">Pickup date</label>
  <input id="pickup" name="pickup" type="date" required aria-describedby="pickup-help">
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
.ok{color:var(--accent);font-weight:600;margin:12px 0 0}
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
const tool = document.getElementById('tool'), pickup = document.getElementById('pickup');

const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
pickup.min = iso(new Date());

function check() {
  if (!tool.value) return [tool, 'Choose a tool.'];
  if (!pickup.value) return [pickup, 'Choose a pickup date.'];
  if (pickup.value < pickup.min) return [pickup, 'Pick a date that is today or later.'];
  const [y, m, d] = pickup.value.split('-').map(Number);
  const day = new Date(y, m - 1, d).getDay();
  if (day === 0 || day === 1) return [pickup, "We're closed Sunday and Monday. Pick a Tuesday to Saturday."];
}

f.addEventListener('input', e => e.target.removeAttribute('aria-invalid'));

f.addEventListener('submit', async e => {
  e.preventDefault();
  err.hidden = ok.hidden = true;
  [tool, pickup].forEach(x => x.removeAttribute('aria-invalid'));

  const problem = check();
  if (problem) {
    const [field, msg] = problem;
    field.setAttribute('aria-invalid', 'true');
    err.textContent = msg; err.hidden = false; field.focus();
    return;
  }

  go.disabled = true; go.textContent = 'Reserving…';
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

**Things to check on your side**
- I assumed `/api/reserve` takes JSON with `tool` and `pickup`. Adjust the body if your backend expects something else, such as form-encoded data.
- If your backend returns a useful error message, such as "that tool is booked that day", show it instead of the generic connection error.
- If this is a full page and not a fragment, add `<html lang="en">` and `<meta name="viewport" content="width=device-width, initial-scale=1">`. Without the viewport tag, mobile will render it zoomed out.
- Closed days are enforced on the client only. The server should check them too.
- I didn't run this in a browser, so click through the error, success and failure paths once before you send it.
