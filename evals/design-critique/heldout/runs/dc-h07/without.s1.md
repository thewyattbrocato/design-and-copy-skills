Go with **B**, with a few changes.

**Why B fits**
- Dispatchers spend most of their time chasing late loads, so the sorted-by-lateness table is their work queue. In A it's squeezed under the map and four large tiles, so they'd scroll or squint at the main thing they use.
- The KPI tiles in A are easy to glance at but hard to act on. "Late loads: 14" tells you a number, and then you have to find those 14 in the table. B's list puts the 14 on screen already sorted.
- On a 27-inch monitor, a full-width table can show many columns (carrier, driver, ETA vs. appointment, minutes late, last ping, next stop, and so on) without truncating. That's where the extra screen space helps most.
- Dropping the sidebar gives that width back. Dispatchers rarely switch sections, so a permanent nav isn't worth it.

**Where B is weaker, and the fixes**
1. **The map is hidden until you click.** Late deliveries often need spatial decisions, like which nearby truck can cover or whether a delay is a regional problem. Make the panel **dockable**, so it stays open and updates as the dispatcher moves through rows with the arrow keys. Keyboard row navigation matters a lot on an all-day screen.
2. **You lose the at-a-glance health numbers.** Put them in a slim one-line strip in the header (on-time %, active trucks, late loads, avg dwell), and make each one clickable to apply the matching filter. That keeps A's best idea at about a tenth of the space.
3. **Filter chips should carry counts**, such as "Late >60 min (7)", "At risk (12)" and "No ping >30 min (3)". They then work as both a summary and a control. Saved or sticky filters also help, since the same dispatcher will use the same view every day.
4. **You still need some navigation.** Use a top bar or a collapsed icon rail instead of a full sidebar.

**When I'd reconsider:** If your research shows dispatchers mostly make geographic decisions, like reassigning by proximity or rerouting around regional disruptions, A's always-visible map becomes more valuable. A docked-map version of B covers most of that case. I'd still put B in front of a few real dispatchers with a realistic late-load scenario before committing.
