**Screen 1: Add your first walk**
- Text: "Choose a dog, a day and a time to schedule a walk."
- Changed "Pick" to "Choose" to match "schedule." The line still says what the screen is for, and "That's all a walk needs" is cut because it adds nothing the form doesn't already show.

**Screen 2: Add your walking area**
- Text: "Drag the circle over the area where you walk. We'll only offer you walks inside it."
- The copy says "Draw a circle," but the circle is already placed, so the user has to move or resize it, not draw it. Saying "Drag" matches what they'll actually do.

**Screen 3: You're ready**
- Text: "Your first walk is on the calendar. Tap it any time to change or cancel."
- Keep as is. It's accurate and names the one next action.

**Skip link**
- Consider "Skip setup" in place of "Skip," so people know it skips setup and not the screen.
- Remove "Skip" from screen 3. The "Go to calendar" button already does that job, so the link is redundant there.

Two things to check before shipping:
1. **Screen 3 assumes a walk exists.** If someone skips screens 1 or 2, "Your first walk is on the calendar" is false. Either make Skip on screens 1–2 lead to a different final message ("You can add a walk anytime from the calendar"), or confirm that skipping still creates a walk.
2. **Screen 2 may be better as a default than a step.** A pre-placed circle over the city, with a "Looks right? Next" framing, makes it clear it's a starting point the user can accept. I've kept the drag instruction, but the screen needs a visible "Drag to adjust" affordance on the map. I haven't seen the design, so I can't confirm it's there.
