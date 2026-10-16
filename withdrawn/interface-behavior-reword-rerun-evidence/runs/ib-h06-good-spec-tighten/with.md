Here's the tightened version. I kept the content and added no features. I reordered it to follow the flow, made each rule a single behavior, and used consistent terms ("booking" for the student's reservation, "session" for an open slot).

**Reschedule a class**

**Choosing a booking**
- The Reschedule button appears only on the student's next three booked classes. Later bookings are not shown. [see question 1]

**Choosing a session**
- Tapping Reschedule opens a list of open sessions at the same class level, nearest date first.
- The student's last-used studio is pre-selected.
- The student can search the list by weekday or teacher. The search choice is remembered for next time. [see question 2]

**Moving the booking**
- Picking a session moves the booking immediately, with no confirmation dialog.
- A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- Undo restores the original booking and takes back the old seat.
  - If the seat is no longer free, the banner says so and offers the waitlist.

**Loading**
- While a new list loads, the previous list stays on screen and a thin progress line shows at the top.
- After 5 seconds, a "Still loading" message appears with a retry link.

**Out of scope for this flow**
- Cancelling a booking less than 24 hours before class is the only action that asks for confirmation. The prompt states the fee that will be charged. This is specified separately.

**Questions to settle before handoff**
1. **"Older ones are under 'Past'."** Do you mean past classes, or upcoming classes beyond the next three? If it's the latter, those bookings need a named place to live, because "Past" would be the wrong label. If it's the former, the first bullet can say "Past classes can't be rescheduled."
2. **"The choice is remembered."** Does this mean the last search term, or the last filter type (weekday or teacher)? Developers will build different things for each.
3. **Banner after a failed Undo.** The spec doesn't say whether the "seat not free" banner has its own duration or stays until dismissed. Since it carries the waitlist action, I'd suggest it stay until dismissed, but that's your call.
4. **Changing the studio.** The studio is pre-selected, but the spec doesn't say whether the student can switch it. I left it as written.
