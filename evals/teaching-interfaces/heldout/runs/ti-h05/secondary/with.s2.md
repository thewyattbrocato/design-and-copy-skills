**Screen 1: Add your first walk**
> Pick a dog, a day, and a time. That's all a walk needs.

Button: **Next**

**Screen 2: Add your walking area**
> Drag the circle over the area where you walk. We'll only offer you walks inside it.

Button: **Next**

**Screen 3: You're ready**
> Your first walk is on the calendar. Tap it any time to change or cancel.

Button: **Go to calendar**

Changes:
- **Screen 2:** "Draw a circle" doesn't match the screen, since the circle is already placed. "Drag the circle" tells people what to do with it. This is the one fix that matters.
- **Screen 1:** Added the Oxford comma. Nothing else needed.

Two things to check before tomorrow:
- **Screen 3 assumes a walk exists.** If someone taps Skip on screen 1, "Your first walk is on the calendar" is false. Either hide Skip on screen 1, or show different copy when no walk was added.
- **Skip on screen 3 is redundant.** It's the last screen, so "Go to calendar" already does the job. You can remove it there.
