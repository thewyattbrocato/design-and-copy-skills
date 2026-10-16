**Short version:** the plan is aimed at a user you don't have. Your users are six people who are past expert level and use the board eight hours a day. Three of the four items would slow them down, and the fourth is useful only in a different form.

I'm assuming the six coordinators are the only users, they work on desktops with keyboard and mouse, and the board is open all shift.

**1. Daily setup wizard for filters: drop it.**
- The board already remembers filters and sort, so the wizard asks six people to re-enter something the product already knows. That adds a mandatory step to every shift.
- It also makes the product's best feature, remembered state, look like a deficiency.
- If the PM's worry is that people start the day with stale filters, show the active filters beside the grid ("Filters: Doors 1–8, Inbound"), and add a one-key reset and a "Clear filters" control.
- If a filter combination gets reused, offer named presets, such as "Morning inbound", that can be switched with a key.

**2. First-login tour with tooltips: skip it, or shrink it a lot.**
- Almost every login is a returning login. A tour helps only on the first one, and only for new hires.
- A better fit is a discoverable shortcut cheat sheet (`?`) and a short empty-state hint. Keep those for new hires and don't show them to everyone.
- Never auto-play anything that blocks the grid.

**3. Bigger rows and a card per truck: this is the most harmful item.**
- Density is what these users need. A terminal with many doors and trucks needs the whole day visible at once. Bigger rows and cards mean more scrolling and less situational awareness.
- Cards also hurt keyboard navigation and scanning down a column to compare ETAs or door assignments.
- If "friendlier" means "easier to read", fix that without losing density:
  - Add a density toggle (compact by default, comfortable optional), remembered per person.
  - Improve contrast, type size and status cues, and don't rely on color alone.
  - Make the row's key fields clearer and put detail in an on-demand side panel.

**4. Confirmation after every door move: wrong as specified, but the concern behind it is real.**
- Drag-to-reassign is a frequent, reversible action. A confirmation on every one trains people to click through without reading, so it protects nothing and costs seconds many times a day.
- The valid concern is accidental drops. Handle it by making the move undoable:
  - Apply the move immediately and show a brief "Truck 4471 moved to Door 6. Undo" notice. `Ctrl/Cmd+Z` should work too, and screen readers should be told.
  - Give the drag a keyboard route: select the truck, then pick a door.
  - Show clear drop targets and block conflicts, such as a door that is already occupied, in place.
- Reserve a real confirmation for what can't be undone, such as a move that triggers a notification to a carrier or driver. If one exists, name that consequence in the prompt.

**What I'd tell the PM:**
- Reframe "friendlier" for this audience. It means fewer interruptions, faster paths, and mistakes that are cheap to fix.
- Shadow a coordinator for a shift and note where they slow down, make errors or work around the board. Real friction there will give better candidates than this plan.
- Treat the board's current memory and keyboard speed as assets to protect.

**Worth doing instead:**
- Undo for door moves.
- A keyboard route for reassignment.
- Visible active-filter state and named presets.
- A density toggle.
- A shortcut cheat sheet for new hires.

I haven't seen your codebase or usage data, so the reasoning rests on the board as you described it. If any coordinators have said they struggle with a specific part, that would change my view of the relevant item.
