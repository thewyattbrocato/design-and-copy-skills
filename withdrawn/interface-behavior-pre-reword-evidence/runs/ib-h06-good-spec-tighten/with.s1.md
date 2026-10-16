Here's the tightened version. I kept every rule and added no features.

**Reschedule a class**

- **Which classes:** The Reschedule button appears only on the student's next three booked classes. Older bookings are under Past.
- **Session list:** Tapping Reschedule opens the open sessions for the same class level, nearest date first. The student's last-used studio is pre-selected.
- **Search:** The student can search the list by weekday or teacher. The app remembers their search choice for next time.
- **Moving the booking:** Picking a session moves the booking immediately, with no confirmation dialog.
- **Undo banner:** A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
  - Undo restores the original booking and takes back the old seat if it is still free.
  - If the seat has been taken, the banner says so and offers the waitlist.
- **Loading:** While a new list loads, the old list stays visible and a thin progress line shows at the top. After 5 seconds, a "Still loading" message appears with a retry link.
- **Out of scope:** Cancelling a booking less than 24 hours before class is not part of this flow. It asks first, and the question states the fee.

I changed three things in the wording:
- I merged the "Default:" label into the first rule. A label with no alternative case read as if a rule were missing.
- I replaced "Cancelling... is the one place we ask first" with a scope note. As written, it implied this flow had an exception.
- I split the undo outcomes into two bullets so developers can test each one.

Three points are still unclear, and I left them as they were. Please settle them before handoff:
1. **What does search remember?** It could be the last search term, or the last filter type (weekday or teacher). The wording fits both.
2. **How do the studio pre-selection and the search interact?** For example, does a remembered search apply across studios?
3. **What does retry do after "Still loading"?** The spec doesn't say whether it re-requests the list or restarts the wait. I assumed the first.
