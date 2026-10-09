This is mostly solid. A few things I'd change or check:

1. **Tide table alignment.** `tabular-nums` makes digits the same width, but it doesn't line up the columns. Right-align the numeric cells (`text-align: right`, or `end` for RTL safety) and add `white-space: nowrap` so times like `06:42` never wrap. Use `<th scope="col">` headers so screen readers announce the columns.

2. **Put `tabular-nums` only where numbers are columnar.** `.meta` is probably dates, bylines, and captions. Tabular figures there are harmless but make prose-like text look slightly gappy. If `.meta` is mostly prose, drop the `font-variant-numeric` line from it and keep it on `.tide-table`.

3. **Check the serif bold and italic faces.** Charter ships with bold and italic on macOS, but `Bitstream Charter` on Linux and `Sitka Text` on Windows may not have every weight. If articles use `<strong>` or `<em>` heavily, test on a Windows or Linux machine, or accept that the browser will synthesize them.

4. **Set body rhythm.** System serifs vary in x-height, and Cambria and Sitka look larger than Charter at the same size. Give the body an explicit `line-height` around 1.6 and a `max-width` around `65ch` so line length stays comfortable regardless of which face loads.

5. **Sans tables can look smaller than the serif body.** If the tide table sits next to serif prose, bump its size slightly (for example `font-size: 0.95em`) so the numbers don't look undersized.

6. **Small cleanup.** `-apple-system` and `system-ui` overlap on macOS. Keeping both is harmless, but `system-ui` alone is enough for current browsers if you want less noise.

The stack itself is fine: each family has a sensible generic fallback, the system fonts mean no web font loading or layout shift, and the serif/sans split matches a newsletter feel. I haven't rendered the page, so the Windows and Linux fallbacks are based on which fonts those systems usually ship, not on a test. A quick check in one non-Mac browser would confirm it.
