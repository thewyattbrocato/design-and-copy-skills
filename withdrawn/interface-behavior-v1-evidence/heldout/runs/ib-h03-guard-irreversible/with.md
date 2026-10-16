**Neither one rule. Give Archive list an undo toast and give Send campaign a specific confirmation. Consistency should come from one principle: recoverable actions get undo, and unrecoverable ones get a confirmation.**

Assumption: small-shop owners using this on a laptop, a few times a week. I'm not assuming any usage numbers.

**Archive list: undo toast, no dialog**
- Archiving only hides the list from the sidebar, so it's fully reversible.
- A dialog on a reversible action trains people to click through, which weakens the dialogs that matter.
- Toast text: "Archived 'Spring Sale'. Undo". Keep it up for several seconds, announce it to screen readers, and don't let it disappear before it can be read.
- Also provide an "Archived" view where a list can be restored later, in case the toast is missed.

**Send campaign: specific confirmation, not an undo toast**
- Once an email reaches 200 to 30,000 inboxes, it can't be pulled back. An undo toast would promise something the product can't deliver.
- The confirmation should name the consequences, not ask "Are you sure?". For example: "Send 'Spring Sale' to 12,400 subscribers in 'Customers'?", with the button labeled "Send to 12,400 people" and a Cancel button.
- Show the recipient count and list name in the dialog, because the usual mistake is picking the wrong list.
- Optional, and better than a dialog alone: a short send delay of about 30 seconds to a few minutes. It gives you a real "Undo send" window, as Gmail does. The email isn't sent until the delay ends, so the undo is honest. If you can build it, it fits the "make mistakes cheap to undo" principle better than a dialog.
- Consider scaling the friction to list size. A 200-person send can use the plain confirmation, while a 30,000-person send could add a test-send prompt or a typed confirmation. Pick the thresholds yourself.

**What to tell your product lead**
Users don't experience consistency as "both actions have the same widget." They experience it as "the app only interrupts me when it matters." If both actions got a dialog, Archive would produce needless friction. If both got an undo toast, Send would give false reassurance and make irreversible mistakes easy. A single rule that covers both is: **undo where we can truly restore, confirm where we can't.**
