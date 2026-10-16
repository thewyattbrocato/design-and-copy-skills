Without user testing, I'd stick to changes that are well-established UX practice and easy to undo. In priority order:

## Do before this release

1. **Group the 38 settings and put the common ones first.**
   - Split the page into 5-6 labeled sections, ordered by how often people touch them. For example: Alerts, Sensors, Units, Sync, Notifications, Account/Advanced.
   - Use collapsible sections or a short top-level list that opens sub-screens. Sub-screens are better if your layout allows them.
   - Ordering by the order engineering added things is almost certainly the main cause of "confusing", and this change carries almost no risk.

2. **Save changes as they're made.**
   - Toggles and unit pickers should apply immediately, which is the platform convention on iOS and Android.
   - That removes the Save button and the "Discard changes?" popup together. Show a brief "Saved" confirmation.
   - Keep an explicit Save only for number fields with validation, such as alert thresholds. Even there, saving on blur with inline validation is usually better.
   - If immediate apply is too big a change for this release, keep Save but make it sticky and disabled until something changes. Then the discard prompt only fires when there are real unsaved edits.

3. **Remove the "Are you sure?" on the temperature unit.**
   - It's trivially reversible, so the prompt only adds friction and makes people doubt a harmless choice.
   - Show the converted values in place so people can see the effect. If they've set thresholds, convert them automatically and say so ("Threshold changed from 95°F to 35°C").

4. **Make new hives start with sensible alerts on.**
   - Turn on a small recommended set by default, such as temperature out of range, a weight drop (possible swarm), and low battery. Say so on the screen: "We've turned on recommended alerts. Customize."
   - Leave noisy or niche alerts off.
   - Add a one-tap "Copy alert settings from another hive" for people with several hives.
   - This is probably the change that most affects whether the product feels useful. Today a new user can easily go weeks without alerts and not realize it.

5. **Isolate and protect "Reset everything".**
   - Move it to the bottom of an Advanced or Account section, away from Save, and make it less prominent.
   - Rename it to say what it resets. It may mean settings, hive data, or both, and those are very different.
   - Use a confirmation that names the consequence, with a button labeled for the action ("Reset all settings") rather than a generic OK. For anything that deletes data, require typing a word or a long press.
   - A red button next to Save is a real risk of accidental data loss, so I'd treat this as a must-do.

## Worth doing if time allows

- **Plain-language labels and helper text.** Replace internal names like "Sensor 2 thr_hi" with what the setting means ("Alert me if hive temperature goes above..."). Add the unit next to every number field and show sensible-range hints.
- **Search or a short "common settings" list** at the top, if you can't restructure fully.
- **Hide per-sensor notification toggles** behind one master switch per category, with "Customize per sensor" expandable.
- **A "Restore defaults" per section**, so people don't need the global reset.

## Making this safe without user testing

- **Ship it in stages.** Grouping, removing the unit popup and moving Reset are low risk. Autosave and default-on alerts change behavior, so put them behind a feature flag or a staged rollout if you can.
- **Add basic instrumentation:** which settings get opened, how often Reset is tapped, how many hives have at least one alert on, and support tickets tagged "settings". You'll then have real data for the next release.
- **Mine what you already have.** Read the 'confusing' reviews and support tickets and tally which settings or tasks they mention. That is cheap, and it may show that two or three specific items cause most of the confusion.
- **Run a quick internal check.** Have 3-5 people outside engineering, ideally one actual beekeeper, try to complete tasks like "make me get an alert if the hive gets too cold". It takes under an hour and isn't formal testing, but it will catch the worst problems.

## Caveats

- **Default-on alerts** can annoy people if they're too sensitive. Pick conservative thresholds and make it easy to turn them off.
- **Autosave on number fields** can save half-typed values. Validate before applying.
- I haven't seen the actual screen or review text, so the ordering of sections is a guess. Use the review and ticket tally to check it.

If you share the 38 settings and a sample of the reviews, I can draft the section grouping and the label rewrites.
