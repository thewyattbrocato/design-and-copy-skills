Keep push for the few events that need the user to act or that change their trip. Move the rest to in-app or email, and let users control categories instead of all-or-nothing. Turning off everything is a symptom of too many low-value pushes, and right now the critical ones get lost with the rest.

| # | Event | Channel | Why |
|---|---|---|---|
| 10 | Agent paused, card expired | **Push, repeat until fixed** | Blocks rebooking. Users must act. |
| 5 | Cancelled, auto-rebooked | **Push** | Trip changed, and they should see the new itinerary. |
| 4 | Delay ≥ 20 min | **Push, only if it affects connections or departure is within ~3 hrs** | Otherwise it's background noise. |
| 3 | Gate change | **Push only within ~3 hrs of departure**, otherwise in-app | Gate changes are frequent and rarely matter early. |
| 6 | Check-in open | **One push, skipped if they've already checked in** | Useful once, annoying if it nags. |
| 1 | Booking confirmed | **Email + in-app** | Push duplicates the email. |
| 2 | Price dropped $12 | **In-app; push only at a meaningful threshold (e.g., ≥ $50 or ≥ 10%)** | $12 is probably the biggest source of noise. |
| 9 | Seat upgrade | **In-app banner** | Nice to have, not urgent. |
| 7 | Weekly deals | **Email, opt-in only** | Marketing in push is the most common reason people disable everything. |
| 8 | "No better fare found" | **Remove** | Not an event. Show it on the trip page if someone looks. |

Net effect: about four push types, all conditional, instead of ten unconditional ones.

Other changes:
- **Per-category toggles with sane defaults.** Let people mute "deals" and "price" without losing cancellations or card problems. Consider making card-expired and cancellation non-disableable, or warn before turning them off.
- **Collapse related updates.** A gate change plus a delay in the same window should be one push, not two.
- **Log everything in-app.** Every event still gets recorded on the trip timeline, so users who want the detail can find it without a push.
- **Measure it.** Track the share of users with push disabled, opt-out rate per category, and whether cancellation and card-expired pushes still get acted on. Use that to tune the thresholds above, since 3 hours and $50 are starting guesses.

I haven't looked at your codebase, so this is a product recommendation, not a mapping to specific code. If you want, I can find where these notification types are defined and draft the routing rules.
