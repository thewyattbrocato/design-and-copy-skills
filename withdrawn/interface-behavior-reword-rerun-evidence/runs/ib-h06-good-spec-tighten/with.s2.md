**Reschedule a class**

- **Which classes:** Only the student's next three booked classes show a Reschedule button. Older bookings are under "Past".
- **Choosing a session:** Tapping Reschedule opens the open sessions for the same class level, nearest date first. The student's last-used studio is pre-selected.
- **Moving the booking:** Picking a session moves the booking immediately, with no confirmation dialog. A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- **Undo:** Undo restores the original booking and returns the old seat if it is still free. If the seat has been taken, the banner says so and offers the waitlist.
- **Loading:** While a new list loads, the old list stays on screen with a thin progress line at the top. After 5 seconds, a "Still loading" message appears with a retry link.
- **Search:** The session list can be searched by weekday or teacher. The choice is remembered for next time.
- **Cancelling (separate flow):** Cancelling a booking within 24 hours of class is the only action that asks first. The question states the fee that will be charged.

**Changes I made**
- I split the cancellation rule from the reschedule rules, so it reads as a contrast and not as a step in this flow.
- I turned the loading sentence into separate cases and put them in order.
- I made the wording parallel and cut filler. I added no features.

**Questions for you before this goes to developers**
1. **"Default: the Reschedule button shows only…":** I read this as the button appearing only on the next three classes. If you meant something else, such as a list of three, please correct it. I also dropped the word "Default", since nothing here overrides it.
2. **"The choice is remembered":** This could mean the search term, the weekday or teacher filter, or the studio. The studio is already covered by "last-used". Please name what is remembered.
3. **Undo after 10 seconds:** The spec doesn't say whether the student can still undo once the banner is gone. I left it unstated, but a developer will ask. If you want to add a rule, say so and I'll word it.
