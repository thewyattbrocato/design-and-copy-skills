Here's what's wrong with each button and what to replace it with.

| Button | Problem | Replacement name |
|---|---|---|
| Microphone | "button" is just the role, so it says nothing about the action. Screen readers already announce "button". | **Record** |
| Square | "stop icon" describes the picture, not the action. The role is also missing from the name, and "icon" is noise. | **Stop recording** (or just **Stop** if only one thing can be stopped) |
| Scissors | "Click here to trim" is too long. "Click" is wrong on a touch device, where users double-tap, and the screen reader already announces that it's a button. | **Trim** |
| Bookmark with a plus | "bookmark_add_24px" is the raw icon asset or font-ligature name. It's read out as a string of tokens, including the size. | **Add bookmark** |
| Three dots | "More" is vague, and it doesn't say what it opens. | **More options**. If it opens a menu, also expose it as a popup/menu button, so it's announced as "collapsed" or "expanded". |
| Heart | The label never changes, so the on/off state is conveyed only by colour. Screen-reader users can't perceive that, and it fails WCAG 1.4.1 (Use of Color). | See below. |

**Heart (favourite toggle)**

Keep one stable name and expose the state programmatically. Don't swap the label between "Favourite" and "Unfavourite". A changing label combined with a state gets announced confusingly, as in "Unfavourite, pressed".

- Name: **Favourite** (the same in both states).
- State: expose it as a toggle button.
  - Android: use `stateDescription` / `AccessibilityNodeInfo` checked state, or a `Switch`/`ToggleButton`-style role.
  - iOS: set the `.selected` trait.
  - Web view: use `aria-pressed="true"` or `"false"`.
- What the user hears: "Favourite, toggle button, off" and then "Favourite, toggle button, on".
- Also announce the change when they activate it, because focus stays on the button. Where the platform supports it, send a short announcement such as "Added to favourites" or "Removed from favourites".
- Visual: keep the colour change, but also change the heart from outline to filled. That helps sighted users who can't distinguish the colours.

**General notes**

- Names should be short, start with the verb, and say what the button does. They shouldn't describe the icon.
- Don't include the word "button" or "icon" in any name.
- Localise the names. Don't let them fall back to asset names.
- Record is also a state-changing control. If the mic button turns into a pause button during recording, update its name to match, for example **Pause**, so the toolbar never has two buttons that both read "Record".
- Mark the icon graphics themselves as decorative so the screen reader doesn't also read the image.
- Test with VoiceOver and TalkBack, swiping through the toolbar left to right.
