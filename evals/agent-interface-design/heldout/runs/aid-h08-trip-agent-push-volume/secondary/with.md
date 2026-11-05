**Assumed:** Wayfarer acts for the user within a rebooking fare cap the user sets, and push is currently its only channel. The thresholds below ($12, 20 minutes, 3 hours) are starting points to test, not findings.

**Promise:** "While you're away I'll rebook cancelled flights within your fare cap and watch for fare drops. I won't spend above that cap without asking."

Sort the ten events into five kinds. Only problems interrupt, so most of the ten stop being pushes.

**Problem (push now):** the trip changed or the agent is blocked.

- **5. Cancelled and auto-rebooked.** Keep. This is the push users most need, because the itinerary changed without them. "Your 6:10 to Denver was cancelled. I rebooked you on the 8:05 at no extra cost, seat 14C. [View itinerary] [Change flight]"
- **10. Agent paused, card expired.** Keep, and make it the most visible item. Send push and email, and show a banner until fixed. "Wayfarer is paused: your card ending 4421 expired. Your flight is still booked, but I can't rebook it if it's cancelled. [Update card]"
- **4. Delay.** Push only if it breaks a connection or passes a set arrival threshold (test 60 minutes). Otherwise it goes in the trip status. Example: "Your 6:10 is delayed 75 min. Your Denver connection still works. No action needed."

**Completion (digest or trip status, never push):**

- **1. Booking confirmed.** Send the receipt by email and show it in the app.
- **3. Gate changed.** Push only within 3 hours of departure, once. Otherwise show it in the trip status.
- **8. "Looked for a better fare, found none."** Cut the notification. Show it as a line in the trip status: "Last fare check Tue: no better fare. Next check Fri."

**Suggestion (rare, opt-in, the person chooses to act):**

- **2. Price drop.** Push only if the drop clears the threshold and the booking can still change. Otherwise, include it in the weekly digest.
- **9. Seat upgrade.** In-app only, unless it expires within 24 hours. Then one push.
- **7. Weekly deals.** Opt-in email digest. Never push.

**Check-in (proof of life or deadline reminder):**

- **6. Check-in open.** One reminder, 24 hours before departure, only if they haven't checked in yet.

**Result:** a typical trip gets one or two pushes (the rebook, and the card expiry if it happens), instead of up to ten. Each kind has its own off switch, and the app shows a per-week push ceiling.

**Measure:** pushes per trip, the share of pushes that get an action, and how many users turn each kind off. A kind that is mostly ignored should be cut or moved to digest.
