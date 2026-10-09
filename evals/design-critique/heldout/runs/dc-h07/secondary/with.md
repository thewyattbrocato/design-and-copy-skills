**Go with B.** Dispatchers spend their day on one question: which loads are late, and what do I do about them. B puts that list on screen at all times, sorted by lateness, so the most urgent work is always at the top.

A spends its prime real estate on things a dispatcher doesn't act on:

- **Four big KPI tiles** take a lot of vertical space and mostly restate information the sorted table already shows. Avg dwell time is a diagnostic, not something you act on mid-shift.
- **The sidebar** eats horizontal space on a 27-inch screen, and dispatchers rarely navigate between sections while working a queue.
- **The map at two-thirds width** gives the most space to the least-used element. The map matters when you're choosing a truck near a pickup, but that's a secondary task.

B's main risk is that the map is hidden until a row is clicked, so dispatchers lose the spatial overview. Fix that with a few changes:

1. **Replace the tiles with a slim summary strip** above the table: on-time %, late count, and active trucks as single-line stats. Keep the numbers, drop the tile chrome.
2. **Keep a small, always-visible map thumbnail or a toggle** so the geography is never fully gone. Clicking a row can still open the full side panel.
3. **Make the side panel non-blocking.** Dispatchers will click through many rows in a row, so the table should stay usable and the panel should update in place rather than fight for focus.
4. **Support multi-select and bulk actions** (reassign, notify customer). Chasing late loads usually means handling several at once.
5. **Make the lateness column readable at a glance:** signed minutes late, colour-coded, with the most overdue rows first.

Before committing, run a quick task test with two or three dispatchers on each layout. Ask them to find the five most late loads and reassign one. Time it and watch where they hesitate. That will settle the map question better than either of us guessing.
