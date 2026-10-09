Here are four options for the 2-day-out text. I counted each with the merge fields at their literal length (`{first_name}` is 12 characters). Real values will change the length, so I left a buffer of at least 12 characters under the cap.

**1.** (~137)
Hi {first_name}, your Birchwood Dental appt is {date} at {time}. Reply C to confirm or R to reschedule. $45 fee if changed within 24 hrs.

**2.** (~130)
Birchwood Dental: {first_name}, see you {date} at {time}. Reply C to confirm, R to reschedule. Less than 24 hrs notice = $45 fee.

**3.** (~125, no fee mention, includes the phone number)
Birchwood Dental: Hi {first_name}, you're booked {date} at {time}. Reply C to confirm or R to reschedule. Or call (555) 0100.

**4.** (~132)
{first_name}, your Birchwood Dental visit is {date} at {time}. Reply C to confirm, R to reschedule. Late cancels (<24 hrs) cost $45.

- **Length:** Each should stay under 160 if `{date}` is short, like "Oct 9" or "Thu, Oct 9". A long format like "Wednesday, October 15" adds about 15 characters, which would push #1 close to the limit. Send yourself a test with your longest-name patient and your longest date format.
- **Fee wording:** #3 leaves out the $45 fee to make room for the phone number. If you want the fee in every message, use #1, #2, or #4.
- **Performance:** I have no no-show data, so I can't say which will cut no-shows most. If your tool supports it, A/B test them.
