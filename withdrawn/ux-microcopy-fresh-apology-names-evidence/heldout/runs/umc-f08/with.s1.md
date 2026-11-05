# Echoline toolbar accessible names

Screen readers already announce the role ("button"), so each name should say what the control does. It shouldn't describe the icon or repeat the role.

| Icon | Current | What's wrong | Replacement |
|---|---|---|---|
| Microphone | `button` | It only repeats the role, so users hear "button, button" and get no purpose. | **Record** |
| Square | `stop icon` | It describes the picture, not the action, and "icon" is noise. It also doesn't say what is being stopped. | **Stop recording** |
| Scissors | `Click here to trim` | "Click here" is filler. It also assumes a mouse, and on mobile screen-reader users double-tap. The action is buried in the middle. | **Trim** |
| Bookmark with plus | `bookmark_add_24px` | This is the icon asset or ligature name leaking through. It's meaningless when spoken, and the underscores and size are read out. | **Add bookmark** |
| Three dots | `More` | It's vague, and nothing says it opens a menu. | **More options**, exposed as a menu button (collapsed or expanded state, or the platform's popup or menu hint) |
| Heart | `favourite` (always) | The on/off state is shown only by colour, so screen-reader users can't tell whether the recording is already a favourite. Colour-only state also fails for low-vision and colour-blind users. | See below |

## Heart behaviour

Make it a toggle button with a fixed name and an exposed state:

- **Name:** "Favourite", and it never changes.
- **State:** expose it programmatically.
  - On iOS, use the selected trait.
  - On Android, use a checkable or toggle role with state description "On" or "Off", or a checked state.
  - On web, use `aria-pressed`.
- **Result:** the user hears "Favourite, toggle button, off" or "Favourite, toggle button, on". Activating it flips the state, and the screen reader announces the new state.
- **Visual:** don't rely on colour alone. Use an outline heart when off and a filled heart when on, with enough contrast.

Don't change the label and expose the pressed state at the same time. "Remove from favourites, pressed" is confusing. If your framework can't expose toggle state, the fallback is to change the name instead: "Add to favourites" when off and "Remove from favourites" when on.

## Other points

- **Record and Stop:** if Record turns into Pause and Resume during a recording, the name must change with it. Alternatively, keep a stable name and expose the state, as with the heart.
- **Localization:** put these strings in your localization files, not just the English text.
- **Testing:** check with VoiceOver and TalkBack that each name is announced once, with the role appended.
