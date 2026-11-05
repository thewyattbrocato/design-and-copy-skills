**Bottom line:** this is a generic SaaS admin template with Coldshelf's name on it. Nothing on the screen says "temperature" or "fridge," and a food bank volunteer would have no idea what Revenue or Conversion Rate means here. Cosmetic polish won't fix that. The content needs rewriting around the actual job.

## The core problem
Someone opening this screen wants to know whether everything is cold enough and whether they need to do anything. The screen can't answer either question. A failed walk-in at 2am means lost food and possibly a food-safety incident, so the answer needs to be the first thing visible.

## Section by section

**Subtitle ("Welcome back! Here's what's happening today.")**
This is filler. Replace it with a live status sentence, e.g. "All 6 units in range · Last reading 2 min ago" or "1 unit out of range for 25 min." If it has to be one line, it should be this line.

**Stat cards**
- Total Users, Revenue, Active Sessions and Conversion Rate are all irrelevant to this product.
- Replace them with something like: *Units in range (5 of 6)*, *Active alerts*, *Sensors offline / stale*, and *Excursions this week*.
- "vs. last month" comparisons don't help for safety data. Current state matters more than trend.
- Arrow color alone carries meaning, which fails for colorblind users. Active Sessions down is also shown in red, though down isn't inherently bad. Pair status colors with an icon and text.

**Chart ("Overview", Jan–Dec, one blue line, no y-axis labels)**
- A line with no y-axis labels can't be read.
- Jan–Dec is the wrong time scale. Temperature needs hours or days, with a 24h/7d/30d toggle.
- It needs units (°F/°C) and a shaded safe-range band, so excursions are obvious. Common thresholds are ≤41°F (5°C) for refrigerators and ≤0°F (-18°C) for freezers. Please confirm against your local health code.
- One line can't show multiple units. Default to a per-unit view, or a small chart per unit.
- Blue is fine for a normal reading. Don't reuse it as the only signal for "bad."

**Table ("Recent Activity")**
- "Item 1 / Active / Pending / Inactive / View" is placeholder data.
- Make it a units table: *Unit name · Current temp · Status · Last reading · Action*. Sort out-of-range units to the top.
- Use a clear action like "Acknowledge" or "Log corrective action." Food banks often need a paper trail for inspectors.
- 01/02/2026 is ambiguous (Jan 2 or Feb 1?). For recent events, use relative times ("12 min ago").

**Navigation**
- Analytics, Reports, Users and Settings are generic. Consider *Units* (or Locations), *Alerts*, *Logs/Reports* (inspection exports), *Team* (volunteers), and *Settings*.
- Volunteers may use a shared tablet in a busy back room. Use large tap targets and keep the main view free of jargon.

**Top bar**
- "Search..." should say what it searches ("Search units, alerts").
- The bell needs an unread badge. Critical alerts also can't live only in a bell icon, since nobody's looking at the dashboard overnight. You need SMS, push or email escalation.

**Empty state (Reports)**
- "Add your first item!" is wrong. Reports are empty because no readings have been logged yet, not because the user forgot to add an item.
- Say that directly: "No readings yet. Add a fridge or freezer and connect a sensor to start building inspection-ready logs." The button should read **Add a unit**, not "Add Item."
- A generic document outline icon is fine, but not distinctive.

**Error toast ("Something went wrong. Please try again.")**
- This is the most dangerous string here. In a logging app, the user's real question is "is my temperature data still being recorded?" The toast doesn't answer it.
- Say what failed and what's safe, e.g. "Couldn't reach the sensor in Walk-in Freezer 2. Last reading 14 min ago. Check that it's powered and in Wi-Fi range."
- Walk-in boxes are metal-lined and often have bad Wi-Fi. Design a persistent "stale / offline" state per unit, not just a toast that disappears.
- "Used everywhere" is a smell. Each failure type needs its own message.

## Missing entirely
- An offline or stale-data state.
- A way to log a manual reading as a fallback when a sensor dies.
- Alert history showing who acknowledged what and when.
- Alert threshold settings, including how long a door can be open before alerting.
- A one-click export for health inspectors.

## Priority order
1. Rewrite the stat cards and table around units and status. This is the biggest gap.
2. Fix the chart with units, axes, time scale and a safe-range band.
3. Design stale/offline states and specific error messages.
4. Fix the nav, empty state and alert escalation.

I can draft a replacement layout in the same text format, including the microcopy, if you'd like.
