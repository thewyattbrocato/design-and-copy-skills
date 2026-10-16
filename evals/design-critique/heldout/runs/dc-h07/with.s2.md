**Go with B, with one addition: keep a slim KPI strip above the table.** Fairly confident, based on the task you described. I haven't seen either design, only your descriptions.

**Why B wins for chasing late loads**
- **The task is a ranked worklist.** Sorting by lateness puts the next load to call about in row one. In A the table sits under the map and tiles, so it gets the least space of any element. A dispatcher scans it all day, so that placement is backwards.
- **A spends its prime space on things that rarely change a decision.** Four large tiles take a full-width band at the top. "Late loads" is the only one that points to action, and it only gives a count. Nothing in A says which loads are late. On-time % and avg dwell are shift-level numbers a dispatcher checks occasionally, not continuously.
- **The map in A is always on, but the question it answers is per load.** "Where is this truck?" only matters once a load is selected. Showing all trucks at once on a map is useful for spatial problems like rerouting or clustering. If your dispatchers do that a lot, it weakens B (see below).
- **B's click-to-open map is one click per load.** That's cheap compared with scanning a permanent map. The risk is that opening and closing the panel gets tedious on a 27-inch screen with plenty of room.
- **Dropping the sidebar frees width for table columns.** Those would be ETA, delay, carrier, customer, driver contact, and last ping. Dispatchers need those columns to decide who to call.

**What to fix in B**
1. **Make the side panel persistent and non-modal.** Keep it open as the selected row changes, and add up/down arrow navigation through rows. On a 27-inch screen the panel should sit beside the table and not cover it, so working through five late loads takes five keypresses, not ten clicks.
2. **Add a compact KPI strip (one line, not tiles) above the chips.** Make "late loads" clickable so it applies the late filter. That keeps the useful part of A at a fraction of the height.
3. **Make the lateness cue more than a sort order.** Show delay as a number ("+2h 40m") and use color together with text or an icon. Sorting alone won't show where "slightly late" turns into "customer will call".
4. **Save filter state.** Dispatchers will reuse the same two or three filters (their region, their accounts) all day, so remember them per user.

**When I'd change my answer**
If dispatchers mostly work spatially (rerouting, reassigning nearby trucks, watching clusters in weather), A's always-visible map matters more. That's the cheapest thing to check: watch two or three dispatchers for an hour and note how often they look at the map without a specific load in mind. If it's rare, B holds.

**Not checked:** table row density, column set, alert/notification needs, and whether dispatchers use multiple monitors.
