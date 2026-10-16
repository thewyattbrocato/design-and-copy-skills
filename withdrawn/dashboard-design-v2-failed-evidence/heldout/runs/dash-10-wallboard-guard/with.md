The layout works, so leave it alone. A fixed row order, stable positions, a dense top strip and a table of 12 queues are what supervisors need on a wall board. The "cleaner" version probably failed because it moved things or hid them. These are the changes I'd make, most important first.

1. **Make "longest wait" one format.** Showing 2:14 in some rows and 134s in others is the one real defect. A supervisor scanning down that column has to convert in their head, and 134s next to 2:14 reads as a much shorter wait than it is. Convert the two older-system queues to m:ss in the display layer, so 134s becomes 2:14. It doesn't touch the layout, and it's the only change I'd call necessary.

2. **Show when the data was last updated, and flag stale feeds.** I didn't hear that the board has this. Two queues come from an older system, so that feed is the likeliest to stall. A stalled feed would show frozen numbers that look normal, and the red thresholds would never fire. Add a small timestamp in a corner. Make it turn visibly different if any source is older than its refresh interval, and ideally mark the affected rows. This matters more than anything cosmetic.

3. **Add a small marker so red doesn't depend on color alone.** Red on "answered in target" and "away" is fine as an alert color. On a wall, from a distance, or for a colorblind supervisor, red can be missed. A bold weight, a "▼" or a thin outline on the red cell fixes that without changing the layout. Check that red isn't used for anything else on the board.

4. **Give "longest wait" an alert state.** You have red for answered-in-target and for away, but not for the measure that usually matters most to a caller. Only do this if the team already has a wait limit. I won't suggest a number. If there's no limit, leave it as it is.

5. **Check that the red thresholds are rare enough.** If "answered in target" is red on a quarter or more of the rows most days, or "away" is over 6 most of the afternoon, people stop reacting. In that case the 80% and 6 values need re-basing, not the supervisors. A fixed 6 also ignores staffing levels. If a queue with 8 staffed and one with 40 staffed both use it, that's worth a look. I can't judge either from a description, so check a week of history.

6. **Make sure the sparklines share a scale.** If each one scales itself, a queue that wobbles between 0 and 2 looks as dramatic as one that goes from 5 to 40. Use one shared y-range, or a fixed range for all 12, so they compare across rows. If they already do this, ignore this item.

Two things I'd leave alone even though a design review might flag them. The fixed row order is correct, because supervisors build position memory from it. The monospace strip of eight numbers is also fine, as long as each number has a label they can read from where they sit.

I haven't seen the board itself, only your description, so these are conclusions from the description. A screenshot would let me check item 3 (contrast at a distance) and item 6 (sparkline scales).
