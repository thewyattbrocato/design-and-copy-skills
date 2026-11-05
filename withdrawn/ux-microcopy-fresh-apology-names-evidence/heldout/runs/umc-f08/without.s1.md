Each name should say what the button does. The platform already announces the role ("button"), so names shouldn't repeat it.

| Icon | Current name | What's wrong | Replacement |
|---|---|---|---|
| Microphone | `button` | It gives only the role, not the action, so the user can't tell what it does. | **Record** |
| Square | `stop icon` | It describes the picture, not the action. "Icon" is noise. | **Stop recording** |
| Scissors | `Click here to trim` | "Click here" is filler. It also assumes a mouse, and screen-reader users double-tap or activate. It's longer than it needs to be. | **Trim** |
| Bookmark with a plus | `bookmark_add_24px` | This is an asset or icon-font name that leaked through as the label. It's read as gibberish and has no spaces. | **Add bookmark** |
| Three dots | `More` | It's vague, and it doesn't say that the button opens a menu. | **More options**. Also expose that it opens a menu or popup, and its expanded or collapsed state if your platform supports that. |
| Heart | `favourite` (unchanged when on) | The on/off state is shown only by colour, so screen-reader users can't tell whether the recording is already a favourite. | **Favourite**, as a toggle with a state (see below) |

**Heart behaviour**

- Keep the name constant as "Favourite", and expose the state separately as a toggle. A screen reader then says "Favourite, toggle button, on" or "off".
  - **Android:** use a checkable or toggle control. Alternatively, set `stateDescription` to "Favourited" or "Not favourited".
  - **iOS:** keep the label "Favourite" and add the `.selected` trait when it's on.
  - **React Native:** use `accessibilityState={{ selected }}` or `checked`.
- Don't change the label as well as the state. "Unfavourite, on" or "Remove from favourites, selected" is confusing.
- If your framework has no toggle or selected state, use the label swap instead. Use "Add to favourites" when it's off and "Remove from favourites" when it's on. Never use both approaches together.
- Change the icon's shape as well as its colour, for example an outline heart when off and a filled heart when on. This also helps sighted users who can't distinguish the colours.

**Other points**

- Decorative icons inside these buttons should be hidden from accessibility, so the glyph isn't read in addition to the label.
- Localize the new names.
- Test with TalkBack and VoiceOver, and check that the focus order matches the visual order.
