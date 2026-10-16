Your code works on the happy path, but I'd fix these before Thursday. I only read the snippet, so I haven't checked the server side.

**Blockers**

1. **XSS and injection.**
   - `s.month`, `s.total` and `s.id` go straight into `innerHTML`, and `s.id` also goes into an inline `onclick` string. If any of those values can contain user-influenced text, such as a `'` or `<`, you get script injection on a billing page.
   - Build the DOM with `createElement` and `textContent`, or escape the values. Drop the inline handler.
   - Better still, make the download a real link: `<a href="/api/statements/${encodeURIComponent(id)}.pdf" download>`.
2. **Authorization on the PDF endpoint.** `/api/statements/<id>.pdf` must check that the statement belongs to the logged-in account. Otherwise anyone can enumerate IDs and download other customers' bills. The list endpoint needs the same check. This is the highest-risk item and it lives outside this snippet, so verify it.
3. **No error handling.**
   - `fetch` doesn't reject on 4xx or 5xx, so a 500 or an expired session (401) will hit `r.json()` and fail silently, leaving a blank page.
   - Check `r.ok`, add a `.catch`, and show an error message with a retry. Redirect to login on 401.

**Should fix**

4. **Accessibility.** A `<div onclick>` can't be focused or activated by keyboard and isn't announced as a control. Using an `<a>` or `<button>` fixes that. Add `:focus-visible` and hover styles.
5. **Loading and empty states.** Right now the page is blank while loading and blank when the user has no statements. Show "Loading…" and "No statements yet".
6. **Formatting.**
   - `s.total` is printed raw. Use `Intl.NumberFormat` with the currency, and be sure whether the API returns cents or dollars.
   - `s.month` should be formatted for the user's locale, not shown as a raw ISO string.
7. **PDF response headers.** Set `Content-Disposition: attachment; filename="statement-2026-09.pdf"` and `Cache-Control: private, no-store`. Otherwise shared caches can keep the billing PDFs.
8. **Failed downloads.** `location.href = …` navigates the page away to an error page if the PDF 404s. A plain `<a download>` link is a bit better, but you still need a decision on what the user sees when generation fails.

**Nice to have**

- Pagination or "show older" if accounts can have years of statements.
- Row layout on narrow screens, since three flex children with `space-between` may cramp on mobile.
- Move the script out of global scope if you adopt a CSP that blocks inline scripts.
- A test for the render function with hostile input (`"><img src=x onerror=alert(1)>`), plus a manual check that user A can't fetch user B's PDF.

If you'd like, I can rewrite the snippet with items 1, 3, 4, 5 and 6 done.
