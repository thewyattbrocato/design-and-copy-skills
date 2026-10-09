**Why the testers reacted that way**

- **Queasy:** The number is the biggest thing on the screen, and for 2.5 seconds its digits are all moving at once. Rolling digits move fast and the eye can't settle on them, which bothers some people, especially those who are sensitive to motion. The animation also runs on every open, so there's no way to get used to it. I can't say for sure what caused one tester's reaction, but this is the most likely cause. Check whether the app respects the OS "Reduce Motion" setting.
- **Waiting to read:** The screen shows false numbers for 2.5 seconds, and the real one only appears at the end. People open this screen to read one fact. The animation puts a delay in front of that fact, and the delay is charged on every open. On a money screen, a balance of $0 that isn't real can also cause a moment of alarm.

**Is it worth keeping?**

Not as built. The animation doesn't do any of the jobs motion should do. It doesn't orient the user, point at a change, or confirm an action. It's there for delight, and that isn't enough to justify it on the most frequently visited screen. The PM's reaction is probably to the polish, which you can keep in a smaller form.

**What I'd keep**

The feel I'd aim for is calm and decisive, like a quiet money tool.

1. **Normal open:** Show the real balance immediately, with no animation. Use tabular numerals so the digits don't shift width.
2. **Balance changed since the last view:** Roll only the digits that changed, from the old value to the new one. This is the one place the animation has a job: it tells the user the number is different now.
   - Duration is 300 ms, with ease-out `cubic-bezier(0.2, 0, 0, 1)`.
   - Each digit travels about half a line height, with an opacity crossfade.
   - Stagger is 30 ms per digit, with a total cap of 150 ms.
   - The number is readable and correct from the first frame, because the old value is a true value.
   - A new update mid-roll retargets from the current state. Nothing is blocked.
3. **Reduced motion:** Swap the value instantly, with at most a 150 ms opacity or color highlight. No movement.
4. **Accessibility:** The accessible label holds the final value from the start. Don't let a screen reader announce intermediate values.
5. **Optional long version:** Keep the 2.5 s count-up only for a rare moment, such as first linking an account or hitting a savings goal. Make it skippable with a tap, and turn it off under reduced motion.

**How to settle it with the PM**

Build the changed-value version and run the same two testers through it. If the queasiness and the waiting both go away, the case is closed. If the PM still wants more, add the long version to a rare moment rather than to every open.
