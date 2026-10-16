**Recommendation: don't unify them on one pattern. If you must pick one, pick the confirmation dialog.**

**Why the two actions differ**

- **Archive list is reversible.** It only hides a list from the sidebar, and nothing leaves your system. An undo toast fits this well. It adds no friction, and a mistake costs the user a few seconds.
- **Send campaign is irreversible.** Once up to 30,000 emails go out, nothing can recall them. An undo toast would only work if you delay the send and hold it in a queue for the undo window. That's doable, but then "Sent" isn't true yet, and users can't tell when the send actually happens. A confirmation dialog is the standard fit for an action you can't take back.

**If the lead insists on one pattern**

A confirmation dialog on both is the safer choice:

- The cost of a needless dialog on Archive is a small annoyance.
- The cost of a missing dialog on Send is a mass email to the wrong list, which can't be fixed afterward.

An undo toast on both would need a delayed-send mechanism for campaigns. That's a bigger build, and it changes what "send" means.

**What I'd propose instead**

Make consistency about the principle, not the widget: *confirm what you can't undo, and offer undo for what you can.* Users then learn one rule, and the UI follows it everywhere.

- **Archive list:** act immediately and show an undo toast.
- **Send campaign:** show a confirmation dialog that states the list name and recipient count, for example "Send to 12,400 people on *Spring Sale*?" The button should say "Send to 12,400 people", not "OK". That specific wording catches wrong-list mistakes better than a generic prompt.

If the lead wants a send-side undo, a short delayed send (for example 30 seconds to a few minutes, with a "Sending soon… Undo" state) is a legitimate option. Treat it as a separate feature, not a consistency fix.
