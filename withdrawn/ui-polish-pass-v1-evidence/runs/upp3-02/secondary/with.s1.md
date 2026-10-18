The basic fetch-and-render works, and the row layout is fine at desktop width. Four things need fixing before Thursday, ranked by harm:

1. **Silent failure.** A failed request or bad JSON leaves a blank box forever. There's no loading state, no error, and no empty state.
2. **Unescaped server data in `innerHTML`.** `s.month`, `s.total` and `s.id` are injected as markup. Build the nodes with `textContent` instead.
3. **"Download" is a `div` with `onclick`.** Keyboard users can't reach it, and it has no link semantics. Make it a real link, which also needs no JavaScript.
4. **Five identical "Download" links** give screen-reader users no way to tell them apart. Name each one with its month.

Also: the link needs an underline so it isn't identified by color alone, and the row should wrap at 320px.

```html
<div class="stmts" id="stmts" aria-live="polite">
  <p class="stmts-status">Loading statements…</p>
</div>
<style>
.row{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px;padding:8px}
.dl{color:#06c;text-decoration:underline}
.stmts-status{padding:8px}
</style>
<script>
const box = document.getElementById('stmts');

function showStatus(text, retry) {
  box.replaceChildren();
  const p = document.createElement('p');
  p.className = 'stmts-status';
  p.textContent = text;
  box.append(p);
  if (retry) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.textContent = 'Try again';
    btn.onclick = load;
    box.append(btn);
  }
}

function load() {
  showStatus('Loading statements…');
  fetch('/api/statements')
    .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(list => {
      if (!list.length) return showStatus('No statements yet.');
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
        a.setAttribute('aria-label', 'Download statement for ' + s.month);
        row.append(month, total, a);
        return row;
      }));
    })
    .catch(() => showStatus("Statements couldn't load.", true));
}
load();
</script>
```

Notes:
- The copy ("No statements yet.", "Statements couldn't load.") is my wording. Check it against your product voice, and confirm "No statements yet." is true for accounts that have none.
- `s.total` still renders raw. If the API returns cents or no currency symbol, format it before it reaches the page. I don't know your API's format.
- I checked this by reading the code only. I didn't run it in a browser, test the 320px layout, or test with a screen reader.
