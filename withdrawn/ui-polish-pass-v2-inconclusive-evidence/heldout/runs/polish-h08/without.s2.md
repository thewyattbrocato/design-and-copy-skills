Spend the two days on the unhappy paths:

**Day 1: break it**
- Double-bookings and race conditions: two clients grabbing the same slot.
- Time zones, DST, and past-date bookings.
- Bad input: empty fields, long names, odd characters in pet names.
- Failed payments, email/SMS failures, and network drops mid-booking.
- Cancel and reschedule flows.

**Day 2: prepare to launch**
- Error tracking (e.g., Sentry), uptime monitoring, and automated database backups.
- Test the restore process.
- Security basics: auth checks, rate limiting, HTTPS, and no secrets in the repo.
- Clear error messages, empty states, and a mobile check on a real phone.
- Privacy policy, terms, and a support contact.
- A rollback plan.

**Rule:** No new features. Have one real groomer run through the app before launch.
