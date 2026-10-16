**The proposal works against your constraint.** A hero stat and large cards take space that 40 to 60 trucks need. At 1080p, a 56px card per truck means about 3,000px of content, so the cards would have to scroll or hide trucks. Your dispatchers are right to refuse both. The hierarchy should come from position and a few loud exceptions, not from size.

**What I'd build instead:**

1. **A thin summary strip, not a hero.** One line of counts by status ("On site 52 · Waiting over 30 min 7 · Ready to leave 9"). It orients the eye without taking a block of the screen.

2. **Five status lanes as columns, left to right in process order:** Arriving → Waiting → Loading/Unloading → Ready to leave. Trucks sit in their lane as compact chips, so the status column is already grouped and nobody has to scan 60 rows to find the waiting ones. With 60 trucks across five lanes, that is about 12 per lane, which fits at roughly 56px per chip.

3. **Compact chips, one line plus a second line.** Line one: truck ID, dock door, minutes on site. Line two: carrier and the notes, truncated. Dispatchers can scan the ID and time without reading the rest.

4. **Make the exceptions loud, and nothing else.** Use one technique for the trucks that need action: a value and weight step for minutes over a threshold (e.g. waiting over 30 min), plus a status shape or icon so it survives grayscale. Everything else stays calm. Don't use a second emphasis for the same chip.

5. **Sort within each lane by urgency**, longest on site first. The top of each lane is where attention goes.

**Things to check before you commit:**
- **Lane overflow:** If one lane regularly holds 20 or more trucks, let that lane switch to a two- or three-column chip grid rather than making the lane taller.
- **Screen size:** I'm assuming a single large monitor at 1080p or larger. On a smaller display, the chip height has to shrink, and the second line may need to go.
- **Real status mix:** If the counts are heavily skewed (say, 40 of 60 are "unloading"), the lane widths should be uneven or the lanes should become a single list with status as a column. Check with a day's data.
