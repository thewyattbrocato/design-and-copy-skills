**Go with B**, with three changes.

Dispatchers are triaging exceptions, so the screen should put the late loads first. B does that: sorting by lateness puts the most urgent load at the top, and the filter chips let them narrow it. A makes them scan four tiles and a map before they reach the list, and the sidebar takes width they need for the table.

Adjustments to B:

1. **Turn the KPIs into chip counts or a thin status strip.** "Late 14" on the chip is the same information as the late-loads tile, without the space cost. Keep on-time % and dwell time in a single slim header line, since they're reference numbers, not triage targets.
2. **Keep some spatial context.** A side panel that only opens on click hides where trucks are relative to each other, which matters when dispatchers reroute. Offer a pinned or toggleable map that stays open, or a small thumbnail map that stays visible when no row is selected. Let the panel be wide, since you have 27 inches.
3. **Make it keyboard-driven.** Arrow keys should move through rows and update the panel as the selection changes, and a key should jump to the next late load. On an all-day tool, this matters more than the layout choice.

Before you commit, test it with two or three dispatchers using real sort orders. If they regularly need to see the map while working through the list, pin it open by default. The sidebar question is separate: if they use other screens, a collapsed icon rail costs less width than a full sidebar.
