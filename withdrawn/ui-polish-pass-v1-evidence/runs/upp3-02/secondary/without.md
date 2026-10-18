The biggest risks are unescaped data in `innerHTML`, no handling for failed or empty responses, and a clickable `div` that keyboard users can't reach. Each is a small fix.

**Blocking before Thursday**

1. **XSS.** `s.month`, `s.total`, and `s.id` go straight into `innerHTML`, and `s.id` is also placed inside an inline `onclick` string. If any of those values contain `<`, `"`, or `'`, or come from data a user can influence, the page runs their script. Build the nodes with `textContent` instead.
2. **Failure states.** If `/api/statements` returns a 401, 500, or times out, `r.json()` throws or the page stays blank with no error. Check `r.ok` and show a message. A 401 may need a redirect to login.
3. **Empty list.** A new account gets a blank card. Show "No statements yet."
4. **Loading state.** Without one, users see a blank area while the request runs.

**Should fix**

5. **Download is a `location.href` navigation.** If the PDF endpoint fails, the user leaves the billing page with an error or JSON on screen. An `<a href download>` avoids that and works with the keyboard and with middle-click.
6. **`div` as a button.** It isn't focusable or announced as a control. Use `<a>` or `<button>`.
7. **Encode the ID.** Use `encodeURIComponent(s.id)` in the URL.
8. **Formatting.** Check what `s.total` looks like. If it's cents or a bare number, format it with `Intl.NumberFormat` and a currency code. Consider a header row ("Statement", "Amount") and a stable sort order.
9. **CSP.** Inline `<script>`, `<style>`, and `onclick` will break if the release sets a Content-Security-Policy. Check the headers in staging.

**Why it works on your machine:** your data is probably clean, the API is up, and the network is fast. Test with an empty account, an API error (throttle it in DevTools or stub a 500), a slow response, a long or special-character value, and Safari.

Here's a version with these fixes. I haven't run it against your API, so verify it in staging:

```html
<div class="stmts" id="stmts" aria-live="polite">Loading…</div>
<style>
.row{display:flex;justify-content:space-between;padding:8px}
.dl{color:#06c;cursor:pointer}
</style>
<script>
const el = document.getElementById('stmts');

function row(s) {
  const r = document.createElement('div');
  r.className = 'row';
  const month = Object.assign(document.createElement('span'), { textContent: s.month });
  const total = Object.assign(document.createElement('span'), { textContent: s.total });
  const link = Object.assign(document.createElement('a'), {
    className: 'dl',
    textContent: 'Download',
    href: `/api/statements/${encodeURIComponent(s.id)}.pdf`,
  });
  link.download = '';
  r.append(month, total, link);
  return r;
}

fetch('/api/statements', { credentials: 'same-origin' })
  .then(r => {
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return r.json();
  })
  .then(list => {
    if (!list.length) {
      el.textContent = 'No statements yet.';
      return;
    }
    el.replaceChildren(...list.map(row));
  })
  .catch(() => {
    el.textContent = "Couldn't load statements. Please refresh the page.";
  });
</script>
```

Two things I'd confirm with the backend: what `/api/statements` returns on error (and whether a 401 should redirect to login), and whether the PDF endpoint sends `Content-Disposition` so the download has a sensible filename.
