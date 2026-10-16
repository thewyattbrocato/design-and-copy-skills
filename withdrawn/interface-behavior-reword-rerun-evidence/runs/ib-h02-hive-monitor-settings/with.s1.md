**Assumption:** The user is a hobbyist beekeeper on a phone, often standing at the hive with gloves on or in sun glare. They open settings rarely, mostly when adding a hive or after an alert annoys them. Nobody has tested any of this, so I'd ship changes that are easy to undo and avoid anything that depends on guessing behavior.

## Changes, in priority order

**1. New hives start with sensible alerts on.**
- **When** a hive is added, **do** turn on a small default set (for example temperature out of range, and hive offline). Show "Using recommended alerts" next to the list, with a link to change them and a "Restore recommended" action.
- **Why:** this is the biggest cause of "confusing" I can see. Today the app looks broken until someone sets up alerts one by one. A beekeeper can't judge thresholds, so defaults need to come from you. The threshold values are for your bee and sensor people to pick. I have no numbers to offer.
- **Also:** copy the last hive's alert settings as the starting point for the next hive. Show "Copied from Hive 1" so the assumption is visible.

**2. Save automatically and drop the Save button and "Discard changes?" popup.**
- **When** a toggle or value changes, **do** apply it immediately and show a quiet "Saved" indicator in place only if it fails or is delayed. Show a toast with Undo (about 8 seconds, pauses on focus, announced to screen readers) for changes that alert thresholds.
- **Why:** the discard popup exists only because of the Save model. Every setting here is reversible, so none of it needs a gate.
- **Exception:** number fields should commit on blur or Done, not on every keystroke. Out-of-range values should be flagged in place and not applied.
- **If you can't remove Save this release:** at least keep edits as a draft when someone leaves, with a "Unsaved changes" banner at the top and no modal.

**3. Remove the "Are you sure?" on temperature unit.**
- **When** the unit changes, **do** switch immediately and show the new value in the row, such as "°F: alert at 95°F". Offer Undo.
- **Why:** it's fully reversible, and the popup makes a trivial choice look dangerous.
- **Better still:** set the unit from the phone's locale at first run so most people never touch it. Keep the thresholds stored in one unit internally and convert for display, so switching never changes what the alert actually means. Check that this is how it works today.

**4. Make "Reset everything" hard to hit.**
- **When** the screen loads, **do** move it to the bottom of an "Advanced" or "Data" group, away from any primary control, in plain text and not red-filled.
- **When** tapped, **do** show one specific confirmation: "Reset all settings for all hives? Alert thresholds, units and sync settings return to defaults. Hive history is not deleted." (Fix that sentence to match what it really does.)
- **Why:** this one can't be undone, so it's the one place a confirmation earns its keep. If you can store the previous settings for a short time, an Undo toast is better than the dialog.
- **Also:** consider splitting it into "Restore recommended alerts" (the common need) and a rarer full reset.

**5. Restructure the 38 items by what people do, not the order engineering added them.**
- **Top level, 5 to 6 rows at most**, each opening a sub-screen:
  - Hives (pick one, then its alerts and sensors)
  - Alerts and notifications (how you're told: push, quiet hours)
  - Units
  - Sync and devices
  - Account
  - Advanced (reset, diagnostics)
- **Per-sensor settings** live under each hive, with a summary on the row, such as "Temperature: on, 35°C max". People can see state without opening anything.
- **Move rarely used toggles** into "Advanced" instead of deleting them.
- **Add search** over settings if the count stays above about 30.
- **Mark each setting** as per hive, per device or per account.
- **Why:** an unordered page of 38 items is the other half of "confusing". Grouping is the fix with the least risk because it removes no function.

**6. Cut the settings that shouldn't be settings.**
- Go through the 38 and sort each as: (a) must be user-controlled, (b) has a good default, hide it, (c) engineering knob, remove it. I'd expect many in (b) and (c), such as sync intervals and per-sensor notification duplicates. A single "notify me about this hive" master switch with per-sensor overrides underneath removes a lot of rows.
- This is the riskiest change without testing, so do it last and only for items you're confident about.

## What I'd ship before the release

With no user testing, take the lower-risk changes: 1, 2 (or the draft fallback), 3 and 4. They remove friction without changing what any setting does. Do the regrouping in 5 if the engineering time is there, since it only moves things. Leave 6 for a later release, when you can compare against real usage.

## How to check without a test

- Have 3 or 4 people who've never seen the app, ideally colleagues' family members, add a hive and turn on a temperature alert, and watch where they hesitate. That takes under an hour and isn't a formal study.
- Look at existing reviews and support messages for which settings are named. That tells you which of the 38 to put first.
- Log, without personal data, how often each setting is changed after release. That gives you real evidence for step 6.

If you can share the full list of 38 settings, I can sort them into groups and mark which should be defaults, hidden or removed.
