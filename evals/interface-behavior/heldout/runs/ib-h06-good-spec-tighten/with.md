# Reschedule a class

**Which bookings can be rescheduled**
- The Reschedule button appears only on the student's next three booked classes. Older bookings are under **Past**.

**Choosing a session**
- Tapping Reschedule opens a list of open sessions at the same class level, nearest dates first.
- The student's last-used studio is pre-selected.
- The list can be searched by weekday or teacher. The student's choice is remembered for next time.

**Loading**
- While a new list loads, the previous list stays on screen and a thin progress line shows at the top.
- After 5 seconds, a "Still loading" message appears with a retry link.

**Moving the booking**
- Picking a session moves the booking immediately, with no confirmation dialog.
- A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- Undo returns the booking to its original session.
  - If the original seat is still free, the student gets it back.
  - If it is not, the banner says so and offers the waitlist.

**Cancellation (separate flow)**
- Cancelling a booking within 24 hours of class asks for confirmation first, and the prompt states the fee that will be charged.

I only reworded and regrouped the spec. I added no features. Four points are ambiguous, and I left them as written because the answers are your decisions:

1. **"The choice is remembered."** It could mean the search term, the studio selection, or both. I kept your wording.
2. **"Nearest dates."** It's unclear whether this means nearest to today or nearest to the original class date.
3. **Undo and the waitlist.** The spec doesn't say what the booking's state is when Undo fails and the student joins the waitlist. It could stay in the new session or be released.
4. **The cancellation rule.** It's the only line outside the reschedule flow. I moved it to its own section, but you may want to cut it and keep it in the cancellation spec.
