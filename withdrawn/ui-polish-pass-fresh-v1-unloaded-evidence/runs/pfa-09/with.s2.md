The errors were rendering, but nothing drew attention to them. They're small text under each field, and on a phone the button can sit off-screen from them. Nothing moved focus or scrolled to them, and the status line stayed empty. There were also two related bugs. Errors were never cleared once fixed. A failed `fetch` still showed "Sent", because the response was never checked.

Here's the fixed version. Markup and CSS are unchanged except for a few attributes and one added rule.

```html
<form id='req' novalidate>
  <h2>Request a table at Fennel &amp; Rye</h2>
  <label for='nm'>Name</label>
  <input id='nm' name='name' aria-describedby='e-nm'>
  <div class='err' id='e-nm'></div>
  <label for='pp'>Party size</label>
  <input id='pp' name='party' type='number' min='1' max='12' aria-describedby='e-pp'>
  <div class='err' id='e-pp'></div>
  <label for='dt'>Date</label>
  <input id='dt' name='date' type='date' aria-describedby='e-dt'>
  <div class='err' id='e-dt'></div>
  <button type='submit'>Send request</button>
  <div id='status' role='status' aria-live='polite'></div>
</form>
<style>
  .err { color: #d33; font-size: .85rem; min-height: 1rem; }
  input { border: 1px solid #aaa; padding: .4rem; }
  input.bad { border-color: #d33; }
  #status.bad { color: #d33; }
</style>
<script>
  document.getElementById('req').addEventListener('submit', async (e) => {
    e.preventDefault();
    const f = e.target;
    const status = document.getElementById('status');
    const btn = f.querySelector('button[type=submit]');
    status.className = '';
    status.textContent = '';

    const checks = [
      [f.name,  'e-nm', v => v.trim() ? '' : 'Required'],
      [f.party, 'e-pp', v => !v ? 'Required'
                           : (v < 1 || v > 12) ? 'Party size must be between 1 and 12' : ''],
      [f.date,  'e-dt', v => v ? '' : 'Required'],
    ];

    let firstBad = null;
    for (const [input, errId, test] of checks) {
      const msg = test(input.value);
      document.getElementById(errId).textContent = msg;   // also clears old errors
      input.classList.toggle('bad', !!msg);
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (msg && !firstBad) firstBad = input;
    }

    if (firstBad) {
      status.className = 'bad';
      status.textContent = 'Please fix the highlighted fields.';
      firstBad.focus();   // scrolls to the field and announces it
      return;
    }

    btn.disabled = true;
    status.textContent = 'Sending…';
    try {
      const res = await fetch('/request', { method: 'POST', body: new FormData(f) });
      if (!res.ok) throw new Error(res.status);
      status.textContent = 'Sent';
    } catch {
      status.className = 'bad';
      status.textContent = 'Sorry, something went wrong. Please try again.';
    } finally {
      btn.disabled = false;
    }
  });
</script>
```

**What changed**
- **Visibility:** On a failed submit, focus jumps to the first invalid field, which also scrolls it into view. A message next to the button says "Please fix the highlighted fields."
- **Stale errors:** Each submit re-evaluates every field, so fixed fields lose their error text and red border.
- **Honest status:** The button disables while sending. "Sent" only appears on a successful response. A network or server error shows a retry message instead.
- **Range check:** Party size is checked against the 1–12 range. `novalidate` was turning off the browser's own check, so 50 used to pass.
- **Whitespace:** A name made only of spaces now counts as empty.
- **Screen readers:** I added `aria-describedby`, `aria-invalid` and a live region for the status.

I haven't run this in a browser, and I don't know what `/request` returns. If it replies 200 even on failure, the success message will still be wrong. I also didn't block past dates, since you didn't ask for it. It's an easy addition if you want it.
