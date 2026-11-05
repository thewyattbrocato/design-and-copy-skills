**Cut push to the few things that need action or change someone's travel plans, and move the rest to in-app or email.** Users turn notifications off entirely when they can't tell which ones matter. Fewer, higher-stakes pushes protect the channel you most need for cancellations and payment failures.

| # | Notification | Channel |
|---|---|---|
| 5 | Cancelled, rebooked | **Push**, time-sensitive priority |
| 10 | Agent paused, card expired | **Push + email**, since the agent can't protect them until they act |
| 4 | Delay of 20+ minutes | **Push** |
| 3 | Gate changed | **Push** only within about 24 hours of departure. Earlier, show it in-app. |
| 6 | Check-in open | **Push** only if the agent can't check in for them. If it does, send a quiet confirmation instead. |
| 1 | Booking confirmed | **Email + in-app** receipt. The user just did this, so they don't need a buzz. |
| 2 | $12 price drop | **In-app / digest**. Push only for a big drop (say $50+ or 10%+), or when the agent acted on it ("rebooked you, saved $63"). |
| 9 | Seat upgrade | **In-app or email**. Push only if the offer is time-limited and the user opted in. |
| 7 | Weekly deals | **Email only**, opt-in. It's marketing and shouldn't share a channel with cancellations. |
| 8 | "Found no better fare" | **Don't send.** Show "Last checked 2h ago, no better fare" in the trip view instead. Nothing happened, so it shouldn't interrupt anyone. |

That takes you from 10 pushes to 3 or 4 that are almost always urgent.

**Supporting changes:**
- **Group related updates.** If a gate change and a delay arrive together, send one "Flight update" push rather than two.
- **Offer categories instead of one switch.** Use something like "Trip disruptions" (always on by default), "Savings," and "Offers." Someone who wants fewer alerts can then mute savings without losing cancellation alerts.
- **Respect quiet hours,** except for disruptions within a few hours of departure.
- **Protect the critical channel.** If someone has disabled push, fall back to SMS or email for cancellations and payment failures, and prompt them to re-enable push.

**How to tell if it worked:**
- Watch the push opt-out rate and the open rate on disruption pushes.
- Track how often users miss a disruption because they had notifications off.
- Consider a short A/B test of the old setup against the tiered one before rolling it out fully.

I'd verify the thresholds (20 minutes, $50, 24 hours) against your own data. They're reasonable starting points, not tuned numbers.
