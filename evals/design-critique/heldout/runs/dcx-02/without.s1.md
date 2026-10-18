**Short version:** this is a generic SaaS admin template with Coldshelf's name on it. A food bank volunteer opening it couldn't tell it's for fridges. Nothing on the screen mentions temperature, units, or whether the food is safe. That's the main problem, and the rest follows from it.

I only have your text description, so I can't judge layout, spacing, contrast, or type size. Check those separately.

## Biggest problems

**1. The stat cards are the wrong metrics.** Total Users, Revenue, Active Sessions, and Conversion Rate mean nothing to a food bank. Revenue and conversion rate are especially off for community nonprofits. The dashboard should answer "is my food safe right now?" Better cards:
- Units in range (e.g. 5 of 6)
- Units in alert or out of range
- Last reading received, or sensors offline
- Missed or overdue manual logs, if volunteers log by hand

"+12% from last month" comparisons don't suit temperature data. Current state and exceptions matter more than trends.

**2. The chart can't do its job.** A single blue line over Jan–Dec with no y-axis labels tells you nothing about temperature. A temperature chart needs:
- A labeled y-axis with units (°F/°C)
- A time range that matches the job (last 24 hours or 7 days, not 12 months)
- A visible safe-range band or threshold line (e.g. 41°F for refrigeration, 0°F for freezers), with excursions marked
- One line per unit, or a unit selector

Don't use color alone to mark out-of-range readings. Add a marker or label too.

**3. "Recent Activity" with Item 1/2/3 is placeholder content.** It should be a units table: unit name, current temp, status, last reading, and maybe a small trend. Sort problems to the top. "Active / Pending / Inactive" doesn't map to anything real here. You want In range / Warning / Out of range / No signal. Three identical "View" links are also ambiguous for screen readers and for scanning. Make the row itself clickable and drop the Action column.

**4. The welcome subtitle wastes your best spot.** "Welcome back! Here's what's happening today." could be a live status line: "All 6 units in range. Last reading 2 min ago." or "Walk-in Freezer 2 has been above 10°F for 40 minutes."

## Other issues

- **Sidebar:** There's no Units/Locations or Alerts. Those are the core objects. Analytics vs. Reports is also vague. Health inspectors will want exportable logs, so call it something like "Compliance logs" if that's what it is.
- **Bell icon:** It needs an unread count. Also, in-app alerts aren't enough, because nobody is watching the dashboard when a compressor fails at 2 a.m. Make sure SMS, email, or push alerts exist, and say so in the product.
- **Search:** "Search..." doesn't say what it searches. Use "Search units, alerts, logs".
- **Red/green arrows:** Don't rely on color alone, since about 1 in 12 men are red-green colorblind. Also, a green up arrow isn't always good. On a temperature metric, up is bad.
- **Reports empty state:** "Add Item" and "first item" are generic. Say what's missing and why: "No readings yet. Add a fridge or freezer to start logging temperatures," with a button labeled "Add unit". If the page is empty because no report has been generated, offer "Generate report" instead. A document outline icon is fine.
- **Error toast:** "Something went wrong. Please try again." is the weakest piece, and it matters most here. If a temperature log fails to save, the user needs to know:
  - What failed ("Couldn't save the 2:15 pm reading for Walk-in Fridge")
  - Whether data was lost
  - What to do next

  Toasts also auto-dismiss. A failed save of a safety record should persist until acknowledged. Also plan for offline use, because walk-in coolers are often wifi dead zones.

## Context to design for

Your users are volunteers, often non-technical and sometimes older, and often on a phone or tablet in a cold, busy back room. That argues for large tap targets, high contrast, plain language, and a status you can read at a glance from a few feet away. A big "All good" or "1 unit needs attention" banner would do more than any of the current cards.

## What's fine

The overall structure works: top bar, sidebar, summary row, detail below. Selected-state nav and an outline-icon empty state with one clear action are also sound patterns. It's the content that needs replacing, not the skeleton.

If you want, I can sketch a revised version of this screen as text or build a quick mockup.
