Separate "Stop all agents" from "Refresh" and make it unmistakably destructive, with a confirmation step.

Concretely:

1. **Move it away from Refresh.** Put a clear gap, or a divider, between them, or move Stop all to its own spot. Refresh is a frequent, harmless action, and Stop all is rare and high-impact. They shouldn't be neighbors with the same look.
2. **Restyle it as a danger button.** Use a red outline or red fill with a stop icon, so it reads differently at a glance. Leave Refresh as the neutral grey.
3. **Add a confirm dialog.** Something like "Stop all 12 agents?" with a red "Stop all agents" button and a Cancel button. Make Cancel the default focus, so a stray Enter doesn't confirm it.

If you can only do one thing, do the confirm dialog. It's the safeguard that actually prevents the mistake. The restyle and spacing reduce how often someone reaches for the wrong button, but a confirm catches it when they do.

The 40 minutes to notice is a separate gap. Consider a persistent banner or status color change when agents are stopped, such as "All agents stopped by [user] at [time]". That's a second change, though, so I'd leave it until after this one.

If you share the toolbar component, I can make the edit.
