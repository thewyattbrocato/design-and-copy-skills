The biggest problem is that every option starts off or blank. A new household has to configure the app before it works. Flip that: the app should work correctly with zero setup, and a setting should exist only if households really disagree and no default is a good guess.

## Should just happen (no setting)

- **Rotation:** Round-robin among active members, skipping anyone marked away. Ship one rule. Fairness weighting and other variants can wait.
- **Swaps:** Anyone can request one, and the other person accepts with one tap. Swap requests always notify, with no toggle.
- **Point values:** Chores come from templates with a size (small, medium, large = 1/3/5). Edit points on the chore itself, not in settings.
- **Chore frequency:** Set it when you create the chore (weekly by default). It's a property of the chore.
- **Overdue:** The chore stays with its owner. Send one nudge the next day, then offer a swap after 2 days. Don't auto-reassign.
- **Time zone, week start, theme:** Take them from the device and locale. Theme follows the system.
- **Quiet hours:** Never send reminders outside roughly 8am–9pm local, and let the OS Do Not Disturb handle the rest. A custom schedule duplicates what phones already do.
- **Notification channels and digests:** Use push only. Add others when someone asks.

## Real settings (about 5), with defaults

| Setting | Scope | Default |
|---|---|---|
| Reminder time | Per person | 9:00 am on the day a chore is due |
| Reminders on/off | Per person | On |
| Away mode | Per person | Off. Put it on the home screen, not in settings. |
| Show points and leaderboard | Household | On. Some households find points awkward, so this is the one opt-out. |
| Who can edit chores and members | Household | Everyone edits chores. Only the creator can remove members or delete the household. |

Reminder time is per person because people really do differ on it. Away mode is a setting because rotation can't guess it.

## Make the empty state useful

Replace blank-until-configured with a short onboarding:
1. Add the household members' names.
2. Tick chores from a starter pack of about 15 common ones, such as dishes, trash, bathroom and laundry. Each has a preset size, frequency and points.
3. Done. Rotation starts, and reminders use the defaults.

Everything else is adjustable later, but nobody has to touch it first.

## Plan for the week

- **Days 1–2:** Build the chore templates and the onboarding flow. This is where most of the 24 settings go away.
- **Days 3–4:** Implement the fixed rotation, overdue and swap behavior, and the 5 settings with their defaults.
- **Day 5:** Move per-chore options into the chore editor, and delete the rest from settings.
- **Days 6–7:** Test with one real household from a clean install. Log which settings people change.

If people keep asking for something you cut, such as custom quiet hours or per-chore points in bulk, add it back with evidence.

If you paste the full list of 24, I can sort each one into these buckets. I've only covered the ones you named plus the obvious neighbors.
