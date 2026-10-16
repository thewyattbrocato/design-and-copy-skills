I'd push back on the hero stat plus bigger cards. Those take space from the one thing dispatchers need, which is seeing all 40 to 60 trucks at once. Making some cards bigger means fewer trucks fit, and the screen still feels crowded. The overwhelm probably comes from 60 identical rows competing equally for attention, not from the count alone.

**What I'd build instead**

1. **Split the trucks by where they are, not into a single list.** Trucks at a door and trucks in the yard are different jobs.
   - **Left: door grid.** Show every door as a fixed tile with the truck currently in it, its status, and its minutes. Doors don't move, so dispatchers learn where to look and stop searching.
   - **Right: yard queue.** Trucks that are arriving, waiting, or ready to leave, grouped into lanes by status. Each lane header shows its count, and rows sort by minutes on site, longest first.

2. **Replace the hero stat with a count strip.** A single thin row across the top: `Arriving 8 · Waiting 14 · Loading 12 · Unloading 9 · Ready 11`, plus one alert count, such as `⚠ 4 over 90 min`. A total is not useful to a dispatcher. The alert count is what they act on, so that's the one number to make big.

3. **Use color only for exceptions.** Five saturated status colors plus badges will read as noise. Keep status as a neutral label or a small icon. Save color for trucks over the dwell threshold, and maybe doors that have been idle too long. If everything is colored, nothing stands out.

4. **Keep the rows dense and fixed-height.** Use a single line per truck with tabular numerals so the minute counts line up. Dispatchers have to read a lot of rows, so 14 px or larger for truck ID and minutes is a reasonable floor. Truncate notes to one line, and let a hover or click show the full text.

5. **Stabilize the layout.** If rows reorder every time minutes tick up or a status changes, the screen will feel chaotic. Keep lanes and door positions fixed, update values in place, and briefly highlight only what changed.

**The honest constraint**

Sixty single-line rows at a readable size need roughly 900 to 1000 px of height. That fits a 1080p display, but barely, and not with much room for a header. If the rows get smaller to fit more, they'll be harder to read at arm's length. A large monitor or a wall display will do better than a laptop. Before you commit, load the screen with 60 realistic mock trucks on the actual hardware and check whether the top five exceptions jump out within a couple of seconds. If they don't, the fix is more contrast on exceptions, not more space for hero cards.

If you tell me the screen size and whether you have door-to-truck assignments in the data, I can sketch the exact grid and the sizes.
