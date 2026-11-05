The errors do get written, but nothing draws attention to them. They're small text under each field, and the user is looking at the button. On a long form or a phone they can be offscreen. They're also not announced to screen readers, and old errors are never cleared once the user fixes a field.

The fix keeps the layout and styling as they are:

- On a failed submit, put a short message in the existing `#status` div next to the button.
- Move focus to the first invalid field, which scrolls it into view.
- Make the error and status divs live regions so assistive tech announces them.
- Clear old errors on each submit.

I also fixed two related bugs in the same handler:

- **Success on failure:** it said "Sent" even if the request failed.
- **Party size:** `novalidate` turned off the browser's min/max check, so 0 or 50 got through.

```html
<form id='req' novalidate>
  <h2>Request a table at Fennel &amp; Rye</h2>
  <label for='nm'>Name</label>
  <input id='nm' name='name' aria-describedby='e-nm'>
  <div class='err' id='e-nm' role='alert'></div>
  <label for='pp'>Party size</label>
  <input id='pp' name='party' type='number' min='1' max='12' aria-describedby='e-pp'>
  <div class='err' id='e-pp' role='alert'></div>
  <label for='dt'>Date</label>
  <input id='dt' name='date' type='date' aria-describedby='e-dt'>
  <div class='err' id='e-dt' role='alert'></div>
  <button type='submit'>Send request</button>
  <div id='status' role='status' aria-live='polite'></div>
</form>
<style>
  .err { color: #d33; font-size: .85rem; min-height: 1rem; }
  input { border: 1px solid #aaa; padding: .4rem; }
  input.bad { border-color: #d33; }
  #status.error { color: #d33; }
</style>
<script>
  document.getElementById('req').addEventListener('submit', async (e) => {
    e.preventDefault();
    const f = e.target;
    const status = document.getElementById('status');
    status.className = '';
    status.textContent = '';

    const checks = [
      [f.name,  'e-nm', v => v.trim() ? '' : 'Required'],
      [f.party, 'e-pp', v => !v ? 'Required'
                           : (+v < 1 || +v > 12) ? 'Party size must be 1–12' : ''],
      [f.date,  'e-dt', v => v ? '' : 'Required'],
    ];

    let firstBad = null;
    for (const [input, errId, test] of checks) {
      const msg = test(input.value);
      document.getElementById(errId).textContent = msg;
      input.classList.toggle('bad', !!msg);
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (msg && !firstBad) firstBad = input;
    }

    if (firstBad) {
      status.className = 'error';
      status.textContent = 'Please fix the highlighted fields.';
      firstBad.focus();
      return;
    }

    try {
      const res = await fetch('/request', { method: 'POST', body: new FormData(f) });
      if (!res.ok) throw new Error(res.status);
      status.textContent = 'Sent';
    } catch {
      status.className = 'error';
      status.textContent = 'Sorry, something went wrong. Please try again.';
    }
  });
</script>
```

- **Visual change:** the only one is a red message beside the button when validation fails, plus a red failure message if the request errors. Otherwise the layout and styles are as before.
- **Not tested:** I haven't run this in a browser.
- **Server check:** the 1–12 party-size check is client-side only, so the server should enforce it too.
