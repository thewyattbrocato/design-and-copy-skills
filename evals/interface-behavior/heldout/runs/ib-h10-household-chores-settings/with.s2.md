**Assumption:** Phones, a household of 2–6 people, a few taps a day. Most people will never open settings, so the app has to work on day one with nothing configured.

The core problem is that "off or blank until set up" makes setup the price of using the app. Flip that: ship defaults that work, and make settings the place to change them.

## What just happens (no setting)

- **Rotation:** Round-robin across active members, skipping anyone marked away. Fairness is the point, so don't offer rule variants in v1.
- **Reminders:** The assignee gets one reminder on the due day, plus one nudge if it's overdue. Everything else is a default, not a choice.
- **Quiet hours:** Hold notifications overnight, using the phone's own Do Not Disturb or a fixed 10pm–8am window. Don't build a per-person scheduler.
- **Theme:** Follow the system light/dark setting. No toggle.
- **Time zone and week start:** Take them from the device.
- **Swaps:** Anyone can propose a swap, and the other person accepts or declines with one tap. Proposals expire on their own after a couple of days (assumed; tune it). No setting is needed.
- **Points:** Scale automatically from a size on each chore (small, medium, large → 1/2/4, a starting value). Nobody types numbers.
- **Saving:** Save changes as the person makes them. No Save buttons and no "Saved!" messages.
- **Undo:** Deleting a chore, marking one done, and swapping all get an Undo toast. Skip the "are you sure?" dialogs.

## Defaults that people can change

Each of these is a real choice, but it has a starting value, so nobody has to fill it in.

| Option | Default | Scope |
|---|---|---|
| Reminder time | 9am on the due day, one time for the whole household | Per person (a later override) |
| Chore size | Medium | Per chore, set when creating it |
| Chore frequency | Weekly | Per chore |
| Who can edit chores | Everyone | Household |
| Points visible to all | On | Household |
| Mark myself away | Off | Per person, used when traveling |

The "who can edit" choice depends on who's in the household. A family with kids may want a parent/child split, but roommates don't. Default to everyone and put an "Admin only" option behind one control. Don't build a permission matrix.

## What to cut or defer this week

- **Per-person reminder times:** Cut for v1. One household time covers most people. Add the override only if users ask.
- **Per-chore point values:** Replace them with the size picker above.
- **Rotation rules** (weighting, pairing, exclusions): Defer. "Away" and "swap" already cover the real cases.
- **Per-chore reminder settings:** Cut.
- **Notification toggles by event type:** Cut. Keep one on/off switch for notifications.

I'd guess this takes you from 24 options to about 6–8. I don't have your list, so that count is an estimate. Send me the 24 and I'll sort each one into these buckets.

## First run

1. Create the household and invite people by link or code.
2. Offer a starter chore list (dishes, trash, bathroom, and so on) that people can edit or remove. Each chore has a size and frequency prefilled.
3. Start the rotation right away. Show "Assumed: weekly rotation, reminders at 9am" on the screen, with a link to change it.

## Settings screen

- Put it in two groups: **Household** (reminder time, who can edit, points visibility, members) and **Me** (notifications, away).
- Say on each item whether it applies to the household or only to that person.
- Apply changes immediately, and add a "Reset to defaults" link.
- Hold the confirmation dialogs back for the one irreversible action, which is deleting the household. Name what goes with it.

## Order of work for the week

1. Defaults and automatic behavior: rotation, reminders, quiet hours, swap expiry.
2. First-run flow with starter chores.
3. The trimmed settings screen.
4. Undo toasts, with screen-reader announcements and keyboard access.
5. Cut features come back only if testing shows people need them.

**Open question:** Is the household mostly roommates or families with kids? That changes the "who can edit" default and whether points need an admin view.
