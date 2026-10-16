The stack is sound. Charter on macOS, Cambria or Sitka on Windows, and a generic serif fallback covers every platform without web fonts, so there's no load flash to worry about. A few things I'd check or change:

1. **Right-align the numeric columns in the tide table.** `tabular-nums` only keeps digits aligned if the columns are right-aligned too. Add `text-align: right` to the numeric `td`/`th` cells, or to a class on them.

2. **Check the size balance between sans and serif.** system-ui fonts like SF and Segoe UI usually have a different x-height than Charter or Cambria, so the tide table and `.meta` can look smaller or larger than the body text. If that happens, nudge the sans size down a little (for example `font-size: 0.95em` on `.tide-table, .meta`), or use `font-size-adjust` where supported.

3. **Decide on h4–h6.** Your rules only cover h1–h3. If articles use deeper headings, they'll render in the serif body face. That may be what you want, but it's worth a deliberate choice.

4. **Consider a `monospace` fallback for the tide table** only if you want the times and heights to look like a printed almanac. `ui-monospace, Menlo, Consolas, monospace` with `tabular-nums` gives strict column alignment. It's a style choice, not a fix.

5. **Naming.** `--serif` and `--sans` are fine. `--font-serif` / `--font-sans` would match common conventions if the site grows.

Nothing here is blocking. Item 1 is the one most likely to show up as a visible bug in the tide table.
