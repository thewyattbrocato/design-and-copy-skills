**Day 1: break the unhappy paths**
- Double-bookings and race conditions, cancellations and reschedules, and past or overlapping slots.
- Time zones and DST, since booking bugs usually live there.
- Form validation, plus empty, loading, and error states on every screen.
- Auth edge cases: password reset, expired sessions, and one groomer being unable to see another's data.

**Day 2: make it launch-ready**
- Confirmation and reminder emails or texts. Check that they send and don't land in spam.
- Error monitoring (Sentry or similar), automated backups, and a tested restore.
- Test on a real phone, since groomers will likely use one.
- Add a privacy policy and terms, and test payments end to end if you take them.
- Write a short onboarding guide or seed data for first-time users.
- Prepare a rollback plan and a support email address.

**Skip:** new features. Keep a post-launch list instead.

If you'd like, I can run the UI polish pass on your code next.
