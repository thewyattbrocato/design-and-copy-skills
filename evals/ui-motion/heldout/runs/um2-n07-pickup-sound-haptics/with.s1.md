**Do three of them, make one of them haptic-only, and drop the every-button buzz.** I'd pick by asking whether the customer might not be looking at the screen and needs to act or know something.

| Candidate | Verdict | Why |
|---|---|---|
| Chime when order is ready | **Yes** | Customers are often away from the app when this happens, and it tells them to start driving over. |
| Vibration when staff head out | **Yes** | Customers are parked, phone down, waiting. This cue means "get ready, pop the trunk," and it's the one that cuts the awkward wait. |
| Sound on "I'm here" | **Haptic instead** | The customer is in a quiet car and the sound reaches no one. What they need is confirmation that the tap registered, so use one crisp success haptic plus a visible state change ("Staff notified"). |
| Jingle on order placed | **Skip, or haptic only** | It fires at home, at work, or in a meeting, where it's more likely to annoy than delight. A light success haptic covers confirmation. If the brand wants a jingle, make it opt-in. |
| Buzz on every button | **No** | If everything buzzes, the important moments stop standing out. Rely on the platform's default feedback for system controls. |

**How to build it**

1. **Send the "ready" and "staff heading out" cues as push notifications.** The app is usually backgrounded at those moments, so in-app sounds won't fire. Give the two different notification text and sound, so they're distinguishable without looking. Also fire an in-app haptic if the app is open.
2. **Use a small haptic vocabulary.** Use a success haptic for "I'm here" and order placed, and a stronger, distinct pattern for "staff heading out." Use native APIs (iOS `UINotificationFeedbackGenerator`, Android `HapticFeedback`) rather than custom vibration durations.
3. **Pair every cue with a visual state change.** Sound and vibration should reinforce the screen, never be the only signal. Many people have their phone on silent, and some have haptics off.
4. **Respect system settings.** Honor silent mode, Do Not Disturb, and reduced-haptics preferences. Add one "Sounds & haptics" toggle in settings, with notifications on by default and anything decorative off.
5. **Don't invite phone use while driving.** Cues should signal "you're done, wait," not "tap now." The "I'm here" button should be reachable only when the customer is near the store, if you have geofencing.

**Settling the team debate:** ship the three yes items first, and measure notification opt-in and mute rates, "I'm here" to handoff time, and no-shows. Then you can decide on the jingle with data. Before shipping, test in a real car with the phone in a mount and in a pocket, since haptic strength and audibility vary a lot there.
