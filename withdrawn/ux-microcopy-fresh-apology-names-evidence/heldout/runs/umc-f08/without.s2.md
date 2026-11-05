Here's what's wrong with each button and what I'd replace it with, left to right.

| Icon | Current name | Problem | Replacement |
|---|---|---|---|
| Microphone | "button" | The name is only the role, which screen readers already announce, so users hear "button, button" and learn nothing. It also doesn't say what the control does. | **"Record"** |
| Square | "stop icon" | "icon" describes the visual, not the action. Users don't need to know it's a square. | **"Stop recording"** |
| Scissors | "Click here to trim" | It's wordy and starts with "Click here". Screen-reader and keyboard users aren't clicking, and touch users double-tap. The action is buried at the end of the phrase. | **"Trim"** (or "Trim recording" if several items can be trimmed) |
| Bookmark with a plus | "bookmark_add_24px" | This is the asset or file name leaking through as the label. It's read as "bookmark underscore add underscore 24 P X". It also isn't localisable. | **"Add bookmark"** |
| Three dots | "More" | It's short, but vague. "More" doesn't say more of what, and a user who navigates by buttons gets no context. | **"More options"** |
| Heart | "favourite" (unchanged when on) | The name is a noun, so it doesn't say what pressing does. Because the label stays the same when it's on, and only the colour changes, screen-reader users get no indication of state. Colour alone also fails WCAG 1.4.1 for sighted users who can't distinguish the colours. | **"Favourite"**, exposed as a toggle button with a pressed state (see below) |

**How the heart should behave**

Use one stable name and expose the state separately. Don't swap the label between "Add to favourites" and "Remove from favourites". If you also expose the state, users hear the change twice, and it's confusing.

- **Name:** "Favourite" (or "Add to favourites" if you want it more explicit). Keep it the same in both states.
- **Role and state:** make it a toggle button.
  - Android: `AccessibilityNodeInfo` checkable/checked, or `Switch`/`ToggleButton` semantics. In Compose, use `Modifier.toggleable(role = Role.Checkbox)` or `Role.Switch`.
  - iOS: `.isButton` plus `.isSelected` in `accessibilityTraits`. In SwiftUI, use `.accessibilityAddTraits(.isSelected)` when it's on.
  - React Native: `accessibilityRole="button"` with `accessibilityState={{ selected: isFavourite }}` or `checked`.
- **Announcement:** the screen reader then says "Favourite, toggle button, on" or "Favourite, button, selected", and "off" or "not selected" in the other state.
- **Visual state:** also change the icon shape, for example an outline heart when off and a filled heart when on. Don't rely on colour alone.
- **Feedback:** on toggle, the state change should be announced, which most platforms do automatically for toggles. If the app also shows a toast like "Added to favourites", make sure it's announced as a live region or it won't be heard.

**General points for the whole toolbar**

- Don't put the role in the name ("button", "icon"). The platform adds it.
- Start with the verb, and keep names short and in sentence case.
- Move the strings into your localisation files so they're translated, and don't derive them from asset names.
- Check that touch targets are at least 44×44 pt (iOS) or 48×48 dp (Android), and that focus order matches the visual left-to-right order.
- If Stop is only valid while recording, mark it as disabled (not hidden) when idle, or hide it from the accessibility tree. Likewise, consider changing Record to "Pause" or "Resume" if that's how the control behaves.
