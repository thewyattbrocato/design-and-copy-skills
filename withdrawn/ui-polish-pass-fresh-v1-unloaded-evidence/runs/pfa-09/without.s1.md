I can't run this, so I haven't reproduced it. By reading the code, I found these likely causes:

- **Nothing draws attention to the errors.** Each message is 0.85rem text in a small slot under its field. If the invalid field is scrolled off-screen, or the user is looking at the button, nothing seems to happen. Focus never moves to the problem, and screen readers aren't told.
- **Errors never clear.** After a user fixes a field and resubmits, the old "Required" text and red border stay.
- **The status line reports success even when the request fails.** `fetch` doesn't throw on a 4xx or 5xx, so "Sent" appears regardless. A network failure throws and shows nothing, which is another way the button "does nothing".

Here's the fix. The markup and styles are unchanged except for `role='alert'` on the error divs. The visible layout is the same.

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
  <div id='status' role='status'></div>
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
    const status = document.getElementById('status');
    status.textContent = '';

    const checks = [
      [f.name, 'e-nm'],
      [f.party, 'e-pp'],
      [f.date, 'e-dt'],
    ];

    // Reset previous errors, then collect the invalid fields
    let firstBad = null;
    for (const [input, errId] of checks) {
      const empty = !input.value;
      document.getElementById(errId).textContent = empty ? 'Required' : '';
      input.classList.toggle('bad', empty);
      input.setAttribute('aria-invalid', empty);
      if (empty && !firstBad) firstBad = input;
    }

    if (firstBad) {
      firstBad.focus();   // also scrolls it into view
      status.textContent = 'Please fix the highlighted fields.';
      return;
    }

    try {
      const res = await fetch('/request', { method: 'POST', body: new FormData(f) });
      if (!res.ok) throw new Error(res.status);
      status.textContent = 'Sent';
    } catch (err) {
      status.textContent = 'Sorry, something went wrong. Please try again.';
    }
  });
</script>
```

What changed:
- **Focus:** the first invalid field is focused, so the page scrolls to the error and the cursor lands there.
- **Summary:** the status line says "Please fix the highlighted fields." next to the button, where the user just clicked.
- **Clearing:** errors and red borders reset on every submit.
- **Announcements:** `role='alert'` and `aria-invalid` make screen readers announce the errors.
- **Request failures:** "Sent" only appears if the server returned OK. Otherwise the user sees an error message.

I didn't add enforcement of the `min`/`max` on party size. `novalidate` turns off the browser's check, so someone can still submit 50. I can add that if you want it.

The status messages are plain unstyled text. If you want the failure message in red like the field errors, add `#status` to the `.err` color rule.
