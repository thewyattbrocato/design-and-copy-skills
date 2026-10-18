The list works on the happy path. The date and total layout is fine, and `#06c` on white has enough contrast. These are the gaps, ranked by harm:

1. **Download isn't keyboard accessible.** It's a `<div onclick>`, so it can't be tabbed to, has no focus ring, and isn't announced as a link. Every row also just says "Download", so a screen reader user can't tell the rows apart. Use a real `<a>` with a name that includes the month.
2. **A failed fetch leaves a blank page.** There's no `r.ok` check and no `.catch`, so a 500 or an offline user sees nothing. Show an error in words, with Retry.
3. **`innerHTML` with unescaped API values.** `s.month`, `s.total` and `s.id` go straight into markup and an inline `onclick`. A quote in an id breaks the handler, and a hostile value is script injection. Build the nodes with `textContent` instead.
4. **No loading or empty state.** The container is blank while the request runs, and blank again if there are zero statements.
5. **Raw `s.total` and `s.month`.** Whatever the API sends is shown as is, so `1234.5` would appear unformatted. I left this alone because I don't know your currency or the API's month format.

Changed code, with the same look and structure:

```html
<div class="stmts" id="stmts" aria-live="polite">Loading statements…</div>
<style>
.row{display:flex;justify-content:space-between;gap:12px;padding:8px}
.dl{color:#06c}
.dl:focus-visible{outline:2px solid #06c;outline-offset:2px}
.msg{padding:8px}
</style>
<script>
const box = document.getElementById('stmts');

function load() {
  box.textContent = 'Loading statements…';
  fetch('/api/statements')
    .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(render)
    .catch(showError);
}

function render(list) {
  box.textContent = '';
  if (!list.length) {
    box.append(msg('No statements yet.'));
    return;
  }
  list.forEach(s => {
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
    a.setAttribute('aria-label', 'Download statement for ' + s.month);
    row.append(month, total, a);
    box.append(row);
  });
}

function showError() {
  box.textContent = '';
  const p = msg("Couldn't load your statements. Check your connection and try again. ");
  const b = document.createElement('button');
  b.textContent = 'Retry';
  b.onclick = load;
  p.append(b);
  box.append(p);
}

function msg(text) {
  const p = document.createElement('p');
  p.className = 'msg';
  p.textContent = text;
  return p;
}

load();
</script>
```

The `download()` function is gone because the link replaces it.

- **Still open:** a download that fails (expired session, 404) will navigate the user to a raw error page. Fixing that properly means the PDF endpoint needs to return something friendly, or the download should go through `fetch` and a blob. That's a decision for you. The money and month formatting needs your currency and locale.
- **Not checked:** I haven't run this in a browser or tested it with a screen reader. I also haven't tried it at 320px width or with hundreds of statements.
