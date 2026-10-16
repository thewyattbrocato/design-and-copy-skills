It's solid and ready to ship. It's a sensible system-font stack with no webfont cost, and `tabular-nums` on the tide table is the right call. I'd make a few small changes.

1. **Heading coverage:** `h1, h2, h3` skips `h4`–`h6`, so any of those in an article will render in the serif body font and look inconsistent. Use `h1, h2, h3, h4, h5, h6`, or switch to `:is(h1,h2,h3,h4,h5,h6)`.

2. **Serif fallback:** Charter ships on macOS and iOS, Sitka and Cambria cover Windows, and Android falls through to generic `serif`. That works, but adding `Georgia` before `serif` gives a more predictable result on Linux and Android.

3. **Sans stack:** `-apple-system` after `system-ui` is redundant on current browsers. It's harmless, so keep it only if you want to support older Safari.

4. **Numerals in body text:** Articles will mention tide heights and times inline. Some serif fonts default to old-style figures, which look odd next to table data. Add `font-variant-numeric: lining-nums;` to `body` to keep them consistent.

5. **Not in the snippet, but worth checking:**
   - Give `body` a `line-height` of about 1.55–1.65 and constrain the article column to about `65ch`. Charter looks good with that spacing.
   - Right-align the numeric columns in `.tide-table`, so the tabular figures line up.

The first item is the only likely bug. The rest are polish.
