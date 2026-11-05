**Assumption:** push is the only channel today, Wayfarer can rebook without asking, and the thresholds below are starting values to test, not measured figures.

**Recommendation:** cut push to a small number of interruptions per trip. Sort the ten items into the five kinds, and give each kind its own bar.

| # | Item | Kind | Channel |
|---|---|---|---|
| 5 | Cancelled and rebooked | Problem | Push now |
| 10 | Card expired, agent paused | Problem | Push now |
| 4 | Delay that breaks a connection or passes ~90 min | Problem | Push now |
| 6 | Check-in open | Deadline | One push per trip, at the window opening, only if not yet checked in |
| 3 | Gate changed | Concern | Status view; push only within ~3 hours of departure |
| 2 | Price drop | Suggestion | Digest, only above a meaningful threshold (not $12) |
| 9 | Seat upgrade | Suggestion | Digest, only when the offer is likely to be taken |
| 1 | Booking confirmed | Completion | Email or trip page, not push |
| 8 | "Found no better fare" | Remove | Shown as "last checked, nothing better" in the status view |
| 7 | Weekly deals roundup | Not an agent message | Email, opt-in only |

**The rules behind it:**

- **Problems interrupt at once.** When the itinerary changes, say what changed and what was done, for example: "Your 6:10 is cancelled. I rebooked you on the 8:40 at no extra cost. Your seat is 14C. Nothing to do unless you want a different flight." Each problem gets one message. Users can't switch problems off, only choose the channel.
- **Card expired is a problem with a fix.** "Wayfarer is paused: your card ending 4421 expired. Update it to keep watching your flight to Denver." Link straight to the card screen. Don't send this as a generic alert.
- **Completions and suggestions go into one trip digest** on a schedule the user picks, with a ceiling of about three pushes per trip in total (a starting value).
- **Every kind has its own off control.** Suggestions and completions can be turned off. Problems and the check-in deadline stay on, and the user can choose only the channel.
- **Status view replaces "found none" pushes.** It shows running or paused, last check, and the next check. Proof of life belongs there, not in the notification stream.

**Expected effect:** interruptions drop from up to ten types to about three per trip, and each one is worth reading. Track how often users turn off each kind, and whether the ones that remain get acted on, to see if the thresholds are right.
