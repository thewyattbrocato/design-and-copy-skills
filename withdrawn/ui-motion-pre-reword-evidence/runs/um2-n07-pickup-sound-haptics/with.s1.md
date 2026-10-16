**Do three of the five, and keep two of them light.**

| Candidate | Verdict | Why |
|---|---|---|
| Chime when order is ready | **Yes** | The customer isn't looking at the app when this happens, and they need to act on it. |
| Vibration when staff head out | **Yes** | Same reasoning. The customer needs to unlock the trunk, get out, or look up. |
| Feedback on "I'm here" | **Haptic only** | The customer is parked and glancing at the screen. A light success haptic plus a visible state change confirms the tap registered. A sound is loud and unneeded. |
| Buzz on every button | **No** | There's no information in it, and it dilutes the haptics that do mean something. Keep the OS defaults for toggles and steppers. |
| Jingle on order placed | **No** | The customer is looking at the confirmation screen and is often in a store, at work, or on a couch. A jingle is brand decoration, and some customers will find it annoying. If you want a signal, use one success haptic. |

The rule behind this: use sound or vibration when the customer's attention is elsewhere and the event needs a response. Skip it when they're already looking at the screen.

**How to build it**

1. **Use push notifications for "ready" and "heading out."** The app will usually be backgrounded, so in-app sounds won't fire. Send these through APNs or FCM.
   - "Ready" gets the default notification sound. Don't use a custom long sound.
   - On iOS, consider a Live Activity or lock-screen status that moves from Preparing to Ready to Coming out. It keeps the state visible without extra pings.
   - Mark "heading out" as time-sensitive. A notification with no sound doesn't vibrate on iOS, so use the default sound there. On Android, give it its own notification channel with vibration and no sound.
2. **Use separate Android notification channels** for "ready" and "heading out." Customers can then mute one without losing the other.
3. **Use in-app haptics for the foreground cases.** On iOS that's `UINotificationFeedbackGenerator` (success) for "I'm here." On Android it's `HapticFeedback` with `CONFIRM`. Fire it when the server acknowledges the tap, not on touch-down, so it also confirms the check-in went through.
4. **Respect the device settings.** Honor the silent switch, Do Not Disturb, and the system haptics setting. Add an in-app toggle for notification sounds, but don't build a custom sound mixer.
5. **Never make sound or vibration the only signal.** Every event also needs a visible banner or state change, for deaf and hard-of-hearing customers and for phones on silent.
6. **Keep "heading out" rare.** Send it once per order, and don't repeat it if staff tap the button twice.

**How to settle the team debate:** ship the three, then check whether they help. Look at the time from "ready" to "I'm here." Look at the time from "heading out" to handoff. Look at how many customers sit in the lot because they missed the notification. Also look at notification opt-out rates. If opt-outs climb, you're pinging too much.
