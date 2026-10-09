Here's a tidied version. The copy is short already, so most changes are small.

**Screen 1: Add your first walk**
> Pick a dog, a day, and a time. That's all a walk needs.

Button: **Next**

**Screen 2: Add your walking area**
> Drag the circle over the area where you walk. We'll only offer you walks inside it.

Button: **Next**

**Screen 3: You're ready**
> Your first walk is on the calendar. Tap it to change or cancel.

Button: **Go to calendar**

**What changed**
- Screen 1: added the Oxford comma so the list reads cleanly.
- Screen 2: "Draw a circle" is now "Drag the circle." The circle is already placed, so "draw" would make people look for a drawing tool that isn't there. "Drag" matches the draggable circle you described.
- Screen 3: cut "any time." "Tap it to change or cancel" says the same thing.

**Two things to check before you ship**
1. **Screen 3 may be false for some users.** If someone taps Skip on screen 1, there's no first walk on the calendar, so "Your first walk is on the calendar" is wrong. Either the Skip path needs different copy on screen 3, or Skip on screen 1 shouldn't be available.
2. **The Skip link on screen 3 probably isn't needed.** The "Go to calendar" button already exits the flow. A Skip there is one more thing to explain, and it's the screen where skipping makes the least sense.

If you send me the source files for these screens, I can apply the copy changes directly and check the Skip behavior in the code.
