**Anchor:** calm and decisive, like a quiet productivity tool. Dispatchers do about 200 assignments a shift, so every animation gets paid for 200 times. "Alive" should mean the board is trustworthy and easy to read, not that it moves a lot. I'm assuming a web console with CSS transitions and system reduced-motion honored.

## Ask the designer for these (ranked)

1. **Assign: job moves to the driver.** This is the cause-to-result moment, and it happens 200 times a shift. The job row slides toward the driver's lane and settles, and the driver's status chip changes color. It takes 150–200 ms with ease-in-out, because it moves between two on-screen places. It must be interruptible, so the next click never waits for it. Effort is medium.

2. **Row insert and removal.** New jobs arriving and completed jobs leaving are currently silent, and rows shifting under a dispatcher's cursor cause misclicks. Specs:
   - New rows fade in with a short travel (opacity plus 8 px, 200 ms ease-out).
   - Removed rows fade out in about 150 ms.
   - The rows below slide closed over 200 ms instead of jumping.
   - No stagger, because the list is long and live.

3. **"Something changed off to the side" cue.** This is probably the most valuable one. A dispatcher looking at one side won't notice a new urgent job, a driver going offline, or an ETA slipping on the other side. Give it a brief background highlight on the changed row (a color flash that fades over about 600–800 ms, no movement). It must not flash more than three times a second. Cap it to meaningful changes, or the board turns into noise. Effort is low.

4. **Press and hover feedback on rows and buttons.** Use 100–150 ms color or background changes only. No lift, scale or bounce. Effort is trivial.

5. **Failed assignment.** If an assignment fails or is rolled back (driver went unavailable, conflict), the job returns to its origin and the row gets a brief highlight. Persistent error text stays near the row, because the motion alone is easy to miss. Effort is low once #1 exists.

## Not animating

- **Count-ups or ticking numbers.** Dispatchers read these, and animation makes them wait.
- **Idle or ambient motion, pulsing badges, looping "live" indicators.** Across a 10-hour shift this is fatigue and noise. A badge that always pulses also hides the one that matters.
- **Row hover lifts, shadows or parallax.** They add nothing on a dense board.
- **Page-load fades or staggered entrances.** The board should be usable instantly at shift start.
- **Bounce or overshoot on anything.** It's too playful for a tool people use all day.
- **Spinners under about a second.** Show progress only after a wait of a second or more, inside the control that started it.

## Requirements to hand the designer

- Never disable input while something animates. New clicks retarget the motion.
- Use transform and opacity only, so the board stays smooth with many rows.
- Reduced motion removes the sliding and keeps the color highlights, focus rings and state changes.
- Ask them to deliver numbers (duration, easing, trigger, interruption), not adjectives.

## Answer for the owner

Tell them the board will feel alive because it's always clear what just changed and where each job went. If you want one demo, build #1 and #3 together. Before building the rest, test with a couple of dispatchers whether they feel faster. If they say it feels slower, cut motion rather than tune it.

**Cost of this posture:** it may look plain next to the consumer app the owner saw. That's the tradeoff, and it's the right one for this audience.

If you tell me the stack and whether jobs can arrive in bursts, I can turn #1–#3 into a one-page motion spec for the designer.
