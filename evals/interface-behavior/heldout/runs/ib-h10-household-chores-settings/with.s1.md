**Assumption:** a household of 2–6 people, mostly on phones, opening the app briefly a few times a day. Nobody wants to administer it. I only have your category names, not the full list of 24, so map your actual options onto the buckets below. All numbers are starting values to adjust, not data.

## The core fix
"Everything is off or blank until someone sets it up" means the app does nothing on day one, and most households will never configure it. Ship defaults that work immediately, so the settings screen is only for changing things.

## What should just happen (no setting)
- **Rotation:** when someone is added or removed, rebuild the rotation automatically. Use round-robin, skip anyone marked away, and carry over a chore that was missed.
- **Reminders:** send one reminder on the due day. Stop it once the chore is done or swapped. Don't nag people who've already finished.
- **Points:** award them on completion. Compute them from a chore's size (small/medium/large), not a free number.
- **Swaps:** one tap to offer, one tap to accept or decline. If nobody responds, the offer expires and the chore stays with the original person. Put Undo on the swap, since it's reversible.
- **Theme:** follow the system setting.
- **Time zone and week start:** take them from the device and household locale.
- **Quiet hours:** apply the phone's own Do Not Disturb. Add a default of roughly 9pm–8am for reminders, but don't ask during setup.
- **Sync, history and completion state:** save automatically and show nothing on success.

## Defaults to ship (visible and resettable)
| Area | Default |
|---|---|
| Reminder time | One household default, such as 9am on the due day. A per-person override is optional (see below). |
| Chore size to points | Small = 1, medium = 2, large = 3 (placeholders). Starter chores come pre-sized. |
| Rotation | Weekly, round-robin, and the chore stays with its assignee until done. |
| Who can edit | Everyone can mark done, swap, and add chores. Only the household creator, or anyone they promote, can remove members or change rotation rules. |
| Notifications | Own chores, swap requests, and "someone completed your swapped chore." Everything else is off. |
| Overdue | One gentle follow-up the next day, then stop. |

Preload a starter chore list (dishes, trash, laundry, and so on) so the first screen isn't empty. Show a one-line summary like "Reminders at 9am, rotating weekly" next to the control that changes it.

## What should actually be a setting
Keep roughly 6–8, grouped by how often people touch them:

1. **My reminder time** (per person, account-level). It's the one thing that really differs between people.
2. **My quiet hours** (per person), with the default above.
3. **Away or on vacation** (per person). This is a toggle or date range, and the rotation skips them.
4. **Rotation frequency** (household): daily, weekly, or custom per chore.
5. **Chore size or points** (per chore), edited inline on the chore, not on a settings page.
6. **Who can edit** (household), reduced to two roles: member and admin.
7. **Notification types** (per person), with three or four toggles.
8. **Theme** (per device), only if you want an override. Otherwise cut it.

Everything else is either automatic or goes below.

## Cut or hold back
- **Per-chore reminder times and per-person-per-chore anything.** This combinatorial setting is where 24 options come from. Use one household default plus one personal override.
- **Free-form point values.** Use sizes. Allow custom numbers later if people ask.
- **Granular permission matrices** ("who can edit points," "who can edit reminders," and so on). Use member and admin.
- **Advanced rotation rules** (weighted, skip rules, fairness balancing). Hold these back behind an "Advanced" link, or ship them after launch. Don't delete the code if it's built.
- Anything you can't explain in one sentence to a housemate.

## Behavior rules
- **Reversible settings apply immediately** with an Undo toast. Only changes that affect others need confirmation. For example, changing the rotation could show "This reassigns 6 chores for everyone," with a specific Apply button.
- **Run versus configure:** the "Done" button uses remembered options. Settings are a separate link.
- **Label scope:** mark each setting "just you," "this device," or "whole household."
- **Add a "Reset to defaults"** per group.
- **Setup is one screen:** the household name and who's in it. Everything else is inferred, and the starter list is editable in place.
- **Only ask about a conflict:** if two people's reminders or quiet hours conflict with a due time, show it where the chore is, not in a dialog.

## A week
- **Day 1:** sort the 24 options into automatic, default, setting, or cut. Be strict.
- **Days 2–3:** implement defaults, the starter chores, and the one-screen setup. This delivers most of the value.
- **Day 4:** build the settings screen with 6–8 options and scope labels.
- **Day 5:** swap flow with expiry and Undo, and the away toggle.
- **Days 6–7:** test with one real household for a few days. Watch which defaults get changed. Those are your real settings, and the rest can stay hidden.

If you paste the actual 24, I'll sort them one by one.
