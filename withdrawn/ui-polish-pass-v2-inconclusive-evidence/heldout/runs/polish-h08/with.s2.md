**Day 1: break the unhappy paths**
- Double-bookings, overlapping slots, and time zones or DST.
- Cancellations and reschedules. Check what a groomer sees and what a customer sees.
- Failed payments, expired sessions, and bad input.
- Every empty, loading, and error state. Replace raw errors with plain-language messages.
- Mobile screens, since groomers will likely use phones.

**Day 2: prepare to launch**
- Confirmation and reminder emails or texts. Check that they arrive and aren't marked as spam.
- Set up error monitoring (e.g. Sentry), uptime checks, and automated database backups.
- Add a privacy policy, terms, and a support contact.
- Test your production deploy and a restore from backup.
- Walk through the full flow as a brand-new user on a real phone.
- Have one groomer try it while you watch.

**Skip:** new features and refactors. Keep a "v1.1" list instead.

Freeze changes a few hours before launch.
