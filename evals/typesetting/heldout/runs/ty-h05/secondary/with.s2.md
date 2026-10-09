**Ship B.** It's the only one that keeps the columns aligned and the lines intact.

- **A** uses a proportional font, so timing columns won't line up. `white-space: normal` also collapses the indentation in stack traces, and `60ch` would wrap 150–200 character lines into 3–4 fragments each.
- **C** keeps the monospace font, but `max-width: 60ch` with `pre-wrap` still breaks alignment. Every wrapped continuation starts at the left edge, so a long line's second half no longer lines up under the columns it belongs to, and the stack trace indentation gets mangled.
- **B** keeps each log line on one row, so columns stay aligned and indentation is preserved. The cost is horizontal scrolling for lines over the pane width, which is what GitHub Actions and most CI log viewers do. At 13px monospace, a 200-character line is about 1,500px wide, so developers will scroll on narrow panes. That's the trade-off, and it's the right one for logs.

Two small additions to B:

```css
.log { font: 13px/1.45 ui-monospace, Menlo, Consolas, monospace; white-space: pre; overflow-x: auto; tab-size: 4; }
```

- `tab-size: 4` keeps any tabs in tool output from rendering at the browser default of 8.
- If you want the blog's look, change the page chrome around the log, not the log text. The log body should stay monospace.
