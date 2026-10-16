**Short answer:** Don't ask for "alive." Ask for four small motions that help dispatchers keep track of the board, and write down what you're not animating. A dispatcher does about 200 assignments in 10 hours. Any decoration gets paid for 200+ times a shift, and it competes with the thing they're scanning. Posture: calm and decisive, like a quiet productivity tool. The cost is that it will look plain next to a consumer app, so tell the owner that up front.

## Ask the designer for (ranked)

1. **Assignment: job moves to the driver (highest value, do first).**
   - **Job:** cause and effect. It confirms the assignment landed and shows where the job went.
   - **Spec:** the job row travels or collapses toward the driver's lane and the driver card updates. About 200 ms, ease-in-out (it moves between two on-screen places). Never block the next click. A new assignment retargets or interrupts any motion still running.
   - **Effort:** medium. Prototype this one first.

2. **Highlight on changes the dispatcher didn't make.**
   - **Job:** "what changed?" Covers a new job arriving, a driver's status flipping, an ETA shifting, or another dispatcher grabbing a job.
   - **Spec:** a background tint on the row or cell that fades out. About 150 ms in, then 1 to 1.5 s out. Use color and opacity only, with no position change, so nothing jumps under the cursor. Cap simultaneous highlights, because a busy board that flashes constantly is worse than none.
   - **Effort:** cheap. This is probably the most useful one for the "alive" request, because the board visibly reflects live data.

3. **Row insert and removal.**
   - **Job:** orientation. When rows appear or vanish silently, everything below shifts and the dispatcher loses their place.
   - **Spec:** about 150 to 200 ms. Removed rows fade, then the gap closes. Inserted rows ease out into place. No stagger on a list this long.
   - **Effort:** cheap to medium.

4. **Press feedback and error response.**
   - **Job:** "did it work?" Use a 100 ms press state on buttons. A failed assignment (driver unavailable, conflict) gets a brief shake or highlight plus persistent text and a visible rollback.
   - **Effort:** cheap.

Every one of these needs a reduced-motion variant. Remove the movement, but keep the color highlight and focus states. Animate only transform and opacity, and never use `transition: all`.

## Not animating (tell the owner this too)

- **Hover lifts and row scale on the job list.** The cursor is on it constantly, and the target shouldn't move.
- **Count-ups and animated totals.** Dispatchers read these numbers, so show them immediately.
- **Page-load fades, staggered entrances, scroll reveals and parallax.** They repeat every session and delay the data.
- **Looping pulses and attention-getters.** After hour three they turn into noise and mask the real alerts, like a stuck job or a late pickup.
- **Bounce or overshoot, and anything over about 300 ms.** The board is a constant-use tool.

## Suggested pitch to the owner

"The consumer app is meant to be browsed. This one is meant to be read at speed for 10 hours. We're adding motion that shows what changed and confirms each assignment, so the board feels responsive and alive without getting in the way."

Before you brief the designer, check two things. First, how often the board updates from outside the dispatcher's own actions, which decides how aggressive the highlight cap in #2 needs to be. Second, whether you have an existing design system with motion tokens. If you do, the designer should use those values and not invent new ones.
