This is solid and ready to ship. The stacks fall back sensibly, and there are no web fonts to load, so there's no FOUT or licensing to worry about. A few small things to consider:

1. **Sans-serif headings will vary by OS.** `system-ui` resolves to SF on macOS, Segoe UI on Windows, and whatever the distro uses on Linux. That's usually fine, but if you want the masthead to look identical everywhere, name one face explicitly (for example, Roboto or Inter as a web font) and keep the system stack as fallback.

2. **Tabular figures only apply where you've scoped them.** `.tide-table, .meta` is right. If the tide table has `<td>`s or `<th>`s with a class that isn't `.tide-table`, they won't pick it up. For the tide table itself, I'd also right-align numeric columns (`text-align: right`) so the decimals and times line up vertically. Tabular figures handle width; alignment handles position.

3. **The sans stack covers a lot of ground, so check the tide table on one Windows and one Linux machine.** Segoe UI and Roboto both have tabular figures, but some system fonts don't, and the column alignment can shift without warning. A quick visual check in each will catch it.

4. **Consider a `font-feature-settings` fallback.** `font-variant-numeric` is well supported now, so this is optional. But if you ever use a font that lacks the feature, the figures will silently go proportional.

5. **Minor: add `h4`–`h6` if they appear.** Right now they inherit the serif body. If you only use h1–h3 in the articles, leave it alone.

I haven't rendered the page, so the cross-platform points are from reading the CSS, not from looking at it.
