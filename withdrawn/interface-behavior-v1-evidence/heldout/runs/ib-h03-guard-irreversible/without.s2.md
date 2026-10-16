Neither one uniformly. The two actions have different risk profiles, so matching them would leave one of them wrong. My recommendation is to match the pattern to reversibility.

**Send campaign: confirmation dialog.**
- A send can't be undone. Once emails go out, you can't recall them.
- A mistake affects up to 30,000 people. A wrong list or a premature send can hurt sender reputation and deliverability, and it can embarrass a small shop in front of its customers.
- An undo toast doesn't work here unless you build a real delay window, where the send is queued for 10–30 seconds and then released. That's a different feature, and "undo" would be misleading if the emails had already left.
- Make the dialog specific: "Send to 12,480 subscribers on *Spring Customers*?" Showing the recipient count and list name is what stops wrong-list mistakes. A generic "Are you sure?" gets clicked through.
- For large lists, you could add friction, such as typing the list name or requiring a test send first. That's optional.

**Archive list: undo toast.**
- It's easily reversible. The list is only hidden, and no data is lost.
- A confirmation dialog on a low-stakes, reversible action trains people to click "OK" without reading. That weakens the dialog on Send campaign, where it matters.
- An undo toast ("List archived. Undo") is faster and fits the action.

**Consistency without making them identical.** Consistency should mean the rule is predictable: *destructive or irreversible actions get a confirmation, and reversible ones get an undo.* You can apply that rule across the whole product. It's the form of consistency users actually notice.

**What to tell your product lead.** If they insist on a single pattern, use confirmation for both, not undo for both. A redundant dialog on Archive costs a little speed. An undo toast on Send could cause real harm. I'd still push for the split, because the extra dialog on Archive weakens the one on Send.

**Option to offer.** If they want undo on Send, build a short "sending in 30 seconds, cancel" delay. It would still deserve the recipient-count confirmation, so it would add to the dialog and not replace it.
