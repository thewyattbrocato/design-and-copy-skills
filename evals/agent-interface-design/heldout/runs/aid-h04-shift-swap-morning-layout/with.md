**Assumptions:** the GM manages all six locations from one phone. The agent offers shifts and updates the rota, but it never approves overtime and never assigns anyone who hasn't opted in. Those limits are my starting values, so change them if they're wrong.

## Morning summary screen (top to bottom)

**1. Status strip (always visible, one line)**
"Shift swaps: running · last action 1:42 am · next check now"
- A **Pause** button sits right on the strip, one tap away. When paused, the whole strip turns a solid warning colour and reads "Paused since Tue 9 pm. 2 swap requests are waiting and haven't been handled." It gets **Resume** and **Resume on a date** buttons.
- On a night with 0 actions, the screen still shows this strip plus "Quiet night. No swap requests came in." That way idle doesn't look like broken.

**2. Needs you (only shown if something is stuck, always first)**
Header: "Needs you · 2". Each stuck item is its own card, ordered by the soonest shift start, since that's the deadline. Each card has:
- **Plain headline:** "Fri dinner, Harbour St: Maria can't work, no cover yet."
- **Why stuck, one line:** "Offered to 6 opted-in staff, none accepted," or "Dev accepted, but it takes them to overtime for the week."
- **What the agent has already done:** "Re-offered at 8 am. Will try again at noon."
- **Time pressure:** "Shift starts in 2 days."
- **Buttons (specific to the reason):**
  - No takers: **Widen the offer** (shows who it would reach before you confirm), **Offer a bonus or call someone** (opens the contact list), **Leave it uncovered**.
  - Overtime: **Approve overtime for Dev**, **Offer to someone else**, **Decline the swap**.
- Tapping the card body opens the full thread: who was asked, when, and what they said.

Nothing here relies on you noticing. If a card is still open when the shift gets close, the agent sends a push notification then, not only a morning card. That push is the only kind of alert that interrupts you.

**3. Handled overnight (the digest)**
Header: "Handled · 11". A single sentence of totals is not enough, so every item is listed.
- Rows are grouped by location (collapsed to the location name and count when there are many, expanded by default when there are 5 or fewer).
- Each row is one line: "Tom → Aisha, Sat lunch, Dockside. Accepted 11:20 pm. Rota updated."
- Rows the agent was less sure about sort to the top of their group and carry a small tag. Examples are a cover who accepted after a long delay, a swap that crossed a day boundary, or a cover who's near their weekly hours.
- Tap a row to see the message trail and the rota change.
- **Swipe or tap "Undo"** on a row to put the rota back as it was and tell the affected people. Under the button it says plainly: "Messages already sent can't be unsent. Staff will get a correction."

**4. Skipped or declined (collapsed by default)**
Header: "Not actioned · 3". It lists requests the agent chose not to handle, such as someone who isn't opted in, a request that came in too late, or one it couldn't understand. Each row says why, with **Handle it myself** and **Tell the agent to treat this kind differently** buttons. This section exists because missed items go unnoticed.

**5. Footer**
- **Rules** opens a plain-language list: "It offers shifts only to staff who opted in. It never approves overtime. It stops after N offers per shift." (N is yours to set.) Each rule has an edit button that previews what would change.
- **Message settings** controls which alert kinds can reach your phone, plus the time the digest arrives.
- **Contact someone** reaches a person at head office or support, not just a chat.

## Why this order
- You came to find out what needs a decision, so stuck items come first.
- Routine completions are reference material. They go below, but each can be undone.
- Skipped items are third because they're easy to miss but rarely urgent.
- Settings stay available but out of the way.

## Two behaviours to decide
- **Corrections:** each item offers "not this one" (this time only) and "always or never for this kind of case". The second shows the rule it would create before it saves.
- **Widening trust:** if you approve the same kind of overtime several times, the agent may suggest a standing rule with a cap. It won't apply that rule without your confirmation.
