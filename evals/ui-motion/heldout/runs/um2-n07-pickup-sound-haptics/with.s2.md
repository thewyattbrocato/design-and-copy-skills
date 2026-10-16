**Recommendation:** do the two moments where the customer isn't looking at the screen, add a light confirmation to the two actions they take, and skip the buzz on every button.

| Candidate | Verdict | Why |
|---|---|---|
| Chime when order is ready | **Yes** | The phone is probably in a pocket or bag, and this is the main async signal. |
| Vibration when staff head out | **Yes** | The customer is parked and waiting. It tells them to get ready, and it's useful when they're not watching the screen. |
| Sound on "I'm here" | **No sound, add a haptic** | A single success haptic confirms the tap. A sound in a car park or with passengers adds little and can annoy. |
| Jingle on order placed | **No sound, add a haptic** | It's a deliberate action, so a haptic plus a clear visual confirmation is enough. A jingle gets old and may play in a quiet place. |
| Buzz on every button | **No** | It carries no information, adds noise, drains the battery, and makes the two meaningful buzzes less noticeable. |

The rule behind this: use sound or haptics only when they carry information the user needs while not looking, or confirm a consequential action. Nothing should depend on them, because many phones are on silent.

**How to build it**

1. **Ready and staff-heading-out should be push notifications, not in-app sounds.** The app will usually be backgrounded.
   - Use the system's default notification sound. It's the least work, and it respects silent mode and Focus settings.
   - Make the two notifications distinct: different text, and on Android separate notification channels ("Order ready" and "Bags on the way"). Users can then mute one without losing the other.
   - Send "staff heading out" as time-sensitive, since it's only useful for a few minutes.
   - If the app is in the foreground, show a banner and play a short haptic.
2. **Haptics for "I'm here" and "order placed."** Use one light "success" haptic, with the visual state change as the primary feedback.
   - iOS: `UINotificationFeedbackGenerator` with `.success`.
   - Android: `HapticFeedbackConstants.CONFIRM`.
   - Fire it only after the action succeeds, not on the tap. If the request fails, use the error haptic and a visible message.
3. **Leave ordinary buttons on the platform defaults.** Don't add custom feedback.
4. **Add a settings toggle** for sounds and haptics, and follow the system's reduced-haptics and silent settings.
5. **Don't ask drivers to look at the phone.** If they might use it while moving, the cue should work without the screen. Keep it short and make the visual state readable at a glance.
6. **Measure it.** Track time from "I'm here" to handoff, notification opt-in and mute rates, and "ready" notifications opened. If the mute rate climbs, scale back.

If the team still wants a branded sound, add a short, quiet one to the "order ready" push only, since that's where it earns its place. I'd leave the jingle out.
