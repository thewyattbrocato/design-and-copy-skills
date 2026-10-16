**Skeleton rows.**

- **Layout stability:** You know the shape of the content (40 rows with a consistent structure), so skeletons reserve the space and nothing jumps when data arrives. A spinner leaves an empty area that suddenly fills.
- **Perceived speed:** At 1–2 seconds, skeletons feel faster because the user sees the page structure immediately and their eye is already in position to scan. A spinner at that duration feels like waiting, not progress.
- **Right duration range:** Spinners suit short, indeterminate actions (under about 1 second, or button-level actions) or cases where you can't predict the layout. A 1–2 second list load is the classic skeleton case.

A few details if you build them:
- Show maybe 8–10 skeleton rows, enough to fill the viewport, not all 40.
- Delay showing them by about 150–200 ms, so fast responses (cached or quick) don't flash a skeleton.
- Keep the animation subtle (a slow shimmer or pulse), and respect `prefers-reduced-motion`.
- Mark the container `aria-busy="true"` so screen readers know it's loading.

Use a spinner only for later refetches, such as filtering or paging, where you keep the old rows visible and want a small non-blocking indicator.
