**Assumption:** one GM reads this for all six locations. The overtime limit and the "opted in" lists already exist as rules. I haven't put any volume figures in, so the counts below are placeholders for real data.

## Morning summary screen (phone, portrait)

**1. Status strip (pinned at top, always visible)**
- Left: "Shift swaps" with a green dot and "Running". Below it: "Last action 11:42 pm · Watching for new requests".
- Right: a **Pause** button, one tap. When paused, the whole strip turns amber and reads "Paused since Tue 6 pm. 2 requests came in and were not handled." with **Resume** and **Resume on a date** buttons.
- Under the strip is a location filter chip, "All 6 locations". Tapping it narrows the screen to one site.

**2. One-line headline**
- "2 need you · 9 handled · 1 not understood". On a quiet night: "Nothing needed you. 3 handled."
- If there was no activity, it says "No swap requests overnight. Agent is running." That way a quiet night doesn't look like a broken agent.

**3. Needs you (first section, shown only if something is stuck)**
These are cards sorted by **shift start time, soonest first**. Each card has:
- A title line: "Fri dinner · Line cook · [Location]. Dana can't work."
- A reason line in plain words, either "Asked 6 opted-in people, nobody accepted" or "Only available cover is Sam, which puts Sam at [X] hrs, over your [limit] limit."
- A "What I'm doing" line: "Offer to Jo and Lee still open, I'll re-ask at 10 am." This tells the GM the agent hasn't given up.
- The deadline: "Shift starts in 2 days".
- Buttons, specific to the problem:
  - *Nobody accepted:* **Ask more people** (a picker of the next candidates, which can include people who haven't opted in, with each one marked), **Call Dana**, **Mark as short**.
  - *Overtime:* **Approve overtime for Sam**, **Keep looking**, **Leave uncovered**.
- The agent never approves overtime itself. The card body is tappable and opens a detail view: who was asked, when, how each person replied, and the rota as it stands.

**4. Handled (second section, collapsed to a few rows with "Show all 9")**
- One line per swap: "Tue lunch · Marco → Priya · [Location] · 9:14 pm".
- **Order: doubtful ones first**, flagged with a small tag. Examples are cover that took several asks, cover arranged less than a set time before the shift, or someone close to the overtime limit. Everything else follows in time order.
- Tapping a row shows the message thread, who was asked, and the rota before and after. It has an **Undo** button that restores the original rota. Before you confirm, it states that "Priya and Marco will be told, but messages they've already read can't be unsent."
- A row's "⋯" menu has **Not this one** (for example, "don't offer to Priya again this week") and **Never for this kind** (for example, "never offer closing shifts to under-18s"). The second option shows the rule it would create before saving.

**5. Not acted on (third section, shown only if present)**
- Messages the agent didn't treat as swap requests, or wasn't sure about: "Alex: 'might be late Sat, will confirm'". Each has **Handle as swap request** and **Ignore**.
- This section is there because a missed request is invisible otherwise.

**6. Footer**
- **Rules** (opens the plain-language list: who it can ask, overtime limit, quiet hours for messaging staff), **Full activity history**, and **Contact a person** for help.
- **Turn off** is reachable from here and from the pause strip. It needs no reason and states what happens to offers already sent.

## Why it's ordered this way
- Stuck items come first because they're the only ones with a deadline the GM can still act on.
- Handled items are visible but secondary, and the doubtful ones surface first, so the GM can trust the routine ones without checking each.
- The morning screen shows only stuck swaps. If a stuck one is urgent (a shift starting in a few hours), it should be a push notification, not wait for the morning summary. That rule is worth settling separately.
