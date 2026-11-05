**Reschedule a class**

- **Which bookings:** Each booking shows a Reschedule button only for the student's next three booked classes. Earlier classes are listed under "Past".
- **Session list:** Tapping Reschedule opens the open sessions for the same class level, soonest first. The student's last-used studio is pre-selected.
- **Search:** The student can search the session list by weekday or teacher. The app remembers the last search for next time.
- **Moving:** Picking a session moves the booking immediately, with no confirmation dialog. A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- **Undo:** Undo restores the original booking and its seat. If the seat has been taken, the banner says so and offers the waitlist.
- **Loading:** While a new list loads, the previous list stays visible and a thin progress line shows at the top. After 5 seconds, a "Still loading" message appears with a retry link.
- **Cancellation (separate flow):** Cancelling a booking less than 24 hours before class asks for confirmation first, and the prompt states the fee. This is the only action that asks first.

I changed only wording and structure. I did not add any features. These are the changes:

- "Default: the Reschedule button shows…" is now about which bookings get the button. The old wording read as if the button itself showed the classes.
- I moved the cancellation rule into its own item. It is a different flow, and it was buried in the middle of the reschedule rules.
- "Inside 24 hours" is now "less than 24 hours before class", so the boundary is clearer.
- I put the bullets in the order a user meets them.

Some points are ambiguous, and developers will probably ask about them:

1. **"The choice is remembered":** Which choice is that? I assumed it means the last search term. If you meant the studio selection, or a chosen session, the line needs to say so.
2. **Studio:** The spec pre-selects a studio but doesn't say whether the student can change it. I left that as is.
3. **Failed Undo banner:** The spec doesn't say whether this banner also disappears after 10 seconds. I left that as is.
4. **Undo and the waitlist:** It's unclear whether the booking stays in the new session when Undo fails and the student joins the waitlist for the old one. I left that as is.

I can add wording for any of these once you've decided.
