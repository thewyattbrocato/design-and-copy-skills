**Skeleton rows.**

- **The layout is known.** You're loading 40 rows of a predictable shape. Skeletons reserve that space, so nothing jumps when the data arrives. A spinner gives you a blank area that then snaps to a full list.
- **1–2 seconds is long enough to notice.** In that range users want to see that something is coming and what it will look like. Skeletons make the wait feel shorter because the page already looks mostly built. A spinner is better for short or unpredictable waits, or for actions with no fixed shape, such as a button submit.
- **It matches how people use the page.** A ticket list is something people scan. Seeing the column structure right away lets them orient before the content fills in.

Some details to keep it working well:
- Show about 8–10 skeleton rows, not all 40. They only need to fill the viewport.
- Don't show anything for the first ~150–200 ms. Fast responses then skip the flash of skeleton.
- Use a gentle shimmer or no animation at all. Respect `prefers-reduced-motion`.
- Mark the container with `aria-busy="true"` and give screen readers a "Loading tickets" status message.

Use a spinner only for refetches where the old rows stay on screen, such as changing a filter or sorting. In that case, keep the stale rows visible and dim them slightly, with a small inline indicator.
