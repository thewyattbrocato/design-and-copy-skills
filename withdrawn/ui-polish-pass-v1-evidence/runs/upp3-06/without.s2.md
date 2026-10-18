It's close, but I'd fix four things before it goes to the client. The first two are real bugs.

**Bugs**

1. **Server errors show as success.** `fetch` only rejects on network failure. A 400 or 500 still reaches `ok.hidden = false`, so the user sees "Reserved" when nothing was booked. Check `res.ok`.
2. **The request sends nothing.** `fetch('/api/reserve', {method: 'POST'})` has no body, so the tool and date never leave the page. I assumed a JSON body below. Adjust it to whatever your endpoint expects.
3. **The date rules aren't enforced.** The help text says "Tuesday to Saturday", but you can submit a Sunday, a Monday, or a date in the past. I added a `min` of today and a weekday check.
4. **The "Check your connection" message is wrong for server errors.** I made it neutral.

**Smaller polish**

- `aria-invalid` stays set after the user fixes a field. The fix below clears it on input.
- The form keeps its old values after a successful booking. The fix resets it.
- The success message sits flush against the button, so it needs a margin.
- Use `finally` to restore the button, so it can't get stuck if something throws.
- If this is a standalone page rather than a fragment, it also needs `<!doctype html>`, `<html lang="en">`, and `<meta name="viewport" content="width=device-width, initial-scale=1">`.

**Replacement script**

```html
<script>
const f = document.getElementById('reserve'), go = document.getElementById('go');
const err = document.getElementById('err'), ok = document.getElementById('ok');
const tool = document.getElementById('tool'), pickup = document.getElementById('pickup');

// Local-date "today" (toISOString alone would use UTC and can be off by a day)
pickup.min = new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().slice(0, 10);

f.addEventListener('input', e => e.target.removeAttribute('aria-invalid'));

f.addEventListener('submit', async e => {
  e.preventDefault();
  err.hidden = ok.hidden = true;

  let bad = null, msg = '';
  if (!tool.value) { bad = tool; msg = 'Choose a tool.'; }
  else if (!pickup.value) { bad = pickup; msg = 'Choose a pickup date.'; }
  else if (pickup.value < pickup.min) { bad = pickup; msg = 'Pickup date can’t be in the past.'; }
  else if (new Date(pickup.value + 'T00:00').getDay() < 2) { bad = pickup; msg = 'We’re closed Sunday and Monday. Pick Tuesday to Saturday.'; }

  f.querySelectorAll('[required]').forEach(x => x.removeAttribute('aria-invalid'));
  if (bad) {
    bad.setAttribute('aria-invalid', 'true');
    err.textContent = msg; err.hidden = false; bad.focus();
    return;
  }

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
  } catch {
    err.textContent = "That didn't go through. Please try again.";
    err.hidden = false;
  } finally {
    go.disabled = false; go.textContent = 'Reserve';
  }
});
</script>
```

**CSS addition**
```css
.ok{margin:12px 0 0}
```

I haven't run any of this. You pasted it inline and there's no file in the working directory. Before sending, try one submit with the server returning a 500, and one with a Sunday date.

Also check that the server rejects closed days and past dates itself. The client-side check is only a convenience.
