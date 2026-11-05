**Short version:** keep 3 of the 10 as always-push, make 3 conditional, and move the other 4 out of push. Then give people a "problems only" setting so they don't have to choose between everything and nothing.

## Sort by what the person can do about it

| # | Notification | Kind | Where it goes |
|---|---|---|---|
| 10 | Agent paused, card expired | Problem | **Push now.** Nothing is being watched until they fix it, so this is the most important one. Repeat it as a persistent banner on the status screen, and by email if the push is off. |
| 5 | Cancelled, rebooked automatically | Problem | **Push now.** Show the new itinerary, what changed, and a "change this" action. |
| 6 | Check-in is open | Deadline | **Push once**, but only if the agent isn't checking them in itself. If it does, this becomes a line in the activity feed. |
| 3 | Gate changed | Deadline | **Push only when departure is close** (starting value: within 3 hours). Otherwise, update the trip screen quietly. |
| 4 | Delayed 20+ minutes | Problem or concern | **Push if it breaks a connection or the agent changed something.** Otherwise, update the trip screen and include it in the digest. |
| 2 | Price dropped $12 | Completion | **Don't push.** Push only if the agent acted (rebooked or claimed a credit), or if the drop passes a threshold the user sets. Otherwise, put it in the digest. |
| 9 | Seat upgrade available | Suggestion | **In-app card and digest.** Push only if the user opted in, or if it expires soon and matches a preference they set. |
| 1 | Booking confirmed | Completion | **No push.** They just did it, and the confirmation screen and email receipt cover it. Push only when the agent books on their behalf (for example, an automatic rebooking). |
| 7 | Weekly deals roundup | Marketing | **Email, opt-in, off by default.** Keep it out of the push channel entirely. Mixing it in teaches people to ignore real alerts. |
| 8 | "Looked for a better fare, found none" | Check-in | **Never notify.** Show it as "Last checked 2h ago, next check in 4h" on the status screen. That's the proof the agent is working, and no one needs to be interrupted for it. |

## Settings

- **Three modes at the top of notification settings:**
  - **Problems only**
  - **Problems + daily digest**
  - **Everything**

  "Problems only" is a middle option for people who would otherwise turn everything off.
- **Per-kind switches underneath**, so someone can drop suggestions but keep delays.
- **One digest, at a time the user picks**, holding the price drops, upgrade offers and completed actions. Put anything doubtful first.
- **A cap on pushes per trip.** Anything over the cap folds into the digest, except a problem that needs action.
- **Fallback when push is off at the OS level.** Send problems (#10 and #5) by email or SMS. Say so in settings: "If you turn off push, we'll still email you if your card expires, because we can't watch your flights until it's fixed."

## Win back people who already turned push off

Don't re-prompt them with a generic "turn notifications on" banner. Show one in-app message the first time they open the app after a trigger event: "Your flight changed and you had notifications off. Want alerts for only cancellations and card problems?" This is tied to something real, offers the narrow option, and is easy to dismiss.

## What to check after launch

- Notification opt-out rate, split by mode chosen.
- Whether people in "Problems only" still act on #5 and #10.
- How often the per-trip cap is hit. If it's often, the thresholds are too loose.

I haven't invented any numbers. The 3-hour window and the price-drop threshold are starting values to test.
