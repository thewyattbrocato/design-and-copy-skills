The code works, but it has a few things I wouldn't ship on a billing page. They're listed by priority.

## Blockers

**1. Unescaped data goes into `innerHTML`, which is an XSS risk.**
`s.month`, `s.total` and `s.id` are interpolated straight into markup. `s.id` also lands inside a JS string in an inline `onclick`, so a value containing `'` can break out and run code. Even if the IDs are server-generated today, billing pages shouldn't depend on that. Build the DOM with `textContent` and `addEventListener`, or use a real link (see the snippet below).

**2. Authorization on `/api/statements/:id.pdf`.**
I can't see the backend, so please check this one. The server must verify that the statement belongs to the logged-in account, not just that the user is logged in. Otherwise anyone can walk the IDs and download other customers' statements. Also confirm that the list endpoint is scoped to the current account, and that PDF responses send `Cache-Control: private, no-store`.

**3. No error handling.**
- There's no `r.ok` check, so a 401 or 500 with a non-JSON body throws and leaves a blank list.
- There's no `.catch`, no loading state and no empty state ("No statements yet").
- `location.href = ...pdf` replaces the whole page with the error if the download fails (expired session, 404). An `<a href download>` or a `fetch` with an error toast handles this better.

**4. Accessibility.**
A `<div onclick>` can't be focused or activated with the keyboard, and screen readers don't announce it as a control. Use a real `<a>` or `<button>`. The `#06c` link color on white passes contrast, but there's no focus or hover style. A list or table with proper semantics would also help.

## Should fix

- **Formatting:** `s.total` is shown raw. If it's cents or a bare number, you'll see `12900` instead of `$129.00`. Use `Intl.NumberFormat` with the account's currency. `s.month` probably needs `Intl.DateTimeFormat` too.
- **Scale:** There's no pagination or "load more." That's fine for 12 rows but not for years of history.
- **CSP:** Inline `onclick` and inline `<script>` will break if you ever add a Content-Security-Policy, which is common for billing pages.
- **Layout:** The `.row` has no responsive handling, and the download target is small on mobile.
- **Tests:** Cover empty, error, and long or odd values (a month string containing `<`, for example).

## Safer version

```html
<ul class="stmts" id="stmts" aria-live="polite"><li>Loading…</li></ul>
<style>
.row{display:flex;justify-content:space-between;padding:8px}
.dl{color:#06c}
.dl:hover{text-decoration:underline}
.dl:focus-visible{outline:2px solid #06c;outline-offset:2px}
</style>
<script>
const box = document.getElementById('stmts');
const money = new Intl.NumberFormat(undefined, {style:'currency', currency:'USD'});

fetch('/api/statements')
  .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
  .then(list => {
    box.replaceChildren();
    if (!list.length) { box.innerHTML = '<li>No statements yet.</li>'; return; }
    for (const s of list) {
      const li = document.createElement('li');
      li.className = 'row';
      const month = document.createElement('span');
      month.textContent = s.month;
      const total = document.createElement('span');
      total.textContent = money.format(s.total); // adjust if total is in cents
      const a = document.createElement('a');
      a.className = 'dl';
      a.textContent = 'Download';
      a.href = '/api/statements/' + encodeURIComponent(s.id) + '.pdf';
      a.setAttribute('download', '');
      a.setAttribute('aria-label', `Download ${s.month} statement`);
      li.append(month, total, a);
      box.append(li);
    }
  })
  .catch(() => { box.innerHTML = '<li role="alert">Couldn’t load statements. Please try again.</li>'; });
</script>
```

Add `list-style:none;padding:0` to the `ul` if you don't want bullets.

If you can share the backend handler for the PDF route, I can check item 2 too. It's the one most likely to cause a real incident.
