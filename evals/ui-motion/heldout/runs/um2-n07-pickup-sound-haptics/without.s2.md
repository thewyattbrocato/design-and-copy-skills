**Recommendation: do two of the five, add a light haptic for a third, and skip the other two.**

The test is whether the customer is looking at the screen. Sound and vibration earn their place when something happens while the phone is in a pocket, on a mount, or face-down. They're noise when the customer is already tapping the screen.

| Candidate | Verdict | Why |
|---|---|---|
| Chime when order is ready | **Do it** | The customer is away from the app, possibly driving over. This is the main case for an alert. |
| Vibration when staff head out | **Do it** | The customer is parked and waiting with the phone down. The alert tells them to get the trunk or window ready. |
| Sound on "I'm here" | **Change to a haptic** | The customer is looking at the screen and often in a quiet car or a parking lot. A sound adds nothing, and a loud one is awkward. A single light haptic plus a clear visual "Staff notified" state is enough. |
| Jingle on order placed | **Skip** | The customer is at home or in a store, looking at a confirmation screen, so there's nothing to alert them to. It also gets annoying on repeat orders. If the team wants some delight, use a small animation. |
| Buzz on every button | **Skip** | It's noise on a screen the customer is already watching. Rely on the platform's default control feedback, and add haptics only to a few meaningful confirmations like "I'm here". |

**How to build it**

1. **Use push notifications for the two background alerts.** The app won't be foregrounded, so in-app audio won't fire.
   - Send "Order ready" and "Staff on the way" as separate notification types.
   - On Android, give each its own notification channel, so users can tune them.
   - On iOS, mark both as time-sensitive. They matter now, but they aren't critical alerts.
   - Use a short custom sound for "ready" and the default vibration or a subtler tone for "heading out".
2. **Add in-app handling for when the app is open.** Play the same cue as a foreground haptic or sound, plus a visible banner.
3. **Respect the phone's settings.** Honor silent mode and Do Not Disturb, and don't override volume. Add one setting in the app, "Pickup alerts: sound / vibrate only / off".
4. **Never make the cue the only signal.** Every cue needs a matching visual state and a notification, for deaf and hard-of-hearing users and for muted phones.
5. **Keep the cues short and distinct.** "Ready" should sound and feel different from "heading out". Both should be under a second or two.
6. **Measure it.** Track the time from "ready" to "I'm here", and from "I'm here" to handoff. If the chime works, the first number should drop. Also watch the notification opt-out rate, because a spike means the alerts are too noisy.

**For the team debate:** the disagreement is mostly about what the alerts are for. Frame them as "events the customer would otherwise miss", not "polish". That rule settles all five and gives you a way to judge future requests.
