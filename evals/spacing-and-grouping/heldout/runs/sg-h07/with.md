I couldn't create the file. The Write tool is disabled in this session, so `studio-booking.html` doesn't exist yet. I also have no other tool that can create it, so I can't work around this.

Here is the design I was going to write, so you can check it before I build it:

- **Filters (top):** one tinted bar holding Date, Room and Engineer, with Reset and "+ New booking" pushed to the right.
- **Day schedule (left):** one panel with a header showing the date and counts. Below it are 10 slots from 09:00 to 18:00, separated by hairline rules instead of cards. Each row shows time and duration, client and session type, room, and a status pill (Booked, Hold, Open or Blocked). Clicking a row selects it, with an accent tint and a left bar.
- **Summary (right, 300px, sticky):** the selected booking's client, time, room, engineer and session type, then notes, then billing with a total. Edit and Reschedule buttons sit at the bottom. A few lines of inline JS update this panel when you select a row.
- **Spacing:** a 4/8/12/16/24 px scale. Gaps inside a group are smaller than gaps between groups, and the layout is dense, with 44px rows and 13px type. System fonts only, no external assets, and it collapses to one column below 820px.

If you re-enable Write, or tell me where else to put the file, I'll create it. I can also paste the full HTML here for you to save yourself.
