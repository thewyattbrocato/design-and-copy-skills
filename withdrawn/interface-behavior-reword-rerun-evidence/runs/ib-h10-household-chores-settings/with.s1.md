**Assumption:** a household of 2–6 people, mostly on phones, opening the app briefly once or twice a day. Most of them never open Settings. A week means the defaults have to carry the product.

## Main change: nothing starts blank

"Off or blank until set up" makes every person configure the app before it works. Each option should either ship with a working default or be removed. Setup should be one short step: household name, member names, and the chores to start from.

## Things that should just happen (no setting)

| Behavior | Why |
|---|---|
| Rotation advances automatically when a chore is done or its period ends | Rotation is the core of the app. Making it opt-in defeats the point. |
| Points are awarded on completion | The user shouldn't have to approve anything. |
| Reminders go to the person whose turn it is | Everyone else gets nothing. |
| Time zone and locale come from the device | The product already knows them. |
| Theme follows the system light/dark setting | The OS already records this choice. |
| Completed chores can be undone from a toast for about 10 seconds | Mistakes are cheap, so there's no "are you sure?". |
| Overdue chores stay with their owner and show as overdue | There's no need to ask what to do about late chores. |
| Sync, ordering, and remembering the last-used filter | These are internal details. |

## Things that need a default plus a way to change it

| Setting | Default | Notes |
|---|---|---|
| Reminder time | One household default, say 9am day-of (assumed, so test it). | Per-person override lives in each person's own profile, not in a household table. |
| Quiet hours | On by default, 10pm–8am, no reminders. | This is the one most likely to cause a deleted app if missing. |
| Point value per chore | Three tiers (small/medium/large = 1/3/5, assumed). Each chore starts at "medium". | Choose a tier when adding a chore. Don't show a numeric field per chore. |
| Rotation rule | Round-robin. | Offer "fixed person" per chore as the only alternative. |
| Swap | Anyone can request. The other person accepts with one tap. Unanswered requests expire in 48h (assumed). | Both people must agree, so no admin is needed. |
| Who can edit | Everyone in the household can edit everything. | Households are high trust. Add one "adult/organizer" role only if users ask for it. |

## What to cut or defer

- **Per-chore reminder times:** use one household default plus a per-person override.
- **Granular edit permissions** (who can edit what): replace them with the single default above, and revisit after launch.
- **Numeric point values per chore:** use the three tiers.
- **Several rotation rules:** ship round-robin and fixed-person only.
- **Extra display options** (density, sort, etc.): remove them, or remember the last choice silently.

Doing this should take 24 options down to about 6–8. These are household-level: reminder time, quiet hours, swap expiry, and the member list. These are personal: reminder override, notification on/off, and theme override.

## How the Settings screen should work

- **Two groups:** "Me" (device or account-level, labeled as such) and "Household" (shared, and changing it affects everyone).
- **Apply immediately** with an Undo toast for reversible changes. Household changes that affect others, such as removing a member, get one specific confirmation naming what changes.
- **Show the current default beside each control** ("Reminders at 9:00 am"), plus a "Reset to default" link.
- **Notify the household** when someone changes a shared setting, so changes aren't silent.

## Week plan

1. **Days 1–2:** decide the defaults above and build the one-step setup.
2. **Days 3–4:** implement automatic rotation, points, reminders, quiet hours and swap with those defaults.
3. **Day 5:** build the cut-down Settings screen.
4. **Days 6–7:** test with one real household using only the defaults, and note which settings they reach for.

The numbers (9am, 10pm–8am, 1/3/5 points, 48h expiry) are my starting guesses, not data. The test week should confirm or change them.
