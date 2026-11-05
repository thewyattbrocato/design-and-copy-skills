Separate "Stop all agents" from "Refresh" and make it visibly destructive. The most effective single change is to make it a red (danger-styled) button and add a confirmation step.

Concretely:

1. **Restyle it as a danger action.** Use a red outline or fill, plus a stop icon. Leave Refresh as the neutral grey button, ideally with a refresh icon. Two identical grey buttons side by side is the root cause, so they shouldn't look alike.
2. **Gate it with a confirm dialog.** Something like "Stop all 12 agents?" with a red "Stop all" button and a Cancel. Stopping everything is a bulk, hard-to-notice action, so a click shouldn't be enough.

If you can only do one, do the confirmation. Styling lowers the odds of a mis-click, but only a confirmation stops one from taking effect. Also move the stop button away from Refresh (for example, to the far left or into an overflow menu) so a mis-aim doesn't land on it.

The 40 minutes to notice is a separate problem. If you have room for a second change, add a persistent banner when agents are stopped. That's a different fix, though, so I'd keep it out of this one.
