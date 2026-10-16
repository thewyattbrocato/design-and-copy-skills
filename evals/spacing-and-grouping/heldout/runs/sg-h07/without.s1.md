I couldn't save the file. The Write tool is disabled in this session, and I have no other way to create files here. Nothing exists on disk yet. If you enable Write, or tell me another route, I'll save it as `studio-booking.html` in the working directory.

I haven't opened the page in a browser, so the layout is untested. Here is the design and the main pieces.

**Layout**
- **Header:** the title, plus a live count such as "10 slots · 7 booked · 3 open".
- **Filters:** a single row across the top with Date, Room, Engineer and a Reset button. It drops to two columns on narrow screens.
- **Day schedule (left):**
  - A list of 10 hourly slots from 09:00 to 18:00, each 44px tall.
  - Each row shows the time, client and room, engineer, and a status pill (Confirmed, Hold or Open).
  - Rows are selectable by click, Enter or Space, and the selected row has an accent bar.
- **Side summary (right, 300px, sticky):** the selected booking's status, time range, room, engineer, session type, rate, total, and two action buttons. The buttons change with the booking: Open shows Block and Book slot, Hold shows Reschedule and Confirm, and Confirmed shows Reschedule and Edit.

**Styling**
- Everything is inline CSS and one small script, with a system font stack and no external assets.
- Colors are CSS variables with a `prefers-color-scheme` dark variant.
- Status colors always come with a text label.

**Behavior:** the Room and Engineer filters narrow the slot list and update the count, and Reset restores the defaults. Changing the date updates the day heading, but the sample bookings stay the same for every date.

**Sample data:** an array of 10 objects, with fields `time`, `room`, `client`, `type`, `eng` and `status`. You'd replace it with real bookings.

I can paste the full file (about 200 lines) here so you can save it yourself.
