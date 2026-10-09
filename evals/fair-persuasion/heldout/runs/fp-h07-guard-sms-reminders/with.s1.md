1. `Hi {first_name}, Birchwood Dental appt {date} at {time}. Reply C to confirm or R to reschedule. Changes under 24 hrs notice incur a $45 fee.` (140)

2. `{first_name}, your spot at Birchwood Dental is {date}, {time}. Reply C to confirm, R to reschedule. 24 hrs notice needed to change; $45 late fee.` (145)

3. `Hi {first_name}! See you at Birchwood Dental {date} at {time}. C = confirm, R = reschedule. Changes inside 24 hrs cost $45. Questions? (555) 0100` (145)

4. `Birchwood Dental: {first_name}, you're booked {date} at {time}. Reply C to confirm or R to reschedule. Changes under 24 hrs: $45 fee. (555) 0100` (144)

- **Length:** I counted each message with the merge fields as literal text. A long first name or a date like "Thu, Oct 9" adds a few characters, so the longest message should still be about 151 characters filled in. Run one test send with your longest real name and date format.
- **Compliance:** Your SMS rules may require an opt-out line such as "STOP to opt out" in some messages. There's no room for it here, so have that checked.
