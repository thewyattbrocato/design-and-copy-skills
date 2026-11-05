# Morning summary screen: general manager view

The screen answers one question first: does anything need me? Stuck items come before routine ones, and each stuck item carries its own decision buttons.

## 1. Top bar
- Date, and a location filter: **All six** (default) or a single site. Tappable.
- One status sentence, e.g. *"Overnight: 11 requests. 9 handled, 2 need you."* The numbers always add up to the total, so the GM trusts that nothing is missing.
- If nothing happened: *"Quiet night. No swap requests."* The rest of the screen collapses.

## 2. Needs you (always first, shown only if non-empty)
Sorted by shift start, soonest first. Each card has:

- **Header:** location, role, shift time, and time remaining (e.g. *"Starts in 6 h"*). Tappable to open the rota for that shift.
- **The problem, in plain words:**
  - No cover: *"Nobody accepted. Asked 14 opted-in staff: 0 yes, 3 no, 11 no reply."*
  - Overtime: *"Covering puts Maya at 41 h this week (over the 40 h limit)."*
- **The agent's recommendation**, stated once, with the cost of each option shown inline:
  - *"Suggested: Jordan (32 h, no overtime). Cost: none."*
- **Buttons, in this order:**
  1. **Approve suggestion** (one tap, assigns the person and updates the rota)
  2. **Choose someone else** (opens the eligible list, each row showing name, hours this week, and whether they'd go into overtime)
  3. **Widen search** (includes sister locations or staff who haven't opted in yet, if policy allows; a choice the GM makes, not the agent)
  4. **Leave uncovered** (marks it and notifies the shift lead)
- **Call** links for the people who didn't respond or said no. Tapping opens the phone dialer.

If there are no stuck items, this section is replaced by one line: *"Nothing needs you."*

## 3. Handled overnight (routine, collapsed by default)
- Header: *"9 handled"* with an expand arrow.
- When expanded, one row per swap: time, requester → cover, shift and location. Each row is tappable.
- Row detail: the staff member's original message, who was contacted, the rota change, and the confirmation sent.
- **Undo** button on any swap whose shift hasn't started yet. Undo reverts the rota and notifies both people. It's the only routine action the GM can take.

## 4. Watch (optional, only if relevant)
- Items not failing yet but at risk, e.g. *"Thursday dinner: 1 request open, 3 contacted, no reply yet."* Each is tappable into the same card format as section 2. Leave this out if it's noisy.

## 5. Footer
- **Ask the agent** (free-text field, e.g. "why did Maya get nothing this week?")
- **Pause agent** (stops new swaps; existing ones continue)
- **Settings** (opt-in rules, overtime threshold, who can approve)

## Rules behind the layout
- **Stuck items are never below the fold on routine clutter.** If there's a problem, it's the first card.
- **Don't show the agent's process** ("searched 47 messages"). Show outcomes and the people involved.
- **Don't wait for morning on urgent items.** If a stuck shift starts within a set window (say, 6 h), push a notification at that time too. The morning screen is the digest, not the only alert.
- **Two taps or fewer for the common decision.** Approve suggestion is always one tap.
- **Overtime approval belongs to the GM** and the agent never assigns overtime on its own. Confirm this matches your policy.

**Assumption:** I read "general manager" as a group-level role over all six sites, with the location filter for site-level use. If each site has its own GM, drop the filter and show only that site.
