I couldn't see the live page, so this comes from reading the code. The validation does run, but nothing draws attention to it. The errors are small and sit beside each field, while the button and the empty `#status` sit below them, so someone who presses the button sees no change. Three related problems:

- Errors never clear, and `.bad` is never removed, so stale errors stay after a field is fixed.
- Nothing is announced to screen readers, and focus never moves to the problem.
- The form says "Sent" even when the server rejects the request, because `fetch` doesn't throw on a 4xx/5xx. A failed send is another way the form can seem to do nothing.

The fix below keeps the look the same. The only visible additions are a one-line message in `#status` by the button and focus on the first bad field.

```html
<form id='req' novalidate>
  <h2>Request a table at Fennel &amp; Rye</h2>
  <label for='nm'>Name</label>
  <input id='nm' name='name' aria-describedby='e-nm'>
  <div class='err' id='e-nm' aria-live='polite'></div>
  <label for='pp'>Party size</label>
  <input id='pp' name='party' type='number' min='1' max='12' aria-describedby='e-pp'>
  <div class='err' id='e-pp' aria-live='polite'></div>
  <label for='dt'>Date</label>
  <input id='dt' name='date' type='date' aria-describedby='e-dt'>
  <div class='err' id='e-dt' aria-live='polite'></div>
  <button type='submit'>Send request</button>
  <div id='status' role='status'></div>
</form>
<style>
  .err { color: #d33; font-size: .85rem; min-height: 1rem; }
  input { border: 1px solid #aaa; padding: .4rem; }
  input.bad { border-color: #d33; }
  #status.bad { color: #d33; }
</style>
<script>
  const form = document.getElementById('req');
  const status = document.getElementById('status');
  const button = form.querySelector('button[type=submit]');

  const checks = [
    ['nm', v => v.trim() ? '' : 'Required'],
    ['pp', v => !v ? 'Required' : (v < 1 || v > 12) ? 'Enter a party size from 1 to 12' : ''],
    ['dt', v => v ? '' : 'Required'],
  ];

  function setStatus(msg, isError) {
    status.textContent = msg;
    status.classList.toggle('bad', !!isError);
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    setStatus('');

    let firstBad = null;
    for (const [id, check] of checks) {
      const input = document.getElementById(id);
      const msg = check(input.value);
      document.getElementById('e-' + id).textContent = msg;
      input.classList.toggle('bad', !!msg);
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (msg && !firstBad) firstBad = input;
    }
    if (firstBad) {
      setStatus('Please fix the highlighted fields.', true);
      firstBad.focus();   // also scrolls it into view
      return;
    }

    button.disabled = true;
    try {
      const res = await fetch('/request', { method: 'POST', body: new FormData(form) });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      setStatus('Sent');
    } catch (err) {
      setStatus('Sorry, we couldn\u2019t send your request. Please try again.', true);
    } finally {
      button.disabled = false;
    }
  });
</script>
```

Changes:
- **Visible feedback:** a failed validation puts a red message next to the button and moves focus to the first invalid field. Focus scrolls it into view on a small screen.
- **Stale errors:** every submit re-checks all fields and clears the ones that are now fine, including the red border.
- **Accessibility:** the inputs get `aria-invalid` and `aria-describedby`, and the error and status regions are live regions, so screen readers announce them.
- **Send failures:** a non-2xx response or a network error now shows a red "couldn't send" message instead of "Sent". The button is disabled while the request is in flight to stop double submits.
- **Party size range:** `novalidate` was switching off the `min`/`max` check, so 0 or 50 got through. I added a check for it. Remove that branch if you'd rather not have it.

I haven't run this in a browser. Please check one failing submit and one successful submit, and confirm `/request` returns a 2xx on success. If it returns a redirect or a non-standard status, the `res.ok` check will need adjusting.
