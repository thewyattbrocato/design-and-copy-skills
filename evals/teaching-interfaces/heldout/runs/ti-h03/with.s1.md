**Ship (c), the interactive setup with a live preview.**

**Why, given you have no data:**

- **The task is the lesson.** Height range, wind limit and time window only make sense against real conditions. A surfer who sees "0.8–1.5 m, offshore only, 6–9 am" matched against today's forecast learns what the settings do. A video or carousel can only describe them. People learn an interface by doing a real task in it, and (c) is the only option that makes the first alert that task.
- **Both alternatives rely on memory.** The video and the carousel run before the user has acted, so they have to remember a 90-second video or four cards when they reach the form. In (c) the instruction sits next to the control while they use it.
- **It addresses the actual failure.** The problem is that new users set up alerts wrongly. (c) gives immediate feedback in their own terms, such as "With these settings, today's alert would have fired from 7 to 9 am." That shows them whether their limits are too tight or too loose. The other two options can't do that.
- **Even without data, it's the safer bet.** If the preview helps, the user ends up with a working alert. If it helps less than hoped, they still end up with a working alert. Neither (a) nor (b) produces an alert by itself, and both are the kind of intro that many people skip.

**Design notes to keep (c) small enough for one sprint:**

1. **Four steps in a fixed order.** Beach, swell height, wind limit, time window. Each step shows its choice and the preview together. The preview updates after every change.
2. **Use real data only.** Show today's real conditions for the beach they picked. Don't use sample numbers that could be mistaken for their own. If today's data is unavailable, fall back to a clearly labelled sample.
3. **Give each setting a starting value.** Pre-fill it with a sensible default for the chosen beach, not a blank field. Users adjust a default more easily than they invent a value.
4. **Add a one-line explanation per step.** Use plain wording, for example "Wind limit: the strongest wind you'll still surf in, and from which direction." Don't add a tour or a "Got it" gate.
5. **Provide a visible Skip.** Experienced surfers should be able to go straight to the plain form. Keep a way to reopen the guided version later.
6. **Make the end a real alert.** The last screen should say what was saved and what will trigger it. Skip the confetti.

**How to judge it afterward.** Look at how many new users have a working alert after day 1, and how many create or edit a second alert within a couple of weeks without the guide. Compare these with your current flow, which gives you the baseline you lack today. Also check how many alerts get edited or deleted soon after creation. That would suggest users are still setting wrong limits.

**Assumptions and trade-off:**
- I assumed the forecast data for the preview is already available in the app. If it needs new backend work, that is the main risk to fitting (c) into the sprint.
- (c) costs more to build than (a) or (b), but it is the only option that fixes the problem instead of describing it.
