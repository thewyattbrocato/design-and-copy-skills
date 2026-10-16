**Assumptions:** The user is a hobbyist beekeeper on a phone, often standing at the hive, who opens settings rarely and mostly wants to know whether the bees are okay. These are my guesses from your description, not research. Without user testing, I'd favor changes that remove friction and are easy to reverse.

## Changes, in priority order

**1. Apply settings immediately and drop the Save button and the "Discard changes?" popup.**
- *When* someone changes a toggle or number, *save it right away* and show a brief inline "Saved" state on that row.
- *Because* "Save at the bottom" is easy to miss on a 38-row page, and the discard popup punishes people for leaving. Silent success with an undo is cheaper than lost edits.
- Show an error in place if sync fails, and keep the value on screen so nothing is lost.
- Keep an explicit Apply only for a setting that can't be reversed. Nothing in your list sounds like that.

**2. Remove the "Are you sure?" on temperature unit.**
- *When* the unit changes, *convert the display immediately*. Show the converted thresholds beside the control, for example "Alert above 95 °F (35 °C)".
- *Because* it's reversible and nothing is lost. Store thresholds internally in one unit so switching back doesn't introduce rounding drift.
- Default the unit from the phone's locale, and show that it was assumed.

**3. Give new hives sensible alert defaults.**
- *When* a hive is added, *turn on a small recommended set of alerts for the sensors that hive actually has*. Candidates are temperature out of range, a sudden weight drop, and a sensor offline or low battery. Keep the rest off.
- *Because* "everything off" means a beekeeper can believe they're monitored when they aren't, which is the costliest failure here.
- Show a line such as "Recommended alerts are on. Review" on the new hive, so the assumption is visible and changeable.
- Offer "Copy settings from [another hive]" when they have one, and remember their last choice.
- I don't have beekeeping threshold values for you. Get those from your apiary advisor or product team, and mark them as placeholders until then.

**4. Make "Reset everything" safe.**
- *Move it* to the bottom of an "Advanced" section, away from other controls, in a quiet style rather than a red filled button.
- *Split it* if possible: "Reset alert thresholds to defaults" is the common need. It should be undoable with a toast of at least 6 to 10 seconds that pauses on focus.
- *Keep one specific confirmation* only for anything that can't be restored, such as deleting hive history. Name what goes: "Delete all settings and history for 3 hives?"
- *Because* a destructive button directly under Save is an accident waiting to happen. Removing the Save button also takes away its neighbor.

**5. Restructure the 38 items by how often people touch them.**
- Group them, with the common ones first:
  1. **Alerts**, grouped per hive with a master on/off per hive, then per sensor underneath.
  2. **Notifications**: how and when to be told, including quiet hours.
  3. **Units and display.**
  4. **Sync and devices.**
  5. **Advanced**, where reset lives.
- Collapse each group by default and show a one-line summary, for example "Alerts: 4 on".
- Add search once the page is grouped.
- Label each setting as per device or per account.
- *Because* the current order reflects when engineering added things, not what a beekeeper is trying to do.
- Audit the 38 for items to cut or hide. Anything that is almost never changed (you'll need your analytics for this) can move to Advanced rather than being deleted.

**6. Show status outside Settings.**
- Put a plain-language state on the hive screen, such as "All sensors reporting, 4 alerts on". This answers most "what's going on?" questions before anyone opens Settings.

## Pre-release checks, since you can't test with users
- Walk through five tasks yourselves, counting taps: change the unit, add a hive and confirm alerts work, change one threshold, silence notifications overnight, and undo a reset.
- Ask five or so beekeepers from your support inbox or community to try the same tasks on a prototype, even informally. That isn't formal testing, but it will catch the worst problems.
- Ship in an order that limits risk. Items 1 to 4 are behavior changes with small layout impact. Item 5 is the bigger restructure and could follow in a later release if time is short.
- Confirm keyboard and screen-reader access: the "Saved" and undo messages should be announced, and nothing should depend on color alone.

If you tell me which sensors a hive can have and which settings exist today, I can draft the specific default alert set and the grouping.
