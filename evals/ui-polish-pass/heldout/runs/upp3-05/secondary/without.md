**Skeleton rows.**

- **You know the shape of the content.** 40 rows with known columns means a skeleton can match the final layout, so nothing jumps when the data arrives. A spinner gives no hint of what's coming.
- **1-2 seconds is long enough to notice.** Users will wait, but a blank area with a spinner feels slower than a page that already looks like a table.
- **It helps the user start scanning.** Column headers and row structure are visible immediately, so they can read the filters or orient themselves while the data loads.

To avoid flicker on fast responses, wait about 150-200ms before showing the skeleton, and keep it visible for a short minimum time once shown. Use a spinner instead for short actions inside an existing view, like saving or refreshing a single row, or when the content shape is unknown.
