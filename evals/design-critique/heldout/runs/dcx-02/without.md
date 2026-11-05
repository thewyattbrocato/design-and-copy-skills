**Bottom line:** this is a generic SaaS template, not a Coldshelf screen. Nothing on it mentions a fridge, a freezer, or a temperature. A food bank coordinator would see "Revenue" and "Conversion Rate" and conclude it wasn't built for them. That's the main thing to fix before a demo. The rest follows from it.

## The core problem
The one question this screen should answer is: **"Is the food safe right now, and do I need to do anything?"** Today it can't answer that. A volunteer opening it should know within two seconds.

## Section by section

**Stat cards**
- Total Users, Revenue, Active Sessions and Conversion Rate don't apply to your product. Replace them with something like:
  - Units in range (e.g. 5 of 6)
  - Active alerts
  - Sensors offline
  - Last reading received (e.g. "2 min ago")
- "+X% from last month" is meaningless for temperature safety. Show current state instead.
- Green up and red down arrows encode direction, not good or bad. For an alert count, up is bad. Color by good or bad, and don't rely on color alone, since red/green is a problem for colorblind users. Pair it with an icon and a word such as "In range" or "Out of range".

**Chart ("Overview")**
- A Jan to Dec x-axis doesn't fit this data. Temperature problems play out over hours. Use the last 24 hours and 7 days, with a unit picker.
- A y-axis with no labels is unusable here, because the number is the whole point. Label it in °F (or °C) and draw the safe-range limits as lines or a shaded band. Typical limits are 41°F or below for fridges and 0°F for freezers, but confirm them with your food safety source.
- Mark excursions, such as door-open events, on the line. One blue line for "everything" suggests it's an aggregate, which would hide a failing freezer behind a healthy fridge. Show one line per unit, or one small chart per unit.

**Table ("Recent Activity")**
- "Item 1 / Active / View" is placeholder content. Replace it with real events, for example:
  - Walk-in Freezer 2
  - Out of range, 12°F
  - 02:14 AM
  - Acknowledge
- Status should be what happened (excursion, sensor offline, back in range, manual log), not Active, Pending or Inactive.
- Dates need times, and an alert at 2 AM vs 2 PM matters. `01/02/2026` is also ambiguous between US and international readers.
- Repeated "View" links are an accessibility problem for screen readers. Use specific labels, or make the row clickable.
- The action should be the thing someone needs to do, like acknowledging or logging a corrective action. Food safety inspections generally want to see that someone responded.

**Header and nav**
- "Welcome back! Here's what's happening today." is filler. Use that line for a live status, such as "All 6 units in range" or "2 units need attention".
- "Search..." doesn't say what it searches. Say "Search units, alerts, logs" or remove it until it does something.
- Reports is probably where inspection and compliance logs live, so it's worth making it a first-class, obvious destination. Consider adding Units or Sensors and Alerts to the nav. Analytics may not earn its place yet.
- The bell can't be the only alert channel. Nobody is watching the dashboard at 2 AM, so alerts need SMS, email or push. Make sure the demo covers this.

**Reports empty state**
- "No data yet. Get started by adding your first item!" followed by "Add Item" is unclear. What item? Say what the user is adding and what happens next, for example: "No reports yet. Reports appear once your first unit has a day of readings." The button would be "Add a fridge or freezer".
- If manual logging is a fallback for places without sensors, offer it here.

**Error toast**
- "Something went wrong. Please try again." is the riskiest string on the page. If a reading fails to load or save, a vague message leaves the user guessing whether the fridge is fine.
- Say what failed and whether data was lost or saved, for example: "Couldn't load live temperatures. Showing readings from 2:10 PM."
- Anything touching safety data should be persistent, not an auto-dismissing toast. Show a "stale data" indicator when readings are old.

## Missing states to design
- Sensor offline or stale (this will happen constantly with walk-in fridges and spotty wifi)
- Loading
- The all-clear state
- A critical alert state that visually dominates the page

## Questions that will change the design
- Who's looking at this? A coordinator at a desk, or a volunteer on a shared tablet? That affects touch target size and how much to show.
- Are readings automatic from sensors, manual entry, or both?
- Do you need to produce records for health inspectors? If so, that should shape Reports.

I'm working from your text description, so I can't judge spacing, contrast, type size or visual hierarchy. If you can export a screenshot later, I'll check those too.

If you'd like, I can sketch a replacement layout in text (status strip, unit cards, per-unit chart, event log) for you to react to.
