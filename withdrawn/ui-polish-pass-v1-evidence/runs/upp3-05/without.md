**Skeleton rows.**

- **The wait is long enough to notice.** At 1–2 seconds, a spinner is a blank page with a small animation. Users have nothing to look at or orient to.
- **The layout is predictable.** You know it will be 40 rows with consistent columns. Skeletons show that structure up front, so the page doesn't jump when data arrives and users can see what's coming.
- **They feel faster.** Skeletons show progress toward a specific result, and users tend to judge a skeleton load as shorter than the same wait behind a spinner.
- **A spinner fits better for short or unpredictable waits.** That means actions under about a second, or content with no known shape, like a button submit or a modal. Neither applies to a list page.

Some details that help:
- Use roughly the number of rows that fit above the fold, not all 40.
- Match the real row height and column widths so nothing shifts on load.
- Use a subtle shimmer or pulse, and keep it slow.
- Keep the page header, filters, and table headers rendered for real, and skeleton only the rows.
- If the response comes back in under about 200ms, delay showing the skeleton slightly so it doesn't flash.
- For refetches such as filter or page changes, keep the old rows visible with a dimmed state or a thin progress bar instead of resetting to skeletons.
