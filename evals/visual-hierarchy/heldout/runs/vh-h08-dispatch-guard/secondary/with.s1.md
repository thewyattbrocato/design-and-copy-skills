**Short answer: I'd push back on the hero stat and big cards.** Your dispatchers need all 40 to 60 trucks visible at once, so every pixel given to a hero or large cards takes space from the trucks. The overwhelm probably comes from every row looking equally urgent, not from the row count. Fix the ranking and the grouping, and keep the density.

**What the screen is for:** "Which truck needs me next, and is any door stuck?"

**Ranking**
1. **Needs action now:** waiting past threshold, ready to leave but door still occupied, unloading or loading over time.
2. **Door state:** which doors are free, busy, or blocked.
3. **Everything else:** arriving and in-progress trucks.
4. **Meta:** clock, total on site, shift counts.

**Proposed layout**
- **Thin summary strip, not a hero (about 56 to 64px tall).** Counts per status and free doors, like "Waiting 14 · Over 60 min 5 · Doors free 3." Show numbers only, no filters that hide trucks.
- **Status lanes as columns:** Arriving | Waiting | At door (loading/unloading) | Ready to leave. Position tells the dispatcher the state before they read anything. Sort each lane by minutes on site, longest first, so the most urgent truck is always at the top.
- **One compact row per truck:** truck ID in primary weight, dock door as a chip, carrier in muted text, minutes in tabular numerals, notes truncated with the full text on hover or focus. Four lanes of about 15 rows each fit a 1080p screen with room to spare. Row height around 36 to 40px.
- **Emphasis used once:** only the minutes figure changes when it crosses the SLA threshold, with a color plus an icon or bold weight so it survives grayscale. Remove row borders, badges, and per-row icons. One divider rule per lane.

**Alternative worth considering:** a dock-door grid that mirrors the physical yard. Dispatchers who think in doors may prefer it. It works if doors are numbered and fairly fixed, but a truck waiting without a door has no obvious home, so the lanes are the safer default.

**Trade-off:** lanes make the status scannable at the cost of putting one truck's dock number and its lane in separate places, which the row chip handles.

**Next step:** I can build a static HTML prototype with about 60 realistic trucks and screenshot it at your dispatchers' resolution. That will show whether the rows fit and whether the urgent ones stand out. Do you know their monitor size and what the SLA threshold is?
