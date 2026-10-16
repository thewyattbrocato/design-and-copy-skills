Your layout and styling are fine. The gaps are in the code around them, listed here by how much harm they do.

**1. Injection through `innerHTML` and the inline `onclick`.**
`s.month`, `s.total` and `s.id` go into markup unescaped. If any of them can contain a quote or `<`, that's script injection on a billing page. Build the rows with DOM calls instead.

**2. A failed load shows nothing.**
There's no `r.ok` check and no `.catch`, so a 401, a 500 or being offline leaves a blank page. There's also no loading state and no empty state for a new customer with no statements.

**3. "Download" is a `<div>`.**
Keyboard users can't focus or activate it, and screen readers don't announce it as a control. Every row also reads just "Download", so nobody can tell which statement it is. Use a real link with a name that includes the month.

**4. Raw `total` and `month` values.**
I can't tell what the API returns. If `total` is cents or an unformatted number, or `month` is an ISO date, users will see that raw. Format them for display.

Here are the changed pieces:

```html
<div class="stmts" id="stmts" aria-live="polite" aria-busy="true">Loading statements…</div>
<style>
.row{display:flex;justify-content:space-between;padding:8px;gap:12px}
.row span{overflow-wrap:anywhere}
.dl{color:#06c}
.dl:focus-visible{outline:2px solid #06c;outline-offset:2px}
.msg{padding:8px}
</style>
<script>
const box = document.getElementById('stmts');

function show(text, retry) {
  box.setAttribute('aria-busy', 'false');
  box.innerHTML = '';
  const p = document.createElement('p');
  p.className = 'msg';
  p.textContent = text;
  if (retry) {
    const b = document.createElement('button');
    b.textContent = 'Try again';
    b.onclick = load;
    p.append(' ', b);
  }
  box.append(p);
}

function load() {
  box.setAttribute('aria-busy', 'true');
  box.textContent = 'Loading statements…';
  fetch('/api/statements')
    .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(list => {
      if (!list.length) return show('No statements yet. Your first one will appear here after your first billing cycle.');
      box.innerHTML = '';
      list.forEach(s => {
        const row = document.createElement('div');
        row.className = 'row';
        const m = document.createElement('span'); m.textContent = s.month;
        const t = document.createElement('span'); t.textContent = s.total; // format currency here
        const a = document.createElement('a');
        a.className = 'dl';
        a.textContent = 'Download';
        a.href = '/api/statements/' + encodeURIComponent(s.id) + '.pdf';
        a.setAttribute('aria-label', `Download ${s.month} statement (PDF)`);
        row.append(m, t, a);
        box.append(row);
      });
      box.setAttribute('aria-busy', 'false');
    })
    .catch(() => show("We couldn't load your statements. Check your connection and try again.", true));
}
load();
</script>
```

The link navigates the same way `location.href` did, so the server's `Content-Disposition` header still decides whether the PDF downloads or opens inline. A link also means a failed PDF request at least lands on a normal page.

**Decisions for you:**
- Currency and date formatting depends on what the API returns, so I left a marker comment on `total`. I didn't guess a format.
- Check what `/api/statements/:id.pdf` returns for an expired session or someone else's statement ID. That authorization check has to happen on the server.
- If users could have hundreds of statements, you'll want pagination or a "show older" control.

**Not checked:** I haven't run any of this in a browser or with a screen reader. I also haven't tested narrow widths or the real API's error responses.
