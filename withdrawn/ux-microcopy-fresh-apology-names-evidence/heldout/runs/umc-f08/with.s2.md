Here's what's wrong with each button and what its name should be.

| Icon | Current name | Problem | New name |
|---|---|---|---|
| Microphone | "button" | It only gives the role, which the screen reader already announces, so the name says nothing about the action. | **Record** |
| Square | "stop icon" | It describes the picture, not the action. Users need to know what stops. | **Stop recording** |
| Scissors | "Click here to trim" | "Click here" is wrong for touch and screen-reader gestures, and it's wordy. It also doesn't say what gets trimmed. | **Trim recording** |
| Bookmark with a plus | "bookmark_add_24px" | This is the asset filename, so it gets read out as "bookmark underscore add underscore 24 px". | **Add bookmark** |
| Three dots | "More" | It's vague, and "More" what? Users can't tell it opens a menu of actions. | **More options** |
| Heart | "favourite" (never changes) | It's the right word, but the on/off state is only visible through colour, so screen-reader users can't tell whether the recording is already a favourite. | **Favourite**, as a toggle (see below) |

**How the heart should behave**
- Keep the name fixed as "Favourite", and expose the on/off state through the platform's toggle state instead of changing the label.
  - **Android:** make it a checkable or toggle control, or set `stateDescription`. TalkBack then says "Favourite, toggle button, on" or "off". In Compose, use `Modifier.toggleable` or `IconToggleButton`.
  - **iOS:** set the `selected` trait when it's on, or use a value such as "On" and "Off". VoiceOver then says "Favourite, selected, button".
  - **React Native:** use `accessibilityRole="togglebutton"` with `accessibilityState={{ checked }}`. `selected` also works.
- Don't also change the label to "Remove from favourites" when the state is on. The user would hear both the new label and the state, which is confusing and contradictory, for example "Remove from favourites, selected".
- The state must be announced when the user toggles it, which the platform does when the state property updates. Don't rely on colour alone, and make sure the on state also looks different in shape, for example a filled heart versus an outline.

**General rules for the whole toolbar**
- Don't put "button" or "icon" in any name, because the role is announced separately.
- Keep names short, starting with a verb where it's an action.
- Put the names in your localisation files rather than hardcoding them. Translators will otherwise never see them.
- If the microphone button turns into Pause or Stop while recording, update its name to match, since that's a real change of action rather than a toggle state.
