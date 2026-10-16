# Settings and instant controls

Load this for a settings, preferences or notification screen, a switch or mute control, anything the system does on its own, "remember me", or defaults and limits on inputs.

## Save or instant: pick one per screen

- Instant-apply: every control takes effect when changed. Show a quiet saved state near the control ("Saved"), and on failure put the control back and say so beside it.
- Save: changes wait for a Save button, with Cancel and a warning on leaving. Use it when settings depend on each other or one wrong change is costly.
- Never mix them on one screen. A page of switches with a Save button leaves people unsure which ones already took effect.
- A grid of the same switch (channels by event types) is a table of preferences, not twelve decisions. Give rows a sensible default, a master control per row or column, and group rare events behind "More". Do not add a Save button just because the grid is big.

## Switches

- The label names the effect, not the verb ("Email me about mentions", not "Mentions: toggle").
- State must be readable without color: on/off text, position and shape.
- If the setting has an exception, say it where the person acts: "Mute notifications. Calendar reminders still sound." A mute that silently spares something reads as a bug.
- While a mode is on (mute, do not disturb, offline), keep a persistent indicator next to the trigger, not only inside settings.
- A switch that looks off but still sends something is the worst outcome; check every path the setting claims to cover.

## Where a control lives

- Frequent actions sit in context, one tap away; rare ones live in settings. The more often used, the more visible.
- Do not give a frequent action and a rare one the same control style.

## Things the system does on its own

Prompts, notifications, automatic changes. Each needs three exits: a stop control at the point it appears ("Don't show again", "Turn off these"), an entry in settings, and a manual way to trigger the same thing on demand.

## Time limits and promises

- Auto-off, expiry, snooze: say the length when it starts ("Muted for 1 hour, until 3:40 pm"), and offer to extend before it ends.
- "Remember me": say how long and what is remembered ("Stay signed in on this device for 30 days"). Do not promise a duration the server does not enforce.

## Defaults from context

- Derive a default from what is already known: locale for country and currency, last choice for repeat actions, device for input type. Show the value in the control, never hide it, and make changing it one step.
- Do not infer anything about income, health, religion, ethnicity, orientation or similar traits to set defaults or targeting. Ask, or leave it out.

## Prevent the invalid state

When it costs nothing, make the error impossible instead of reporting it:

- Date range: the end field starts at the start date, earlier dates are disabled with a reason on focus, and changing the start past the end moves the end.
- Stepper or quantity with limits: stop at min and max, and say why at the limit ("Max 10 per order").
- Dependent fields: adjust them automatically and show that you did.
- Keep manual typing working; constraints guide the picker, they do not block pasted or typed values, which still get checked.

Before: a return date before departure shows a red error after submit. After: the return picker opens on the departure date, earlier days are unavailable, and moving departure later moves return with a one-line note.
