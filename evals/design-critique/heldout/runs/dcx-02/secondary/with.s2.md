**Verdict: this reads as a generic SaaS admin template, not a food-safety tool.** The first screen doesn't answer the question a food bank opens Coldshelf to answer: are our fridges and freezers in range right now? Nothing on it is about temperature, units, or alerts. Fix that before the demo.

I'm judging the text description only. I can't assess layout, color, spacing, contrast, or responsive behavior.

## Findings, in order

**1. Blocker: the stat cards measure the wrong things.** Total Users, Revenue, Active Sessions, and Conversion Rate are web-app metrics. A food bank manager has no use for conversion rate, and the cards don't show whether anything is safe. Replace them with operational status: units in range, units out of range or in alarm, readings overdue, and last reading time per unit. Keep the delta pattern only where it means something, such as "missed logs this week vs last week."

**2. Blocker: the navigation lacks the product's core objects.** The sidebar is Dashboard, Analytics, Reports, Users, Settings. There's no Fridges/Units, Readings/Logs, or Alerts. "Dashboard" and "Analytics" also overlap with no visible difference. Add the core objects to the sidebar and make Alerts reachable from every screen.

**3. Major: the chart can't be read.** "Overview" shows a single line over Jan–Dec with no y-axis labels, so nobody can tell whether 3°C or 30°C. Temperature is best shown as a line per unit against a labeled safe-range band, with units (°F or °C) on the axis and a time range control. A year view on a "what's happening today" screen is also the wrong default.

**4. Major: the data looks stale and placeholder.** Today is October 16, 2026, and the Recent Activity rows are dated 01/01/2026 through 01/03/2026, roughly nine months old. The subtitle says "here's what's happening today," which the screen contradicts. Real data or not, there's no freshness indicator. For temperature logging, "last reading 4 min ago" is essential. Replace the rows before the demo; a food bank will notice.

**5. Major: the error toast can cause real harm.** "Something went wrong. Please try again." doesn't say what failed, whether the reading was saved, or what to do. If a temperature log fails to save, the user may believe it was recorded when it wasn't, and that's a compliance problem for them. Use a message that names the failed action and its state, for example "Reading for Walk-in Fridge 2 wasn't saved. Check your connection and try again." Confirm it's true to your app's behavior, and keep the toast until dismissed for errors.

**6. Major: the Recent Activity table is generic.** Columns are Name, Status, Date, Action, with rows "Item 1/2/3," "Active/Pending/Inactive," and "View" on every row. Nothing says what a status means for a fridge. Use unit names and reading or event types (e.g. "Out of range: 6.2°C"). Show time as well as date, and use an unambiguous date format (e.g. 16 Oct 2026), since food banks may be in several countries.

**7. Major: the Reports empty state is generic and its button is vague.** "No data yet. Get started by adding your first item!" with an "Add Item" button could be any product. Better: "No reports yet. Reports summarize temperature readings by fridge or freezer. Log your first reading to start." with a primary button that names the action, such as "Log a reading" or "Add a fridge or freezer." Keep the outline document icon and the single primary CTA, since those work.

**8. Minor to moderate: the top bar doesn't show scope.** Search is "Search...", which doesn't say what it searches. Food banks often run several sites, but the avatar "JD" shows no organization or site. A site switcher and a labeled search ("Search units, readings, volunteers") would help. Confirm whether the bell shows an unread count, since an alert count matters more than a generic notification.

## What works and should stay

- **Clear sidebar selected state.** Knowing where you are is a basic requirement and it's met.
- **Trend deltas with arrows and text.** Direction is shown by the arrow and sign, not color alone, and the "from last month" baseline gives context.
- **Single primary action on the empty state.** One blue button with a clear next step is the right pattern. Its label needs fixing, not its form.
- **Consistent header on the title and subtitle.** The hierarchy is predictable, so the fixes above can slot in without restructuring the page.

## Not checked

Contrast, type sizes, touch targets, spacing, responsive layout, keyboard and screen-reader behavior, and the bell and avatar states. Send a screenshot or Figma export and I can check those.
