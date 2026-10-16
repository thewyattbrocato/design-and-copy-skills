Most of this is well-established UI convention, so you can make the changes with reasonable confidence without user testing. Here they are in rough priority order.

## 1. Save automatically and drop the "Discard changes?" popup
- Apply each change as it's made and show a brief "Saved" confirmation.
- For number fields, validate and save when the user finishes editing. Show inline errors like "Must be between 5 and 40 °C" instead of blocking.
- Today a user can change a threshold, assume it worked, and leave without saving. Because these are alert thresholds, that means a missed alert.
- If autosave is too big a change for this release, make Save sticky at the top or bottom, mark which fields are unsaved, and replace the popup with Save/Discard on back. That's a fallback, not the goal.

## 2. Remove the "Are you sure?" on temperature unit
- Switching units is harmless and reversible, so the confirmation adds friction and no safety.
- Check that thresholds are stored in one canonical unit and converted for display. If they're stored as typed, switching units will silently change what they mean, and that bug needs fixing in this release.

## 3. Turn on a small set of sensible alerts for new hives
- All alerts off is the worst default for this product. A new user who skips setup gets no protection, and a missed alert can mean a lost colony.
- Enable a short recommended set, such as temperature out of range, sensor offline, and low battery. Don't enable all of them, because alert fatigue makes people turn everything off.
- After adding a hive, say what happened: "We turned on 3 recommended alerts. Review them."
- Keep the notification-permission request tied to this moment, where the benefit is obvious.

## 4. Make "Reset everything" harder to hit and clearer
- Move it out of the Save area to the bottom of a separate "Advanced" or "Data" section, away from any primary action.
- Prefer a narrower action such as "Reset alerts to recommended". If you keep a full reset, the confirmation should list what will be erased, and the confirm button should say "Erase all settings" instead of "OK".
- Better still, apply the reset immediately and show an Undo for a few seconds.

## 5. Group and trim the 38 items
- Sort the list by what people care about instead of the order engineering added items. For example:
  - **Alerts:** a few top-level rows
  - **Units**
  - **Notifications**
  - **Sync & devices**
  - **Advanced**
  - **Data & reset**
- Move per-sensor and per-hive options into that hive or sensor's own screen. A global page with a toggle for every sensor is much of why this feels long.
- Put rarely changed items (sync intervals, diagnostics) behind "Advanced."
- Aim for roughly 8–10 visible rows on the top-level screen.
- For each threshold, add plain-language helper text and show the default and the unit: "Alert me if the hive drops below __ °C (default 10)." Beekeepers aren't necessarily engineers.

## Reducing risk without user testing
- **Read the reviews.** Tag them by cause: settings, setup, alerts, or something else. This confirms the settings screen is the main source before you invest in it.
- **Run a quick informal check.** Hand 3–5 beekeepers, or even non-engineers on your team, a prototype or screenshots. Ask them to find the low-battery alert and change the units, and watch where they hesitate. That's an hour or two, not a study.
- **Use a staged rollout or feature flag**, if you have one, so you can roll back.
- **Log a few events** so the next release has evidence: settings exits, reset taps, alerts enabled per new hive, and support tickets mentioning settings.
- **Split the work if time is tight.** Items 1–4 are small, low-risk behavior changes that address the clearest problems. The regrouping in item 5 is a bigger redesign, so it can follow once you have data.

I can draft the new settings structure as a concrete section-by-section outline if you share the full list of 38 items.
