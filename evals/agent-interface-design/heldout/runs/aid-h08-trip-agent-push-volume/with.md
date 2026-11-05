**Short version:** push only when the person has to act or know now. Put everything else in a digest or the status screen, and delete #8.

| # | Event | Where it goes | Why |
|---|---|---|---|
| 10 | Agent paused, card expired | **Push**, plus email if unread | The agent can't protect the trip until this is fixed. Repeat in stages if ignored, and show a persistent "Paused" banner on the status screen. |
| 5 | Cancelled, rebooked automatically | **Push** | The plan changed and they need to see the new flight. Include old flight, new flight, and an undo or "call a person" option. |
| 4 | Delay of 20+ min | **Push**, only within about 24h of departure | It's useful only while they can still act on it. Earlier than that, show it in-app. 20 min is a starting threshold to test. |
| 3 | Gate changed | **Push** only on travel day, otherwise in-app | It has a short shelf life, and it's noise on any other day. |
| 6 | Check-in open | **Push** once per flight, unless the agent checks in for them | It has a deadline they can act on. If the agent checks in, report it in the digest. |
| 1 | Booking confirmed | In-app confirmation plus email receipt | They just did the action, so a push repeats what's on their screen. |
| 2 | Price dropped $12 | **Digest**, unless the agent acts on it | A small drop isn't worth interrupting anyone. Push only above a threshold they set, or when the agent rebooks or claims a credit for them. |
| 9 | Seat upgrade available | In-app card. Push only if it expires soon and matches their past choices. | It's a suggestion, so keep it rare and make it very likely to be useful. |
| 7 | Weekly deals | **Email, opt-in only**, never push | It's marketing. Sending it through the channel they use for trip alerts teaches them to mute that channel. |
| 8 | "Found no better fare" | **Delete as a notification.** Show "Checked 2h ago, no better fare, next check at 6pm" on the status screen. | Nothing happened, so there's nothing to tell them. The status line still shows the agent is working. |

**Structure to build around this**

- **Five kinds, each with its own control:** problems, concerns (like a trend toward a limit), completions (digest), suggestions, and check-ins. Users can turn down suggestions and completions without silencing problems.
- **Ceiling:** cap non-urgent pushes per day. I'd start at 1, but treat that as a number to test.
- **Per-trip rules:** push for a trip only as the travel date approaches. A flight three months out shouldn't generate daily noise.
- **Digest:** one scheduled summary of what the agent did. List each action, put the doubtful ones first, and give each its own undo.
- **Status screen:** shows running or paused, last action, and next check. Pause is one tap away.
- **Feedback on each notification:** "Not this one" and "Never for this kind", with the second showing the rule it creates.

**Winning back people who turned notifications off**

Treat #10 and #5 as safety messages, and don't let them ride on the same switch as everything else. When someone mutes everything, ask once, "Keep alerts for cancellations and payment problems?", and fall back to email or SMS for those two. For people who already muted everything, a persistent banner on the status screen saying "Alerts off, you won't hear about cancellations" is better than silently failing.

I haven't seen your current volumes or opt-out data. If you can share which of these ten fire most often, I can help set the thresholds and the daily cap.
