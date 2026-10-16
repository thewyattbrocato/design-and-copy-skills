Nothing here is wrong on the happy path, but the page has no failure, waiting, or empty state, and the Download control can't be reached by keyboard. Ranked by harm:

1. **Silent failure (blocks billing).** If the request fails or returns a non-2xx status, nothing renders and the user gets no message. `r.json()` also throws on an HTML error page. Fix: show a loading line while fetching, check `r.ok`, and show a message with a retry button on failure.
2. **Download isn't operable by keyboard.** A `div` with `onclick` gets no focus, no role, and no Enter/Space handling. Fix: make it a real link, so it's focusable and works with the keyboard.
3. **Empty list shows a blank box.** A customer with no statements sees nothing. Fix: an empty message.
4. **Unescaped HTML and attribute injection.** `s.month`, `s.total`, and `s.id` go into `innerHTML` and an `onclick` string. Even if the API is trusted, a value with a quote or `<` breaks the page. Fix: build the nodes with `textContent` and encode the id in the URL.
5. **Repeated "Download" links have no distinct names.** Screen reader users hear a list of identical links. Fix: `aria-label` naming the month.
6. **No visible focus style and no wrapping.** The inline styles don't set a focus ring, and a long total or month can overflow a narrow screen. Fix: a `:focus-visible` ring and `flex-wrap`-safe spacing.

Changed pieces (same IDs, classes, and blue link color):

```html
<div class="stmts" id="stmts" aria-live="polite"></div>
<style>
.row{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:8px;overflow-wrap:anywhere}
.dl{color:#06c;cursor:pointer}
.dl:focus-visible{outline:2px solid #06c;outline-offset:2px}
.msg{padding:8px}
</style>
<script>
const box = document.getElementById('stmts');

function message(text, retry) {
  box.replaceChildren();
  const p = document.createElement('p');
  p.className = 'msg';
  p.textContent = text;
  box.append(p);
  if (retry) {
    const btn = document.createElement('button');
    btn.textContent = 'Try again';
    btn.onclick = load;
    box.append(btn);
  }
}

function load() {
  message('Loading statements…');
  fetch('/api/statements')
    .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(list => {
      if (!list.length) return message('No statements yet.');
      box.replaceChildren(...list.map(row));
    })
    .catch(() => message("We couldn't load your statements.", true));
}

function row(s) {
  const div = document.createElement('div');
  div.className = 'row';
  const month = document.createElement('span');
  month.textContent = s.month;
  const total = document.createElement('span');
  total.textContent = s.total;
  const link = document.createElement('a');
  link.className = 'dl';
  link.href = '/api/statements/' + encodeURIComponent(s.id) + '.pdf';
  link.download = '';
  link.textContent = 'Download';
  link.setAttribute('aria-label', 'Download statement for ' + s.month);
  div.append(month, total, link);
  return div;
}

load();
</script>
```

Open items:
- **Total formatting:** I left `s.total` as-is. If the API returns a raw number, it needs currency formatting, and I need the currency and locale to do that without guessing.
- **Not checked:** I haven't run this against the real API, a failing endpoint, or a screen reader, and I didn't test 200% zoom or a 320px width. Also confirm the backend returns 401 (not a redirect to HTML) when the session expires, since the retry path assumes it.
