**Assumptions:** a household of about 2–6, mostly on phones, opening the app daily to glance at "what's mine". One person sets it up and the others join by invite. I haven't seen your 24 options, so I've worked from the categories you named. Every number below is a starting value, not something I've measured.

## The core problem

"Off or blank until someone sets it up" means the app does nothing until a person configures it. A household where only one person finishes setup gets no reminders for everyone else, and nobody finds out why. Every option should work on day one and be something you can change later.

## What to do with each option

| Option | Verdict | Default |
|---|---|---|
| Rotation rule | **Just happens.** Round-robin, skipping anyone marked Away. | Rotates when a chore is done, or when its due date passes. |
| Per-chore override (fixed person, or everyone) | **Per-chore field**, not a setting. It sits in the chore editor. | Rotate. |
| Point values per chore | **Per-chore field** as a Small/Medium/Large picker, not a number box. | Starter chores come pre-sized, for example 1/2/3 points. |
| Points period and reset | **Just happens.** | Weekly tally, with history kept. |
| Reminder time | **Personal setting**, kept on the user's own device or account. | One reminder at 8:00 on the due day, plus one nudge the day after if overdue. |
| Reminder on/off per type | **Cut.** Keep one master switch for reminders. | On. |
| Quiet hours | **Personal setting.** | On, 21:00–08:00. Reminders held until it ends, not dropped. |
| Swap | **Just happens.** A "Can't do this" button on the chore offers it to the next person. | If nobody answers in 24 hours (assumed), it reverts to the original person and tells them. |
| Away / vacation | **Real setting**, the most useful one. Put it on the member's row. | Off. Auto-ends on a date they pick. |
| Who can edit what | **Collapse to one toggle**, admins only. | Anyone can edit chores and mark done. Only admins manage members or delete the household. Show edits in an activity list, each with Undo. |
| Theme | **Follow the system.** | System. Keep an override only if it's cheap. |
| Time zone, week start, 24h clock | **Just happens.** Take them from the device and locale. | Device values. |
| Completion attribution | **Just happens.** Anyone can mark a chore done for someone else, and it records who did it. | Undo toast. |

For any of your other options, ask whether two reasonable households would pick different answers. If they wouldn't, it isn't a setting. If the choice is really about one chore, put it in the chore editor.

## Result

- **Settings screen:** about 5 items in two groups.
  - *Me:* reminder time, quiet hours, theme.
  - *Household (admins):* the edit-permission toggle, and members with Away.
- **Chore editor:** assignee rule and size.
- **Everything else:** hard-coded defaults.

## Rules

- **At first run, ask only for member names (or an invite link) and chores.** Offer a starter list to tick, such as dishes, trash, laundry and bathroom. Everything else defaults, because the first task should produce a working rotation.
- **Show assumptions where people already look.** For example, a line under the chore list says "Reminders at 8:00 · change". Changing it is a small link, not a trip into settings.
- **Apply changes immediately with no Save button.** Put a "Reset to defaults" at the bottom. Reversible settings need no confirmation.
- **Make quiet hours hold, not drop.** A dropped reminder looks like a broken app. A held one arrives at 8:00.
- **Make swaps cheap to undo and cheap to decline.** The requester sees "Waiting on Sam" in the chore row. The recipient gets one notification with Accept and Decline. If nobody responds, the chore reverts, so a swap never leaves a chore with no owner.
- **Never silently reassign an overdue chore.** It stays with its owner, who gets one nudge. After a couple of days (assumed), it offers "Swap?" to that person.
- **Deleting a chore moves it to an archive, with an Undo toast.** No "Are you sure?" popup. Points already earned stay.
- **Notifications:** Use one push for a reminder or swap request. Don't send "saved" or "done" confirmations. Show state in the list itself (done, overdue, waiting on swap).
- **Accessibility:** the swap, done and undo actions need visible buttons, not swipe-only gestures. Undo toasts are announced to screen readers and last at least 6–10 seconds.

## One-week order

1. **Days 1–2:** the defaults, the rotation and the reminders. Nothing else matters if these don't work out of the box.
2. **Day 3:** swap flow, with the 24-hour revert.
3. **Day 4:** Away, quiet hours, and the personal reminder-time link.
4. **Day 5:** the permission toggle and activity list with Undo.
5. **Days 6–7:** test with one real household. Cut anything they asked about but never changed.

## Open questions

These would change the design:
- **Kids in the household:** they may need a different view, and parents might need to approve their completions.
- **Whether points matter:** if they're a game, you may want a visible leaderboard. If they're only a fairness tally, make them quieter.
