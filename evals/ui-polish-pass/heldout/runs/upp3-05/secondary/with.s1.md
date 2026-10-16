**Skeleton rows.**

- **Layout stays put.** The table keeps its columns and row heights while loading, so the content doesn't jump when the data arrives.
- **Wait feels shorter.** At 1 to 2 seconds, users notice a blank or spinning area. Skeleton rows show the shape of what's coming, which makes the wait read as progress.
- **The shape is known.** You always load a table of the same columns, so the placeholder can match it closely. A spinner earns its place when the result's shape is unpredictable.

Practical details:

- Render about 8 to 12 skeleton rows, not 40. That fills the viewport without implying a fixed count.
- Add a short delay, around 150 to 300 ms, before showing skeletons. This avoids a flash when the response is fast or cached.
- Keep a spinner for secondary actions like refreshing or paging. Use a small inline indicator there, not a full-table placeholder.
