**Skeleton rows.**

- **Layout stability:** You know the shape of the content (40 rows, fixed columns), so skeletons reserve the exact space. Nothing jumps when data arrives, and a spinner followed by 40 rows causes a visible layout shift.
- **Perceived speed:** At 1–2 seconds, skeletons make the wait feel shorter because the page looks like it's already assembling. A spinner says "waiting" and gives no sense of progress.
- **Right duration for it:** Under about 300ms, neither is worth showing, and a flash of skeleton is worse than nothing. At 1–2s, a skeleton is the better choice. Spinners are better for indeterminate or longer waits, or for actions with no predictable layout (like a button submit).
- **Context:** The header, filters and column labels can stay rendered while only the rows are skeletons. Users can orient themselves, and some can start interacting with filters right away.

Two small tips: delay showing the skeleton by about 150–200ms so fast responses don't flash, and use a subtle pulse or shimmer, not a heavy animation. Keep the skeleton row height identical to real rows.
