I couldn't find a file for this in the working directory, so here's the fixed snippet from your paste.

**Why people don't notice the errors**
- Nothing moves focus or scrolls to the error. The message is small text under a field, so on a phone it can be off-screen. Screen readers aren't told about it either.
- Errors and the red border are never cleared, so a second attempt looks the same as the first.
- A failed request also looks like nothing happened. `fetch` doesn't throw on a 4xx/5xx response, so the form says "Sent" anyway. A network failure throws and shows nothing.
- `min` and `max` on party size are ignored because of `novalidate`, so 0 or 50 would pass.

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
</style>
<script>
  document.getElementById('req').addEventListener('submit', async (e) => {
    e.preventDefault();
    const f = e.target;
    const btn = f.querySelector('button[type=submit]');
    const status = document.getElementById('status');
    status.textContent = '';

    const checks = [
      [f.elements.name,  'e-nm', v => !v.trim() ? 'Required' : ''],
      [f.elements.party, 'e-pp', v => !v ? 'Required'
                                  : (v < 1 || v > 12 || !Number.isInteger(+v)) ? 'Enter a party size from 1 to 12' : ''],
      [f.elements.date,  'e-dt', v => !v ? 'Required' : ''],
    ];

    let firstBad = null;
    for (const [input, errId, test] of checks) {
      const msg = test(input.value);
      document.getElementById(errId).textContent = msg;
      input.classList.toggle('bad', !!msg);
      if (msg) input.setAttribute('aria-invalid', 'true');
      else input.removeAttribute('aria-invalid');
      if (msg && !firstBad) firstBad = input;
    }
    if (firstBad) { firstBad.focus(); return; }

    btn.disabled = true;
    try {
      const res = await fetch('/request', { method: 'POST', body: new FormData(f) });
      if (!res.ok) throw new Error(res.status);
      status.textContent = 'Sent';
    } catch (err) {
      status.textContent = 'Sorry, your request didn\u2019t go through. Please try again or call us.';
    } finally {
      btn.disabled = false;
    }
  });
</script>
```

**What changed**
- On a failed check, focus jumps to the first invalid field. The browser scrolls it into view, and the red border is now easy to spot.
- The error divs have `role='alert'`, and the inputs have `aria-describedby` and `aria-invalid`, so screen readers announce the errors.
- Errors and borders are cleared and re-evaluated on every submit.
- Party size is checked against 1–12, and a whitespace-only name counts as empty.
- "Sent" only shows if the server returns OK. Otherwise the user sees a failure message, and the button is disabled while the request is in flight to stop double submits.

The layout and styling are unchanged. I only added attributes and script logic, no CSS.

**Two things to check**
- The "call us" wording in the failure message is my placeholder, so edit it to whatever you want customers to do.
- I haven't run this against your real `/request` endpoint. Test the success and failure paths there.
