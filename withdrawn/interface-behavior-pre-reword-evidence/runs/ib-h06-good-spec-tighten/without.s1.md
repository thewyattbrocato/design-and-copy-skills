**Reschedule a class**

1. **Eligible bookings**
   - The Reschedule button appears only on the student's next three booked classes.
   - Older bookings are listed under "Past".

2. **Session list**
   - Tapping Reschedule opens a list of open sessions at the same class level.
   - Sessions are sorted by date, nearest first.
   - The student's last-used studio is pre-selected.

3. **Moving a booking**
   - Picking a session moves the booking immediately, with no confirmation dialog.
   - A banner appears at the top of the screen for 10 seconds: "Moved to Thu 14 Mar, 6 pm. Undo".
   - Tapping Undo restores the original booking if the old seat is still free.
   - If the seat is no longer free, the banner says so and offers the waitlist.

4. **Loading**
   - While the new list loads, the previous list stays visible and a thin progress line shows at the top.
   - After 5 seconds, a "Still loading" message appears with a retry link.

5. **Search**
   - The session list can be searched by weekday or teacher.
   - The student's search choice is remembered for next time.

6. **Cancellation (outside this flow)**
   - Cancelling a booking within 24 hours of class is the only action that asks for confirmation.
   - The confirmation states the fee that will be charged.

I kept your meaning and added no features. These points are still ambiguous, and the developers will probably ask about them:

- **Item 1:** I read "the Reschedule button shows only the student's next three booked classes" as "the button appears only on those classes". Please confirm that's what you mean.
- **Item 3:** The spec doesn't say whether the new seat is released on Undo. I assumed it is, but I left that out of the spec.
- **Item 5:** "The choice is remembered" could mean the search term, the weekday/teacher filter, or both. Please pick one.
- **Item 6:** I moved the cancellation rule to its own item, since it isn't part of rescheduling. You could also cut it here and put it in the cancellation spec.
