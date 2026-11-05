**Assumption:** Your users are hobbyist beekeepers on a phone. They are often outdoors, with gloves or one hand free, and usually only glance at the app. They open settings rarely, mostly after adding a hive or when an alert annoys them. I'm assuming you have no usage data, so everything below is a starting rule and not a measured result.

## What I'd change, in priority order

**1. Apply settings immediately and drop Save and "Discard changes?"**
- When someone flips a toggle or edits a number, apply it right away and show a small "Undo" toast for about 6–10 seconds.
- Why: nearly every setting here can be reversed, so there's nothing to protect. The Save button is the reason people lose changes, and the Discard popup only exists to patch it.
- Keep the toast only for edits that can't be seen in place. A toggle that visibly flips needs no toast.
- Show failures, such as a sync error, in place beside the setting.
- Number fields should commit when the person finishes (blur or Done). Validate the range and flag bad values inline.

**2. Remove the temperature-unit "Are you sure?"**
- Switch units immediately and convert any displayed thresholds. For example, a 95°F alert becomes 35°C, so the alert means the same thing.
- Undo covers any mistake.
- Why: the change is trivially reversible. The popup also teaches people to dismiss confirmations, which weakens the ones that matter.
- Check that stored thresholds are kept in one canonical unit, so toggling back and forth doesn't cause rounding drift.

**3. Give new hives sensible default alerts**
- Turn on a small set of alerts by default for each new hive. Candidates: hive temperature out of range, sensor offline, and low battery.
- Leave noisy or specialized ones off.
- Show what was assumed on the hive's alert row, for example "Default alerts on · Customize", with a reset-to-defaults option.
- Better still, copy the last hive's alert setup as the starting point, since people with several hives usually want them alike.
- Why: all-off means a new user gets silence from a monitoring product until they do 10+ toggles, and a hive may fail in the meantime. The default threshold values are a beekeeping/product call for you to make. I won't invent them.

**4. Restructure the 38 settings: lead with the few that matter, group the rest**
- **Top level:** about 4–5 groups ordered by how often people touch them, for example *Alerts*, *Hives & sensors*, *Units & display*, *Sync & account*, *About*.
- **Alerts:** a per-hive view, so someone can see "Hive 2: 3 alerts on" at a glance and open it for details. Don't use one global list of every sensor notification.
- **Per sensor:** one row with a toggle and, once it's on, the threshold revealed beneath it. Don't show every number field at once.
- **Search:** add settings search at the top, since there are many items.
- **Scope:** label each setting as per device or per account, especially notifications and units.
- **Rarely used:** settings almost nobody needs go under "Advanced". Don't delete them.
- Whether any of the 38 can be removed or inferred (for example, units from device locale) is worth a pass with engineering. Each setting that gets a good default is one fewer thing to explain.

**5. Make "Reset everything" harder to hit and easier to survive**
- Move it out of the Save area to the bottom of an Advanced or Account group, styled as a plain text button. The danger is the red button next to the primary action.
- Give it one specific confirmation: name what it will reset, whether it touches only settings or also hives and history, and use a verb label like "Reset all settings" instead of "OK".
- If it only resets settings, I'd also offer Undo afterwards. Keep the explicit confirmation only if it deletes data that can't be restored.
- Also add per-group "Reset to defaults". That covers most of what people actually want, with much less risk.

## Why this order
- Items 1–3 are behavior changes that remove friction and risk. They need no new design system, and you can ship them without user testing because each one has a safe fallback.
- Item 4 is the biggest change to how the screen looks. If you only have time for part of it, do the grouping and per-hive alerts and hold the rest.
- Item 5 is a small fix with a large safety payoff.

## Shipping without user testing
- **Release behind a flag** if possible, so you can turn off the new settings if something breaks.
- **Dogfood** with a few beekeepers or staff who own the kit.
- **Watch what you already have:** support contacts, reviews that mention "confusing", and, if you collect it, how often people reach the settings screen and which settings they change first. Those can validate the new grouping after release.
- **Test the risky bits on your own devices:** unit conversion round trips, offline behavior of immediate-apply (queue the change and show sync state), and that the default alerts actually fire on a new hive.

If you tell me the platform (iOS, Android, or cross-platform) and whether alerts are stored per hive on the server, I can write this up as a one-page behavior spec for engineering.
