**What's wrong:** the page has no order, so the one thing that matters most, a room that has left its range, looks like everything else.

- **Everything is the same weight.** Eight identical cards with 32 identical 28px numbers give the eye nothing to land on. Room 5's 61% is styled the same as a healthy 90%.
- **The alert is a color shift, the weakest signal available.** A slightly darker orange on a 28px bold number is a small value and hue change. It disappears in grayscale, in peripheral vision, and under a glance from across the room. Nothing about the card's shape or position changes.
- **The alert word is styled like metadata.** An 11px grey "alert" is the same treatment as the labels. The status is quieter than the labels it sits beside, which inverts the hierarchy.
- **No duration or target.** A reading that has been wrong for six hours looks identical to one that just crossed the line. The card doesn't show the target range either, so the viewer has to remember what "in range" means for each metric.
- **Decoration without a job.** The shadow and border make each card look finished, but they don't separate levels. That's why it reads as flat: the design is uniform, not calm.

**What to change first:** make out-of-range a structural change on the card, not a color change. For example:

- A thick left or top band in a strong status color, plus a bold status word in the card ("HUMIDITY HIGH · 6 h"). The status must still show in grayscale.
- Show the target range under each metric (e.g., "target 85–95%") so the number can be judged without memory.
- Sort out-of-range rooms to the top of the grid.

After that, add a one-line summary above the grid ("7 in range · 1 out of range: Room 5 humidity, 6 h") so the answer is visible before anyone scans the cards. Then remove the shadow, since it does no work.

Two notes: I haven't seen your code, so these are based on your description. I also don't know your target ranges, so the page needs them from you (or from your config) before the range display can be built.
