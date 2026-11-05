**Cut push down to the few alerts that need action in a time window. Move everything else to the in-app trip timeline and an email digest.** Right now, low-value alerts are crowding out the two that matter, and users are turning off push to escape the noise. Once they turn it off, they miss the cancellation and the card problem.

| # | Alert | Channel | Why |
|---|---|---|---|
| 5 | Cancelled, rebooked automatically | **Push** | The itinerary changed and the user may need to act. |
| 10 | Agent paused, card expired | **Push + email** | Rebooking is blocked until they fix it. Don't let it be muted. |
| 4 | Delayed 20+ min | **Push only if it breaks a connection or moves arrival a lot**; otherwise timeline | 20 minutes is common and often harmless. |
| 3 | Gate changed | **Push only within ~2 hours of departure**; otherwise timeline | Matters at the airport, noise the day before. |
| 2 | Price dropped $12 | **Digest/timeline**; push only for large drops (e.g., 10%+ or $50+) | $12 is the likely source of "a lot." |
| 9 | Seat upgrade available | **In-app**; email if it has a deadline | Useful, not urgent. |
| 6 | Check-in open | **Timeline/email**, optional push off by default | The airline already sends this. |
| 1 | Booking confirmed | **Email** | The user expects it in their inbox, not as a push. |
| 7 | Weekly deals roundup | **Email, opt-in** | Marketing, not trip management. |
| 8 | "Found no better fare" | **Remove** (keep it in the trip history at most) | A non-event shouldn't generate a notification. |

The thresholds (20 minutes, 2 hours, $50 or 10%) are my starting guesses. Tune them against your data.

**Other changes:**
- **Protect the critical push types** so users can't disable them. They can still mute everything else.
- **Batch:** one push per trip per event, not one per price check.
- **Check compliance** before changing anything. Cancellation and rebooking notices may have airline-rule or consumer-protection requirements, so confirm with whoever owns that.
- **Track results:** push opt-out rate, notification-to-action rate on cancellations, and rebook success. If opt-outs drop and rebook outcomes hold, the cut worked.
