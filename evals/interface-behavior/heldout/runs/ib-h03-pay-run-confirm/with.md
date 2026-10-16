Your designer is mostly right, but not about "Send payments."

**Assumption:** a few admins use this on a desktop about once a month, and each payment run covers about 60 freelancers. Sending money is irreversible. I don't know how your payment provider handles cancellations, so check that.

**Remove the popups, and make each action undoable instead**
- **Archiving a freelancer:** archive right away and show a toast with Undo for about 8 seconds. Add an "Archived" filter so you can restore them later. Archiving can be reversed, so a popup only slows you down.
- **Editing a rate:** edit it in place and save it quietly. Keep a small history of changes ("$40 → $45, Oct 15"). If the new rate changes the upcoming payment, show the change on the row itself.
- **Attaching a receipt:** attach it right away and show a "Remove" link beside it. This is trivially reversible, so it never needed a popup.

**Keep one confirmation, but make it specific**
- **Send payments:** this moves money and can't be recalled, so it should be the only popup on the screen. Don't ask "Are you sure?" Show a summary of what's about to happen:
  - "Send 58 payments totaling $X to 58 freelancers"
  - Anything unusual flagged: a rate changed since last month, a payment much larger than usual, a missing receipt, or an archived freelancer who's still included
  - A button that names the action ("Send $X to 58 freelancers") and a plain Cancel
- This works because it's the only popup left. When nearly everything asks "Are you sure?", people click through all of them without reading, including the one that matters.

**Two extras that help more than popups**
- **Send delay:** if your payment provider allows it, hold the batch for a short window (assumed: 10 to 30 minutes) with a visible "Cancel send" button. That gives you a real way to undo a mistake.
- **Show problems before the popup:** mark rows with a missing receipt or an unusual amount so you can fix them before you reach "Send." The popup then confirms a checked list instead of being the first time you see the problems.

**Accessibility:** the toasts should be announced to screen readers and stay up long enough to read. The send dialog should trap keyboard focus and return it to the Send button when it closes.

So your designer is right about three of the four popups, and "lazy" is fair for those. The popup on "Send payments" is the one that should stay, and it should show details instead of a generic question.
