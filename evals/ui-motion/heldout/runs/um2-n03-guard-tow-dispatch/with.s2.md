**My recommendation is to ask for four small animations and leave everything else static.** For dispatchers working 200 jobs over 10 hours, "alive" should mean the board shows what changed without making them wait or watch. The tone I'd give the designer is quiet and crisp, like a focused productivity tool. The cost is that the board may look plain next to the consumer app the owner saw. Speed and clarity are the better trade for this audience.

## Ask for these, in priority order

1. **Assignment confirmation (highest value).** When a dispatcher assigns a job, the job row moves to the driver's side, or the driver's card updates in place, instead of vanishing and reappearing.
   - **Question it answers:** "Did it work, and where did it go?"
   - **Spec:** 150–200 ms, ease-in-out for the move, transform and opacity only. Dispatchers can keep clicking during it, and a new action interrupts it.
   - **Effort:** medium. It needs layout-animation support.

2. **Highlight on changes made behind the dispatcher's back.** This covers a new job arriving, a driver's status changing, or another dispatcher claiming a job.
   - **Question it answers:** "What changed while I was looking elsewhere?"
   - **Spec:** a background tint that fades over about 1.5 s, with no movement. A new row inserts without shoving the list down under the cursor. Reserve a distinct, slightly stronger treatment for urgent states such as a stuck or overdue job.
   - **Effort:** low. This is probably the best value for the cost.

3. **Press and hover feedback on rows and buttons.** The change is color or tone only, and it happens in 100–150 ms.
   - **Question it answers:** "Did it register?"
   - **Spec:** no lift, scale, or travel. Nothing should move away from the pointer.
   - **Effort:** low.

4. **Detail drawer or panel.** When a job's detail panel opens, it slides from the edge it lives on.
   - **Question it answers:** "Where did this come from?"
   - **Spec:** about 200 ms ease-out in and about 150 ms out.
   - **Effort:** low.

If the owner wants one extra, add an inline loader inside the button that started a slow action. It should appear only after about 300 ms, so quick actions show nothing.

## Tell the designer not to animate

| Skip | Why |
|---|---|
| Staggered or fade-in list loads | A 200-job board repeated all shift becomes a tax, and the last item arrives late. |
| Count-ups on totals or ETAs | Dispatchers came to read the number, not watch it climb. |
| Bounce, overshoot, or pulsing attention-getters | These get irritating by hour three. Constant pulsing also competes with real urgency signals. |
| Row hover lifts or scaling | Moving targets cause mis-clicks on a board built for speed. |
| Scroll reveals, parallax, or background motion | These add nothing on a working tool. |
| Any animation that blocks input | A dispatcher on job 150 won't wait for a transition to finish. |

## Constraints to put in the handoff

- **Budget:** frequent actions get 150–250 ms or less, and nothing on the board goes over 300 ms.
- **Interruptible:** a new click retargets or reverses the motion, and no control is disabled during it.
- **Reduced motion:** honor the system setting. Remove the movement, but keep color highlights and focus states.
- **Performance:** animate transform and opacity only, and test with 200 live rows. Slowness on a busy board is more often input lag than animation length.

## What to tell the owner

Frame it as "alive" meaning the board shows what's happening right now. The change highlights (item 2) deliver that most visibly. Decorative motion would work against dispatchers during a long shift.

Two questions would change this advice: whether the board updates live from other dispatchers, and whether you already have motion tokens or a design system. If the board is live, item 2 matters even more. If you have tokens, the designer should use those values instead of mine.
