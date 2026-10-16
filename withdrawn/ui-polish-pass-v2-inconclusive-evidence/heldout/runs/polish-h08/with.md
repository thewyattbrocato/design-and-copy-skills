Spend the two days on what breaks real users, not on new features.

**Day 1: unhappy paths**
- Double-bookings and race conditions (two people grabbing the same slot).
- Time zones and DST in appointment times.
- Cancel and reschedule flows, plus past dates and overlapping appointments.
- Failed payments, expired sessions, and bad input.
- Reminder emails/SMS: confirm they send and show the right time.

**Day 2: launch safety**
- Backups and a tested restore.
- Error monitoring (Sentry or similar) and uptime alerts.
- Auth basics: password reset, rate limiting, and one groomer can't see another's data.
- Privacy policy, terms, and a support email.
- A mobile pass on a real phone.
- Empty, loading, and error states. I can run a UI polish pass for those if you want.

**Before launch:** have one real groomer run a full day of bookings, and write a rollback plan.
