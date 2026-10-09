**What's wrong:** the page has no order. All eight rooms share one card, all four numbers share one size and weight, and a problem appears only as a slightly darker orange digit plus an 11px grey word. A room that is out of range looks almost the same as one that is fine. On a status board, the exception should be the loudest thing on screen, and right now it's one of the quietest. The page isn't flat because of the card styling. It's flat because nothing is ranked. Room 5 went unnoticed because the page never asked anyone to look at it.

**What to change first:** add a status line above the grid that answers "is anything wrong?" in plain words, e.g. "1 room out of range: Room 5, humidity 61% for 6 h." If that line is the first thing on the page and it's empty when all is well, the page does its job even at a glance. This one change does more than any styling change.

**Then, in order:**

1. **Make out-of-range cards structurally different.** Give them a tinted fill and a heavier coloured border, and turn the "alert" word into a readable label such as "OUT OF RANGE" at body size. In-range cards stay plain. Color alone is weak, so the label is the second cue.
2. **Sort problem rooms to the top** of the grid, or pin them in a row above the rest. Eight identical tiles make the viewer scan all of them to find the one that matters.
3. **Show how long a reading has been out of range,** not just the value. For mushroom rooms, duration is usually what matters. "61%, 6 h" is far more actionable than "61%".
4. **Quiet the in-range numbers.** Keep the out-of-range number at full weight and let the healthy ones drop to a calmer value. Then the eye lands on the exception first.

**Outside the page:** a page only helps someone who is looking at it. For six hours of humidity drift, you need a push or SMS alert with a threshold and a duration (for example, "out of range for more than 30 minutes"). That is probably the fix that would have caught Room 5, and it isn't a design question.

**Check:** squint at the page and the problem room should still be the first thing you see. If it isn't, widen the gap between states.

I don't know your target ranges or whether 61% is out of range for Room 5. If you send me the thresholds and your current CSS or markup, I can make the status line and the out-of-range card styles directly.
