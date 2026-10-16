**Assumptions:** The users are hobbyist beekeepers. They use the app on a phone, often outdoors and in short sessions. They open settings rarely, usually right after setup or when an alert goes off at a bad time. They aren't technical. Since you can't test, I've ranked the changes by how confident I am in them and how cheap they are to ship.

## Do these first

1. **When someone adds a hive, turn on a small set of sensible alerts and show what was assumed.**
   - Why: today a new hive is silent until the user finds and flips toggles one by one. That is the worst default on the screen, because the app fails at its main job without telling anyone.
   - Behavior:
     - Turn on the alerts that protect the colony, such as temperature out of range, a weight drop that suggests a swarm, and a sensor offline.
     - Leave the nice-to-know alerts off.
     - Right after the hive is added, show one line: "Alerts on: temperature, weight, offline. Change".
     - The threshold values need a beekeeping source (an apiculture reference or your own advisor). I'm leaving them as placeholders, not inventing numbers.
   - Also: offer "Copy alert settings from another hive" when the user already has one.

2. **Remove the "Discard changes?" popup and the Save button by applying changes immediately.**
   - Why: nearly everything here can be reversed by changing it back, so a save step only creates a way to lose work.
   - Behavior:
     - Apply each toggle or value the moment it changes.
     - Show a brief "Undo" toast, announced to screen readers.
     - Keep a typed number as a draft until the field loses focus or the value is valid. Flag an odd value in place, such as a threshold outside a plausible range, and don't block it.
   - Exception: if a setting can disrupt other people, such as notifications shared with family members, use an explicit Apply for that one.

3. **Remove the "Are you sure?" on the temperature unit.**
   - Why: the change is reversible and affects only display.
   - Behavior:
     - Convert the display immediately.
     - Keep the stored thresholds in a single canonical unit, so switching °F/°C changes the numbers shown and never the alert behavior.
     - Better still, default the unit from the phone's region, and show it beside the control.
   - Check before shipping: if thresholds are currently stored in the display unit, this needs the conversion fix first, otherwise a unit flip could silently move alert points.

4. **Replace "Reset everything" with scoped resets and move it away from the everyday controls.**
   - Why: a red, irreversible button right under Save invites a mis-tap, and "everything" is rarely what anyone wants.
   - Behavior:
     - Offer "Reset alerts for this hive to defaults" inside that hive's section.
     - Put any full reset at the very bottom of an "Advanced" group.
     - Make the reset undoable with a toast. If the reset really can't be restored (it deletes history, for example), use one specific confirmation. It should say what goes away: "Erase settings for 3 hives. Sensor history is kept."

## Restructure the page

5. **Group the 38 items by how often people touch them, not by when engineering added them.**
   - Why: people come to settings to fix a specific annoyance, and a flat list makes them scan 38 rows to find it.
   - Proposed groups:
     - **Alerts** is the most visited. List it per hive, with a short summary row like "Temperature: 2 alerts on". Each row expands to its thresholds.
     - **Notifications** covers how and when you're told, including quiet hours.
     - **Units & display** (temperature, weight).
     - **Devices & sync** (sensors, connection, battery).
     - **Account & Advanced**, with the resets at the bottom.
   - Add a search field at the top. At this item count it earns its place.
   - Label each setting as per device or per account (notification preferences are usually per device, units per account).

6. **Make per-sensor notifications a single hive-level choice with an optional override.**
   - Why: a per-sensor toggle for every sensor on every hive is where most of the 38 rows come from.
   - Behavior: one "Notify me about this hive" master control, with per-sensor tuning tucked behind "Customize".

7. **Look at which of the 38 settings should stop being settings.** Anything that exists only because engineering needed a switch, such as sync internals, should get a good default and either move to Advanced or go away.

## Leave alone
- Don't add a wizard or onboarding tour for this. The smart defaults in item 1 replace most of it.

## Ship order given no testing
Items 1, 2, 3 and 4 are low risk and targeted, so ship them first. The regrouping in 5 and 6 changes where everything lives, so it carries the most risk. If you can only do part of it, ship the regrouping with the old order reachable through search. Since you can't run a test, add lightweight measures to check afterward, such as how often users open settings and how often they tap Undo. I'm not assuming any baseline for those.

If you tell me what the 38 settings actually are, I can sort them into these groups and mark which ones to drop or default.
