**Reschedule a class**

1. **Which bookings can be rescheduled.** The Reschedule button appears on the student's next three booked classes. Earlier classes are listed under "Past".

2. **Session list.** Tapping Reschedule opens the open sessions for the same class level, nearest date first. The student's last-used studio is pre-selected.

3. **Moving the booking.**
   - Picking a session moves the booking immediately, with no confirmation dialog.
   - A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
   - Undo restores the original booking and returns the old seat, if it is still free.
   - If the seat is taken, the banner says so and offers the waitlist.

4. **Loading.**
   - While the new list loads, the previous list stays visible and a thin progress line shows at the top.
   - After 5 seconds, a "Still loading" message appears with a retry link.

5. **Search.** The session list can be searched by weekday or teacher. The last search choice is remembered for next time.

6. **Cancellation (separate flow).** Cancelling a booking within 24 hours of class asks for confirmation first, and the prompt states the fee. This is the only confirmation in the booking flows.

I made these changes without altering the behavior:
- I split the content into numbered, single-topic items.
- I moved the cancellation rule into its own item. It describes a different flow, and it was mixed into the no-confirmation line.
- I removed "Default:", which suggested a setting that can be changed.

Three points need your answer before this goes to developers:
- **Search memory (item 5):** "The choice is remembered" doesn't say what is remembered. It could be the search term, the weekday or teacher filter, or the studio. The studio is already covered by "last-used" in item 2.
- **Rescheduling a "Past" class (item 1):** The spec doesn't say whether past classes can be rescheduled. I assumed they can't.
- **Undo on the last second (item 3):** The spec doesn't say what happens if the student taps Undo as the banner expires. I left it unspecified rather than invent a rule.
