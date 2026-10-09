**Go with B**, but keep two things from A.

**Why B fits this job:**
- The core task is triage: find the most late loads and act on them. Sorting by lateness puts the answer at the top of the screen. In A, the worst load could be anywhere in a table under a map.
- A map at two-thirds width is good for overview but poor for scanning. Dispatchers need to compare many loads at once, and a table does that far better.
- Clicking a row to open a side panel keeps the list in place. The dispatcher can work down the list without losing their place, which matters when they're handling a dozen late loads in a row.
- Full-width rows on a 27-inch screen give you room for more columns (ETA vs. promise, dwell time, next stop, driver contact) without cramming.
- Filter chips above the table are a fast way to narrow to "late," "at risk," or a specific lane or terminal.

**What to borrow from A:**
- **Keep the KPI numbers, but shrink them.** Four giant tiles eat vertical space on the screen where dispatchers spend the most time. Use a slim header strip with on-time %, late count, active trucks, and avg dwell as single numbers. Make the late count clickable so it applies the "late" filter. Tiles make sense for a manager dashboard, not for a live triage screen.
- **Replace the sidebar with a thin top nav or a collapsible icon rail.** Dispatchers mostly stay on one screen, so a full sidebar wastes horizontal space. Don't remove navigation entirely.

**Two risks to design for:**
- **Loss of geographic context.** Dispatchers often think in terms of where trucks are. Consider a small map toggle inside the side panel, or a "show on map" action that opens a larger map only when needed. Don't make the map the default view.
- **Side panel on a single row.** Make sure the panel updates when the dispatcher moves through rows with arrow keys. Keyboard navigation will matter a lot for people who sit on this screen all day.

If you can test only one thing, test B with real dispatchers. Ask them to find the three loads most at risk and fix one. That will show quickly whether the sort order and panel work for them.
