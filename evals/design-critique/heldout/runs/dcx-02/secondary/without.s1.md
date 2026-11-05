The screen reads like a generic SaaS admin template. Its metrics and placeholder data don't match what Coldshelf is for, so I'd fix that before showing it to a food bank.

## The big problem

The first thing a food bank manager needs to know is whether every fridge and freezer is in its safe range right now. This screen doesn't answer that anywhere. There are no units, no temperatures, no alerts, and no missed logs. Users, Revenue, Active Sessions, and Conversion Rate are the wrong headline metrics for a nonprofit that logs cold-chain temperatures.

## Element by element

**Stat cards**
- Replace all four with product metrics, for example: Units in range, Units out of range, Units not logged today, Last reading (time and who logged it).
- "Revenue" and "Conversion Rate" will confuse a food bank and may read as misplaced.
- "Active Sessions" down 3% shows a red arrow, which suggests bad news for something that may not matter.
- Don't rely on color alone for in-range or out-of-range. Use a text label and an icon too. Color-blind volunteers and anyone on a glare-heavy screen need the label.

**Overview chart**
- The y-axis has no labels, so nobody can read a value. For temperature this is the core chart, and it needs the real scale (°F or °C) with a shaded safe band, for example 0–40°F for fridges and below 0°F for freezers.
- Jan to Dec is the wrong time range. Staff care about the last 24 hours or 7 days per unit, with gaps shown where logs were missed.
- As described, it's unclear what the line plots. Label it.

**Recent Activity table**
- The columns don't fit. Use Unit, Reading (temp), Status (In range / Out of range / Missed), Logged by, and Time.
- "Item 1 / Active / Pending / Inactive" is placeholder data. Don't demo with it.
- Dates like 01/01/2026 are ambiguous (US vs. day-first locales). Use an unambiguous format, or the locale's format consistently.
- "View" on every row is weak. Make the whole row or the status a tap target, and keep an audit trail of who logged what and when. Health inspectors will ask for that.

**Sidebar**
- Add Units (fridges and freezers) and Logs or Alerts. These are the core objects of the product.
- "Users" should probably be "Volunteers" or "Staff," matching how food banks talk about their people.
- "Analytics" and "Reports" overlap. Decide what each is for.

**Bell icon**
- Make sure it's for temperature alerts and missed logs. A generic notification bell is a missed opportunity.

**Reports empty state**
- "Add your first item!" is vague. Say something specific, such as "Add your first fridge or freezer to start logging temperatures," and show what the report will contain.
- Reports for food banks probably need a date range and an export or print option for auditors. Confirm that's in scope.

**Error toast**
- "Something went wrong. Please try again." is the most dangerous message on the screen. If a temperature reading didn't save, the volunteer needs to know that, with "Reading not saved. Try again" and a retry action.
- Toasts that vanish too quickly are a problem for failed saves. Keep errors visible until dismissed.

## Things the mockup doesn't show that matter here

- **Offline logging.** Walk-in fridges are often in basements or back rooms with weak signal. If logging needs a connection, that's the most likely real-world failure. Confirm it works offline and syncs later.
- **Mobile and tablet.** Volunteers will probably log on a phone or a shared tablet at the fridge. I can't see responsive layouts from this description.
- **Contrast and text size.** I can't verify these from text, so check them against WCAG AA in the real design.

## What I'd do before the demo

1. Rebuild the top of the dashboard around unit status, alerts, and missed logs.
2. Replace the placeholder table and chart with realistic temperature data.
3. Fix the error-state copy and make failed saves persistent.
4. Check offline behavior on a real device in a cold room or with signal off.

I haven't seen the actual design, only your description, so treat this as a review of the content and structure rather than the visuals. If you can tell me which units and alert thresholds Coldshelf uses, what food banks in your pilot already track, and whether logging works offline now, I can draft a revised layout and copy for the dashboard.
