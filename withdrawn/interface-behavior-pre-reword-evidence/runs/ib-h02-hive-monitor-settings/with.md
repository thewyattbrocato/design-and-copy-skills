**Assumptions:** The user is a hobbyist beekeeper on a phone, often outdoors at the hive, opening the app briefly and rarely. They touch settings a few times in the first week and almost never after that. I haven't seen the app or any data, so these are judgment calls. They aren't test results, and I'd treat them as hypotheses to check once you can get feedback.

## Changes, highest impact first

**1. New hives start with sensible alerts on.**
- **Rule:** When a hive is added, turn on a small recommended set, such as temperature out of range, hive weight drop (possible swarm), and sensor offline or low battery. Show a line like "Recommended alerts on · Customize" on the hive.
- **Why:** Defaults decide what most people experience. Switching on alerts one by one is likely a big source of "confusing", because a new user sees a silent app.
- **Detail:** Remember the last hive's alert choices and offer to reuse them for the next hive. Use your own thresholds (placeholders until you confirm them with whoever knows bee biology) and mark them as defaults.

**2. Apply settings immediately and drop Save and "Discard changes?".**
- **Rule:** When a toggle or field changes, save it right away and show nothing on success. If it fails, show the error in place and keep the old value.
- **Why:** Save-at-the-bottom on a 38-item page means people lose changes or don't know whether they applied. The discard popup is a symptom of that design.
- **Exception:** Number fields save when the field loses focus and the value is valid, not on every keystroke. Invalid values show an inline message with the allowed range.

**3. Remove "Are you sure?" on the temperature unit.**
- **Rule:** Switch the unit immediately and show the converted values everywhere. Add a short Undo toast only if you want a safety net.
- **Why:** The change is fully reversible. Convert any stored thresholds, so "35°C" becomes "95°F" rather than staying "35".
- **Better still:** Default the unit from the phone's region and show it as "Units: °F (from your phone)".

**4. Make "Reset everything" safe.**
- **Rule:** Move it out of the Save area to the bottom of an "Advanced" section, and rename it to say what it resets, for example "Reset alert settings to recommended". Offer separate resets per group where useful.
- **Confirmation:** Keep one specific confirmation, because a full reset can't be undone cheaply. Name what will change ("Resets 38 settings on all 3 hives. Your sensor data is kept."). Better, take a snapshot first and offer Undo for about 10 seconds, which lets you drop the confirmation.
- **Why:** A red destructive button next to the primary action invites accidents.

**5. Restructure the 38 settings by how often people use them.**
- **Rule:** Put a short top level of about five groups: Alerts, Hives and sensors, Units, Notifications, Account and sync. Each opens its own screen.
- **Alerts:** Group per hive, then per sensor, with a master switch for each. Within a hive, show the few common alerts first and put the rest under "More alerts".
- **Advanced:** Rarely touched items such as sync intervals and raw thresholds go in Advanced.
- **Search:** Add a search field at the top of Settings, since 38 items is enough to need one.
- **Scope:** Label each setting as "this phone" or "all your devices" where that matters (units and sync, for example).
- **Why:** The current engineering order means nothing is findable. Grouping by task is the cheapest big readability win, and it needs no research to justify.

**6. Show current state in the main view.**
- **Rule:** Put alert status and sync status on the hive screen, such as "3 alerts on · Last synced 2 min ago". Tapping it opens the matching settings.
- **Why:** Many people open settings only to check whether something is on. Showing it in place removes that trip.

## Things to leave alone
Keep the ability to configure every sensor alert and threshold. Power users will want it. Just move it behind "More alerts" and Advanced.

## Shipping without user testing
- **Sequence:** Items 1 to 4 are small, low-risk behavior changes that I'd ship first. The regrouping in item 5 is the biggest change, so it carries the most risk of confusing existing users.
- **Reduce the risk:** Keep setting names unchanged where you can, and use search to bridge the move. Consider a one-time "Settings moved" note, not a tour.
- **Check after release:** Add lightweight measurement. Useful signals are the share of new hives that keep alerts on after a week, how often people reset, and whether "confusing" shows up in new reviews. I haven't seen your numbers, so I won't guess targets.
- **Cheap review now:** Ask three or four colleagues or friends to find a specific setting on a prototype. It isn't proper testing, but it will catch obvious problems.

If you share the actual list of 38 settings, I can draft the grouping and the default alert set.
