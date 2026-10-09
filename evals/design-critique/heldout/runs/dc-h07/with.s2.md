**Go with B, with one change: keep a thin summary strip above the table.** The change is below.

The main task is chasing late loads. B makes that the whole screen. A makes it a secondary element.

**Why B wins for this task**
- **Lateness is the sort order.** In B the worst load is row one and the next action is one click away. In A the table sits under a map and four tiles. On a 27" monitor the table gets roughly the bottom third of the height, so a dispatcher sees only a handful of rows without scrolling. That is my rough estimate, not a measurement.
- **The KPI tiles take the most space and give the least.** Of the four, only "late loads" prompts action, and the table already shows that. On-time % and avg dwell time change slowly, so they don't need to be that big for someone who is on the screen all day. Active trucks is context.
- **The map is wrong as the default view.** A map shows where trucks are, not which ones are late. It takes two-thirds of the width to answer a question the table answers faster. Behind a row click, it appears when a dispatcher needs location for one load.
- **The sidebar costs width and does little.** If the dispatcher works from one screen all day, a permanent nav takes columns from the table. Use a collapsed icon rail or a top bar.
- **Filter chips fit the work.** "Late > 60 min", "Unassigned" and "At risk" are the questions a dispatcher asks repeatedly.

**Where B is weaker, and the fix**
1. **Losing the aggregates.** Add one compact line above the chips, for example "Late 14 · At risk 6 · On-time 91% · Active 212". It should be small, with only late loads emphasized. This keeps what's useful about A in about 40px of height.
2. **The map panel can slow comparison.** If the dispatcher clicks row after row, the panel should update in place and not close and reopen. Make it dockable, so hovering or arrow-keying through rows updates the map. On a 27" monitor you have room to leave it open at about 30% width.
3. **Sorting by lateness alone can bury "about to be late."** Consider a visible "at risk" band (ETA slipping, not yet late) so the sort isn't only about loads already late.

**Where A would win:** if dispatchers also act as supervisors who need a glanceable overview, or if geography drives decisions (rerouting nearby trucks). I'm assuming they don't, from what you described.

**How sure I am:** fairly. The task description supports it strongly, but I haven't seen real mockups or how your dispatchers work. The cheapest check is to give 3–5 dispatchers a list of 10 late loads and time how long each takes to find and act on the worst one in a quick prototype of each layout.

**Not checked:** visual design, density, color, and your real data volume. If you routinely have hundreds of active rows, table design (row height, sticky headers, column choice) matters more than the choice between A and B.
