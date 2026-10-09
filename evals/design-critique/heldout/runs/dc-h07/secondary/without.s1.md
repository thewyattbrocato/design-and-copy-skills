**Go with B**, with two changes: keep a slim header strip of KPIs, and don't hide the map entirely.

**Why B fits the job:**
- The work is triage: find the worst late load, act on it, move to the next. A table sorted by lateness puts the answer at the top of the screen, so the dispatcher's eyes don't have to search.
- Big KPI tiles across the top take a lot of vertical space on a 27" monitor and mostly repeat what the sorted table already shows. "Late loads" is just the length of the list.
- A sidebar is wasted width on a single-purpose screen. Dispatchers learn the screen and rarely navigate away from it.
- The click-to-open map matches the follow-up question for a late load, which is "where is this truck and what's around it?" That's a per-load question, so it belongs in a panel tied to the selected row.

**What I'd change:**
- **Replace the four tiles with a one-line KPI strip** (on-time %, active trucks, late count, avg dwell). It keeps the at-a-glance numbers without the height cost. Make "late count" clickable so it toggles the late filter.
- **Keep some fleet-level map view.** Hiding the map entirely loses the overall picture, like clusters of late trucks in one region or a weather problem on a corridor. Options: a collapsed mini-map in the header, or a map toggle that replaces the table on demand.
- **Use a slim icon rail or top nav** instead of a full sidebar if you need access to other screens.
- **Make the sort visible and reversible.** Show lateness as a signed value ("+42 min") and keep the sort direction obvious. Dispatchers should always know why a row is at the top.
- **Keep the selected row and panel in sync with keyboard navigation**, since they'll be working through the list all day.

**Test before committing:** run a quick task-based session with two or three dispatchers. Give them a scenario like "find the load most at risk and tell me where that truck is," and watch whether they ever want the map visible while scanning the list. If they do, that's the signal to make the map persistent or resizable rather than panel-on-click.
