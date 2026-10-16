**Do three, skip two.**

| Candidate | Verdict | Why |
|---|---|---|
| Chime when order is ready | **Yes** | The customer is usually not looking at the app, so this is the highest-value cue. |
| Vibration when staff head out | **Yes** | The customer is waiting in a car, and this tells them to get ready. |
| Sound on "I'm here" | **Haptic only, no sound** | The customer needs to know the tap registered, and a sound is unnecessary in a car or store lot. |
| Buzz on every button | **No** | It's noise. Haptics should mark moments that matter. |
| Jingle on order placed | **No** | It's brand decoration that gets annoying by the third order. A short success haptic and a visual confirmation are enough. |

**How to build it**

1. **Ready chime: use a push notification with a sound, not an in-app sound.**
   - The app will often be backgrounded or the phone locked, so an in-app sound would never play.
   - Use a short, distinct custom sound.
   - On iOS, mark it time-sensitive so it gets through Focus modes. On Android, use a high-importance channel.
   - Respect the phone's silent mode and system settings.

2. **Staff heading out: send a push notification with a haptic or vibration pattern.**
   - Use a different pattern from the ready chime so the two events feel distinct.
   - If the app is in the foreground, fire a haptic directly. On iOS use `UINotificationFeedbackGenerator`. On Android use `HapticFeedbackConstants` or `VibrationEffect`.
   - Make this a text and visual update too: "Alex is bringing your bags out."

3. **"I'm here": fire one light haptic on tap, and change the button to a visible "Sent" state.**
   - The haptic should fire only after the server confirms.
   - On failure, use a different error haptic and a visible retry.

4. **Ground rules**
   - Every cue needs a visual equivalent, so nothing depends on sound or vibration alone.
   - Add a notification settings screen with toggles for sound and haptics. Honor OS-level settings by default.
   - Use native haptic APIs rather than custom vibration durations, since they feel consistent across devices.
   - Keep the sounds short (about 1–2 seconds) and not harsh.

**Suggested rollout:** ship the ready chime first, then the heading-out haptic, then the "I'm here" haptic. Watch opt-out rates and pickup wait times (arrival to handoff) to see whether the cues help.

I haven't looked at your codebase. If you tell me the stack, such as native iOS and Android, React Native, or Flutter, I can get more specific about the notification and haptic setup.
