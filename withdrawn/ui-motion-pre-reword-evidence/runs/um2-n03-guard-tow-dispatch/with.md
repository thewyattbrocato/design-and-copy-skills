**Ask for a small set of motions that explain real changes. Skip decorative "alive" motion.** A dispatcher doing ~200 assignments in 10 hours pays for every animation hundreds of times, and they watch the board in their peripheral vision all day. Anything ornamental becomes friction or fatigue. The board feels alive when it reacts to real events, such as a job arriving or a driver changing status. Anchor the feel as "calm and decisive, like a quiet productivity tool."

## Ask the designer for these (in priority order)

1. **Unprompted changes (new jobs, driver status changes).**
   - **Job:** draw the eye to something that changed while the dispatcher was looking elsewhere.
   - **Spec:** the row gets a tinted background that fades out over ~1.5 s, with an opacity fade-in of ~150 ms.
   - **Layout rule:** new rows must not shove content the dispatcher is aiming at. If they're mid-interaction, show a "3 new" pill instead of reflowing.
   - This is the best answer to the owner's request, because it's the board visibly responding to reality.

2. **Assignment confirmation.**
   - **Job:** show cause and effect when a job goes to a driver.
   - **Spec:** the job row collapses out of the unassigned list in ~150–200 ms (ease-out), and the driver's card gets a brief highlight (~200 ms in, short fade).
   - **Rules:** it must be interruptible and never block the next click. Show a rollback visibly if the server rejects the assignment.
   - **Cost check:** at 200 assignments per shift, a 200 ms motion adds up. That's fine only because input never waits on it.

3. **List reflow when rows leave or reorder.** Rows slide to close the gap in ~150–200 ms so the eye can track what moved. Turn it off during rapid sequences if it makes targets shift while the cursor is heading for them.

4. **Drag feedback, only if you support drag-to-assign.** Cover pickup, valid-drop-target highlight, and snap or return on release. Springs with minimal overshoot are acceptable here because it's direct manipulation.

5. **Press and hover feedback.** 100–150 ms color or shade change on rows and buttons. It's cheap and confirms the click registered.

## Tell the designer not to do these

- Looping pulses or glows for "urgent" jobs. Use a static color or icon change instead. At most, play one pulse when a job crosses into overdue.
- Page-load staggers, count-ups, scroll reveals or parallax.
- Bounce or overshoot on rows, buttons or map markers.
- Anything over ~300 ms on a frequent action, or any control disabled while an animation plays.
- Ambient or decorative movement of any kind.

## Handoff requirements

- Every motion is specified as numbers: duration, easing, trigger, and what happens if interrupted.
- Reduced-motion variant: remove movement, keep the color and highlight changes, and keep focus states.
- Animate only transform and opacity. A board with many live rows needs to stay smooth.

## For the owner

Show a before/after of a new-job arrival with the highlight and the "no layout shift" rule. Then explain that a consumer app is used for minutes, while this console is used for 10-hour shifts. Motion that delights in minute five hurts by hour six. I can draft a one-page motion spec with these values if that would help.
