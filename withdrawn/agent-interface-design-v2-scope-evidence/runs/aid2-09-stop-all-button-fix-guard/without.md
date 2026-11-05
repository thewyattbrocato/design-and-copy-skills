Separate "Stop all agents" from "Refresh" and make it unmistakably destructive, then gate it with a confirmation.

Concretely:

1. **Restyle and move it.** Make Stop all agents a red (danger) button, with a stop icon, and put it away from Refresh. Put a divider or a gap of at least a few button-widths between them, or move it into an overflow or "danger zone" menu. Leave Refresh as the plain, safe, default-looking action.

2. **Add a confirmation.** Clicking it opens a dialog such as "Stop all 12 agents? In-flight documents will be interrupted." The confirm button should repeat the action ("Stop 12 agents"), not say "OK", and Cancel should be the default focus.

If you can only do one thing, do the confirmation. The styling and spacing reduce misclicks, but the dialog is what stops a misclick from taking effect. The 40-minute detection gap is a separate problem, and a persistent "Agents stopped" banner or status change would help with it. You didn't ask about that, so I'd treat it as a follow-up.

I haven't looked at your code. This working directory has no repo, so if you want me to make the change, point me at the dashboard source.
