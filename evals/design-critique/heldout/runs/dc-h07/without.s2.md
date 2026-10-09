**Go with B, with a couple of borrowings from A.**

**Why B fits this job**
- **Their main task is triage.** Dispatchers spend most of the day chasing late deliveries. B's table sorted by lateness puts the next load to act on at the top. In A, the worst offenders are in a table squeezed under the map, so they have to hunt for them.
- **A's KPI tiles take up prime space for little return.** Four big tiles are glanceable, but a dispatcher who sits on the screen all day will stop seeing them. Two of the four (on-time % and avg dwell) are trend metrics that don't prompt action. Active trucks is context. Only late loads is actionable, and the table already shows it.
- **27 inches is a lot of width, and B uses it well.** A full-width table has room for the columns dispatchers need: carrier, driver, ETA vs. promised, delay minutes, last ping, and customer. A's two-thirds map with a table under it leaves the table short and cramped.
- **The map is a drill-down tool, not a monitoring tool.** The question that matters is usually "why is this load late and what do I do?", and the map helps once you've picked a load. Opening it on row click ties it to that load. An always-on map of every truck is mostly visual noise.
- **No sidebar gives you more room.** If the app only has a few top-level areas, a slim top bar or icon rail is enough.

**What to borrow from A**
1. **A compact summary strip above the chips.** Make it one line of small numbers (late loads, on-time %, active trucks), not four big tiles. Make "late loads" clickable so it applies the filter.
2. **Keep the map in view while a row is selected.** Arrow keys should move through rows and update the panel, so a dispatcher can work down the list without closing and reopening it.
3. **Add a toggle for a split view.** Some dispatchers, especially for regional or geographic problems like weather or a closed road, will want a persistent map. A "table / split" switch covers them without making it the default.

**Risks to design for in B**
- **Hidden spatial context.** If a storm hits a region, a table won't show that six late trucks are clustered. A "group by region" option or a cluster indicator helps.
- **Chip sprawl.** Keep the chips to a few high-value filters (late, at risk, by carrier, by region) and make them saved views.
- **Row density.** Use a compact row height and a clear lateness color or bar so severity scans quickly. Don't rely on color alone.
- **Live re-sorting.** If the list re-sorts while someone is reading it, rows jump. Freeze the order while a row is selected or the pointer is over the table, and show a "new updates" prompt.

I'm assuming dispatchers mostly work one load at a time. If your research shows they mainly monitor the whole fleet geographically, A's map-forward layout becomes more attractive. A quick test with 3 or 4 dispatchers on a "find and resolve the worst late load" task would settle it.
