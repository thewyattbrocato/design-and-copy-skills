**Principle:** push only what is time-sensitive and changes what the user should do right now. Everything else goes to in-app or email. The agent's value is that users don't have to watch, so most of its routine work should be quiet.

| # | Notification | Channel |
|---|---|---|
| 5 | Cancelled, rebooked | **Push** (high priority) |
| 10 | Agent paused, card expired | **Push**, and follow up by email. The agent is doing nothing until this is fixed. |
| 4 | Delay of 20+ minutes | **Push** |
| 3 | Gate changed | **Push**, only within about 24 hours of departure. Earlier gate changes go in-app. |
| 6 | Check-in open | **Push**, with a setting to turn it off. It's useful but predictable, and some people check in automatically. |
| 9 | Seat upgrade available | **In-app and email.** Push only if the offer expires within a few hours. |
| 1 | Booking confirmed | **Email and in-app receipt.** Optionally one silent or low-priority push. |
| 2 | Price dropped $12 | **In-app only, or fold it into a digest.** If the agent rebooks or claims the savings, report that after the fact. Push only above a meaningful threshold, such as $50 or 10%. |
| 7 | Weekly deals | **Email only, opt-in.** This is the likeliest reason people mute everything. |
| 8 | "Looked, found no better fare" | **Never a notification.** Show it as a "last checked" line on the trip screen. |

**Structural changes:**
- **Group by trip.** If a delay and a gate change arrive together, send one notification, not two.
- **Add category toggles in settings.** Let users pick "Critical only / Critical + savings / Everything" so they don't reach for the OS-level off switch. Don't allow a full mute inside the app for categories 4, 5 and 10. Explain why, and offer SMS or email as the fallback.
- **Cap frequency and respect quiet hours.** Hold non-urgent items overnight. Disruptions within 24 hours of departure always go through.
- **Use a daily or weekly digest for savings.** For example: "Wayfarer checked 14 times this week and saved you $38."

**Measure it:**
- Track the notification opt-out rate per category.
- Track the share of users who disable push entirely. Aim to push this down.
- Track the time from a critical event to the user's response.
- Track the open rate of the critical tier. It should rise once the noise is gone.

Roll it out as an A/B test. Start with the cuts that cost nothing: #8, #7 and #2. These are almost certainly the least valuable and the most annoying.

I'd also re-engage users who already turned notifications off. Once the tiers are in place, send them one email explaining that only important alerts will come through now, and ask them to turn push back on.
