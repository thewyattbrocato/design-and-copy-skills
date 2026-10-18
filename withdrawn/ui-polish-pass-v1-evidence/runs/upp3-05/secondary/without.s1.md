**Use skeleton rows.**

- **The shape is known.** You're loading 40 rows of the same structure, so skeleton rows show the table's layout while data arrives. A spinner gives no hint of what's coming and can leave the page looking empty.
- **The wait is long enough to notice.** At 1 to 2 seconds, users feel the delay. Skeletons make the page look like it's already filling in, which usually feels faster than a spinner for the same wait.
- **It avoids layout shift.** When the real rows replace the placeholders, the table doesn't jump, as long as the skeleton row height matches the real row height.

Some implementation notes, in case you go this way later:

- Delay showing the skeleton by about 150 to 300 ms. If the API sometimes responds fast, this avoids a flash of placeholder content.
- Render a fixed count of skeleton rows (around 8 to 10 is typical) rather than 40. Forty placeholders can look like a long list that then shrinks.
- Mark the container with `aria-busy="true"` while loading, and announce the load state for screen readers.

A spinner would be the better choice if the table had no predictable shape, if the wait could run past about 10 seconds, or if you were loading the whole page rather than one section of it.
