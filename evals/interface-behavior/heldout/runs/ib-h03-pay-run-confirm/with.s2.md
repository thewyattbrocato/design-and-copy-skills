Your designer is mostly right, but not about all of them. Remove three of the four popups. Keep one, and make it more useful.

**Assumptions:** one or two admins on a desktop, using this screen about once a month, with about 60 payees.

**Archiving a freelancer: remove the popup and add Undo.**
- Archiving can be reversed, so the popup only slows people down.
- Show a toast with Undo for about 8 seconds.
- Keep an "Archived" filter so people can restore a freelancer later.
- Archived freelancers should be skipped in the next payment run.

**Editing a rate: remove the popup, save quietly, and show what changed.**
- Save the new rate without asking.
- Show the old rate beside the new one for a moment, with Undo.
- The payment run will total up what you're about to send, so a wrong rate is caught before any money moves.
- If a rate changes by a lot, flag it in place. For example, show "Rate up 3× from last month" next to the field. Don't use a popup.

**Attaching a receipt: remove the popup and add a way to detach.**
- Attach the file as soon as it's chosen.
- Let people replace or remove it with one click.
- Nothing is lost if they pick the wrong file.

**Send payments: keep a confirmation, but make it specific.**
- Money can't be recalled once it's sent, so this is the one place a confirmation earns its keep.
- Don't ask "Are you sure?". Show what is about to happen: "Pay 58 freelancers a total of $X from [account]." Add the date and a list of anything unusual, like a first-time payee, a changed rate, or a missing receipt.
- Label the button with the action, such as "Send $X to 58 people", not "Yes".
- Pressing Esc or clicking away cancels without sending.
- If your payment provider supports it, add a short hold of a few minutes after sending, with a "Cancel payments" option. That would be better than any popup.
- Once payments are sent, show their status on the screen, such as "Sent", "Pending" or "Failed". Don't use a success popup.

**Why this works:** people stop reading popups that appear on everything, so they'll click through the one that matters. If you make mistakes easy to undo and keep a single confirmation for the irreversible step, people will notice it.

**Before the designer removes anything,** check that archived freelancers can really be restored and that rate changes aren't pushed to other places, like invoices already sent. If either isn't true, that action needs a specific confirmation of its own.
