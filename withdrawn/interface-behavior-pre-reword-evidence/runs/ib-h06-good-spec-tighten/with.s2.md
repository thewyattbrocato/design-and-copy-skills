**Reschedule a class**

- **Which bookings:** Reschedule is available on the student's next three booked classes. Older bookings are under Past.
- **Session list:** Tapping Reschedule opens the open sessions for the same class level. The nearest dates come first, and the student's last-used studio is pre-selected.
- **Moving:** Picking a session moves the booking immediately, with no confirmation dialog. A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- **Undo:** Undo restores the original booking and its seat. If the seat has been taken, the banner says so and offers the waitlist.
- **Loading:** While a new list loads, the old list stays on screen and a thin progress line shows at the top. After 5 seconds, a "Still loading" message appears with a Retry link.
- **Search:** The session list can be searched by weekday or teacher. The last search is remembered for next time.
- **Cancelling (separate flow):** Cancelling a booking within 24 hours of class is the only action that asks first. The prompt states the fee that will be charged.

I changed only wording and structure. I left these for you to confirm:

1. **Reschedule button:** The original says the button "shows only the next three classes." I read that as the button appearing only on those three bookings. If you meant something else, such as a list capped at three, fix the first bullet.
2. **Remembered choice:** "The choice is remembered" could mean the search term, a weekday or teacher filter, or the studio. I wrote "last search." Please confirm, since remembering a stale search term could hide sessions on the next visit.
3. **Undo and the seat:** The spec doesn't say what happens to the new seat when Undo is used. I assume it is released. Developers will probably ask, so it's worth one line.
4. **Banner timing:** A 10-second banner can disappear before a screen-reader user or slower reader gets to it. After the banner goes, the spec gives no other way to undo. I didn't add anything, but you may want to raise it with the developers.
