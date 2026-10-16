**Day 1: Break it on purpose**
- Test unhappy paths: double-bookings, overlapping slots, cancellations, past dates, time zones/DST, and invalid input.
- Check failure states: payment declines, email/SMS failures, and network drops mid-booking.
- Make sure every error message tells the user what to do next.
- Test on a real phone, since groomers often use phones.

**Day 2: Prepare to launch**
- Set up error tracking (Sentry), uptime monitoring, and automated database backups. Test a restore.
- Confirm that confirmation and reminder emails reach inboxes and don't land in spam (SPF/DKIM).
- Add a privacy policy and terms, and a visible support contact.
- Write a short rollback plan and keep a way to disable signups.
- Seed a real groomer's account, and walk them through onboarding.

**Skip:** new features, refactors, and polish that doesn't affect trust.
