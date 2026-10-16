**Assumptions:** a household of 2–6 people, mostly on phones, opening the app briefly once or twice a day. One person sets it up and the others join by invite. You listed only some of the 24 options, so I've grouped by kind. Slot the rest into the same buckets.

**The main problem:** "everything off or blank until set up" makes setup the product. A household that skips it gets no rotation, no reminders and no points. The app should work from the moment the second person joins, and settings should only be for changing it.

## 1. Just happens (no setting)

- **Rotation order:** When a chore is created, rotate it round-robin through members in join order. Completing it, or the due date passing, hands it to the next person. This is the behavior people expect, and a rotation-rules screen is hard to explain.
- **Skipping people who are away:** Put "I'm away until [date]" on your own profile as one tap. The rotation skips you and resumes automatically. That replaces most "rotation rules" options.
- **Swaps:** Anyone can offer a swap on a chore. The other person gets one Accept/Decline prompt, and the offer expires on its own (assumed 48h, adjust). Don't add a setting for swap rules. The accept step is the safeguard.
- **Who can edit what:** Everyone can edit chores and everyone can swap. Fixed rules cover the rest: only the creator can delete the household or remove members, and members can only change their own reminders and away status. Show an activity log and offer undo on edits so mistakes are recoverable. A permissions matrix is the wrong tool for a household.
- **Theme:** Follow the system light/dark setting. Don't put it in the app.
- **Timezone and week start:** Take them from the device.
- **Quiet hours:** Respect the OS Do Not Disturb. Add a built-in default window (starting value 22:00–08:00, adjust) so nobody gets pinged at midnight. Expose it as one editable line in notifications, not a separate feature.
- **Overdue handling:** The chore stays with its person and shows as overdue in the main view. They get one follow-up reminder the next day, then nothing more. No auto-reassign and no nagging.
- **Notification channels:** Send one notification per event type, with no per-event toggles. Keep a single "mute this chore" action on the notification itself.

## 2. Default on or filled in, with a setting to change it

These are the real settings. Each one has a sensible starting value, and nothing blocks use until it's touched.

| Setting | Default | Scope |
|---|---|---|
| My reminder time | Morning on the day a chore is due (starting value 9:00) | Per account |
| Reminder on/off | On | Per account |
| Quiet hours | As above | Per account |
| Points visible / leaderboard | On, but see below | Per household |
| Point values | Size tiers, not per-chore numbers | Per household |
| Away until | Not away | Per account |

- **Point values:** Each chore gets a size picker (Small / Medium / Large) that maps to a starting 1 / 2 / 3. Per-chore number fields turn into 20 blank inputs. Let someone type a custom value from the chore's edit screen, and keep that off the settings page.
- **Leaderboard:** Some households won't want a ranked competition. Make it a single household toggle, "Show rankings." Points still accrue when it's off.
- **Reminder times per person:** Each person owns their own, set from their own profile. Don't make the organizer set them for everyone.

## 3. What to ask at first run

Ask three things at most, and let all three be skipped:

1. Household name.
2. Add chores, starting from a short suggested list (dishes, trash, laundry) that they can accept in one tap.
3. Invite people with a link.

Don't ask about points, reminders, rotation or theme. The defaults above cover them. Show what was assumed next to each control, for example "Reminds you at 9:00 on due days · Change," and offer a "reset to defaults" link.

## 4. Cut or defer

Anything left in the 24 that isn't above should be cut for now. That includes per-chore reminder overrides, custom rotation orders, custom point-decay rules, and per-person permission levels. If one of them matters to your household, build it after launch and put it behind a "More" section, not the everyday settings.

Result: about 6 visible settings, grouped as "Me" (reminders, quiet hours, away) and "Household" (points, rankings), with no required setup.

## Week plan

1. **Days 1–2:** Build the rotation, round-robin, away mode and swaps, since the app is unusable without them.
2. **Day 3:** Add default reminders, quiet hours and the overdue follow-up.
3. **Day 4:** Add points with size tiers and the rankings toggle.
4. **Day 5:** Build the settings page (about 6 items) and the first-run flow.
5. **Days 6–7:** Test with one real household and watch which defaults get changed. Those are your next settings. The ones nobody touches can stay hidden.

The starting values (9:00 reminder, 22:00–08:00 quiet hours, 48h swap expiry, 1/2/3 points) are my guesses, not data. Adjust them after your first test household.
