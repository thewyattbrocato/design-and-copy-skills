Here's what I'd fix before Thursday, most important first.

**1. Injection (XSS) via `innerHTML`**
You're interpolating API values straight into HTML. If `s.month`, `s.total`, or `s.id` ever contains markup or a quote, it executes. The `id` in the inline `onclick="download('${s.id}')"` is the riskiest spot, because a `'` breaks out of the string. Build the DOM with `textContent` and `addEventListener` instead:

```js
const root = document.getElementById('stmts');
root.replaceChildren(...list.map(s => {
  const row = document.createElement('div');
  row.className = 'row';
  const month = document.createElement('span'); month.textContent = s.month;
  const total = document.createElement('span'); total.textContent = s.total;
  const dl = document.createElement('a');
  dl.className = 'dl';
  dl.textContent = 'Download';
  dl.href = '/api/statements/' + encodeURIComponent(s.id) + '.pdf';
  dl.setAttribute('download', '');
  row.append(month, total, dl);
  return row;
}));
```

Using a real `<a href>` also removes the global `download` function, which can collide with other page scripts. It also gives you keyboard access and middle-click or "open in new tab" for free.

**2. Authorization on the server (can't be seen in this snippet)**
Check that `/api/statements` and `/api/statements/:id.pdf` verify the statement belongs to the logged-in user. Sequential or guessable IDs without an ownership check are a classic billing-page data leak. Test it by requesting another account's statement ID.

**3. Error and empty states**
- There's no `r.ok` check, so a 401, 500, or HTML error page ends in a silent failure or an unhandled JSON parse error. Add a `.catch` and show a "Couldn't load statements. Retry" message.
- Handle an empty list ("No statements yet").
- Add a loading state. Right now the page is blank until the fetch resolves.

**4. Accessibility**
- The download control is a `<div>` with a click handler, so it isn't focusable and screen readers don't announce it. The `<a>` above fixes that.
- `#06c` on white passes contrast, but add a visible `:focus-visible` style.
- Consider a list or table structure (`<ul>` or `<table>`) rather than anonymous divs, and an `aria-label` like "Download January 2026 statement".

**5. Data formatting**
- `s.total` is shown raw. If it's a number or cents, format it with `Intl.NumberFormat` and the right currency. Don't use float math on money.
- `s.month` should be formatted for the user's locale, and make sure the sort order is explicit (newest first) rather than relying on the API.

**6. Download behavior**
- Setting `location.href` to a failing endpoint navigates the user away to an error page. An `<a download>` or `target="_blank"` avoids that.
- Confirm the PDF response sends `Content-Disposition` and `Content-Type: application/pdf`. Check what happens when the session expires mid-download.

**7. Release hygiene**
- Test in a non-dev environment: auth cookies, CORS, and the relative `/api/...` path behind your real proxy or CDN.
- Make sure the statements endpoint isn't cached across users (`Cache-Control: private` or `no-store`).
- Check mobile layout. `.row` with `space-between` and no wrapping can overflow with long totals or on narrow screens.
- Add a basic test: render with fixture data, including a malicious string, an empty list, and a failed fetch.
- Consider a CSP that disallows inline handlers, as a backstop.

If you only have time for three things before Thursday, do #1, #2, and #3.
