**Assumption:** Household of 2–6 people, mostly phones, glanced at daily. One person (the setup person) configures it and everyone else just uses it. I don't have your 24-option list, so I'm sorting by the categories you named. Move anything I don't mention using the same tests.

## The test for each option

- **Remove it:** a sensible answer exists for nearly every household, or the app can learn it.
- **Keep it, with a default:** households really differ, a wrong default is annoying, and the change is reversible.
- **Ask once:** the app can't know it and a wrong guess is costly. This should be 2–3 things at most, all during setup.

## What should just happen (no setting)

| Option | Behavior | Why |
|---|---|---|
| Rotation order | Round-robin through members in the order they joined. Skip anyone marked away. | Almost everyone wants fair turns. |
| Rotation timing | The next person takes over when the chore is completed or its period ends. | One rule is easier to explain than three. |
| Missed chore | It stays with the same person and shows as overdue. The group sees it, and the owner can swap or skip. | Silent reassignment feels unfair. |
| Swap | Either person taps "Swap", picks a person, and that person gets a notification. The swap happens on accept. It expires after 48h (assumed value). | This is a request/accept flow, so it needs no setting. |
| Undo completion | A toast with Undo, and a "mark not done" action later. | Mistaken taps are common. This replaces any "who can undo" setting. |
| Reminder times per person | Don't expose a time picker per person. Send one reminder at a fixed time on the due day, and one more only if the chore is overdue. | Per-person scheduling is the most expensive item to build and the one people ignore. |
| Reminder channel | Use push. If notification permission is denied, show an in-app banner. | Nobody wants to configure this. |
| Theme | Follow the system light/dark setting. | The OS already holds this preference. |
| Time zone | Use the device's time zone. | The app already knows it. |
| Points scale | Start every chore at a derived value, such as 1 point per ~10 minutes of estimated effort, bucketed into 1/2/3/5. Chore templates carry these values. | Nobody wants to invent 30 numbers. |
| Notification for "someone completed X" | A quiet in-app feed entry, not a push. | Push for other people's actions becomes noise quickly. |

## What stays a setting (with defaults)

| Setting | Default | Scope |
|---|---|---|
| Quiet hours | On, 22:00–08:00 (starting value). Reminders are held until the end of quiet hours. | Per person |
| Reminder time | Morning, 09:00 (starting value). This is one time per person and replaces the per-chore, per-person grid. | Per person |
| Point value per chore | Template default. An edit field sits on the chore itself, not in settings. | Per household |
| Points on or off | On. If the household turns them off, hide points and the leaderboard everywhere. | Per household |
| Chore frequency and who's in the rotation | Set when you create the chore. | Per chore |
| Who can edit chores | Everyone can add and edit. Offer an optional "admin only" toggle for households with kids. | Per household |
| Away mode | Off. A person can set "away until [date]". | Per person |

**Per person** means it follows that person across devices. **Per household** means anyone with permission can change it, and it applies to everyone. Label each one that way in the UI.

## What to ask during setup (3 questions, all skippable)

1. Who's in the household? (Needed. Invite by link.)
2. Pick starter chores from a template list. This sets the chores, frequencies and point values together.
3. Do you want points and a leaderboard, or just a rotation? (This sets the points toggle.)

Everything else gets its default silently. Show what was assumed beside the control ("Reminders at 9:00 · change"), and put a "Reset to defaults" in settings.

## What to cut to fit the week

- **Cut for v1:** per-chore reminder overrides, custom rotation rules (weighted, random, fixed), per-chore permissions, and custom themes. If you have 24 options, I'd expect about 8–10 to fall into these groups.
- **Hold back, don't delete:** advanced rotation rules. Add them if the first households ask.
- **Apply immediately:** all of the settings above. They're reversible, so skip the Save button and show an Undo toast. The exception is "admin only" editing, which affects others, so it should have an explicit confirm that names who loses access.

## Settings screen layout

One screen, three groups, ordered by how often people touch them:

1. **Me:** reminder time, quiet hours, away mode.
2. **Household:** points on/off, who can edit, members.
3. **Advanced** (collapsed): anything left over, plus reset.

With around 8 settings, you don't need search.

## Where I'd spend the week

1. Days 1–2: the default behaviors above (rotation, swap, undo, overdue). This is where the app's value is.
2. Day 3: setup flow with the 3 questions and chore templates.
3. Day 4: reminders with quiet hours and the permission-denied fallback.
4. Day 5: the settings screen.
5. Days 6–7: test with a real household, and fix whichever default they changed first.

All numbers here (22:00–08:00, 09:00, 48h, point buckets) are starting values I've assumed, not measured figures. Check whether people change them in your first test households.

If you paste the actual 24 options, I can sort each one into these buckets.
