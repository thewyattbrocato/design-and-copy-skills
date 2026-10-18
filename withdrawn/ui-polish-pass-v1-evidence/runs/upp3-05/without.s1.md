**Skeleton rows.**

- **The wait is long enough to notice.** At 1–2 seconds, a spinner gives no sense of what's coming, and the page feels empty. Skeletons show the table's structure right away, so the load feels shorter.
- **You know the shape.** It's a list of 40 rows with consistent columns. That's the case skeletons suit best. A spinner fits better when the result's layout is unknown or the action is brief and local.
- **No layout shift.** Skeleton rows hold the space the real rows will fill, so the header, filters, and pagination don't jump when data arrives. A centered spinner collapses and then pops into a full table.
- **Spinners flicker on fast loads.** If a response comes back in 300ms, a spinner flashes and vanishes. Skeletons are less jarring.

A few details help:

- Render about 8–10 skeleton rows, enough to fill the viewport. You don't need all 40.
- Match the real row's column widths and height.
- Use a gentle shimmer or pulse, and respect `prefers-reduced-motion`.
- Consider a short delay (about 150–200ms) before showing the skeleton, so very fast responses don't flash it.
- For refetches, such as sorting, filtering, or paging with data already on screen, keep the old rows visible and dim them or show a small inline spinner. Don't swap back to skeletons.
