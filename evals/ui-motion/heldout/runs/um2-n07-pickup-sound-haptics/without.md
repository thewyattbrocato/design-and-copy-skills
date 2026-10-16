**Do three of the five, skip two.**

| Candidate | Verdict | Why |
|---|---|---|
| Chime when order is ready | **Yes** | The customer is probably not looking at the app, so sound is the only way to reach them. |
| Vibration when staff head out | **Yes** | The customer is in a parked car and needs to be ready for the bags, which may mean popping the trunk. A buzz works even when the phone is on silent. |
| Feedback on "I'm here" | **Yes, as a haptic, not a sound** | It's the most important tap in the app. The customer needs to know it registered, but a sound in a parking lot is noisy and often muted. |
| Jingle on order placed | **No** | The customer is looking at the screen and sees the confirmation. A jingle adds nothing and gets annoying by the third order. A single success haptic is enough if you want something. |
| Buzz on every button | **No** | It's noise, it drains battery, and the system already gives feedback on standard controls. It also dilutes the buzzes that matter. |

The rule behind this is to use sound and vibration only for things that happen when the customer isn't looking at the screen, or for confirming the one action that must not fail.

**How to build it**

1. **Ready and "heading out" are push notifications, not in-app sounds.** They have to work with the app closed.
   - Use the platform's default notification sound at first. A custom brand chime can come later.
   - On Android, create separate notification channels for "Order ready" and "Staff on the way". Customers can then tune each one, and you can give "on the way" a vibration pattern.
   - On iOS, mark "staff on the way" as time-sensitive so it gets through Focus modes. Leave "ready" at the default level.
2. **Only send "heading out" after the customer has tapped "I'm here".** Send it when staff mark the order as leaving. Otherwise it's a false alarm.
3. **"I'm here" haptic.** Fire a success haptic when the server confirms the tap, not when the finger lands. On iOS that's `UINotificationFeedbackGenerator` with `.success`. On Android it's `HapticFeedback.CONFIRM`. If the request fails, send an error haptic and show a visible error.
4. **Never use sound or vibration as the only signal.** Every event also needs a visible state change and a notification-center entry. This covers silent mode, deaf and hard-of-hearing customers, and anyone with haptics turned off.
5. **Respect system settings.** Use the OS haptic and notification APIs, which honor silent mode, Do Not Disturb, and accessibility settings. Add a simple toggle in app settings: "Sounds & vibration for order updates."
6. **Test before expanding.** Check that the ready chime fires reliably, and track the time from "I'm here" to bags delivered. If you later want more feedback, add it one event at a time and see whether it helps.

Skipping the jingle and the every-button buzz should settle most of the disagreement, since those are the two options with the weakest case.
