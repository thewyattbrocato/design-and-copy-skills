Your designer is half right. Blanket "Are you sure?" popups are bad design, but deleting all of them would be a mistake on a screen that moves money.

**Why the popups are a problem**
- When nearly everything asks for confirmation, people click "OK" without reading. The one popup that matters, "Send payments", then gets the same reflexive click as the rest.
- Confirmation dialogs are a weak safeguard anyway. They interrupt you but don't help you catch a mistake.

**What I'd do with each action**

| Action | Recommendation |
|---|---|
| **Attach a receipt** | Remove the popup. It's low-stakes and easy to undo, so let people remove or replace the receipt. |
| **Edit a rate** | Remove the popup. Save the edit directly and show the change ("Rate updated from $50 to $55/hr") with an Undo option. Add an inline warning only if the new rate is unusually different, such as more than 25% off. |
| **Archive a freelancer** | Remove the popup, show a toast with Undo, and make archiving reversible (an "Archived" filter with Restore). Archiving is only risky if it's irreversible or cancels pending payments. If it does either, say so. |
| **Send payments** | Keep a confirmation, but make it a review step instead of "Are you sure?". |

**What the "Send payments" step should show**
- The total amount, the number of freelancers, and the funding source.
- A list of who gets paid what, with anything unusual flagged: rate changes since last month, a first-time payee, a much higher or lower amount than usual, or a missing receipt.
- A button that names the action and amount, like "Send $48,250 to 58 freelancers", instead of "OK" or "Yes".
- Optionally, if a mistake would be costly, a short delay or a typed confirmation for unusually large totals.

You pay roughly 60 people monthly, so a rushed or mistaken batch is expensive and hard to claw back. A one-time summary screen costs about 30 seconds a month and is worth keeping.

**Summary for your designer:** reserve confirmations for actions that are irreversible or costly, and use undo for everything else. Then the one confirmation that remains will get read.
