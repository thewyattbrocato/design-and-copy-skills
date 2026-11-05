**Assumptions:** a household of 2 to 6 people, mostly on phones, opening the app briefly once or twice a day. One person sets it up and the others just join. I only have your categories, not the 24 items, so I've sorted by category. Paste the list if you want it mapped line by line.

## The main problem

"Off or blank until someone sets it up" turns setup into the product. A chore app with reminders off, no point values, and no rotation rule does nothing on day one. Ship it working, and let settings be the place people change things.

## What should just happen (no setting)

- **Theme:** follow the system. Drop the option.
- **Time zone, week start, 12/24h:** take them from the device.
- **Rotation:** round-robin by default. Skip anyone marked away. Recompute the next assignee automatically.
- **Swaps:** one tap to propose, one tap to accept, and the swap shows in the list. It expires on its own at the due time. Either side can undo it.
- **Reminders:** each person gets one on the morning of the due day and one if it's overdue. No setup required.
- **Quiet hours:** on by default (starting value 22:00 to 08:00). Defer reminders, don't drop them. Honor the phone's Do Not Disturb as well.
- **Points:** assign by chore size (small, medium, large) from a template. Nobody types numbers on day one.
- **Edit permissions:** everyone in the household can edit chores, complete chores, and swap. Only the creator or an admin can remove members or delete the household. Every edit goes in an activity log with undo. This replaces a "who can edit what" matrix, which is the most over-built item on most lists like this.
- **Completion notices to others:** batch them into a digest or show them in the feed. Don't push every one.

## What should be a setting (about 6 to 8, with defaults filled in)

| Setting | Scope | Default |
|---|---|---|
| Reminder time | per person, per device | Morning (starting value 08:00) |
| Quiet hours | per person | On, 22:00 to 08:00 |
| "I'm away until…" | per person, quick toggle on the home screen | Off |
| Use points / leaderboard | household | On. Some households will want it off. |
| Rotation per chore: rotate, fixed person, or anyone | per chore, in the chore editor | Rotate |
| Admins | household | Creator |
| Notification channels (push, email) | per person | Push on |
| Reset to defaults | each group | n/a |

Each setting applies immediately and says whether it's per person or per household. The exception is anything that changes other people's assignments (for example, changing a rotation). Show who is affected before it applies, with Undo.

## What to hold back from the everyday area

- **Custom point values per chore:** put them under "Edit chore" as an optional field that defaults to the size preset. Don't list 20 of them in settings.
- **Per-person reminder times for other people:** each person sets their own. Nobody sets them for someone else.
- **Rotation variants** (weighted, skip-weekends, and so on): leave them out of v1. Add them only if people ask.

## First run

1. Ask for names, or an invite link.
2. Show a checklist of common chores (dishes, trash, laundry, and so on) with size presets already filled in. People tick the ones they want.
3. Rotation starts, reminders are live, and the first chore shows on the home screen.

Everything else uses defaults, and the chosen defaults appear next to the controls so people can see what was assumed. Nothing gets a tour.

## A plan for the week

1. **Days 1–2:** Build the defaults and the template chore list. Remove theme, time zone, and the permission matrix.
2. **Days 3–4:** Build the first-run checklist and the per-person reminder and quiet-hours settings.
3. **Day 5:** Build the "I'm away" toggle and swap expiry.
4. **Days 6–7:** Test with one real household. Watch where they open settings. Anything they open in the first week and change is a good candidate to promote. Anything nobody touches can stay hidden.

Starting values like 08:00 and 22:00 are guesses. Adjust them once you've seen real households use the app.
