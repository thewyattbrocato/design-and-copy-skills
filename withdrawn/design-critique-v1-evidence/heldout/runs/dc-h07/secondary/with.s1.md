**Go with B**, and borrow one thing from A.

Dispatchers spend their day on one task: finding and fixing late loads. B makes that the main surface. A sorted table puts the worst problem at the top, and filter chips let them narrow it to their lanes or depots. A makes them look at KPIs and a map first, and the map shows where trucks are, not which ones need a call.

What A gets wrong for this job:
- **Four big KPI tiles** take the most valuable vertical space on the screen for numbers that change slowly. Dispatchers already know roughly how the day is going.
- **The sidebar** costs width on a screen where the table needs it. A full-width table with long rows is easier to scan on 27 inches.
- **The map at two-thirds width** is the largest element on the screen, but geography is secondary to lateness. Most of that space will be empty roads.

What to take from A: a slim summary strip above the table (on-time %, late count, active trucks, avg dwell as one line of small numbers, not tiles). It gives the overview without the space cost.

Things to get right in B:
- **Losing map context** when the side panel is closed. Consider a small persistent map thumbnail, or keep the side panel open by default with the last-selected load.
- **Sorting by lateness** should show minutes late with a clear sign for at-risk loads that will become late, not only loads already late. The most useful alert is "will miss the window in 40 min."
- **Keyboard flow**: arrow keys to move between rows, Enter to open the panel, and a shortcut to act on a load (call driver, reassign, notify customer). Dispatchers on long shifts will reward this.
- **Density**: 27 inches can fit a lot of rows, so a compact row height and a few user-chosen columns will serve better than fixed wide spacing.
- **Late state colour**: use it sparingly so the top rows stand out, and don't rely on colour alone. Pair it with the minutes-late text.

I'd test B with two or three dispatchers using real data from a busy hour before committing. The main thing to check is whether they reach for the map when a load is late, and whether the panel makes that easy enough.
