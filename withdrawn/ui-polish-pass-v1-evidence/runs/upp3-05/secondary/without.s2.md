**Use skeleton rows.**

- **The shape is known.** You're loading a table of 40 rows, so placeholder rows show the user where content will appear and roughly how much of it there is. A spinner gives no hint of layout, and the list pops in and shifts when data arrives.
- **1 to 2 seconds is long enough to feel slow.** At that length, users want to see that the page is progressing, and skeletons do that better than a spinner centered on an empty area.
- **Less layout shift.** If the skeleton rows match the real row height, the page doesn't jump when the data lands.

Two details matter more than the choice itself:

1. **Delay the skeleton by about 150 to 200 ms.** If the response comes back quickly, a skeleton flashing for a few frames looks worse than nothing.
2. **Keep the rest of the page interactive while loading.** Headers, filters, and the page title should render immediately, so only the table body shows the placeholder.

A spinner is still fine if the table has a variable structure you can't predict, or if the list sits inside a small panel where skeleton rows would look cramped. For a full ticket list, skeleton rows are the better fit.

I haven't looked at your code, and I made no changes.
