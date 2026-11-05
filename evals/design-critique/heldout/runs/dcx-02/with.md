**Verdict:** This is a generic SaaS admin template with "Coldshelf" in the corner. Nothing on the screen says temperature, fridge, freezer or food safety. The main question a food bank volunteer brings to this screen is "are my units safe right now?", and the screen can't answer it. Fix the content first. The structure is fine.

I'm assuming the users are volunteers or coordinators who aren't technical, and that this is a mid-fidelity design.

1. **[Blocker] The dashboard doesn't answer the core question.**
   - **Seen:** The four stat cards are Total Users, Revenue, Active Sessions and Conversion Rate. If you swap in any other product's name, they still read true. Revenue and Conversion Rate mean nothing to a food bank.
   - **Why it matters:** Someone opening this screen has to dig for the one thing that matters, which is a unit drifting out of range. A missed excursion can mean spoiled donated food.
   - **Change:** Replace the cards with ones like "Units in range: 5 of 6", "Units out of range", "Last reading received", and "Open alerts". Put an out-of-range list at the top, ahead of everything else. Show each unit with its current temperature, its safe limit and how long it has been out of range. Check the limits with your local health department. Refrigeration is commonly 41°F (5°C) or below, and freezers are commonly 0°F (-18°C) or below.

2. **[Major] The chart can't be read and shows the wrong time scale.**
   - **Seen:** One blue line, Jan to Dec, no y-axis labels, titled "Overview".
   - **Why it matters:** With no values or units, nobody can read a temperature off it. Monthly points would hide the excursion that matters, such as a door left open overnight. A single unnamed line also doesn't say which unit it shows.
   - **Change:**
     - Label the y axis in °F or °C.
     - Default to the last 24 hours or 7 days.
     - Draw the safe limit as a reference line.
     - Mark out-of-range stretches directly on the line.
     - Give one line per unit, or a unit picker.
     - Title it "Temperature, last 24 hours".

3. **[Major] The error toast is generic on a path where failure has real consequences.**
   - **Seen:** "Something went wrong. Please try again." is used everywhere.
   - **Why it matters:** If a reading or a log entry fails to save, the volunteer can't tell whether it was recorded. In a walk-in cooler, weak signal is plausible (my assumption, so check it). A toast that disappears also leaves no record of the failure.
   - **Change:** Write messages per case that say what failed, whether anything was lost and what to do next. For example: "Couldn't save the 2:15 pm reading for Walk-in Freezer. It's stored on this device and will retry." Keep failures that need action on screen until the user dismisses them.

4. **[Major] The Reports empty state is generic and points the wrong way.**
   - **Seen:** "No data yet. Get started by adding your first item!" with an "Add Item" button.
   - **Why it matters:** "Item" isn't a Coldshelf concept. Reports are empty because no units or readings exist yet, and the screen doesn't say that.
   - **Change:** Use something like "No reports yet. Add a fridge or freezer and log its first reading to see history here." Label the button "Add a fridge or freezer".

5. **[Minor to major] The navigation and table use the same generic words.**
   - **Seen:**
     - The sidebar has Analytics, Reports, Users and Settings, but nothing named for the things being monitored. Analytics and Reports also overlap.
     - The table rows are "Item 1/2/3", with statuses Active, Pending and Inactive and dates like 01/02/2026.
     - The Action column has three links that all read "View".
   - **Why it matters:**
     - A date like 01/02/2026 can be read two ways and has no time, which matters for a temperature log.
     - Three identical "View" links give a screen reader no way to tell them apart.
     - Without a Units or Locations entry, the main objects have no home.
   - **Change:**
     - Add "Units" (or "Fridges & Freezers") and "Alerts" to the sidebar, and merge Analytics into Reports unless the two do clearly different jobs.
     - Rename the table "Recent readings and alerts" with columns like Unit, Temp, Status (In range / Out of range), and Time.
     - Show the date and time unambiguously, such as "Nov 4, 2:15 pm".
     - Make the links name their target, such as "View Walk-in Freezer".

6. **[Minor] The top bar has unlabeled controls.**
   - **Seen:** "Search..." doesn't say what it searches. The bell and the "JD" avatar are icon-only.
   - **Change:** Use a placeholder like "Search units or readings", and give the bell and avatar accessible names. Show an unread count on the bell, since alerts matter here.

**Keep:**
- **Stat card trend signals:** Each trend combines an arrow, a sign and a percentage, so it doesn't rely on red versus green alone. Carry that over to the new cards.
- **Empty state structure:** An icon, one sentence of explanation and a single primary button is the right structure. Only the words need to change.
- **Sidebar and title:** The selected sidebar item and the clear page title make it obvious where you are.

**Not checked:** colors, contrast, type sizes, spacing, responsive layout, and the focus and keyboard order. If you can send a screenshot later, I can check those. Before the demo, watch 3 to 5 volunteers do one task: "check whether everything is safe right now." That will show whether the revised first screen works.
