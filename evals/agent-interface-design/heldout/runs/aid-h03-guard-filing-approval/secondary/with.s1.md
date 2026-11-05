**Assumption:** you're the only operator, the shared inbox is the only input, and "wrong" means a receipt filed under the wrong client. Nothing is deleted or sent, so every action is reversible.

**My recommendation:** don't approve every filing. Approving 60 items a week makes you rubber-stamp within days, and then the approval protects nothing. Instead, have it act on confident matches and send the uncertain ones to you. Your cofounder's concern is still covered: the matches are reviewable, reversible, and the uncertain tail waits for you.

**Setup (before it goes live)**
- **One-line promise:** "While you're away it will file receipts it can match to a client with high confidence, and it will never delete, send, or touch anything it can't match."
- **Dry run on last week's ~60 receipts first.** Compare its choices with where you actually filed them. This is the evidence your cofounder should want. If it disagrees with you on a meaningful share, tighten the rules before going live.
- **Restate the rules back to you** with three examples, e.g. "A receipt from billing@acme.com with 'Acme' in the subject goes to Acme/Receipts. A receipt with no client name goes to the review queue."
- **Ask for the narrowest permission:** move and rename inside the client folders only. Check that the folders' sharing settings match, since filing a receipt into a folder shared with another client would expose it.

**What it asks you (the review queue)**
- When it can't match a client with high confidence, do nothing and queue it, because a miss is cheap and a wrong filing is what you need to catch.
- Show each queued item with its best guess and why it's unsure, so you can pick the folder in one tap.
- Ask you to confirm a new sender→client mapping once. After that it files that sender automatically.

**What it reports**
- **Problem (interrupts now):** a move failed, permissions changed, or it has stopped running.
- **Digest (once a day, your chosen time):** a list of what it filed, each line showing the sender, the client, and a "move back" control. Queued and low-confidence items go to the top.
- **Concern (when a trend crosses a limit):** e.g. "queue size has doubled this week" or "more than N of this week's filings were corrected by you."
- Not per-filing notifications, and not a bare "60 items handled" total.

**Mistakes**
- **Wrong filing:** "Move back" restores the original location and name from the activity record. Offer "never for this sender" or "not this one" right there.
- **Missed receipt:** it sits in the queue with the low-confidence items first, so you can see what it skipped.
- **Rule edits:** when you change a mapping, show the plain-language rule and a preview: which past receipts it would have caught and which it would now miss.

**If your cofounder still wants a check:** run two weeks with approve-everything, measure how often you'd have changed its choice, then move to act-and-report on confident matches only if the error rate is one you both accept. Set that threshold together before you start, since I don't have a number that's right for your business.
