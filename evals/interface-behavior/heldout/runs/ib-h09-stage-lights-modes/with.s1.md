**Recommendation: neither camp's version as stated. Use Select as the home state, Paint as a visible tool, and Record as a separate button that isn't a mode.**

**Assumptions:** one trained operator, a tablet used in a dark booth, long sessions, and a lot of repeated painting. Paint changes the lights themselves. I've also assumed Record overwrites or creates a cue the operator would hate to lose. Correct me if any of these are wrong.

**Why not the always-on mode (long-press = paint, drag = select)**
- The same finger on the same light does two different things depending on timing. That is a hidden mode, and it's the kind that causes mistakes.
- The costly action, painting many lights, sits behind the subtler gesture. A hesitation, a slow start or a tremor turns a selection into a paint, or the reverse.
- Nothing on screen tells the operator which one is about to happen, and a banner wouldn't help because they're watching the stage.
- Dragging across a 48-light grid is also the natural way to select a range, so you'd be taking the most obvious gesture for the lower-stakes job.
- It has no route for anyone who can't do a timed long-press, and it needs training that cues won't leave time for.

**Why not three modes as stated**
- Select and Paint really are different. Painting is a repeated action, so a persistent tool fits it.
- Record isn't a way of touching the grid. It acts on the whole current look. Making it a mode adds a state to forget and a place to be in when you shouldn't be.

**Behavior spec**

1. **Select is the default and the resting state.**
   - Tap a light to toggle it. Drag selects a range.
   - Adding and removing are separate actions, not a toggle on a modifier. Show the selected count and show the settings of the selected lights.
   - Select never changes output.

2. **Paint is an explicit tool, entered on purpose.**
   - Entering it means tapping a large labeled "Paint" control, then choosing the color or level.
   - While it's active, the chosen swatch or level sits in the toolbar and the whole grid frame is tinted. Each painted light also shows the new value, because the operator's eyes are on the grid, not the toolbar.
   - Exit with one large "Done" button. Paint also ends when the operator leaves the screen or switches to Select, so it never carries over silently.
   - Dragging in Paint only paints, and dragging in Select only selects. No gesture changes meaning without the tint and label changing too.
   - Optional: a "hold to paint" button for the other hand, as a faster alternative. Holding reports its own state, so it can't be left on.

3. **Every paint stroke is undoable.**
   - Each stroke is one undo step. A visible Undo button stays in place, plus an undo toast for about 6 to 10 seconds (a starting value), announced to screen readers.
   - Show the count of lights changed, so a runaway drag is obvious.

4. **Record is a button, not a mode.**
   - It sits off the grid, apart from the Paint and Select controls and away from where fingers drag. Make it large rather than close.
   - Recording to a new cue number needs no confirmation, and success makes no popup. The cue list shows the new entry.
   - Recording over an existing cue shows one specific confirmation naming the cue ("Overwrite Cue 14 'Act 2 Dawn'?"), unless the previous version is kept and restorable. If you keep versions, use Undo instead of the confirmation. Versions are the better design because it keeps this step quick during a show.
   - Because cue-target mistakes are costly, show the target cue number on the Record button itself.

5. **Everything has a non-gesture route.**
   - Select all, clear selection, and select a row or group should all be buttons.
   - The 48 lights stay in fixed positions so the operator learns the grid by location.

**Open question to settle before building:** does Paint change live output immediately, or only a staged look? If it's live, painting during a show is the riskiest step. That would make a "preview, then apply" step worth discussing, or at least a clear live/staged indicator. A single test with your actual operator, in the dark, running a few cues, will settle the argument faster than more debate.
