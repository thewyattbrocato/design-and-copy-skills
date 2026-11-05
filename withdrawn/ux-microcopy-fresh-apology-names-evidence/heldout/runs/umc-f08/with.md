Here is each button, what's wrong with it, and what to replace it with.

| Icon | Current name | Problem | Replacement |
|---|---|---|---|
| Microphone | `button` | It gives the role, not the purpose. The screen reader already announces "button", so users hear "button, button" and don't know what it does. | **Record** |
| Square | `stop icon` | It describes the picture, not the action. "Icon" is noise. | **Stop recording** |
| Scissors | `Click here to trim` | "Click here" assumes a mouse, and mobile screen-reader users double-tap. It's also wordy for a button that's already announced as actionable. | **Trim recording** |
| Bookmark with plus | `bookmark_add_24px` | This is the icon's asset or ligature name, so the implementation leaks into the label. It's read as garbled text, and it isn't localisable. | **Add bookmark** |
| Three dots | `More` | It's vague. Users can't tell what "more" contains. | **More options**. If it opens a menu, also expose that it has a popup and whether it's expanded. |
| Heart | `favourite` (always) | The on/off state is shown only by colour, so screen-reader users can't tell whether the recording is already a favourite. Colour-only state also fails WCAG 1.4.1 for colour-blind sighted users. | See below. |

## Heart behaviour

Keep the name constant and expose the state programmatically. Don't rely on colour.

- **Name:** `Favourite`, the same in both states.
- **Role and state:** make it a toggle button.
  - On iOS, set the `selected` trait. Alternatively, set `accessibilityValue` to "On" or "Off".
  - On Android, use a toggle or checkable role, or set `stateDescription` to "Favourited" or "Not favourited".
  - On React Native, use `accessibilityState={{ selected }}` or `{{ checked }}`.
- **Announcement:** "Favourite, toggle button, on" or "Favourite, toggle button, off".
- **Visual cue:** also change the shape, with an outline heart when off and a filled heart when on. Colour can still change, but it shouldn't be the only signal.
- **Don't do both:** if you flip the label between "Add to favourites" and "Remove from favourites", don't also expose a toggle state. Screen readers would then announce something like "Remove from favourites, on", which is confusing. Pick one pattern. I recommend the constant name plus state, because it's the most predictable.

## Optional, if mic and stop are one control state

If the mic button turns into stop or pause while recording, update its name to match. For example, "Record" becomes "Pause recording". Announce the change, so users know recording started.
