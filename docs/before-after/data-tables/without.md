Your spec is mostly fine, but a few things are worth checking:

**Likely problems**

1. **Header semantics.** If the header is just bold text in a styled row rather than `<th>` elements (ideally in `<thead>` with `scope="col"`), screen readers won't treat it as a header. Check the markup.
[...]
3. **Default values need monospace.** Values like `true`, `30s`, `""` or `null` are easy to misread in proportional text. Empty strings and whitespace are especially ambiguous. Consider `<code>` styling for both Setting and Default.

**Worth checking**

4. **Border collapse.** A "thin bottom border on each row" only renders properly on `<tr>` if you use `border-collapse: collapse`. Otherwise the border may not show, or it may show with gaps between cells. Put the border on `td`/`th` if in doubt.
5. **Last row border.** The last row's border can double up with the table's own bottom edge or container border. Remove it if so.
[...]
8. **Setting column wrapping.** Long setting names like `max_connection_pool_size` can wrap awkwardly. Use `white-space: nowrap` on that column, or `overflow-wrap: anywhere` if you expect very long names.

**Not a problem**

- Left alignment, 14px text, and the padding are all reasonable. Left alignment is correct for text columns. If a Default column is purely numeric, you could right-align it, but mixed values mean left is better.
