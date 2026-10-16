**Reschedule a class**

1. **Which bookings show Reschedule.** Only the student's next three booked classes show a Reschedule button. Older bookings are listed under "Past".
2. **Session list.** Tapping Reschedule opens a list of open sessions at the same class level, sorted by nearest date first. The student's last-used studio is pre-selected.
3. **Search.** The student can search the session list by weekday or teacher. The app remembers their last search for next time.
4. **Moving the booking.** Picking a session moves the booking immediately, with no confirmation dialog. A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
5. **Undo.**
   - If the original seat is still free, Undo restores the original booking.
   - If the seat is taken, the banner says so and offers the waitlist.
6. **Loading.**
   - While a new list loads, the previous list stays on screen and a thin progress line shows at the top.
   - After 5 seconds, a "Still loading" message appears with a retry link.
7. **Cancellation (outside this flow).** Cancelling a booking less than 24 hours before class is the only action that asks for confirmation. The prompt states the fee that will be charged.

**Changes I made**
- I split the spec into numbered items so developers can reference them.
- I moved the cancellation rule to the end and marked it as outside this flow. It was mixed into the reschedule behavior.
- I cut "Default:" from the first line. It implied a non-default option that the spec doesn't describe.
- I made the sort order, the banner timing and the Undo outcomes explicit.
- I wrote the 24-hour rule as "less than 24 hours before class". The original said "inside 24 hours".

**Ambiguities I left as written**
Each of these needs your decision, since resolving them would add behavior:
- **Remembered search.** "The choice is remembered" could mean the search term, the weekday or teacher filter, or both. I wrote "last search". Please confirm.
- **Pre-selected studio.** Does it filter the list to that studio, or only highlight it? Can the student change it?
- **Waitlist.** If Undo isn't possible and the student joins the waitlist, is the new session kept or released? The spec doesn't say.
- **Retry link.** Does it reload the list, or restart the whole request?
