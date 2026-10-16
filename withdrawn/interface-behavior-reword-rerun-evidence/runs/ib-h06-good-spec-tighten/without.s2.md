**Reschedule a class**

**Reschedule button**
- The Reschedule button appears only on the student's next three booked classes. Older bookings are under **Past**.

**Session list**
- Tapping **Reschedule** opens a list of open sessions at the same class level, sorted by nearest date first.
- The student's last-used studio is pre-selected.
- The list can be searched by weekday or teacher. The student's search choice is remembered for next time.

**Moving a booking**
- Picking a session moves the booking immediately, with no confirmation dialog.
- A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- **Undo** returns the booking to its original session and restores the original seat, if it is still free.
- If the seat is no longer free, the banner says so and offers the waitlist.

**Loading**
- While the new list loads, the previous list stays on screen and a thin progress line shows at the top.
- After 5 seconds, a "Still loading" message appears with a retry link.

**Cancellation (separate from rescheduling)**
- Cancelling a booking less than 24 hours before class asks for confirmation first. The prompt states the fee that will be charged. This is the only flow that asks for confirmation.

I kept the content and added no features. I changed the cancellation rule from "inside 24 hours" to "less than 24 hours before class", which is my reading of it. A few points are ambiguous, and developers will likely ask about them:
1. **"Remembered" search:** Is it the last search term, or a weekday or teacher filter? Does it persist across sessions?
2. **"Default" in the first bullet:** Is there a non-default state, such as a setting that shows more than three classes? I dropped the word.
3. **Exactly 24 hours:** Is a cancellation exactly 24 hours out free or charged?
4. **Undo after the banner disappears:** I assumed it is no longer possible.
5. **Last-used studio with no open sessions:** What should the list show?
