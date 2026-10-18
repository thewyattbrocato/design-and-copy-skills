Your happy path works, but there are a few things to fix before Thursday. They're ranked by harm.

**1. The Download control is a `<div onclick>`.**
- Keyboard and screen-reader users can't reach it. It has no focus stop, no link role, and every row just says "Download".
- Use a real link with a name that includes the month.

**2. The markup is built from API strings with `innerHTML`.**
- `s.month`, `s.total` and `s.id` go straight into HTML and into an inline `onclick` string.
- A stray quote or `<` in any of them breaks the row. If any value is user-influenced, it's an injection hole.
- Build the nodes with the DOM API and `encodeURIComponent` the id.

**3. Failure, waiting and empty states are missing.**
- A failed request, a non-2xx response, a slow network or an empty list all leave a blank area with no explanation.
- The fix adds a loading line, an error with Retry, and an empty message.

**4. Smaller issues**
- There's no focus ring on the link.
- Rows don't wrap on a 320px screen or with large text.
- `s.total` is shown raw. Format it as currency if the API returns a number. I don't know your currency field, so I left it as is.

Same look, with the fixes applied:

```html
<div class="stmts" id="stmts" aria-busy="true">Loading statements…</div>
<style>
.row{display:flex;justify-content:space-between;gap:8px 16px;flex-wrap:wrap;padding:8px}
.dl{color:#06c}
.dl:focus-visible{outline:2px solid #06c;outline-offset:2px}
</style>
<script>
const box = document.getElementById('stmts');

function load() {
  box.setAttribute('aria-busy', 'true');
  box.textContent = 'Loading statements…';
  fetch('/api/statements')
    .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(list => {
      box.removeAttribute('aria-busy');
      if (!list.length) {
        box.textContent = 'No statements yet. They will appear here once one is available.';
        return;
      }
      box.replaceChildren(...list.map(s => {
        const row = document.createElement('div');
        row.className = 'row';
        const month = document.createElement('span');
        month.textContent = s.month;
        const total = document.createElement('span');
        total.textContent = s.total;
        const a = document.createElement('a');
        a.className = 'dl';
        a.href = '/api/statements/' + encodeURIComponent(s.id) + '.pdf';
        a.textContent = 'Download';
        a.setAttribute('aria-label', 'Download ' + s.month + ' statement');
        row.append(month, total, a);
        return row;
      }));
    })
    .catch(() => {
      box.removeAttribute('aria-busy');
      const msg = document.createElement('p');
      msg.setAttribute('role', 'alert');
      msg.textContent = 'We couldn’t load your statements. Check your connection and try again.';
      const retry = document.createElement('button');
      retry.type = 'button';
      retry.textContent = 'Retry';
      retry.onclick = load;
      box.replaceChildren(msg, retry);
      retry.focus();
    });
}
load();
</script>
```

- **Still your call:** what a failed PDF download should do. A link to `/api/statements/<id>.pdf` that returns a 401 or 500 will navigate the user to a raw error page. If you can, have the endpoint return `Content-Disposition: attachment`, or fetch the PDF and show an inline error on failure.
- **Not checked:** I only read the code. I haven't run it, tested it with a screen reader, or checked it against your real API responses.
