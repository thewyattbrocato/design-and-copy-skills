**Go with B**, with a couple of borrowed pieces from A.

**Why B fits this job**
- Dispatchers spend their day chasing late loads. B's default view is the thing they act on: a list sorted by lateness, so the worst problem is always at the top. In A, late loads are a number in a tile, and the dispatcher still has to find the loads in the table below the map.
- A's KPI tiles are glanceable, but they're mostly static. Someone staring at the screen all day stops looking at them, and none of them is an action. They suit a supervisor more than a dispatcher.
- A's map takes two-thirds of the width, and the table underneath it gets squeezed. On a 27" monitor you'd see only a handful of rows at once. B's full-width table lets you show many more rows and columns (ETA, carrier, driver, dwell, next stop, contact), which is what you need when triaging.
- The sidebar costs width and helps little if the dispatcher lives on this one screen. Nav can be a slim top bar or a collapsible rail.
- Filter chips (Late >30 min, At risk, Unassigned, By region) match how dispatchers think about their queue.

**Where B is weaker, and the fixes**
1. **No ambient awareness.** Add a slim summary strip above the chips: late count, at-risk count, on-time %. Keep it to one line of small numbers, not four big tiles. Make each one clickable so it sets the matching filter.
2. **Map hidden until a click.** The map matters when a dispatcher is rerouting or judging how far a truck is from the dock. Let the side panel stay open while they arrow through rows, so the map follows the selection. On a 27" screen the panel can be wide enough to be useful. Consider a pinned option for people who want it always on.
3. **Row click is a heavy trigger.** Support keyboard navigation (up/down, Enter, Esc) so triage is fast, and keep the panel from covering the table's key columns.
4. **Live changes.** A table sorted by lateness reshuffles as ETAs update, which can move a row out from under the cursor. Freeze order while a row is selected or hovered, and flag new late loads instead of jumping them in.

**What would change my answer**
If dispatchers mostly make geographic decisions, such as reassigning the nearest truck or managing a yard, the map is the main tool and A's layout (or a map-first variant) is better. The same goes if the screen doubles as a wall display for a supervisor. Your description of the work, chasing late deliveries, points to a list-first workflow, so I'd still pick B.

A quick check is to watch two or three dispatchers for an hour and note how often they look at the map versus scan for the next late load. If it's the map less than a quarter of the time, B is right.
