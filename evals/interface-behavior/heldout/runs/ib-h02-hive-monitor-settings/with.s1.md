**Assumption:** The users are hobbyist beekeepers on phones, often standing at a hive with gloves on or in sun glare. They open settings rarely, mostly to add a hive or tune an alert. I'm also assuming the app has no undo infrastructure today. Nobody has tested any of this, so treat the numbers below as starting values.

## Changes, in priority order

**1. Save as you go and drop the Save button and "Discard changes?" popup.**
- **When** someone changes a toggle or field, **apply it immediately**. Show a small "Saved" state beside the control, or nothing at all.
- **Why:** these settings are all reversible. Today's flow makes people lose work or fear leaving the page. The "Discard?" popup exists only because of the Save button.
- **Exception:** number fields apply when the field loses focus or the person taps Done, so a half-typed "3" never becomes a live threshold. Show a failed sync in place with a retry, and keep the entered value.

**2. Remove the "Are you sure?" on the temperature unit.**
- **When** the unit changes, **switch it and convert the displayed values**. Show a toast with Undo for about 8 seconds.
- **Why:** it's a display preference, and it's reversible by tapping again.
- **Check:** alert thresholds must convert too, for example 35°C becomes 95°F, not 35°F. Test this explicitly, because a silent wrong threshold is the real risk.

**3. Make new hives start with sensible alerts on.**
- **When** someone adds a hive, **enable the core alerts** for the sensors that hive actually has, using defaults from your own beekeeping knowledge. Likely candidates are high and low temperature, a sudden weight drop, and a sensor offline. Leave the noisy or optional ones off.
- **Show** one line on the new hive: "Standard alerts on. Review", linking to that hive's alerts.
- **Also:** offer "Copy alerts from [last hive]" when they add a second hive, since people with several hives usually want them alike.
- **Why:** all-off defaults mean most people never get a warning, which defeats the product. Defaults should fix that without asking questions.
- **Check:** the thresholds must come from someone who knows bees. I can't supply them.

**4. Restructure the 38 settings.**
- **Group by how often people touch them**, not by when engineering added them.
  - *Top level (about 5 rows):* Hives, Notifications, Units, Account and sync, Advanced.
  - *Per hive:* that hive's sensors and thresholds, one sensor per row with its alert toggle and threshold together.
  - *Advanced:* anything most people never change, collapsed.
- **Global versus per-hive:** state which one each setting is. Put one global "Notifications" master switch and quiet hours at the top level, with per-sensor alerts under each hive.
- **Add a search field** at the top of settings. Treat it as the safety net for settings that moved.
- **Why:** the "confusing" reviews most likely come from 38 unrelated controls on one page, but I can't confirm that without the review text. Skim the actual reviews for which settings people name, and put those first.

**5. Make "Reset everything" hard to hit and recoverable.**
- **Move it** off the bottom of the main page into Advanced, away from where Save used to be. Make it a plain text row, not a big red button.
- **Split it:** "Reset alerts to defaults" per hive (undoable with a toast) and "Reset all settings" in Advanced.
- **Keep one specific confirmation for the global reset**, since nothing can restore it. Say what goes: "Resets all settings and alert thresholds for 3 hives. Your sensor data and history are kept." Make the button label the action ("Reset settings"), not "OK".
- **Why:** this is the only place a confirmation is warranted. Keeping it rare means people will still read it.
- **Better:** snapshot the settings before reset, so you can offer Undo and skip the confirmation.

## Accessibility
- Keep touch targets large enough for gloved hands.
- Toasts should be announced to screen readers and last long enough to read.
- Don't rely on color alone for alert on/off state, including the red reset button.

## Checks before release
Without user testing, do these instead:
- Run the temperature-unit conversion on every threshold.
- Confirm that killing the app mid-edit keeps the value.
- Walk through adding a hive with each sensor combination.
- Have two or three people outside engineering try "turn off humidity alerts on hive 2" and "switch to °F". Ten minutes each is enough, and it's informal rather than a formal test.
- Ship behind a flag if you can, so you can revert if support messages spike.

## Lower priority
Plain-language labels for the 38 items matter, but copy is a separate pass. Do the behavior changes first. I can draft the full settings hierarchy if you paste the list of the 38 controls.
