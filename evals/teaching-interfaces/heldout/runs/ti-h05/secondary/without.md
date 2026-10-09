Here's a tidied version. I kept your structure and button labels.

**Screen 1: Add your first walk**
> Pick a dog, a day, and a time. That's all a walk needs.

**Screen 2: Add your walking area**
> Drag the circle over the area where you walk. We'll only offer walks inside it.

**Screen 3: You're ready**
> Your first walk is on the calendar. Tap it to change or cancel anytime.

Changes:
- **Screen 2 contradicts the screen.** The copy says "Draw a circle," but the circle is already placed and draggable. "Drag the circle" matches what the user sees.
- **Screen 1:** Added the serial comma. The rest is unchanged.
- **Screen 3:** "Any time" became "anytime." Otherwise unchanged.

Check before shipping: Screen 3 says "Your first walk is on the calendar," but the Skip link on Screens 1 and 2 lets someone reach this screen without adding a walk. If Skip is available there, the line would be false for those users. Either hide Skip on Screen 1, or change the copy to something like "Here's your calendar. Tap any walk to change or cancel it."

I haven't edited any files because this project isn't a git repo and I didn't find the copy in the working directory. If you send me the file or component that holds these strings, I'll apply the changes there.
