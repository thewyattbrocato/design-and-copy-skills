I'd skip both the hero stat and the bigger cards. With 40 to 60 trucks, no scrolling, and no hiding, every pixel of height is spoken for. A hero stat takes a big band for one number, and enlarged cards push other trucks off the screen. You'd need either scrolling or hiding, and the dispatchers have ruled out both. Make the screen calmer instead of making some trucks bigger.

## Layout (assuming a 1920×1080 wall or desktop display)

**1. Slim status strip across the top (~56px)**
- It has five segments: Arriving 8 · Waiting 14 · Loading 11 · Unloading 9 · Ready to leave 6.
- It acts as a legend and a count, so it takes the hero stat's place at a fraction of the space.
- Add one alert count, such as "5 over threshold", on the right.

**2. Main body: 3 columns of ~20 compact rows each**
- At about 44px per row, 20 rows is roughly 880px, which fits with room to spare. A single 60-row table would force rows under 18px, which is unreadable and is probably why the current table feels overwhelming.
- Each row reads left to right: **Door** (large, bold, since dispatchers think in doors) → Truck ID → Carrier → status chip → minutes on site → one-line note.
- The note is truncated to one line, with a small marker when a note exists. Full text shows on hover or tap. Every truck stays visible, and only the overflow of long note text is shortened.

**3. Group by status, not by one flat sort**
- Order the sections by workflow (waiting, loading, unloading, ready to leave, arriving) and sort by door number within each. A dispatcher can then find a truck by where it is in the process.
- Keep positions stable. If rows reshuffle every minute as the timers tick, the screen feels chaotic. Re-sort only when a status changes, and briefly highlight the row that moved.

**4. Use color for exceptions only**
- Most rows are neutral: grey text on a quiet background, with a small status chip.
- Minutes on site is the main alert signal. Past a threshold (set per status, since 90 minutes waiting is worse than 90 minutes loading), the row gets an amber then red left-edge bar and bold minutes.
- Normal trucks stay visually quiet, so the 5 trucks that need attention stand out among the 55 that don't. This does the job you wanted the bigger cards to do, without using up space.

**5. Readability for people watching all shift**
- Use a dark or low-glare theme with large type (at least 16–18px for body text, tabular numerals for minutes and doors).
- Don't rely on color alone. Pair it with the chip text and the edge bar.
- Avoid animation beyond the brief highlight when a row changes.

## Questions that would change this
- **Is there a spatial layout to the yard?** If dispatchers think "north side, doors 1–20", I'd swap the grouped columns for a door-map layout. Doors become fixed cells showing the truck inside, with a waiting list to the side.
- **What's the screen?** A shared wall display allows more density than a desk monitor at arm's length.
- **Do thresholds already exist?** If there are SLAs for dwell time per status, use them. If not, you'll need to set them with the dispatchers.

I can mock this up as an HTML prototype with realistic fake data (50 trucks) so you can check it against the real density. Want me to do that?
