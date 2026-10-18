Your code has one release blocker, a likely XSS hole. Everything else is a gap that will show up in production but not on your machine, where the API probably returns well-formed data.

## Must fix before Thursday

1. **XSS via `innerHTML`.** `s.month`, `s.total`, and `s.id` go straight into HTML. Anything in those fields, including a malicious value from a compromised record or a stray `<` or `"` in the data, runs as script. The `onclick="download('${s.id}')"` attribute is also injectable. Build the nodes with `textContent` and `addEventListener` instead.
2. **No error handling.** If `/api/statements` returns a 401, 500, or HTML error page, `r.json()` throws and the user sees a blank section with no explanation. Check `res.ok`, show an error message, and handle the empty list.
3. **Server-side authorization.** I can't see the backend, so confirm it. `/api/statements/:id.pdf` must verify that the requesting user owns that statement. Otherwise anyone who guesses or enumerates IDs can download other customers' billing PDFs. Hiding the link in the UI does nothing for this.
4. **Download failures navigate away.** `location.href = ...` replaces the billing page with the server's error response if the PDF request fails. Either confirm the endpoint always succeeds for valid rows, or fetch the blob and handle errors in place.
5. **Formatting.** `s.total` is rendered raw. Confirm whether the API returns a formatted currency string or a number in cents, and format it accordingly (`Intl.NumberFormat` with the right currency and locale). The same goes for `s.month` if it's a date-like value.

## Should fix

6. **Accessibility.** The `<div class="dl" onclick>` isn't focusable and doesn't respond to the keyboard. A `<button>` fixes that.
7. **Content Security Policy.** The inline `<script>`, `<style>`, and inline handlers will be blocked if the release ships a strict CSP. Check the CSP headers in staging.
8. **Loading state and ordering.** Show a loading message, and make sure the API sorts newest first, since the client does no sorting.
9. **CSS collisions.** `.row` and `.dl` are global. Scope them under `.stmts` so they don't clash with the site's stylesheet.

## Revised version

```html
<div class="stmts" id="stmts" aria-live="polite">Loading statements…</div>
<style>
.stmts .row{display:flex;justify-content:space-between;align-items:center;padding:8px}
.stmts .dl{color:#06c;background:none;border:0;cursor:pointer;font:inherit;padding:0}
</style>
<script>
const container = document.getElementById('stmts');

function el(tag, text, cls) {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  node.textContent = text;
  return node;
}

function renderStatements(list) {
  container.replaceChildren();
  if (!list.length) {
    container.textContent = 'No statements yet.';
    return;
  }
  for (const s of list) {
    const row = el('div', '', 'row');
    const btn = el('button', 'Download', 'dl');
    btn.type = 'button';
    btn.addEventListener('click', () => download(s.id));
    row.append(el('span', s.month), el('span', s.total), btn);
    container.append(row);
  }
}

async function load() {
  try {
    const res = await fetch('/api/statements', { credentials: 'same-origin' });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    renderStatements(await res.json());
  } catch (err) {
    console.error(err);
    container.textContent = "Couldn't load statements. Please refresh and try again.";
  }
}

function download(id) {
  location.href = `/api/statements/${encodeURIComponent(id)}.pdf`;
}

load();
</script>
```

This doesn't fix the server-side items (3 and 4), and it doesn't fix the formatting of `s.total` (5), because those depend on the API contract I can't see.

## Test before Thursday

- An empty list, a 401 or 500 from the API, and a network failure.
- A user requesting another user's statement ID directly, which should return 403 or 404.
- Strings containing `<`, `"`, and `'` in the data.
- A long list and narrow mobile widths.
- Keyboard-only navigation through the Download buttons.
- Staging with the production CSP.
