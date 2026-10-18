**What already works:** the happy path renders, the link color (#06c on white, about 5.7:1) passes contrast, and the layout is simple enough to survive narrow widths.

**Findings, ranked by harm:**

1. **Silent failure (blocks the page).** No `.catch`, no `r.ok` check. If `/api/statements` fails or returns an error page, the user sees a blank box. Fix: a loading state, an error message with Try again, and an empty state. Code below.

2. **Download is not keyboard-accessible or named (excludes people).** A `div` with `onclick` can't take focus or be activated with Enter, and three "Download" links are indistinguishable to screen readers. Fix: a real `<a href>` with an `aria-label` naming the month.

3. **HTML injection and broken quoting (security).** `innerHTML` with `s.month`, `s.total`, and `s.id` runs whatever the API returns as markup, and an id containing a quote breaks the `onclick`. Fix: build nodes with `textContent` and no inline handlers.

4. **Layout and tap targets (degrades).** The 8px padding gives the Download target roughly 20px of height, well under the 44px touch minimum, and long values don't wrap on narrow screens. Fix: `min-height` on the link, `flex-wrap`, and `gap`.

5. **Money format (check).** `s.total` is shown raw. If the API sends `1234.5` instead of a formatted currency string, it will read wrong. I can't tell the currency or locale from here, so confirm the API returns a formatted value, or format it with `Intl.NumberFormat` using the right currency.

6. **Session expiry (unknown).** A 401 currently shows as a failure. Confirm whether the app expects a redirect to sign-in for that case.

**Changed code** (same structure and class names, no new theme):

```html
<div class="stmts" id="stmts" aria-live="polite" aria-busy="true"></div>
<style>
.row{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:8px;flex-wrap:wrap}
.dl{color:#06c;text-decoration:underline;min-height:44px;display:inline-flex;align-items:center}
.msg{padding:8px}
</style>
<script>
const box = document.getElementById('stmts');

function showMessage(text, retry) {
  const p = document.createElement('p');
  p.className = 'msg';
  p.textContent = text;
  box.replaceChildren(p);
  if (retry) {
    const b = document.createElement('button');
    b.type = 'button';
    b.textContent = 'Try again';
    b.onclick = load;
    box.append(b);
  }
}

function row(s) {
  const div = document.createElement('div');
  div.className = 'row';
  const month = document.createElement('span');
  month.textContent = s.month;
  const total = document.createElement('span');
  total.textContent = s.total;
  const a = document.createElement('a');
  a.className = 'dl';
  a.href = '/api/statements/' + encodeURIComponent(s.id) + '.pdf';
  a.textContent = 'Download';
  a.setAttribute('aria-label', 'Download statement for ' + s.month);
  div.append(month, total, a);
  return div;
}

function load() {
  box.setAttribute('aria-busy', 'true');
  showMessage('Loading statements…');
  fetch('/api/statements')
    .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(list => {
      box.setAttribute('aria-busy', 'false');
      if (!list.length) return showMessage('No statements yet.');
      box.replaceChildren(...list.map(row));
    })
    .catch(() => {
      box.setAttribute('aria-busy', 'false');
      showMessage("We couldn't load your statements. Check your connection and try again.", true);
    });
}

load();
</script>
```

**Notes:**
- The empty-state and error copy are my wording. Adjust it to match the product's tone.
- The PDF link navigates in the current tab, so a failed download leaves the billing page. Opening it in a new tab, or handling errors on the PDF endpoint, is worth considering.
- I haven't run this against your API, and I haven't tested it with a screen reader or on a real device.
