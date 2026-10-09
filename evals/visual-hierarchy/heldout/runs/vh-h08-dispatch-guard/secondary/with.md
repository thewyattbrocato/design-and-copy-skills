I'd push back on the hero stat and the big cards. With 40 to 60 trucks that must all stay visible, anything that takes space from the grid makes the tiles smaller, and making some cards bigger means others get smaller. Size is also a poor signal here, because "most important" changes every few minutes. When a card jumps in size, dispatchers lose the position they were relying on.

**What I'd do instead**

1. **Keep a thin summary strip, not a hero.** One line across the top: `On site 47 · Arriving 6 · Waiting 12 · Loading 9 · Unloading 8 · Ready 12 · Longest wait 94 min`. Counts are useful for a glance, but a big number takes space that the trucks need.

2. **Group by status as lanes, not a flat grid.** Five columns (Arriving, Waiting, Loading, Unloading, Ready to leave), each holding its trucks as compact tiles. Dispatchers can scan a lane instead of reading 60 rows, and the lane header shows the count. The lane order follows the workflow, so the eye moves left to right through the yard. If the yard is organized around fixed doors, you could group by dock door instead, or put a door grid on top of the lanes. Ask the dispatchers which one matches how they think.

3. **Sort inside each lane by minutes on site, longest first.** The most urgent truck in each lane is always at the top, and that gives you your "importance" without changing the sizes.

4. **Make the urgency visible with color and a border, not size.** A waiting truck over your threshold (say 60 min) gets an amber border, and over a second threshold gets red. Keep the color rules few and fixed, and use shape or an icon too, since some dispatchers may have color-vision problems and the wall display may be read at an angle.

5. **Make each tile readable at arm's length, with fixed fields.** Put the truck ID and dock door on the first line in the largest type, carrier and minutes on the second, and the note on the third, truncated to one line with a note icon if there's more. Every tile has the same fields in the same places, so the eye learns the pattern.

**Rough math for a 1920×1080 screen:** with about 60 px for the summary strip, 5 lanes gives roughly 370 px per lane. Each tile can then be around 340×90 px, which fits about 9 tiles per lane vertically. That covers 45 trucks in the worst case, so you'd likely want to go to tiles of about 80 px or a second column in the busiest lane. Measure this against real counts before committing, especially since the peak could be 60 in one lane.

**Two things to check before finalizing**

- What's the screen size and viewing distance? A wall display read from 2 m needs much larger type than a desk monitor.
- Time a realistic task with dispatchers, such as "find the truck at door 14" or "which truck has been waiting longest," on both the old table and the new layout. That tells you whether the redesign actually helps, which matters more than how it looks.

If you share the door count, screen resolution, and typical peak truck count, I can work out exact tile dimensions and sketch the layout in code.
