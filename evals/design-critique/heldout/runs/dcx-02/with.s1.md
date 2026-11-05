**Verdict: this is a generic SaaS dashboard template with Coldshelf's name on it. Nothing on the screen says "temperature logging for walk-in fridges."** A food bank volunteer opening it can't answer the question they care about: "Are our fridges and freezers safe right now?" I'd call that a blocker, and it would be obvious in a demo.

I'm assuming the users are food bank staff and volunteers, many of them non-technical, who check this quickly, possibly on a phone or tablet. I'm also assuming it's a high-fidelity screen.

## Findings, in priority order

**1. Blocker: the content is not about the product.**
- Total Users, Revenue, Active Sessions and Conversion Rate don't exist for a food bank. A food bank has no revenue or conversion, so the cards read as placeholders.
- Missing is the data this app exists for: each unit's current temperature, whether it's in range, and when it was last logged.
- Fix: replace the four cards with things like "Units in range: 5 of 6", "Out of range now: 1", "Last reading: 12 min ago" and "Missed logs today: 2". Put a per-unit list or grid directly under them, with the out-of-range units first.

**2. Blocker: nothing tells you what needs attention.**
- There's no alert state anywhere. The bell is the only hint, and it's an icon with no stated count.
- A warm freezer is a food-safety problem, and it should be the loudest thing on the page.
- Fix: add a banner or top row for units out of range. Show the unit name, the temperature, how long it's been out of range, and one action ("Log a reading" or "Acknowledge").

**3. Major: the "Overview" chart can't be read.**
- It has no y-axis labels, so the line has no values. It has one unlabeled line and a Jan–Dec axis.
- Temperature monitoring needs recent data, such as the last 24 hours or 7 days, not a year.
- It needs a safe-range band or threshold lines (for example, the cold-holding limit your food-safety guidance specifies) so people can see when a unit crossed them.
- Fix: add a unit selector and a time-range control. Draw one line per unit, or a single selected unit. Label the y-axis in °F/°C, show the threshold, and mark excursions.

**4. Major: the "Recent Activity" table is empty of meaning.**
- "Item 1/2/3", "Active/Pending/Inactive" and dates only tell you the table exists.
- There are three "View" links in a column, so each one is ambiguous to a screen reader. The generic status values don't map to anything real.
- Fix: use real columns: Unit, Reading, Logged by, Time, Status (In range / Out of range / Missed). Make the row itself the link to the unit, or label the action "View Walk-in Fridge".

**5. Major: the generic error toast is risky for a logging app.** "Something went wrong. Please try again." doesn't say what failed. For a logging app the question that matters is "did my reading save?"
- Fix: write specific messages, such as "Reading for Freezer 2 wasn't saved. Check your connection and try again. Your entry is kept." Keep the toast up until dismissed, or at least long enough to read, and announce it to screen readers. Don't retry silently.
- I can't tell from the text whether any of that is already done.

**6. Moderate: the Reports empty state is generic.**
- "Add Item" and "your first item" don't match what a food bank adds, which is a unit or a sensor.
- Reports likely matter for health inspections and audits, and the empty state doesn't say so.
- Fix: for example, "No reports yet. Add a fridge or freezer and start logging to generate inspection-ready temperature reports." with a button reading "Add a unit." Keep the outline icon and the single primary action.

**7. Moderate: the navigation and welcome copy are boilerplate.**
- "Analytics", "Users" and "Welcome back! Here's what's happening today." could belong to any app.
- Fix: nav items like Units, Alerts, Logs, Reports and Settings, with Users under Settings. Replace the subtitle with a status summary, like "1 unit needs attention."

**8. Minor: the trend indicators (stat cards) use color plus an arrow, which is good, but the logic is wrong for this product.** "-3% from last month" in red works for sales, but "more sessions is better" has no equivalent here. Drop month-over-month deltas unless one is actually useful, such as the count of excursions this month.

## What to keep
- **The shell:** a top bar, a left nav with a clearly selected item, and a page title. It's conventional, so it will be familiar to volunteers.
- **Stat cards as a summary row:** a quick status strip is the right pattern. Only the content needs to change.
- **Text with the arrow on trends:** meaning isn't carried by color alone. Keep that rule for in-range and out-of-range states, using an icon or label next to the red and green.
- **The empty state structure:** an icon, one sentence and one primary button. It's simple and has a clear next step.

**Not checked:** contrast, font sizes, touch-target sizes, responsive behavior, keyboard and screen-reader behavior, and the actual colors, since I only have a text description. Before the demo I'd run a quick check with 3–5 volunteers asking them to find any unit that's out of range. If they can't do it in a few seconds, the fixes above aren't done yet.
