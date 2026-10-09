Keep the hero stat, but make it a slim strip, and don't make the trucks themselves bigger. The overwhelm comes from 40 to 60 items competing for attention at once. Size differences can't fix that, because enlarging some trucks shrinks the rest or pushes them off screen. Dispatchers need every truck visible and a fast way to find the few that need action.

**What I'd lay out:**

1. **Top strip (about 80–100px, not a hero).** Counts per status (Arriving, Waiting, Loading, Unloading, Ready to leave), plus the longest current wait and the number of trucks past your wait threshold. Big numbers are fine, but keep them in one row so they don't eat the vertical space the trucks need.

2. **Main area: status lanes as columns, with a fixed-height tile for each truck.** Put each status in its own column, stacked top to bottom. Each tile shows truck ID, carrier, dock door, and minutes on site, with notes as a short line that truncates. Lanes keep the dispatcher's question ("what's waiting?") answerable at a glance, and fixed tiles keep 60 trucks fitting on one screen.

3. **Encode urgency with position and a border or bar, not size.** Sort each lane by minutes on site, longest first, so the most urgent trucks sit at the top of each column. Add a thin color bar or border that changes when a truck crosses a threshold, such as waiting over 45 minutes or ready to leave with the door still occupied.

4. **Don't rely on color alone.** Pair color with a label, icon, or position. Yard lighting and color-vision differences make color-only signals unreliable.

**Rough math:** on a 1080p display, roughly 900px is usable for the grid. Around 60 tiles at about 70px each fits in 5 to 6 columns of 10 to 12 rows with room to spare. Check this against the actual monitors. Dispatchers often run wide, short screens.

**Alternatives worth weighing:**
- **Group by dock door instead of status** if dispatchers act mainly on doors. A door-grid map, with each door showing its current truck and time, may be easier to scan than lanes.
- **Use a dedicated "needs action" lane or header** for threshold breaches, which is closer to what you wanted from the "important trucks" cards without shrinking the rest of the board.

**What I'd validate before committing:** Run a real shift, or a recorded one, with two or three dispatchers on the lane layout versus the current table. Measure how long they take to find the longest-waiting truck and whether they miss anything. Their reaction to the cards idea should count for less than that test.

If you tell me the screen sizes, roughly how many doors there are, and what your wait thresholds are, I can work out exact tile sizes and column counts.
