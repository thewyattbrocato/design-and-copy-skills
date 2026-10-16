You didn't paste the 24 options, so this works from the categories you named. If you paste the list, I'll sort each one.

The biggest problem is that everything starts off or blank. A new household would get no reminders, no points, and no rotation until someone configures them, so the app looks broken on day one. Ship with working defaults and make settings the place to change them.

## Rule for sorting

- **Just happens:** there's one answer almost everyone wants, and picking it is a chore.
- **Setting with a default:** households differ, and the difference matters to them.
- **Cut:** it's only a preference, or you can't explain what it does in one line.

## Just happens, no setting

- **Time zone, theme, and week start:** take them from the device or locale. Theme follows the system.
- **Rotation:** round-robin across active members, advancing when a chore is done or its period ends. Skip anyone marked away.
- **Overdue handling:** a chore stays with its person and shows as overdue. Send one nudge, not a stream.
- **Swaps:** anyone can offer a swap to anyone, and the recipient accepts or declines. Offers expire after 48 hours and the chore reverts. Points go to whoever actually does the chore.
- **Quiet hours enforcement:** hold notifications in the window and deliver them when it ends. Don't ask whether to.
- **Points on swap, skip, or away:** use fixed rules, with no toggles. Being away costs no penalty.
- **Chore templates at onboarding:** offer a checklist (dishes, trash, laundry, and so on) with sensible frequencies, so nobody starts from a blank list.

## Settings, with defaults

**Per person (4):**

| Setting | Default |
|---|---|
| Reminder time | 9:00 am on the day a chore is due, plus one 6:00 pm nudge if it's still undone |
| Quiet hours | 10 pm to 8 am |
| Notifications on/off | On |
| Away mode, with an optional return date | Off |

**Per household (3):**

| Setting | Default |
|---|---|
| Who can edit chores and rules | Everyone. The alternative is "admins only". |
| Rotation per chore | Rotate. The alternative is "fixed to one person". |
| Points | Three tiers: small 1, medium 3, large 5, assigned by the template |

Three more things are worth a small control:
- **Points on or off for the household.** Some people find a leaderboard stressful, so make it a single switch that defaults to on.
- **Per-chore frequency.** This is part of the chore itself, not a setting.
- **Remove member / transfer admin.** This is an action, not a setting.

That gets you from 24 to about 7 real settings.

## Cut or defer

- **Per-person, per-chore reminder times:** one time per person covers most households. Add the finer version only if people ask.
- **Raw numeric point values per chore:** tiers are faster to set and harder to argue over. Allow a custom number later.
- **Granular "who can edit what" matrix:** use the everyone/admins toggle.
- **Rotation rules beyond rotate/fixed:** weighted, random, and skip-patterns can wait.
- **Anything theme-related beyond system default.**

## Week plan

1. **Days 1–2:** build the defaults, the rotation, and the reminder behavior so a new household works with zero setup.
2. **Day 3:** build the onboarding flow with chore templates and member invites.
3. **Days 4–5:** build the seven settings.
4. **Days 6–7:** test with one real household. Watch which defaults they change in the first week, and use that to decide what else deserves a setting.

Log every settings change from day one. If nobody touches a setting, it can probably become a default.
