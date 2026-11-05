**Screen 1**
- Title: Add your first walk
- Text: Pick a dog, a day and a time. That's all a walk needs.
- Button: Next

**Screen 2**
- Title: Add your walking area
- Text: Drag the circle over the area where you walk. We'll only offer you walks inside it.
- Button: Next

**Screen 3**
- Title: You're ready
- Text: Your first walk is on the calendar. Tap it any time to change or cancel.
- Button: Go to calendar

Changes: screen 2 said "Draw a circle," but the circle is already placed and only needs dragging, so the text now matches what people see. Screen 1 and screen 3 are unchanged because they already read clearly.

Two things to check before tomorrow:
- If "Skip" on screens 1 or 2 goes to screen 3, that screen says "Your first walk is on the calendar," which would be false when no walk was added. Either skip should land somewhere else, or screen 3 needs a different message for that case.
- "Skip" on screen 3 does nothing useful, since it's the last step. Consider hiding it there.
