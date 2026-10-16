**Skeleton rows.**

- **Known shape.** You always load 40 rows of a table-like layout, so skeletons can match the real structure. The page looks mostly built from the first frame, and the data fills in.
- **1–2 seconds is long enough to need structure.** A spinner gives no sense of what's coming or how much. Skeletons make the wait feel shorter and keep it from feeling stalled.
- **No layout shift.** If the skeleton rows match the real row height and column widths, nothing jumps when the data arrives. A spinner on an empty page followed by 40 rows causes a big reflow.
- **Spinners fit other cases.** They suit unknown-shape content, short waits (under about 1s), or actions like a button submit. Neither applies here.

Two details to get right:
- Delay the skeleton by about 150–200ms. Fast responses then won't flash it.
- Use a subtle shimmer or pulse, and respect `prefers-reduced-motion`.

For refetches such as filtering, sorting, or pagination, keep the old rows visible with a subtle loading indicator instead of going back to skeletons. Use skeletons for the initial load only.
