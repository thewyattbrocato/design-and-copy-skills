**Go with B.** Dispatchers are triaging, not monitoring. The job is to find the worst late load and act on it, and B puts that answer at the top of the screen. The sorted table makes the most urgent delivery the first row, and the filter chips let them narrow to a lane, customer, or status without leaving the list.

A works against that job in three ways:

- **The KPI tiles take the most prominent space but don't drive action.** Knowing on-time % is 91% doesn't tell a dispatcher which truck to call. Once a dispatcher has seen the numbers once or twice, the tiles are just furniture.
- **The map gets two-thirds of the screen, but the table is the workhorse.** On A, the table sits under the map and is probably squeezed into the bottom third, so the list they actually work from ends up with less room than the map.
- **The sidebar costs horizontal space on a screen where a wide table is the main tool.** B's full-width table fits more columns (lane, ETA vs. promised, dwell, last ping, driver contact) without truncation.

Three things to carry over from A, and one risk to watch:

1. **Keep a slim KPI strip, not tiles.** One line of small text above the table ("On time 91% · 14 late · 2 trucks idle · dwell 42m") gives the same context at a fraction of the height. Make the late count clickable so it applies the "late" filter.
2. **Replace the sidebar with a top bar or a collapsed icon rail.** Dispatchers still need to reach other screens, but nav doesn't need permanent width.
3. **Make the side panel wide enough for the map to be useful.** A 27-inch screen can handle a panel around 40–50% of the width. A narrow panel makes the map a thumbnail, and then the map isn't really there. Also consider a small map of all late loads that stays visible or can be toggled, so dispatchers keep spatial context when several trucks are in the same area.

The risk is that the side panel hides the map until someone clicks a row, so dispatchers lose the big-picture view. If your research shows they regularly reason by geography (for example, "which trucks are near the Memphis terminal?"), the map needs to be visible by default, not opened on demand. That is the one place where A's layout would earn its space.

Before committing, I'd run a quick test with 3–5 real dispatchers: give each a prototype of both layouts and time how long it takes them to find and act on the three most-late loads. That will settle the geography question better than my guess.
