**Assumptions:** 2 to 6 people per household, mostly on phones, opening the app for a few seconds a day. One person sets it up and the others join by invite. I haven't seen your 24 options, so I'm working from the categories you named. The numbers below are starting values to test, not evidence.

## The main change
Don't ship "everything off until set up." The app should work as soon as someone names the household and picks chores from a starter list. Every option below has a default, and the default is what most households get.

## Should just happen (no setting)
- **Rotation:** Rotate in order each cycle, and skip anyone marked Away. Rotation is a property of each chore (rotate, fixed person, or anyone), chosen when the chore is created. It isn't a global rule set.
- **Point values:** Pick a size when creating a chore: Small 1, Medium 3, Large 5 (assumed). Don't ask for a number per chore. Allow a custom number only behind "Edit points" on the chore.
- **Overdue chores:** The chore stays with its owner, they get one nudge the next day, and nobody loses points. A penalty rule is a fight waiting to happen.
- **Swaps:** Anyone can propose a swap to anyone, and the recipient accepts or declines. A proposal expires after 48 hours (assumed), and the person who does the chore gets the points. Recipients are notified, and there are no swap settings.
- **Marking done:** The assignee marks it done. Anyone can mark it done for someone else, and the points go to whoever did it. Show an Undo toast, with no confirm dialog.
- **Weekly points view:** Show the current week and keep history. There's no reset option.
- **Time zone, locale, week start:** Take them from the device.
- **Theme:** Follow the system. Skip the theme setting unless someone asks, or tuck it under one "Appearance" row.
- **Swap and assignment notifications:** Always on. They're how the app works.

## Real settings (about 7, down from 24)
| Setting | Scope | Default |
|---|---|---|
| Reminder time | Per person | One reminder at 8:00 on the day a chore is due (assumed) |
| Quiet hours | Per person | 22:00 to 08:00. Reminders are held until it ends, not dropped. |
| Notification level | Per person | All mine. Other options: Only when due, Off. |
| Away mode | Per person | Off. Put it on the profile as an action with an optional return date. |
| Use points | Household | On. Turning it off hides points but keeps the data. |
| Who can change chores and points | Household | Everyone. Changes appear in an activity list and can be undone. |
| Appearance | Per device | System |

The "who can edit what" matrix should become one choice. The default is that everyone can add chores and mark chores done. An optional switch, "Only organizers can change chores and points," is off by default. Only organizers can remove members or delete the household, and that needs no setting. Most households trust each other. Visibility plus undo handles mistakes better than a permissions screen does.

## Cut or hold back
- **Per-chore reminder times and per-person-per-chore overrides:** Cut them. One time per person covers nearly everyone.
- **Custom rotation rules (weighting, skip patterns):** Hold them for later. Away mode covers the common case.
- **Per-event notification toggles:** Replace them with the three-level choice above.
- **Leaderboard options:** Cut them.

## Behavior rules
- **When a household is created**, show what was assumed next to the control ("Reminders at 8:00 · Change"). Don't open a settings interview.
- **When someone changes a setting**, apply it immediately and show an Undo toast. Don't add Save or Apply buttons.
- **When a household-wide setting changes** (permissions, points on or off), tell the other members in the activity list. The change is reversible, so it needs no confirmation.
- **Settings page layout:** Two groups, "Me" and "Household," each labeled with its scope. Add a "Reset to defaults" link on each group.
- **Quiet hours** apply automatically from first launch. Nobody opts in.
- **Reminders** use the device's local time, so travel doesn't break them.

## Build order for the week
1. **Days 1 to 2:** Defaults for rotation, points tiers, reminders, quiet hours, and swaps. Hard-code the values in one config so you can tune them.
2. **Day 3:** The 7-row settings screen, split into Me and Household, with undo.
3. **Day 4:** Away mode and the optional organizer-only switch.
4. **Days 5 to 6:** Test with two or three real households. Watch which defaults people change. Those are your next settings, and anything nobody touches stays hidden.
5. **Day 7:** Fix the defaults based on what you saw.

If you paste the actual 24, I'll sort each one into just happens, setting, or cut.
