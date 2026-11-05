The errors are drawn, but nothing brings them to the user's attention, so the button feels dead. Here's what I found and fixed.

**Causes**
- Nothing scrolls to or focuses the error. The messages are small and sit under the fields, so on a phone they can be off-screen, away from the button.
- Errors are never cleared. Once a field is fixed, the old "Required" and red border stay.
- `min`/`max` are never checked, because `novalidate` turns off the browser's checks. A party of 50 gets sent.
- The form says "Sent" even if the request fails, and `fetch` doesn't throw on a 4xx/5xx. A double-click also sends it twice.
- Screen readers announce none of it, because there's no `aria-live`.

**Fixed version.** The look is unchanged. The only new style is `:focus` on the status line.

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
  <div id='status' role='status' tabindex='-1'></div>
</form>
<style>
  .err { color: #d33; font-size: .85rem; min-height: 1rem; }
  input { border: 1px solid #aaa; padding: .4rem; }
  input.bad { border-color: #d33; }
  #status:focus { outline: none; }
</style>
<script>
  document.getElementById('req').addEventListener('submit', async (e) => {
    e.preventDefault();
    const f = e.target;
    const btn = f.querySelector('button[type=submit]');
    const status = document.getElementById('status');
    status.textContent = '';

    const checks = [
      ['name',  'e-nm', v => v.trim() ? '' : 'Please enter your name'],
      ['party', 'e-pp', v => !v ? 'Please enter a party size'
                          : (+v < 1 || +v > 12) ? 'Party size must be between 1 and 12' : ''],
      ['date',  'e-dt', v => v ? '' : 'Please choose a date'],
    ];

    let firstBad = null;
    for (const [field, errId, test] of checks) {
      const input = f.elements[field];
      const msg = test(input.value);
      document.getElementById(errId).textContent = msg;
      input.classList.toggle('bad', !!msg);
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (msg && !firstBad) firstBad = input;
    }
    if (firstBad) {
      firstBad.scrollIntoView({ block: 'center', behavior: 'smooth' });
      firstBad.focus({ preventScroll: true });
      status.textContent = 'Please fix the highlighted fields.';
      return;
    }

    btn.disabled = true;
    try {
      const res = await fetch('/request', { method: 'POST', body: new FormData(f) });
      if (!res.ok) throw new Error(res.status);
      status.textContent = 'Sent';
      f.reset();
    } catch (err) {
      status.textContent = "Sorry, we couldn't send your request. Please try again or call us.";
    } finally {
      btn.disabled = false;
      status.scrollIntoView({ block: 'nearest' });
    }
  });
</script>
```

**Behaviour changes**
- On a bad submit, the page scrolls to the first bad field and focuses it. A line by the button also says "Please fix the highlighted fields."
- Errors and red borders clear when the field is valid.
- Party size is range-checked.
- "Sent" appears only on a successful response. Failures show a message, and the button is disabled while the request is in flight.
- I replaced `f.name.value` with `f.elements.name.value`. It's the safer lookup, because `form.name` can clash with the form's own `name` property.

I haven't run this in a browser. Please try an empty submit, a party of 50, and a failed request (for example, by going offline).

The "call us" wording in the failure message is a placeholder, so change it to whatever fits.
