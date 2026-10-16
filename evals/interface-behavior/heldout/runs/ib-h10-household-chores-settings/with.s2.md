**Assumptions:** 2–6 people in one home, mostly on phones, in short daily check-ins. Most members never open settings. One person (the organizer) sets the household up. I only have your categories, not all 24 options, so map your actual list onto the buckets below.

**The core problem:** "off or blank until set up" makes the app do nothing on day one, and most people never change that. Every option needs a working default. The first chore list should work after the organizer adds names and chores.

## 1. Just happens (no setting)

- **Rotation order:** Rotate round-robin through members. When someone completes a chore or its period ends, the next person is assigned automatically.
- **Skipping absent people:** Skip someone marked "away" and don't ask how to handle it. Show it on the chore ("Sam is away, assigned to Jo").
- **Points per chore:** Estimate from a size tag chosen when the chore is created (small, medium, large, e.g. 1/3/5). The points are *assumed* starting values, so tune them after you see use. Don't offer a per-chore number field up front.
- **Theme:** Follow the system light/dark setting. No theme option.
- **Time zone and week start:** Take them from the device.
- **Overdue handling:** A chore stays assigned and is marked overdue. It doesn't silently reassign or lose points. Show it in the main view.
- **Reminder timing, first version:** Send one reminder when a chore is due and one nudge later if it's still open. Both go to the assignee only.
- **Swaps:** A swap request goes to one person, who accepts or declines. Accepting moves the chore and points. No setting for this. The requester can cancel until it's accepted.
- **Undo:** Marking a chore done, swapping and deleting all get an Undo toast, not a confirmation. Only deleting the household or removing a member with history needs a specific confirmation.

## 2. Setting with a good default

| Setting | Default | Scope |
|---|---|---|
| Quiet hours | On, 22:00–08:00 (assumed, adjust to your users) | Per person |
| Reminder time of day | Morning at 09:00 for chores due that day (assumed) | Per person |
| Reminders on/off | On. Offer "mute for today/this week" in the notification itself | Per person |
| Rotation cadence | Weekly, with the household's first-set day | Per chore, set when creating it |
| Chore frequency | Choose when creating the chore (daily/weekly/monthly) | Per chore |
| Points visible to all | On | Household |
| Who can edit | Everyone can mark done, swap, and add chores. Only organizers can remove members or change points | Household |

Rules for these settings:
- They apply immediately and are reversible, with no Save button.
- Show what was assumed next to the control ("Quiet 22:00–08:00") and give a reset to defaults.
- Label each as per person or household, since mixing them up is the common confusion here.
- Ask for quiet hours and reminder time once, in a single prompt during join, with the defaults pre-filled. Don't send people to settings.

## 3. Cut or defer (not for week one)

- **Per-person reminder schedules, per-chore reminders, multiple reminders:** Keep one reminder time per person. Move the rest to "later" until people ask for it.
- **Custom rotation rules** (weighting, exclusions, fixed assignments): Offer just one escape hatch, "pin this chore to a person," and cut the rest. Add more when real households hit a specific need.
- **Granular permissions matrix:** Two roles (organizer, member) cover it. The 24-option version is probably several permission toggles that can collapse into this.
- **Point decay, bonus rules, streaks config:** Cut. Use fixed rules and tune them yourselves.
- **Anything that mirrors an internal option** with no user-visible effect.

If you apply this, I'd expect roughly 6–8 real settings, grouped as **My notifications** (quiet hours, reminder time, mute) and **Household** (permissions, points visibility, members). Put the household group behind the organizer role.

## One-week plan

1. **Days 1–2:** Set the defaults and the automatic behaviors (section 1), and get the app working with no settings touched.
2. **Day 3:** Build the join flow with a single pre-filled notification prompt.
3. **Days 4–5:** Build a two-group settings page with search unnecessary at this size, plus a reset.
4. **Days 6–7:** Test with one real household and watch which defaults they change. Those changes tell you which cut options to bring back.

If you paste the full list of 24, I'll sort each one into these buckets and flag the ones I'd merge.
