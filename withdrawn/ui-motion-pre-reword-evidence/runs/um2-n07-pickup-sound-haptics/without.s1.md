**Recommendation:** do the two that carry information when the customer isn't looking at the screen. Make "I'm here" a quiet haptic confirmation. Skip the other two.

| Candidate | Verdict | Why |
|---|---|---|
| Chime when order is ready | **Yes** | The customer is often away from the app, so this is the most useful of the five. |
| Vibration when staff head out | **Yes** | It tells the customer to be ready (unlock the trunk, stop looking at their phone). It's time-sensitive and they're likely watching the lot, not the screen. |
| Feedback on "I'm here" | **Haptic only, no sound** | They need to know the tap registered, since there's no other visible response while they're parked and distracted. A sound adds nothing in a quiet car and can embarrass them in a public lot. |
| Jingle on order placed | **No sound; a single light success haptic at most** | It's the least useful moment for feedback. It fires at home, at work, or in a meeting, and it gets annoying by the third order. |
| Buzz on every button | **No** | It's noise that dilutes the haptics that matter. System-default feedback on native controls is enough. |

**How to build it**

1. **Send "ready" and "staff heading out" as push notifications, not in-app effects.** The app will usually be backgrounded or the phone locked. Give each its own sound and vibration pattern so they're distinguishable without looking. Make "heading out" the more urgent one. On iOS, consider the time-sensitive interruption level for it. On Android, use separate notification channels so users can tune each one.
2. **Also fire in-app feedback if the app is open.** If the app is foregrounded when the push arrives, play the same sound or haptic locally and update the UI. Don't rely on the OS banner.
3. **Use the platform's semantic haptics.** On iOS that's `UINotificationFeedbackGenerator` (`.success`) for "I'm here" and order placed. On Android it's `HapticFeedback` constants like `CONFIRM`. Don't hand-roll vibration durations.
4. **Keep sounds short and quiet.** Aim for under a second, with a calm tone that fits a grocery brand.
5. **Respect system settings.** Honor silent mode and haptics-off settings. Add a simple in-app toggle for sound and vibration, defaulting to on for the two notifications.
6. **Never use sound or haptics as the only signal.** Pair each with visible status text, such as "Order ready" or "Staff on the way", for deaf or hard-of-hearing users and for muted phones.
7. **Test in a real car.** Check a phone in a cupholder, in a dash mount, and in a pocket. Haptics are easy to miss in a cupholder, so the sound and notification may need to carry more weight there.

**Settling the team debate:** the rule is that feedback has to earn its place by telling the customer something they'd otherwise miss, or by confirming an action they can't easily verify. Ready and heading-out pass. "I'm here" passes as a haptic. The jingle and buzz-everywhere are decoration.

Once it's live, track how long pickups take from "I'm here" to handoff, and track notification opt-outs. Rising opt-outs would mean the notifications are too aggressive.
