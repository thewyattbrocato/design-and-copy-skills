**Assumptions:** The users are hobbyist beekeepers, mostly on a phone, often outdoors and in short sessions. They are checking on a hive, not configuring software. Most of them should rarely open settings after setup. I haven't seen usage data, so the grouping below is a guess about frequency. You can sanity-check it against support tickets and analytics without running user testing.

## What I'd change, in priority order

**1. Hive defaults: new hives start with sensible alerts on.**
- When someone adds a hive, turn on the alerts that matter for bees (for example hive temperature out of range, and sensor offline or low battery). Use starting thresholds you pick with your beekeeping advisor. I'm not inventing values here.
- Show what was assumed next to the hive ("Using standard alerts · Customize"). Keep a "Reset to defaults" option.
- Why: with all alerts off, the app does nothing useful until someone does a chore. Most people never finish it, and then they think the product is broken.
- Remember the last hive's customizations and offer them for the next hive ("Copy settings from Hive 1").

**2. Save automatically and drop the Save button and the "Discard changes?" popup.**
- Apply each toggle or field as soon as it changes. Validate in place, and keep the old value if the new one is invalid.
- Failures show next to the control. Success stays silent.
- Why: the popup exists only because of the Save model. People lose work or get nagged. Settings like these are reversible, so there's nothing to protect.
- If a change is very disruptive (for example, one that alerts other people on a shared hive), give just that group an explicit Apply.

**3. Remove the "Are you sure?" on the temperature unit.**
- Switch the unit immediately and convert the displayed values. Thresholds keep the same physical value, so 35 °C becomes 95 °F.
- Show an Undo toast for about 6–10 seconds, announced to screen readers.
- Better still, pick the default unit from the phone's locale at first run.
- Why: it's reversible, so a confirmation only adds friction.

**4. Make "Reset everything" safe to reach and recoverable.**
- Move it out of the Save area to the bottom of an "Advanced" section, away from everyday controls.
- Split it into narrower resets: "Reset alert thresholds" and "Reset this hive". Then restore the previous values and offer Undo for the same short window.
- Only if full undo isn't feasible, keep a single specific confirmation that names what will be lost ("This clears thresholds and notification choices for 3 hives. Hive data and history are kept.").
- Why: a red destructive button right under the primary action invites mistaken taps. Mistakes there should be cheap to fix.

**5. Restructure the 38-item page by how often people touch things.**
- **Top level, a handful of rows:** Hives (each with its own alerts), Notifications, Units, Sync, Account/Device, Advanced. Each row shows its current value or a summary ("Alerts: 4 on").
- **Per hive:** one screen with alerts grouped by sensor (temperature, humidity, weight, etc.). Each sensor has one on/off switch. Thresholds appear only when it's on, with the default prefilled.
- **Advanced:** rarely changed values, such as fine-tuning ranges, sync intervals and diagnostics. These don't need deleting, just moving out of the everyday area.
- Add search once the list is long, and label each setting as per device or per account.
- Replace free number fields with steppers or sliders that have sensible min/max limits, so bad input is prevented.
- Why: the order engineering added things in says nothing about what a beekeeper looks for. Hiding thresholds behind their toggle removes most of the visible clutter.

## Rollout without user testing
- Ship in two steps if you can: behavior fixes first (1–4, which are low-risk and mostly remove friction), then the restructure (5).
- Put the new defaults and the structure behind a flag. Compare support tickets, "confusing" review mentions, and the share of new hives with at least one alert on, before and after.
- Do a quick internal pass with 3–5 colleagues or a few beekeepers from your community. Ask them to add a hive, change the unit and find the temperature alert. This isn't formal testing, but it catches obvious problems.
- Check accessibility: every control keyboard and screen-reader reachable, undo toasts announced and not removed too quickly, and no meaning conveyed by color alone (the red Reset button needs a label and an icon as well).

If you can tell me which alerts are the most important and what your platform conventions are (iOS, Android, or both), I can turn this into a one-page spec for engineering.
