Here's a tightened version. I kept the behavior as you wrote it and only cut wording and fixed the order.

**Reschedule a class**

1. **Which bookings show Reschedule.** The button appears on the student's next three booked classes. Earlier classes are listed under "Past".
2. **Session list.** Tapping Reschedule opens the open sessions for the same class level, sorted by nearest date. The student's last-used studio is pre-selected.
3. **Search.** The list can be searched by weekday or teacher. The choice is remembered for next time.
4. **Moving the booking.** Picking a session moves the booking immediately, with no confirmation dialog. A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
5. **Undo.**
   - If the old seat is still free, Undo restores the original booking.
   - If it isn't, the banner says so and offers the waitlist.
6. **Loading.** While a new list loads, the previous list stays on screen and a thin progress line shows at the top. After 5 seconds, a "Still loading" message appears with a retry link.
7. **Cancellation (separate flow).** Cancelling a booking within 24 hours of class is the only action that asks for confirmation. The prompt states the fee that will be charged.

**Questions to settle before handoff.** I left these as you wrote them, because answering them would change the behavior.

- **"Older ones are under Past."** This could mean classes that have already happened, or booked classes beyond the next three. Item 1 reads as the first, but the "next three" cap suggests the second may be intended.
- **"The choice is remembered."** Is it the search term, the weekday or teacher filter, or the studio selection? The studio is already covered by "last-used", so I assumed this refers to search. Developers will have to guess if you don't say.
- **Waitlist after a failed Undo.** Does the student stay booked in the new session while they wait, or do they have no booking until a seat opens? Item 5 doesn't say.
- **Cancellation placement.** It isn't part of rescheduling. If it's already specified elsewhere, you could shorten item 7 to a cross-reference.
