**Neither option works for both. Give Archive list an undo toast and Send campaign a confirmation dialog.** Consistency should come from one rule, not from identical widgets: reversible actions get undo, and irreversible actions get a specific confirmation.

*Assumption: small-shop owners on desktop or mobile who send campaigns occasionally and aren't email experts.*

**Archive list: undo toast, no dialog**
- When someone archives a list, hide it right away and show a toast, "List 'Spring customers' archived. Undo", for about 8–10 seconds (starting value). Archiving only hides the list from the sidebar, so the action is fully reversible.
- Also keep an "Archived" view where the list can be restored later, in case the toast is missed.
- Announce the toast to screen readers through a polite live region. Don't remove it before it can be read.
- A dialog here would be an "are you sure?" before a reversible action. People learn to click through those without reading.

**Send campaign: specific confirmation, not undo**
- Once emails reach 200–30,000 inboxes, nothing can pull them back, so an undo toast would promise something the product can't deliver.
- The confirmation should name what's at stake: "Send 'October newsletter' to Spring customers (12,480 recipients)?" The button should say "Send to 12,480 people", not "OK".
- Show the key details in the dialog: subject line, sender, and the list's recipient count. This is where mistakes get caught, such as the wrong list or a stale count.
- Optionally, add a short send delay (for example 30–60 seconds, an assumed value) with a "Cancel send" control. That would give you a real undo, and the dialog could then be lighter for small lists. It depends on whether your sending pipeline can hold messages.
- Keep this dialog to sends only. If other actions start using it, people will stop reading it.

**What to tell your product lead**
Users don't need the two actions to look the same. They need to trust that the product protects them when it matters and stays out of the way when it doesn't. Putting a dialog on Archive would add friction to a harmless action. Putting only an undo toast on Send would give no protection against the costliest mistake in the product. The shared principle is "irreversible means confirm, reversible means undo", and it can also guide future actions.
