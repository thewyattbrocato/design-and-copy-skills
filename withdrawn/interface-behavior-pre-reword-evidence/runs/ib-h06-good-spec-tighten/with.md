Here's the tightened spec. I kept the behavior the same and only changed the wording.

**Reschedule a class**

- **Which bookings:** The Reschedule button appears only on the student's next three booked classes. Older bookings are under "Past".
- **Session list:** Tapping Reschedule opens the open sessions for the same class level, soonest first. The student's last-used studio is pre-selected.
- **Moving:** Picking a session moves the booking immediately, with no confirmation dialog.
- **Undo banner:** A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
  - Undo restores the original booking and reclaims the old seat if it is still free.
  - If the seat has been taken, the banner says so and offers the waitlist.
- **Loading:** While a new list loads, the previous list stays visible and a thin progress line shows at the top. After 5 seconds, a "Still loading" message appears with a retry link.
- **Search:** Students can search the session list by weekday or teacher. The search choice is remembered for next time.
- **Cancelling (separate flow):** Cancelling a booking within 24 hours of class asks for confirmation first. The prompt states the fee that will be charged. This is the only confirmation in the booking flows.

**What I changed**
- Split the "Default" bullet into a plain rule about which bookings show the button.
- Gave each bullet one subject and one behavior, and made the Undo outcomes a nested list.
- Moved the cancellation rule into its own item. It was attached to the "no confirmation" sentence, which made it read as part of rescheduling.
- Changed "gives the old seat back" to "reclaims the old seat", and "the one place we ask first" to "the only confirmation".

**Questions for you (I left these unchanged because answering them would change the behavior):**
1. **"The choice is remembered" in search:** Is it the last search term, or the last filter, such as weekday or teacher? Developers will have to guess.
2. **Retry link:** Does it reload the list, or does it cancel and restart the request?
3. **Seat taken on Undo:** Does the student stay in the new session, or is the booking left unchanged? The spec doesn't say.
4. **Banner timing:** Does Undo stay available after the banner disappears? If it doesn't, the 10-second window may be too short for screen-reader users. You may want to ask for the banner to be announced to screen readers.
