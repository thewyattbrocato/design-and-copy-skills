**Use skeleton rows.**

- **Layout is known.** The table has fixed columns and a known row shape, so skeleton rows show the page's structure while data loads. A spinner shows nothing about what's coming, and the table then pops in all at once.
- **1 to 2 seconds is long enough to notice.** Past about a second, users feel the wait, and a skeleton makes that wait feel shorter than a spinner in the same spot.
- **It avoids layout shift.** Skeleton rows match the real row height, so the page doesn't jump when data arrives.

Details that matter:

- **Render about the number of rows that fit on screen** (roughly 8 to 12), not 40. Matching the 40 adds no information.
- **Delay the skeleton by about 150 to 300 ms.** If the API is fast on a cached call, skeletons that flash for a frame look worse than nothing.
- **Keep the header, filters, and toolbar visible** and only skeleton the body.
- **Use a spinner only for a non-table action,** like a refetch after a filter change where the old rows can stay on screen with a subtle loading state.
