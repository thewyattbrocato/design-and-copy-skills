**Reschedule a class**

- **Which bookings:** Each of the student's next three booked classes has a Reschedule button. Earlier bookings are under Past.
- **Session list:** Tapping Reschedule opens the open sessions for the same class level, nearest date first. The student's last-used studio is pre-selected.
- **Search:** The list can be searched by weekday or teacher. The app remembers the search choice for next time.
- **Moving:** Picking a session moves the booking immediately, with no confirmation dialog.
- **Banner:** A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- **Undo:** Undo restores the original booking and returns the old seat if it is still free. If the seat has been taken, the banner says so and offers the waitlist.
- **Loading:** While a new list loads, the previous list stays visible and a thin progress line shows at the top. After 5 seconds, a "Still loading" message appears with a retry link.
- **Cancellation (outside this flow):** Cancelling a booking less than 24 hours before class asks for confirmation first, and the question states the fee. This is the only confirmation in the booking flows.

**Changes I made**
- I merged the "default" and "Past" lines into one rule about which bookings show Reschedule.
- I moved the cancellation rule to the end and marked it as outside this flow. It reads as a different feature sitting in the middle of the reschedule rules.
- I replaced "inside 24 hours" with "less than 24 hours before class", so the boundary is clear.
- I cut the wording that explained the design choices.

**Questions to settle before handoff**
1. **What is remembered?** "The choice is remembered" could mean the search term, the studio, or both. I kept your wording, but developers will have to guess.
2. **Does the waitlist replace the booking?** If Undo fails because the seat is gone, the spec doesn't say whether the student keeps the new session or is left with no booking.
3. **What happens after the 10 seconds?** I assume the move is final and the banner disappears. If so, say so.
4. **What does retry do?** I assume it reloads the session list. Confirm that.

I haven't answered these for you, because each answer would add or change behavior.
