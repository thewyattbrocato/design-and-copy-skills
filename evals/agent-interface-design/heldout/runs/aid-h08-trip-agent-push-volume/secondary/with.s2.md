**Assumptions:** Push is the only channel today. A typical traveler has one to three trips a year. The numbers below are starting values to test, not measured results.

**The fix:** Keep problems loud and reliable, and make everything else quieter. Turning push off today also turns off the cancellation alert, which is the one that matters most.

**Promise to state in the app:** "While you're away, I watch your booked flights and rebook you if one is cancelled. I won't interrupt you for anything that needs no action from you."

## Sort the ten into five kinds

| # | Today | Kind | New behavior |
|---|---|---|---|
| 5 | Cancelled, rebooked | Problem, already fixed | Push now, with the new flight and an undo window |
| 10 | Paused, card expired | Problem | Push now. Also warn 30 and 7 days before the card expires |
| 4 | Delayed 20+ min | Concern, becomes problem | Push only if it puts a connection or check-in at risk. Otherwise digest |
| 3 | Gate changed | Completion | Digest. Push only within 2 hours of departure |
| 6 | Check-in open | Deadline reminder | One push at check-in opening, only if they haven't checked in yet |
| 2 | Price dropped $12 | Suggestion | Digest. Push only for a meaningful drop (starting value: $50 or 10%) |
| 9 | Seat upgrade | Suggestion | Push only if the price is under a cap and they've said they want upgrades. Otherwise a line in status |
| 1 | Booking confirmed | Not news; they just did it | No push. Show it where they booked |
| 8 | "Found no better fare" | Not news | Remove. Put "Last fare check: today, nothing better" in the status view |
| 7 | Weekly deals | Marketing, not the agent | Remove from push. Make it an opt-in email |

## Decisions

1. **Push ceiling.** At most one non-problem push per trip per day (starting value). Problems are not counted against it.
2. **Digest.** Completions, gate changes and small price drops go into one daily digest per trip, on a time the person picks.
3. **Off switches are per kind, with a floor.** Suggestions and completions can be turned off separately. Problems cannot be turned off. Anyone who disables everything else still gets problems. A global off switch is what caused the current drop-off.
4. **Status home.** One screen shows "Watching: price, gate, schedule, card," last check, next check, and alive or paused. This replaces most of the "nothing found" pings.
5. **Auto-rebook cap.** Rebook without asking only if the fare difference is under a cap (starting value: $75) and the new flight is within a set time of the original. Above the cap, ask first.
   - Sample: "Your 6:40 to Denver was cancelled. I rebooked you on the 9:15, same cabin, no extra charge. Undo within 24 hours, or change it here."
6. **Expired card.** Warn before expiry. Once it has expired, show a persistent banner with one fix action. Say what is paused and what still works.
   - Sample: "I've paused price watching and auto-rebook because your card expired. Your flight is still booked. Update the card to resume."
7. **Delay.** Stay quiet unless the connection is actually at risk.
   - Sample: "UA 512 is 35 minutes late, and your Chicago connection now has 25 minutes. I'll tell you if it becomes a problem."

Start by logging how often each type is dismissed or turned off. That will show which of the ten to cut first and whether the thresholds above are too high or too low.
