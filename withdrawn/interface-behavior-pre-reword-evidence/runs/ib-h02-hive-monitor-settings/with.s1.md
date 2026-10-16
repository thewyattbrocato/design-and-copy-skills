**Assumption:** The user is a hobbyist beekeeper on a phone, often standing outside at the hive with gloves or one hand free. They open the app briefly, and they touch settings rarely. Most of what they need to do is add a hive, turn on sensible alerts, and occasionally change a threshold. I haven't seen your analytics or reviews, so treat the specifics below as starting values. They are not measured.

## Changes, in priority order

**1. Apply settings immediately and drop the Save button and "Discard changes?" popup.**
- When someone flips a toggle or edits a number, apply it right away and show a brief "Undo" toast.
- This is safe because nearly every setting here is reversible. Save plus a discard popup makes people lose work and ask "did that stick?".
- For number fields like thresholds, commit on blur or Done, and validate in place with a sensible min/max range.
- Keep an explicit Apply only for something that disrupts others or can't be undone. I don't see any of those in your list.

**2. Remove the temperature-unit "Are you sure?".**
- When the unit changes, convert the display and any thresholds immediately. For example, 95°F becomes 35°C. Offer Undo in a toast.
- It's a display preference, so confirming it protects nothing.
- Make sure stored thresholds are converted correctly, not just relabeled. That is the one real risk here, so test it.

**3. Start new hives with a sensible set of alerts on.**
- When a hive is added, turn on a small, defensible set. Candidates are hive temperature out of range, a sensor offline, and low battery. Pick the exact set with your beekeeping and support people.
- Show what was assumed on the hive's screen ("3 alerts on · Change") so it isn't a silent default.
- Remember the last choice. If someone customizes their first hive, offer to copy those settings to the next one, so they don't repeat 38 toggles per hive.
- Avoid defaulting every notification to on. Too many alerts is its own failure and gets the app muted.

**4. Restructure the page by how often people touch things, not by when engineering added them.**
- **Top level, short list:** Alerts, Units, Sync & account, Devices/Sensors, and Advanced. That is five or fewer destinations. Each one opens a small group.
- **Alerts, per hive:** one row per sensor with a toggle and a plain-language summary ("Notify me if above 95°F"). Tapping the row reveals the threshold field. Don't show 38 controls at once.
- **Advanced:** rarely used options go here, collapsed by default. Don't delete them.
- Add search if the list is still long after grouping.
- Say whether each setting is per device (units, notifications) or per account (sync), with a small label.
- Use plain words and units next to every number field, such as "°F", "% humidity" and "minutes". Most of the "confusing" reviews probably come from jargon and unlabeled fields, though I haven't seen the reviews.

**5. Fix "Reset everything".**
- Move it out of the Save area to the bottom of Advanced, and stop styling it as a primary-adjacent button.
- Split it by scope: "Reset alerts for this hive to defaults" is the common need, and it's undoable with a toast.
- Keep a full reset, but make it specific: "Erase all settings and hive configurations on this device? Sensor history stays in your account." Say exactly what goes and what stays. This is one of the few places a confirmation is justified, and only if it truly can't be restored. If you can snapshot settings first, offer Undo instead.

**6. Show state where people already look.**
- Show sync status as a small inline indicator ("Synced just now" or "Offline, will sync later"), not a popup.
- Keep success silent. Only failures interrupt, for example "Couldn't save the alert for Hive 2. Retry".
- Offline edits should queue locally and survive the app being closed.

## Accessibility, which matters for gloves and sun glare
- Use large touch targets and a visible on/off label on toggles, not color alone.
- Announce Undo toasts to screen readers, and don't dismiss them too quickly. A few seconds is a starting value.

## Shipping without user testing
- Do the safest changes first: 1, 2 and 5 are low-risk and remove the biggest annoyances.
- Be careful with 3, because the default alert set changes behavior for new hives. Ship it behind a flag if you can, and make the assumed set visible and editable.
- Without testing, watch what happens after release. Track support contacts and reviews that mention settings, whether people turn default alerts off right after adding a hive, and Undo usage on the unit toggle. Treat those as signals to check, because I have no baselines for them.
- If you can only do one extra thing, run the new layout past a few beekeepers informally, such as a club member or a support-team walkthrough. That isn't formal testing, but it will catch label problems.

If you tell me the platform (React Native, Swift, Flutter) and share the list of the 38 settings, I can draft the grouping and the default alert set concretely.
