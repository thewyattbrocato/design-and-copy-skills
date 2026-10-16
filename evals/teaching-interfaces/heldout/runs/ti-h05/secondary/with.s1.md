Here's the tidied copy. The only real change is on screen 2, where "draw" doesn't match a circle that's already placed.

**Screen 1: Add your first walk**
> Pick a dog, a day and a time. That's all a walk needs.

Button: **Next**. No change needed.

**Screen 2: Add your walking area**
> Drag the circle over the area where you walk. We'll only offer you walks inside it.

Button: **Next**

**Screen 3: You're ready**
> Your first walk is on the calendar. Tap it any time to change or cancel.

Button: **Go to calendar**

Two things to check before tomorrow:

1. **Skip can make screen 3 false.** If someone skips screen 1, there's no walk on the calendar, so "Your first walk is on the calendar" is wrong. Either show the alternate line when no walk was added, "Add your first walk any time from the calendar," or confirm that skipping still creates a default walk. The same applies to screen 2: if the circle is skipped, check that "We'll only offer you walks inside it" still holds.
2. **Drop Skip on screen 3.** The last screen already leads to the calendar, so a Skip link there is redundant.

I haven't changed any files, since this directory has no source for the app, only the copy you pasted.
