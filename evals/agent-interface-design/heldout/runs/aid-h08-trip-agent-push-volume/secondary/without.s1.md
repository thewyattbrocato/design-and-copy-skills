**Cut push down to about three alerts. Send everything else to the in-app trip timeline, and put the rest in one weekly email.** Push should be reserved for things that cost the user money or make them miss a flight, or that need them to act now.

| # | Notification | Recommendation | Why |
|---|---|---|---|
| 5 | Cancelled, rebooked automatically | **Push** | Urgent and it changes their plans. Send one message after the rebook is done, with the new itinerary. Don't send "cancelled" and then "rebooked" separately. |
| 10 | Agent paused, card expired | **Push** | Blocks the agent from protecting the trip. Needs action. |
| 4 | Delayed 20+ min | **Push only if it breaks a connection or moves arrival past a threshold** (e.g. 60+ min). Otherwise timeline only. | A 20-minute delay is usually noise. |
| 3 | Gate changed | **Push only in the final ~2–3 hours before departure**. Otherwise timeline. | Matters at the airport, not a day before. |
| 2 | Price dropped $12 | **Timeline, plus push only above a real threshold** (e.g. $50 or 10%, and only if the agent can rebook for savings). | $12 is the main source of "a lot." |
| 1 | Booking confirmed | **Email and timeline, no push** | The user just did it and is looking at the screen. |
| 6 | Check-in open | **Timeline, plus one push at T-4h if not checked in** | The airline already sends this. Ours is a duplicate unless they haven't acted. |
| 9 | Seat upgrade available | **Timeline, push only for a time-limited offer that expires soon** | Mostly an upsell; push creates pressure. |
| 8 | "Looked for a better fare, found none" | **Remove. Keep it in the activity log only.** | It's a notification about nothing. Users would rather not be told that. |
| 7 | Weekly deals roundup | **Email, opt-in, never push** | Marketing belongs in a channel users chose. |

**Structural changes, beyond cutting the list:**

- **Separate "trip-critical" from everything else.** Give users toggles for the non-critical categories. Keep cancellation, agent-paused, and imminent-departure changes on by default, and don't let them turn those off. Right now turning everything off also disables the alerts they need, which is why some users are worse off.
- **Collapse repeats.** Several delay or gate updates on the same flight should update one card, not stack up as separate pushes.
- **Cap pushes per trip per day** (e.g. 2), with critical alerts exempt.
- **Respect quiet hours** for non-critical pushes.

**How to tell if it worked:** track push opt-out rate and how many users fully disable notifications, plus the response rate on the alerts that remain (did they act on the card-expired or check-in pushes?). If opt-outs drop and the critical alerts still get acted on, the cut is right.

The thresholds above are my defaults, not data-backed. The $50 price-drop threshold and the 60-minute delay threshold are the ones I'd check against your actual rebooking savings and missed-connection data first.
