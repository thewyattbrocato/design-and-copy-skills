**Use skeleton rows.**

- **The layout is known.** You're loading a table of 40 rows with a fixed column structure. Skeleton rows show where the data will go, so the page doesn't jump when results arrive.
- **1–2 seconds is long enough to notice.** A spinner over an empty area tells the user "something is happening." Skeleton rows also show the shape of the content, which makes the wait feel shorter.
- **It works with the rest of the table.** Column headers, filters, and pagination can render immediately, and only the body needs the placeholder.

Some details to get right:

- **Don't show the skeleton for the first ~200–300 ms.** If the response is fast, a flash of placeholders looks worse than a short blank.
- **Render only as many skeleton rows as fit the viewport** (roughly 8–12), not all 40. Fill in real rows as the data arrives.
- **Keep the skeleton's column widths close to the real content** so the swap doesn't shift the layout.
- **For accessibility,** set `aria-busy="true"` on the table while loading and announce "Loading tickets" once in a live region. Mark the skeleton rows `aria-hidden` so screen readers don't read them.
- **Respect `prefers-reduced-motion`** by turning off the shimmer animation, but keep the static placeholder blocks.

A spinner is still the right choice for small, in-place actions where the layout already exists, such as a refresh button, a filter that re-queries inside the table, or a "load more" at the bottom.

If 1–2 seconds is typical for this endpoint, the skeleton will help, but the bigger win is probably making the query faster (indexes, fewer joined columns, or a smaller payload). I haven't looked at the API or the page code, so I can't say which is the bottleneck. No changes made.
