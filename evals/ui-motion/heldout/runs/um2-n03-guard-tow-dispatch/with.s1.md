**Short answer:** ask for a small set of motions that help dispatchers keep track of the board, and decline anything that only adds "aliveness." Dispatchers are in the board for 10 hours and make about 200 assignments, so any motion that runs on every assignment gets paid for thousands of times a week. The anchor is quiet and crisp, like a focused ops tool.

## Ask the designer for these (ranked)

1. **Assignment confirmation: the job leaves the queue and lands on the driver.**
   - **What it answers:** "Did it work, and where did it go?"
   - **Why it's first:** this is the most frequent action and the most expensive one to get wrong.
   - **Spec:** the job row collapses out of the unassigned list (opacity plus a short height collapse, about 150 ms, ease-in). The driver's row gets a brief background highlight (about 200 ms in, fading out over about 600 ms). The highlight is color or opacity only, with no travel.
   - **Constraints:** the dispatcher can keep clicking during it, and the next job is targetable immediately. Rows below shift by the collapse, so don't let a target move out from under the cursor mid-aim. Collapse fast or keep the slot stable.

2. **Highlight for changes the dispatcher didn't make.**
   - **What it answers:** "What changed while I was looking elsewhere?"
   - **Examples:** a new job arriving, a driver's status changing, a job being reassigned or cancelled by someone else.
   - **Spec:** a soft background flash on the affected row, about 150 ms in and about 1 s fade out. A new job is inserted with the same flash, with no slide and no bounce. Keep it under three flashes per second and never loop it.
   - **Why it's worth it:** this is the real version of "alive." The board is live, and the dispatcher needs to see which thing just moved.

3. **Press and hover feedback on controls.**
   - **Spec:** about 100 ms color or opacity change. No lift, no scale and no travel.
   - **Why it's worth it:** it confirms the click registered, and it's cheap.

4. **Inline loading or failure state on the assignment action.**
   - **What it answers:** "Did the assignment save or fail?"
   - **Spec:** show nothing under about 300 ms. If the server is slower, show a small indicator on the row. If the assignment fails, revert the row and give a clear inline error.
   - **Why it's worth it:** a silent failure means a truck doesn't get sent. Make the error state obvious. A small horizontal shake is acceptable, but a persistent visual state matters more.

5. **Detail panel or drawer slide (only if one exists).**
   - **Spec:** slide from its own edge, about 200–250 ms ease-out in, faster out.
   - **Why it's worth it:** it orients the dispatcher to where the panel came from.

## Tell the designer *not* to do these

- **Row hover lifts, scaling, or card-style shadows.** They fire constantly and can move the target away from the pointer.
- **Animated reordering or sorting of the whole board.** Rows jumping around while someone aims at them causes misclicks. Re-sort instantly, or only on explicit user action.
- **Slide or bounce entrances for new jobs.** Use the highlight in #2 instead.
- **Count-up numbers** on job or driver totals. Dispatchers read these, so just show them.
- **Page-load fades or staggers.** The board should render fully the moment it opens.
- **Looping pulses or attention-getters**, for example on "urgent" jobs. Over 10 hours they become noise or fatigue. Use a static, high-contrast urgency indicator instead.
- **Ambient or background motion.**
- **Any delay added "so it feels like something is happening."**

## How to frame it for the owner

The owner's instinct, that a board should feel responsive and live, is right. A consumer app gets that from delight. A dispatch console gets it from instant feedback and from showing what just changed. You can say: "A fast, calm board feels alive, and a busy one feels slower and tires dispatchers out. We're adding motion where it tells them something changed, and keeping it off everything they do 200 times a shift."

The cost is that this will look plainer than a consumer app in a demo. If the owner wants something visible, the highlight in #2 is the best candidate.

## Handoff requirements for every motion

- **Interruptible:** no control is disabled while a motion plays.
- **Properties:** animate only opacity, color and transform.
- **Reduced motion:** honor the system setting. Remove movement and keep color and highlight feedback and focus states.
- **Spec as numbers:** duration, easing, trigger and interruption behavior written down, not described in adjectives.

Two facts would change this plan. One is whether the board updates live from other dispatchers (that raises the importance of #2). The other is whether there's a detail panel (that determines whether #5 applies). Send me either one and I'll tighten the spec.
