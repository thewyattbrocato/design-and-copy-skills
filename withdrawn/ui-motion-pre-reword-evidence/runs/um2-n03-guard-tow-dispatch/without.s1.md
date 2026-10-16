**Ask for a small set of animations that show state changes, and none that only decorate.** A consumer app is used for minutes and rewards delight. Dispatchers sit in this console for 10 hours and make about 200 assignments, so motion that's charming on the first day becomes noise by day three.

**Ask for these**

1. **A change highlight on rows the dispatcher didn't cause.** When a job arrives, a driver's status changes, or a coworker reassigns something, the row gets a background tint that fades over 1–2 seconds. This is the most valuable one. Dispatchers look at a phone, a radio, or one side of the board, and they miss changes elsewhere. It also delivers what the owner wants, because the board visibly reflects live activity.
2. **A short transition when the dispatcher assigns a job** (about 150–200 ms). The job slides or settles from the job side to the driver side. This confirms the action worked and shows where the job went. It must never block the next click.
3. **A quick reflow when rows are added, removed, or reordered** (about 150 ms). Without it, rows jump and the dispatcher loses their place in the list. The motion lets the eye track what moved.
4. **Optionally, one clear failure cue.** If an assignment fails or conflicts (say, two dispatchers claim the same job), use a brief highlight plus an inline message. It should be hard to miss and should not loop.

**Don't ask for these**

- Looping or ambient motion, such as pulsing badges, breathing cards, or animated backgrounds. It pulls peripheral attention for hours, and it hides the real signals in #1.
- Persistent pulsing for urgent or overdue jobs. Use a static color or icon change. If you want motion, pulse once when the job crosses the threshold, then hold the static state.
- Bounce, spring, or overshoot easing, page transitions, count-up numbers, or skeleton-loader shimmer. These are slow or purely cosmetic.
- Anything that delays input. At 200 jobs a shift, even 300 ms of lock-out adds up to a real cost.

**Constraints to give the designer**

- User-triggered motion stays under about 200 ms. Fades for incoming changes can be longer, but they must be non-blocking.
- Cap simultaneous animations. If 15 updates arrive at once, they shouldn't all flash. Batch them or fall back to a subtle treatment.
- Respect `prefers-reduced-motion`, and consider an in-app "quiet mode."
- Every animation has to answer the question "What changed, or what did my action do?" If it doesn't, cut it.

**Handling the owner**

"Alive" can be reframed as "the board is current and trustworthy." You could add a small "updated just now" or connection-health indicator, which costs little and supports that message. Before building, show two or three dispatchers a prototype with and without the highlights and ask which they'd want to work with for a full shift. Their answer will settle the debate better than a design opinion will.
