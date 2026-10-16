Spend the two days on the unhappy paths, in this order:

**Day 1: break it**
- **Double-bookings:** test two people grabbing the same slot, and rebooking or canceling mid-flow.
- **Time zones and DST:** wrong appointment times are the worst bug for a booking app.
- **Bad input:** empty fields, odd characters in pet names, and failed payments if you take them.
- **Notifications:** confirm that emails and SMS reminders actually arrive, and check spam placement.

**Day 2: prepare for launch**
- **Safety net:** set up error monitoring (e.g. Sentry), uptime alerts, and database backups. Test a restore.
- **Basics:** add a privacy policy and terms, and make sure password reset works.
- **Real use:** have one groomer use it on their phone, and fix whatever confuses them.
- **Rollback:** write down how you'll roll back.

Don't add features now. Keep a post-launch list instead.
