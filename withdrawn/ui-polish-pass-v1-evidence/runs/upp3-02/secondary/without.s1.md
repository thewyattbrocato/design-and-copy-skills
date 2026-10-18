The code works on the happy path, but it has a security issue and no failure handling, so I wouldn't ship it as-is.

**Must fix before release**

1. **XSS via `innerHTML`.** `s.month`, `s.total`, and `s.id` go straight into the markup. If any of them contain user-influenced text, such as a plan name or a customer-entered field, that's injectable script on a billing page. Build the nodes with `textContent` instead.
2. **Inline `onclick` with interpolated ID.** `onclick="download('${s.id}')"` breaks if the ID contains a quote and is an injection vector. It also means `download` must stay a global. Attach listeners in JS instead.
3. **No error handling.** If the request fails, returns a 401/500, or the session expired and the server redirects to an HTML login page, `r.json()` throws silently and the user sees "Loading" forever or an empty box. Check `r.ok` and show a message.
4. **Inline script and handlers may break under CSP.** If the site sends a Content-Security-Policy header without `'unsafe-inline'`, the `<script>` and `onclick` attributes are blocked in production and the page is empty. This is a common "works locally, fails in prod" cause. Check the production headers.
5. **Download navigates the page.** `location.href = …pdf` replaces the billing page if the server returns an error or a non-PDF response. Confirm the endpoint returns `application/pdf` with `Content-Disposition` on success and a proper error page or status otherwise. Also confirm the server enforces that the statement belongs to the logged-in user. The client can't enforce that.

**Should fix**

6. **Money and date formatting.** `s.total` is shown raw. Confirm whether it's cents or dollars and format it with `Intl.NumberFormat` in the right currency. Confirm `s.month` format and sort order.
7. **Empty state and loading state.** Zero statements currently renders nothing. Add a "No statements yet" message and a loading indicator.
8. **Accessibility.** The "Download" `div` isn't focusable or keyboard-operable. A `<button>` fixes that.
9. **Unscoped CSS.** `.row` and `.dl` are global and can collide with site styles. Prefix them.

**Verify before Thursday (not code changes)**

- Test against the production or staging API, not just local mock data. Check the response shape, field names, and whether `id` is always present.
- Test with an empty list, one statement, a long list, an expired session, a 500 response, and a network failure.
- Test the PDF download in Safari and on mobile.

Here's a revised version addressing items 1–3, 6–8, and 9. I haven't run it.

```html
<div class="stmts" id="stmts" aria-live="polite">Loading statements…</div>
<style>
.stmt-row{display:flex;justify-content:space-between;align-items:center;padding:8px}
.stmt-dl{color:#06c;background:none;border:0;padding:0;font:inherit;text-decoration:underline;cursor:pointer}
</style>
<script>
const container = document.getElementById('stmts');
const money = new Intl.NumberFormat(undefined, {style: 'currency', currency: 'USD'}); // confirm currency and whether total is cents

function render(list) {
  container.replaceChildren();
  if (!list.length) {
    container.textContent = 'No statements yet.';
    return;
  }
  for (const s of list) {
    const row = document.createElement('div');
    row.className = 'stmt-row';

    const month = document.createElement('span');
    month.textContent = s.month;

    const total = document.createElement('span');
    total.textContent = money.format(s.total);

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'stmt-dl';
    btn.textContent = 'Download';
    btn.addEventListener('click', () => download(s.id));

    row.append(month, total, btn);
    container.append(row);
  }
}

async function load() {
  try {
    const r = await fetch('/api/statements', {headers: {Accept: 'application/json'}});
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    render(await r.json());
  } catch (err) {
    container.textContent = "Couldn't load statements. Please refresh and try again.";
  }
}

function download(id) {
  location.href = '/api/statements/' + encodeURIComponent(id) + '.pdf';
}

load();
</script>
```
