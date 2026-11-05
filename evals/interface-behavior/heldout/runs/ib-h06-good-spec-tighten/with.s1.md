**Reschedule a class**

- **Which bookings:** Reschedule is available on the student's next three booked classes. Older bookings are under "Past".
- **Session list:** Tapping Reschedule opens the open sessions for the same class level, nearest date first. The student's last-used studio is pre-selected.
- **Search:** The list can be searched by weekday or teacher. The student's choice is remembered for next time.
- **Moving:** Picking a session moves the booking immediately, with no confirmation dialog.
- **Banner:** A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- **Undo:** Undo restores the original booking and returns the old seat if it is still free. If the seat is taken, the banner says so and offers the waitlist.
- **Loading:** While the new list loads, the old list stays visible and a thin progress line shows at the top. After 5 seconds, a "Still loading" message appears with a retry link.

**Related rule:** Cancelling a booking within 24 hours of class is the only action that asks for confirmation. The prompt states the fee that will be charged.

**Wording I changed**
- I split the long banner bullet into banner and undo.
- I moved the cancellation rule out of the reschedule steps, since it's a separate flow.
- I moved search up to follow the list it applies to.

**Questions I left as written, for you to settle**
- "The choice is remembered" under search is unclear. It could mean the last search term, the chosen session, or the studio. The pre-selected studio already covers the last one, so the developers will need you to say which you mean.
- "The old list" during loading is ambiguous. It could mean the previously shown session list, or the student's bookings.
- If the student reschedules to a session in another studio, does that become the new "last-used studio"? The spec doesn't say.
