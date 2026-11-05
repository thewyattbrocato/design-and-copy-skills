Here are 4 options. Counts are for the template with merge fields as literal text. Fields usually expand to something close to their length (`{first_name}` is 12 characters, `{date}` is 6, `{time}` is 6). A long name or a spelled-out date like "Thursday, October 30" adds some length, so I left headroom in each.

**1. Simple confirm (114 chars)**
```
Hi {first_name}, reminder: your Birchwood Dental visit is {date} at {time}. Reply C to confirm or R to reschedule.
```

**2. Fee mention (133 chars)**
```
Birchwood Dental: {first_name}, see you {date} at {time}. Reply C to confirm, R to reschedule. Changes within 24 hrs incur a $45 fee.
```

**3. Call option (128 chars)**
```
{first_name}, your Birchwood Dental appt is {date} at {time}. Reply C to confirm. Need to change it? Reply R or call (555) 0100.
```

**4. Held spot (138 chars)**
```
{first_name}, your spot at Birchwood Dental is held for {date}, {time}. Reply C to confirm, R to reschedule. Under 24 hrs notice: $45 fee.
```

- **Longest case:** #4 is the tightest. With a long name and a full weekday-and-month date, it could reach about 153 characters, which is still under 160. If your tool formats `{date}` even longer, drop the fee line from #4 or switch to #1 or #3.
- **Fee wording:** #2 and #4 mention the fee. #1 and #3 leave it out, so you can see whether the shorter versions work as well. If you want the 24-hour policy stated in every message, #2 and #4 are the ones to use.
- **Testing:** Since you have no no-show stats, you could send each version to a share of patients and compare confirmation rates. That would give you a baseline.
