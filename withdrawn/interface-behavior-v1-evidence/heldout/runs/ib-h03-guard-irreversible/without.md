Neither one uniformly. The two actions have different risk profiles, so forcing them to match would make one of them worse.

**Archive list: undo toast.**
- It's easily reversible, since the list is only hidden.
- A confirmation dialog on a low-stakes action trains people to click through dialogs without reading them.
- A toast keeps the flow fast, and undo fully repairs a mistake.

**Send campaign: confirmation dialog.**
- Sending can't be undone. Once the emails go out to up to 30,000 people, an undo toast would be misleading unless you build a real delay-and-cancel window.
- The cost of a mistake is high: a wrong list, a typo, or a test send that reaches the full audience.
- The dialog should be specific rather than generic. For example: "Send 'Fall Sale' to **12,431 subscribers** on *Customers*?" with the button labeled "Send to 12,431 people". Showing the recipient count and list name is what catches wrong-list mistakes.

**If the product lead insists on one pattern:** use a confirmation dialog for both. An undo toast on Send is dangerous, and a dialog on Archive is only a small annoyance. The cost of being wrong is lopsided.

**How to frame it for consistency:** the consistent rule is "confirm irreversible actions, offer undo for reversible ones." Users learn that rule quickly. It's also a principle you can apply to future actions, like delete list or remove subscribers.

**Optional upgrade:** a "Send" that waits 10–30 seconds with a visible "Undo" before dispatch gives you an undo toast on a send, but only if your sending pipeline can hold messages. If it can't, stay with the dialog.
