**Recommendation:** do the two alerts for events that happen while the customer isn't looking at the app. Make "I'm here" a haptic only. Skip the other two.

| Candidate | Verdict | Why |
|---|---|---|
| Chime when order is ready | **Do** | The customer is probably elsewhere with the phone in a pocket. This is the main reason to have sound. |
| Vibration when staff head out | **Do** | The customer is parked and waiting. It tells them to look up and unlock the trunk, and it's the one moment where timing matters. |
| Sound on "I'm here" | **Haptic only** | The customer is often driving or pulling in, so a sound is easy to miss or is a distraction. A single success haptic plus a clear visual state ("Staff notified") confirms the tap. A sound adds little. |
| Buzz on every button | **Skip** | It's noise that dulls the signal of the alerts above. It also drains battery and annoys people. The OS already gives native controls their feedback. |
| Jingle on order placed | **Skip** | It plays at home, in a store, or in a meeting, which is the situation where people mute apps. The brand value is small and the annoyance risk is real. A subtle success haptic and a confirmation screen are enough. |

**How to build it**

1. **Ready and heading-out alerts are push notifications.**
   - They have to work when the app is backgrounded or the phone is locked, so don't build them as in-app sounds.
   - On iOS, mark them time-sensitive and use a short custom sound for "ready".
   - On Android, use separate notification channels, for example "Order ready" (sound) and "Staff coming out" (high priority, vibration pattern). That lets users tune each one.
   - Consider a Live Activity on iOS and an ongoing notification on Android that move through *Preparing → Ready → Staff coming out*.
2. **Use the same events as in-app haptics when the app is open.**
   - On iOS use `UINotificationFeedbackGenerator` (success).
   - On Android use `HapticFeedbackConstants` (CONFIRM).
   - Use the system patterns rather than custom ones.
3. **Never make sound or vibration the only signal.** Always pair it with a visible state change and banner text. This covers silent mode, hearing or motor accessibility needs, and noisy cars.
4. **Respect the user's settings.** Honor silent mode, Do Not Disturb, and the system haptics setting. Add one in-app toggle under notification settings for "sounds and haptics". Don't override the OS.
5. **Keep the sounds short and distinct.** Use under 2 seconds, and make "ready" sound clearly different from "staff heading out" so people can tell them apart without looking.
6. **Avoid double-alerting.** If the app is in the foreground, show a banner and a haptic and suppress the push sound.

**How to settle the disagreement:** ship the two alerts and the "I'm here" haptic first. Then look at the data: time from "ready" to "I'm here", time from "I'm here" to handoff, and notification opt-out rates. If the alerts shorten waits and opt-outs stay low, you have a case for adding more. If someone still wants the jingle or the button buzz, you can A/B test them against those same numbers.
