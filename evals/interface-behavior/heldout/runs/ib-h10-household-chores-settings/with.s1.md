I haven't seen the actual 24, so this works from the categories you named. Send the list if you want an exact keep/cut/default call on each.

**Assumption:** a household of 2–6 people, mostly on phones, glancing at the app daily. One person sets it up and everyone else just uses it. The numbers below are starting values to test, not measured.

## Core rule
Nothing should be blank. A new household should get a working rotation, reminders and points from the first three taps. Settings are for overriding a good guess, not for making the app work.

## Keep as settings (about 6)

| Setting | Default | Scope |
|---|---|---|
| Reminder time | One daily time, 8:00 am, for chores due that day. An overdue nudge goes out the next morning. | Household default, with a per-person override |
| Quiet hours | On, 10 pm–7 am, in the person's local time | Per person |
| Rotation per chore | Rotate among everyone. Alternatives are "always this person" and "whoever's free". | Per chore, set where you edit the chore |
| Points per chore | Size-based: small = 1, medium = 2, large = 3. Editable inline on the chore. | Per chore |
| Who can edit | Everyone can edit everything. A single toggle, "Only organizers edit chores and members", is off by default. | Household |
| Notifications on/off | On, and asked for in context | Per person, per device |

For "who can edit", cut the per-feature permission matrix. Two roles are enough: organizer and member.

## Just happen, with no setting
- **Theme, time zone, week start, language:** follow the device. Don't build a theme picker.
- **Rotation advances** when a chore is completed, or when its due date passes. A new member joins at the end of the rotation.
- **Credit goes to whoever did the chore,** even if it wasn't their turn. Points follow the person, not the assignment.
- **Overdue chores stay with their owner.** They don't auto-reassign. The reminder escalates once, then stops. No repeat-count setting.
- **No repeated nags.** One reminder per chore per day, and chores due the same day are batched into one notification.
- **Swaps:** anyone can request one, and the other person accepts or declines in the notification. Unanswered requests expire after about 24 hours (a placeholder to tune), and the chore stays with the original owner. The only user-facing control is the Swap button.
- **Completion is undoable** with a toast. Points are recalculated on undo.
- **Absence:** an "I'm away until…" action on the person, not a setting. The rotation skips them and resumes automatically.
- **Points reset:** weekly totals roll over automatically, and all-time totals are kept.

## Cut or defer
Cut these for week one:
- Per-person point values
- Rotation direction or ordering rules
- Per-chore reminder times
- Snooze duration (fix it at one value)
- Reminder repeat count
- Any separate "points visibility" options

If real households ask for one of these later, add it then.

## First run (keep it to three steps)
1. Name the household and invite people by link. A person can be added without an account at first.
2. Check off chores from a starter list (dishes, trash, laundry, etc.), already sized S/M/L. Rotation and points are auto-assigned.
3. Done. Ask for notification permission right after the first assignment ("Get a reminder when it's your turn?"), not at launch.

Show what was assumed in context, for example "Reminders at 8:00 am · Quiet 10 pm–7 am · Change", rather than hiding it in a settings page.

## Settings screen
- Group it as **You** (reminder time, quiet hours, notifications), **Household** (default reminder time, edit permissions), and **Chores**. Chore settings live on each chore, not here.
- Changes apply immediately. Add a "Reset to defaults" link, and label each setting as per-person or household.
- At 6–8 items, search isn't needed.

## One-week plan
- **Days 1–2:** the defaults and the "just happens" logic. This is the biggest win.
- **Day 3:** first-run flow with starter chores.
- **Day 4:** the reduced settings screen and in-context permission asks.
- **Day 5:** swap flow, away mode and undo.
- **Days 6–7:** test with one real household. Watch which defaults they change, and promote or cut settings based on that.
