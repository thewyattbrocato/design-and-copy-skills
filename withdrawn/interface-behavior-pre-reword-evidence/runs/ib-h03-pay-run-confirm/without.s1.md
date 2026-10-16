Your designer is half right. Blanket "Are you sure?" popups are bad design, but deleting all of them is also wrong. Which fix fits depends on whether the action can be undone and how much damage it does.

**Why blanket confirmations fail**
People click through them by reflex. If every action asks, the one that matters (sending money) looks the same as the trivial ones, and the popup stops protecting anything.

**What I'd do for each action**

| Action | Reversible? | Recommendation |
|---|---|---|
| Attach a receipt | Yes, you can detach it | No popup. Just do it, and let people remove or replace the receipt. |
| Edit a rate | Yes, you can edit it back | No popup. Save inline and show the change ("Rate updated, Undo"). If the rate affects a payment run that's already queued, show a warning at that point. |
| Archive a freelancer | Mostly, if archive means hidden rather than deleted | No popup. Show a toast with **Undo**, and an easy "Archived" filter to restore from. |
| Send payments | **No**, money leaves your account | Keep a confirmation, but make it a real review step, not "Are you sure?" |

**Make "Send payments" a proper review**
- State the specifics: "Send $41,350 to 58 freelancers on Oct 31," not a generic yes/no.
- Show the total, the count, and anything unusual: a new payee, a rate changed since last month, an amount far from their usual, a missing receipt, a freelancer with no payment details.
- Name the button for what it does ("Send $41,350"), not "OK" or "Yes."
- For a monthly batch of about 60, a summary screen or side panel you review before sending works better than a popup.
- Consider a stricter step only for outliers, such as a payment far above that person's norm, rather than for every payment.

**General rule**
Prefer **undo over confirm** wherever you can. Undo costs nothing when you're right and rescues you when you're wrong. Reserve confirmation for actions that can't be reversed. Then make that confirmation specific enough that the person actually reads it.

**What to tell your designer**
"Remove the popups on the three reversible actions and add undo. Redesign 'Send payments' as a specific review step." That keeps their instinct about popup fatigue and protects you from a costly mistake on the one action where it counts.

One caveat: I haven't seen your screen. If archiving a freelancer also cancels pending payments or deletes their history, treat it as less reversible and keep some friction there.
