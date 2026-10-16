**Assumption:** The user is a hobbyist beekeeper on a phone, often standing at the hive. They open settings rarely, but they add a hive a few times a season and get alerts every day. They are not technical. You can't test with users, so I've ranked the changes by how likely they are to help and how cheap they are to revert.

## What I'd change, in priority order

**1. New hives start with sensible alerts on.**
- When someone adds a hive, turn on the alerts that matter for that sensor kit. Examples are hive temperature out of range, a weight drop (a possible swarm), and sensor offline.
- Put a line beside the alerts: "Recommended alerts are on. Change them anytime." Add a "Turn all off" link.
- Why: today a new hive does nothing until someone finds the switches. That is probably the most harmful thing here, because a missed swarm or cold snap is the real cost. Silent defaults also add to the "confusing" reviews.
- Pick the default thresholds with your beekeeping or sensor expert. I'm not inventing numbers here, so use placeholders until they confirm.
- Also remember the last hive's alert choices and offer them to the next hive ("Copy settings from Hive 1").

**2. Apply changes immediately and drop the Save button and "Discard changes?" popup.**
- When someone flips a toggle or edits a number, save it right away and show a small inline "Saved" state.
- For number fields, save when the field loses focus or the person taps Done. Check the range as they type and flag bad values in place, for example "Alert above 60°C isn't possible for a hive."
- If a change can't sync, say so in place ("Not synced, will retry"). Don't say anything on success.
- Why: the Save-at-the-bottom model on a 38-item page is how people lose edits. The discard popup exists only because of that model.
- Exception: if any setting changes what happens to other people, such as sharing a hive with a family member, give that one an explicit Apply.

**3. Remove "Are you sure?" on the temperature unit.**
- Switch the units immediately and convert the displayed values and thresholds. Show a toast with Undo for about 6–10 seconds, announced to screen readers.
- Why: it is fully reversible, so a question adds friction and no safety.
- Default the unit from the phone's region, and say so beside the control ("Set from your phone's region").
- Convert stored thresholds exactly and keep the underlying value in one unit. Otherwise toggling back and forth drifts the numbers.

**4. Move or remove "Reset everything".**
- Take it off the main page, away from Save. It should be a plain text link at the very bottom of an "Advanced" section.
- Make it specific: "Reset alert thresholds to defaults." Use separate resets per group rather than one global reset.
- If the reset can be undone by restoring a snapshot, use the Undo toast, not a confirmation. If it can't, for example because it deletes history, use one confirmation that names what goes ("Deletes readings for 3 hives. This can't be undone.").
- Why: a red destructive button next to the primary action is an accident waiting to happen. It also teaches people to hit the area near Save.

**5. Reorganize the 38 items by how often people touch them.**
Use a short top-level list of groups, each opening to its own screen:
- **Alerts** (per hive, then per sensor)
- **Hives and sensors** (names, adding, pairing)
- **Units and display**
- **Notifications** (how and when, such as quiet hours)
- **Account and sync**
- **Advanced** (reset, export, diagnostics)

Details:
- Put the highest-use group (alerts) first, not in the order engineering added things.
- Inside Alerts, make one row per sensor with a single on/off switch. Show the threshold on that row ("Hive temp: 32–36°C"). Tap the row to edit the threshold on its own screen.
- Say whether each setting is per hive, per device or per account. Alert thresholds are probably per hive. Units are probably per account or device.
- Add search at the top of settings, since 38 items is enough to justify it.
- Hide rarely used options (calibration offsets, sync intervals) behind "Advanced" instead of deleting them.

**6. Reduce what's a setting at all.**
- Fold sync options into one choice, such as "Sync: automatic" with a manual "Sync now" action, unless there is a real reason people need an interval.
- Merge per-sensor notification toggles into the alert rows. An alert and its notification are one thing to the user, so don't make them two settings.
- Review each of the 38 for "would a beekeeper ever change this?" Anything that is only an internal detail should get a good default and move to Advanced, or go away.

## What I'd leave alone
- The fields and thresholds themselves. I can't tell from the description which are wrong, so I won't guess.
- Any platform-standard behavior your OS toggles already provide.

## Low-risk ship order
Since you can't test with users, ship the changes that remove failure modes first:
1. Alerts on by default for new hives
2. Remove the unit popup (with Undo)
3. Move the reset button away from Save
4. Autosave
5. Regrouping the page

Items 1–3 are small changes. Autosave and regrouping are larger, so do them next. If the release is tight, do just 1–3.

## How to check it worked without user testing
- Watch the review text for "confusing", "lost my settings" and "didn't get an alert" after release.
- Track in your analytics how many new hives still have zero alerts on after a day, how often people use the Undo on the unit change, and how often the reset is used. I don't have your current figures, so record a baseline first.
- Keep the old screen behind a flag for one release, so you can roll back.

If you can tell me which of the 38 settings exist and which sensors the kit has, I can draft the grouping and the default alert set in detail.
