**Assumptions:** Your users are hobbyist beekeepers on phones, often outdoors at the hive with gloves or one hand free. They open the app briefly and often to check on a hive. They touch settings rarely, mostly right after setup. Nothing here is based on usage data, since you have none.

## What I'd change

**1. Cut the number of settings people see before you cut the toggles.**
- When someone adds a hive, ship sensible alert defaults, because 38 controls are a symptom of missing defaults.
- Keep a short "Essentials" group with a few items: temperature unit, which hive alerts matter, and notification on/off.
- Move everything else under "Advanced". Hold costly or rare items there rather than deleting them.
- Add search at the top of settings, since the list is long.

**2. Regroup by task and by how often people touch each setting.**
- Replace the engineering order with groups such as Alerts, Units, Sync & account, and Notifications.
- Make Alerts per hive and Units/Sync global.
- Label each group as "this hive", "this phone", or "your account", so people know what a change affects.
- Collapse the per-sensor notifications into one row per sensor (on/off, with threshold on tap), and add "apply to all hives".

**3. Apply changes immediately and drop Save and "Discard changes?".**
- Toggles and number fields are reversible, so apply them as they change.
- Show a quiet "Saved" or sync state in the header. Keep success silent otherwise, and report failures in place.
- For number fields (thresholds), commit on blur or Done and validate with a range, so a bad value can't be saved.
- Add an Undo toast of roughly 6 to 10 seconds for changes that matter, such as a threshold change.
- This removes the data-loss popup and the scroll to the bottom.

**4. Remove the "Are you sure?" on the temperature unit.**
- Changing the unit is trivially reversible, and stored readings can stay in a base unit and be displayed in the chosen one.
- Show a live preview beside the control, such as "Currently 34 °C → 93 °F".
- Default the unit from the phone's region, and say so ("Set from your phone's region").

**5. Turn alerts on by default for new hives.**
- Use a small set of conservative defaults, such as temperature out of range, a sudden weight drop, and sensor offline. The specific values need beekeeping input from you, so I'd mark them as placeholders for now.
- New hives should copy the settings from your last hive, with an "Alert settings copied from Hive 1" line and a link to change them.
- Alerts off by default is a safety gap here, since a missed alert can mean a lost colony.
- Because these defaults notify people who haven't asked, offer one clear off switch and quiet hours.

**6. Make "Reset everything" hard to hit by accident and recoverable.**
- Move it to the bottom of Advanced, away from any primary control, in neutral styling with a clear label.
- Prefer scoped resets: "Reset alert settings for this hive" and "Reset to defaults" per group.
- If it clears settings only, make it undoable with a toast.
- If it deletes readings or hives that can't be restored, use one specific confirmation naming what goes. For example: "Delete all data for 3 hives and 14 months of readings? This can't be undone." Make the button say "Delete all data" rather than a generic confirm.

## What I'd leave alone
- Keep the option to reach every current setting. Nothing is removed, only reorganized.
- Keep one explicit confirmation if a change can disturb others or can't be reversed, such as removing a sensor or unlinking an account.

## Shipping without user testing
- Ship these as a few independent changes, in order of risk: reorder and group, remove the popups, immediate apply, and new-hive defaults last, since it changes behavior.
- Check that the review complaints match your assumptions by tagging the "confusing" reviews against specific screens. This is a free read of what people are saying.
- Do a quick internal pass with someone who hasn't seen the screen, and have them add a hive and set one alert with no help.
- Add basic instrumentation so you can learn after release, such as settings opened, which items get changed, and how many people turn alerts off after the new defaults.
- Make the new defaults and the immediate-apply behavior switchable remotely if you can, so you can roll back if reviews get worse.

I haven't seen your code. If you share the settings screen source, I can turn this into a concrete grouping and defaults spec.
