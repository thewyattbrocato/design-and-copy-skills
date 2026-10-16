**Assumptions:** The user is a hobbyist beekeeper on a phone, often outdoors at the hive. They open settings rarely, and most of them want the kit to work and alert them when something is wrong. I'm assuming the platform can undo a settings change. Any numbers below are starting values to adjust, not data.

## Changes, in priority order

**1. Turn on sensible alerts by default for new hives.**
- When a hive is added, turn on the alerts that matter most for bees and set sensible thresholds. Likely candidates are low or high temperature, a sudden weight drop (which can mean a swarm), and a sensor offline. Pick the exact values with a beekeeping advisor. I haven't invented any here.
- Show a line such as "Standard alerts on for this hive. Change" so the assumption is visible.
- Remember the user's last alert setup and offer it for the next hive: "Copy alerts from Hive 1?"
- Why: all-off means a user who never opens settings gets no warnings. That is the most costly failure in this app. Switching things on one at a time across several hives is also the most tedious part of setup.

**2. Remove Save and the "Discard changes?" popup. Apply changes immediately.**
- Toggles and fields take effect when changed. Show a brief inline "Saved" state or a quiet toast with Undo, lasting about 6 to 10 seconds, and pausing on focus.
- Validate number fields in place, for example "Must be between X and Y". Don't apply an invalid value.
- Why: nearly everything on this screen is reversible. Leaving without saving silently loses work, and the discard popup only papers over that.
- Exception: if some change affects the kit hardware (a firmware or sync-interval change that needs the device connected), give it an explicit Apply with a visible pending state. Show a clear failure message if it doesn't reach the device.

**3. Remove the temperature-unit "Are you sure?".**
- Switch the unit immediately and convert displayed values. Convert the stored alert thresholds too, so "35°C" becomes "95°F" rather than staying "35".
- Default the unit from the phone's locale.
- Why: it's fully reversible, so the popup only adds friction. The real risk is thresholds silently changing meaning, and conversion fixes that.

**4. Reorganize the 38 settings by how often people touch them.**
- **Top level, a few rows:** Hives (each with its alerts), Notifications (on/off, quiet hours), Units, Account and sync.
- **Per-hive screen:** the sensor alerts for that hive, each with a plain-language summary like "Temperature: alert below 10° or above 38°". Tapping opens the threshold. Per-sensor notifications belong here, next to the sensor.
- **Advanced:** rarely touched items such as sync intervals and diagnostics.
- Add search if the list still exceeds a few dozen rows after regrouping.
- Label each setting as per device or per account.
- Why: the current engineering order means users must learn the codebase's history to find anything. That is the main source of "confusing". You can do this without user testing by sorting each setting into used often, rarely, or never by an ordinary user.

**5. Cut settings that shouldn't be settings.**
- Go through the 38 and ask of each: could the app pick a good value, or infer it? Fold the ones that are internal options into defaults or Advanced. This is likely to shrink the visible list considerably. I can't tell you how many without seeing the list.

**6. Make "Reset everything" safe and quiet.**
- Move it off the Save area, to the bottom of Advanced, styled as a plain text link rather than a red button.
- Replace it with narrower resets such as "Reset alerts for this hive to standard".
- If a full reset stays, it needs one specific confirmation, because it can't be undone. Say what goes ("Alert thresholds and preferences for all 3 hives. Your sensor history is kept."). Use a labeled button like "Reset settings" rather than "OK". Ideally, offer a short Undo window or a restorable snapshot, which would let you drop the confirmation.
- Why: it's the one destructive control, and it sits where a thumb lands after Save.

## Checks you can do without user testing
- **Walkthrough:** have someone unfamiliar with the app (a colleague, or a beekeeper friend) add a hive and change one threshold while you watch. Even three people is informal feedback, not proof.
- **Support tickets and reviews:** tag the "confusing" reviews by setting. They'll show which of the 38 matter most. I haven't seen them, so I can't tell you what they say.
- **Safe rollout:** ship the autosave and defaults changes behind a flag if you can, and watch for support contacts about missing or unexpected alerts.

## Order if the release is tight
1. Alert defaults for new hives (#1).
2. Remove the two popups (#2, #3).
3. Move and soften Reset (#6).

These are small, low-risk changes. The regrouping (#4, #5) is bigger and can follow, though it is likely the biggest fix for "confusing".

If you share the list of 38 settings, I can sort them into the groups above and flag which ones to drop.
