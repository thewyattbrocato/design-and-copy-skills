**Go with B.** It's built around the task you described: finding the late loads and acting on them. This is a judgment from your description. I haven't seen mockups or tested either with dispatchers.

**Why B wins for this task**
- **The first thing on screen is the work.** Sorting by lateness puts the worst load at the top of the table. In A, the table sits under the map and below the KPI row. Its first rows start far down the screen, and they aren't ordered by urgency unless you add that.
- **A's KPI tiles use prime space on information that doesn't prompt action.** On-time % and avg dwell time are summary numbers. A dispatcher who watches the screen all day will stop reading them within a day or two. "Late loads" is the only tile tied to the job, and the table already shows it.
- **A spends two-thirds of the width on the map.** The map answers "where is it", which a dispatcher needs for one load at a time. B keeps the map one click from a selected row, so the map always matches the load being worked.
- **The sidebar costs width on every screen, and it earns little.** A dispatcher works on this one screen. Nav can be a slim top bar or a collapsible rail.
- **The table suits 27 inches.** A full-width table shows many rows and columns at once: ETA delta, carrier, driver, last ping, dwell, and next stop. You can see more loads without scrolling.

**What to keep from A**
- **A compact summary strip.** Make it one line of small counts, such as late loads and on-time %, above the chips. Don't use four big tiles. Late-load count is useful as a live indicator, and the chips can double as it (for example, "Late 14").
- **A map you can see without a click.** B's weak point is that the map only appears after you select a row. Dispatchers who need to see clustered delays, like a storm or a closed road, can't see them. Cover this with a map toggle, or a persistent narrow map that docks beside the table.

**Risks to fix in B**
1. **Row-click-to-map is slow if repeated hundreds of times a day.** Use keyboard up/down to move through rows with the panel following. Keep the panel open while selection changes, so the map doesn't open and close for each load.
2. **A pure sort by lateness can bury a load that is about to go late.** Add a "going late" group, such as loads whose ETA is within 30 minutes of the window. Otherwise dispatchers only learn about problems after they happen.
3. **The panel will cover part of the table.** On a 27-inch screen, use a docked panel that pushes the table over. Don't use an overlay.

**Cheapest test:** Give 3 to 5 dispatchers a real scenario, such as "three loads are about to miss their window, find and reroute them", on both layouts. Compare time to the first action and whether anyone asks for the map before they've opened it. If they keep asking for it, add the docked map.

**Not checked:** your real column set, how many active loads there are at peak, and whether dispatchers handle many loads or a few high-priority ones.
