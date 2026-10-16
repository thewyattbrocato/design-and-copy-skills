Here are four reminders for the 2-day-out send:

**1. Simple and friendly** (136 characters)
> Hi {first_name}, reminder: your Birchwood Dental visit is {date} at {time}. Reply C to confirm or R to reschedule. Questions? (555) 0100

**2. Fee up front** (139)
> Birchwood Dental: {first_name}, you're booked {date} at {time}. Reply C to confirm, R to reschedule. Changes within 24 hrs incur a $45 fee.

**3. Reschedule-focused, with phone** (138)
> Hi {first_name}! Birchwood Dental appt: {date} at {time}. Reply C to confirm. Need to change it? Reply R or call (555) 0100 24+ hrs ahead.

**4. Direct, with late-cancel rule** (134)
> {first_name}, you're booked at Birchwood Dental {date}, {time}. Reply C to confirm or R to reschedule. Late cancel (<24 hrs): $45 fee.

**On the 160 limit:** the counts above include the merge fields as literal text, for example `{first_name}` is 12 characters. Real values change the length. I checked a worst case of a 15-character name, a date like "Wednesday, Oct 21" and a time like "10:30 AM". Every message stays at or under about 155 characters in that case.

- **Date format:** if your tool fills `{date}` with something longer, like "Wednesday, October 21st", messages 2 and 3 could go over. Use a short date format if you can.
- **Fee wording:** #1 doesn't mention the fee, and #3 only implies the 24-hour rule. #2 and #4 state the fee outright, so use one of those if you want it in every reminder.
- **Testing:** I'd A/B test them against each other. You have no no-show baseline, so I'd start tracking no-show rates per variant now.
