Ask for a small set of animations that show what just changed, and none that only decorate. Over a 10-hour shift with about 200 assignments, anything ambient or slow turns from charming into fatiguing or obstructive. Motion also pulls the eye, so decorative motion competes with the signals dispatchers need to catch.

**Ask the designer for these**

1. **Assignment confirmation.** When a job is dropped on a driver, the job visibly moves into or highlights on that driver's card (about 150-200ms). This confirms the right driver got it, so it cuts misassignment.
2. **Change flash for updates the dispatcher didn't make.** This covers a new job arriving, a driver status change, or another dispatcher reassigning something. The changed cell gets a brief highlight that fades over 1-2 seconds. It answers "what just changed?" on a board that updates while they're looking elsewhere, and it's probably the highest-value item.
3. **Drag and drop feedback**, if the board uses dragging. Lift the item, highlight valid targets, and snap back on an invalid drop. Keep it fast.
4. **Failure feedback.** If an assignment fails or is rejected, the item should visibly revert with a clear cue. A silent failure is the worst outcome on this screen.
5. **One-shot escalation cue.** When a job crosses an SLA or wait-time threshold, change its color persistently and add a single pulse at the moment it crosses. Don't loop the pulse.

**Rules to give the designer**

- Keep every animation under about 200ms, except the change-flash fade.
- Animations must never block input. A dispatcher should be able to act mid-animation.
- Never move rows out from under the cursor. New jobs shouldn't shove the list down while someone is aiming at a target.
- Support reduced-motion, and make sure the board still communicates every change without animation.

**Push back on these**

- Looping or "breathing" indicators. They create constant peripheral motion and dilute real alerts.
- Animated re-sorting or reflowing of the whole list.
- Page or panel transitions, bouncy easing, count-up numbers, and shimmer skeletons on a screen that's open all day.

**What to tell the owner**

The consumer apps feel alive because the data is live, not because of flourishes. Frame it as: "The board will feel alive because you can see changes the instant they happen." The change flash and assignment confirmation deliver that. Ambient animation would make the board feel busier and slower.

**A quick check before you commit**

Sit with a dispatcher for part of a shift and note where they miss changes or hesitate. Then ask for animation only where it fixes one of those. For each proposed animation, ask "What does this tell the dispatcher that they'd otherwise miss?" and cut it if there's no answer.
