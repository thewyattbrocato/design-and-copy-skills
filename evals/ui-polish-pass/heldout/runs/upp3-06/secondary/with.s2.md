Two real defects are fixed below in the script. Everything else already works and is unchanged.

```html
<script>
const f = document.getElementById('reserve'), go = document.getElementById('go');
const err = document.getElementById('err'), ok = document.getElementById('ok');
const hint = { tool: 'a tool', pickup: 'a pickup date' };
f.addEventListener('submit', async e => {
  e.preventDefault();
  err.hidden = ok.hidden = true;
  const required = [...f.querySelectorAll('[required]')];
  const missing = required.filter(x => !x.value);
  required.forEach(x => x.setAttribute('aria-invalid', !x.value));
  if (missing.length) {
    err.textContent = 'Choose ' + missing.map(x => hint[x.id]).join(' and ') + '.';
    err.hidden = false; missing[0].focus(); return;
  }
  go.disabled = true; go.textContent = 'Reserving...';
  try {
    const res = await fetch('/api/reserve', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tool: f.tool.value, pickup: f.pickup.value })
    });
    if (!res.ok) throw new Error(res.status);
    ok.hidden = false;
  } catch (x) {
    err.textContent = "That didn't go through. Check your connection and try again.";
    err.hidden = false;
  }
  go.disabled = false; go.textContent = 'Reserve';
});
</script>
```

**What changed**

1. **Silent data loss (blocks the task).** The original `fetch` sent no body, so the server never received the tool or date. It now sends both as JSON.
2. **False success (misleads).** A 500 or 404 response counted as "Reserved." Now any non-OK response goes to the error message and keeps what the person typed.
3. **Vague error.** "Choose a tool and a pickup date." was shown even when only one field was empty. It now names only the missing field(s).

**Assumptions to confirm**

- The endpoint expects `{ "tool": "...", "pickup": "YYYY-MM-DD" }` as JSON. If your backend takes form data or different keys, adjust the `body` line.

**Left alone (already good):** the layout, colors, labels, help text linked with `aria-describedby`, the `role="alert"` and `role="status"` regions, focus moved to the first problem, the visible focus ring, the busy label on the button, and the 44px touch targets.

**Remaining notes**

- Past dates can still be picked. If that matters, set `pickup.min` to today's date in the script and check it in the validation. I didn't add it because it's a small behavior decision for you.
- I haven't run this against a server or tested it with a screen reader or on a device. These checks are from reading the code only.
