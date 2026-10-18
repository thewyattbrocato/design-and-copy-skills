**Verdict: this reads as a generic SaaS admin template with Coldshelf's name on it. A food bank operator opening it would not learn that the product monitors fridge temperatures, and nothing on the screen tells them what to do next. Fix this before any demo.**

**Blocker**

1. **The first screen doesn't say what Coldshelf does.** Every metric and label (Total Users, Revenue, Active Sessions, Conversion Rate, Analytics, Users) comes from a sales-analytics dashboard. There is no unit, fridge, freezer, temperature, or alert anywhere. The core job is "is every unit in its safe range right now?" and the screen doesn't answer it. Fix: lead with unit status (for example, "4 units: 3 in range, 1 out of range since 9:40 AM"), then the readings.

2. **Out-of-range alerts have no visible home.** The bell is the only plausible place for them, and nothing on the screen indicates an alert. For a food-safety tool this is the most important thing a volunteer needs to see at a glance. Fix: an alert banner or count near the top, and a bell with a badge when something needs attention.

**High**

3. **The four stat cards are wrong for this audience.** Revenue and Conversion Rate don't apply to a nonprofit, and "Active Sessions" in red reads as a problem with no meaning here. Replace them with operational numbers: units in range, readings logged today, overdue logs, open alerts. Keep the arrow-plus-percent pattern only where a trend matters.

4. **The "Overview" chart can't be read.** It has no y-axis labels, no units, and no reference for what a good value is. A temperature chart with the axis removed is unusable. Fix: plot temperature per unit over time, label the axis in °F or °C, and draw the safe range as a shaded band (for example, a fridge at or below 41°F). Show Jan to Dec only if the data is annual, and only if that's the question a volunteer is asking.

5. **The error toast will cause real harm.** "Something went wrong. Please try again." doesn't say whether a temperature reading was saved. A volunteer who thinks a log was recorded when it wasn't has a food-safety gap. Fix: say what happened and the state of the data, for example "Reading not saved. Retry now or the reading will be lost." Use the same wording for every failed save; a generic toast is fine for a failed page refresh.

6. **Recent Activity holds placeholder data.** "Item 1 / Item 2 / Item 3" and three identical "View" actions tell the user nothing. Dates are fixed to January 2026, which is stale for a screen dated October 2026, and "01/02/2026" is ambiguous for anyone outside the US. Fix: real rows such as unit name, latest reading, status ("In range" / "Out of range" / "Missed log"), last logged by, and time, with one row-level action where it matters, such as "Log reading." Use a consistent date format and show relative times ("2 h ago") with the exact time on hover.

**Medium**

7. **The sidebar labels are generic.** For this product, "Users" and "Analytics" probably mean less than "Units," "Logs," "Alerts," and "Volunteers." Taste-level note: "Dashboard" and "Analytics" overlap here, so one of them needs a clear reason to exist.

8. **The subtitle is filler.** "Welcome back! Here's what's happening today." Replace it with the status summary from finding 1. Labeled as a copy suggestion, not a rule.

9. **The Reports empty state is close, but vague.** "Get started by adding your first item!" doesn't say what a report is or what it contains. Fix: "No reports yet. Log temperatures for a few days and generate your first report for [your food bank's] records." Change "Add Item" to the actual noun, such as "Add a unit" or "Generate report."

10. **The search box has no defined scope.** "Search..." doesn't say whether it searches units, people, or logs. Fix: "Search units, volunteers, or logs."

**What works and should stay**

- The top bar and sidebar layout is familiar, so volunteers won't have to learn navigation from scratch.
- The stat cards pair arrows with text, not color alone, which keeps the trend readable.
- The empty state has one clear primary action and an appropriate icon.
- The table uses standard columns, so the structure can carry real data once the content is correct.

**Fix order:** 1 and 2 first (what the product is and how alerts surface), then 4 and 5 (chart legibility and failed-save messaging, which are the riskiest for food safety), then 3 and 6 (replace the data with operational content), then the rest.

**Not checked:** colors, contrast, type sizes, spacing, and tablet or phone layouts. Your description doesn't include them, and volunteers may be using tablets beside a fridge, which would change the layout. I also don't know whether logging works offline; that changes the wording in finding 5. Send an export or a screenshot and I can check the contrast and layout.
