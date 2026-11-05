**Recommendation:** push only for things that need the person now or that change their trip. Move everything else into a digest or the in-app status view. Users who find notifications "a lot" are reacting to the push stream carrying completions, marketing and "nothing happened" alongside real problems. Once they can't tell the two apart, they turn off all of it, including the card-expired and cancellation alerts that matter most.

Sort each item into one of five kinds:

| # | Item | Kind | Treatment |
|---|---|---|---|
| 5 | Cancelled, rebooked | Problem | **Push, always.** Show the new itinerary, with "Change" and "Talk to a person" in the notification. |
| 10 | Card expired, agent paused | Problem | **Push, always.** Also keep a persistent banner on the status home until it's fixed. |
| 3 | Gate changed | Problem, time-boxed | **Push only inside the travel window** (starting assumption: day of departure). Before that, update it silently in the app. |
| 4 | Delay ≥20 min | Problem or concern | **Push when it matters:** a connection is at risk, or the agent is changing something. Otherwise show it in the app. Make the threshold adjustable, because 20 minutes on a nonstop is noise. |
| 6 | Check-in open | Time-boxed | **One push** unless the agent checks them in. In that case it goes in the completion digest. |
| 2 | Price dropped $12 | Completion | **Digest.** Push only if the agent acted on it (for example, rebooked for a refund) or the drop crosses a threshold the user set. |
| 9 | Seat upgrade | Suggestion | **Digest.** Push only if it expires soon and the user has shown interest in upgrades. |
| 1 | Booking confirmed | Completion | **No push.** The user just did it, so show an in-app confirmation and send an email receipt. |
| 7 | Weekly deals | Marketing | **Off for push.** Offer it as opt-in email or an in-app tab. |
| 8 | "Found no better fare" | Check-in | **Never push.** Show "Checked 2h ago, no better fare, next check ~6h" on the status home. This also proves the agent is alive, which is its real job. |

**Add a concern notice for the card.** Don't wait for the card to expire. Send a staged warning before it, for example 14 days and 3 days out (starting values to test). Say what's drifting and what the agent will do: "Your card ends 11/26. Wayfarer can't rebook after that. Update it here." This is the only way to avoid a pause at the worst moment.

**Controls:**
- **Per-kind controls:** each kind gets its own toggle, and the digest schedule is the user's choice (daily or weekly). Replace the one global "notifications" switch with these.
- **Quiet hours:** a cancellation or a pause bypasses them. Say so in the setting: "Urgent trip changes still come through."
- **Protected problem alerts:** if someone turns off every push, keep problem-level alerts on by default and say plainly what that means. A complete mute shouldn't be a single tap.
- **Ceiling:** set a cap on non-problem pushes per week. The number is a placeholder to tune from your own data.

**What to measure:** the opt-out rate per kind, and how many people disable all notifications. Don't judge success by open rates. Review it after a few weeks. If the problem pushes still get muted, the threshold on #3 and #4 is probably the culprit.

I assumed Wayfarer can act on a user's behalf (rebooking, possibly checking in). If it only suggests, #2 and #9 are even clearer digest items.
