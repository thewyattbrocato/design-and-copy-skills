Your spec is mostly fine, but a few things are worth checking:

**Likely problems**

1. **Header semantics.** If the header is just bold text in a styled row rather than `<th>` elements (ideally in `<thead>` with `scope="col"`), screen readers won't treat it as a header. Check the markup.
2. **Long "Meaning" text.** With left-aligned, three-column content, the Meaning column can wrap into narrow columns on small screens. Make sure the table has `overflow-x: auto` in a wrapper, or a sensible `min-width` on that column, so it doesn't squash or break the layout on mobile.
3. **Default values need monospace.** Values like `true`, `30s`, `""` or `null` are easy to misread in proportional text. Empty strings and whitespace are especially ambiguous. Consider `<code>` styling for both Setting and Default.

**Worth checking**

4. **Border collapse.** A "thin bottom border on each row" only renders properly on `<tr>` if you use `border-collapse: collapse`. Otherwise the border may not show, or it may show with gaps between cells. Put the border on `td`/`th` if in doubt.
5. **Last row border.** The last row's border can double up with the table's own bottom edge or container border. Remove it if so.
6. **Gray header contrast.** Light gray with bold dark text is usually fine, but verify it still passes contrast in dark mode, and that the gray is distinguishable from the page background.
7. **Row separation.** With 8px 12px padding and 14px text, rows are fairly tight. That's fine for 8 short rows, but if Meaning wraps to multiple lines, the thin borders alone may make rows hard to tell apart. Consider a slightly larger vertical padding or `vertical-align: top`.
8. **Setting column wrapping.** Long setting names like `max_connection_pool_size` can wrap awkwardly. Use `white-space: nowrap` on that column, or `overflow-wrap: anywhere` if you expect very long names.

**Not a problem**

- Left alignment, 14px text, and the padding are all reasonable. Left alignment is correct for text columns. If a Default column is purely numeric, you could right-align it, but mixed values mean left is better.

If you share the markup and CSS, I can check the specifics.
