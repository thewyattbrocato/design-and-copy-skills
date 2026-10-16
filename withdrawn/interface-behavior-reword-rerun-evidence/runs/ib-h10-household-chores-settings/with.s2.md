**Assumptions:** A household of 2–6 people uses this on phones, a few times a day. Most of them won't open settings. One person (the "organizer") sets things up. I haven't seen your 24 options, so I've sorted the kinds you listed. Map the rest by the same rules.

## The main fix
"Every option is off or blank until set up" is the biggest problem. A blank reminder time means no reminders. A blank point value means points don't work. Nobody opens settings to fix that. Ship defaults that make the app work on first use, show what was assumed beside each control, and give each setting a reset.

## Just happens (not settings)

| Behavior | Rule | Why |
|---|---|---|
| Rotation | Round-robin among active members, skipping anyone marked away. | Every household wants this. The rotation rules can be a per-chore choice later (rotate / fixed person). |
| Reminders | Remind the assignee on the due day at a default time, plus one nudge if it's overdue. | Both are needed for the app to work at all. |
| Quiet hours | Default 22:00–08:00, using the phone's own do-not-disturb where possible. Held reminders go out when quiet hours end. | This is a courtesy people expect without being asked. |
| Time zone and week start | Take from the device. | The phone already knows. |
| Theme | Follow the system. | No setting needed. |
| Points | Seed each chore with a value from its size tag (small 1, medium 3, large 5, assumed starting values). Editable on the chore itself. | Points should not be 10 separate blank settings. |
| Swaps | Anyone can propose a swap. It applies when the other person taps accept. If there's no reply in 48h (assumed), it expires and nothing changes. | There's no setup and no one can be stuck with a chore silently. |
| Undo | Completing, swapping and deleting a chore all get an undo toast. No "are you sure" dialogs. | Everything here can be reversed. |
| Saving | Every change saves immediately, with no Save button. | Same reason as undo. |
| Completion | Whoever finishes a chore can mark it done, and points go to whoever did it. | This avoids a "who gets credit" setting. |
| New member | They join the rotation at the next cycle, with default reminders. | No setup flow for them. |

## Real settings (keep these, about 6–7)
1. **My reminder time.** Default 18:00 (assumed). Per person, because people's days differ. Put it in the first-run step as a prefilled time with one tap to confirm.
2. **My quiet hours.** Default as above, per person. Put it beside the reminder time.
3. **Away until [date].** Skips you in the rotation and pauses your reminders. This is the one thing people really need to change often, so give it a button on the home screen.
4. **Who can edit chores and points.** Default: everyone, with a visible change history so mistakes are easy to spot and undo. Offer "organizer only" as one switch, not a per-field permission grid. Off by default because a household is a high-trust group.
5. **Rotation per chore.** Rotate or fixed person. Default is rotate. It lives on the chore, not in settings.
6. **Points on or off** (household level). Default on. Some households hate points, so hiding them completely is worth one switch.
7. **Notifications by channel.** Use the OS controls and link to them instead of rebuilding them.

## Cut or fold in
- Per-person reminder times for each chore: fold into the single reminder time in #1, with an optional per-chore override on the chore itself.
- Separate permissions for each action (who can swap, who can delete, who can edit points): collapse into the one switch in #4.
- Per-chore point values as a settings list: move onto the chore.
- Theme, time zone, week start: remove, as above.
- Anything where you can't say who would change it and why: cut for now. You can add it back if people ask. A week is short, and each setting you keep is a screen to build and test.

## First run (the only setup)
One screen, with everything already filled in: "Your reminder is 6 pm, quiet 10 pm–8 am. Chores start from a template list (dishes, trash, laundry, and so on, which they can edit). Looks good?" Then they invite people. No wizard. Everything else is reachable later from one short settings page, grouped as "Me" (reminders, quiet hours, away) and "Household" (permissions, points on/off), with a reset link for each default.

## Order for the week
1. Defaults and automatic behavior first (rotation, reminders, points seeding, swaps). Those are the product.
2. First-run screen and the "Me" settings.
3. Undo toasts and change history.
4. The "Household" settings last, since they're used least.

The default values above (18:00, 22:00–08:00, 1/3/5 points, 48h expiry) are my guesses. Treat them as starting points and change them once you see how real households use the app.
