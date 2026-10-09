**Ship (c), the interactive setup with a live preview.**

**Why, given you have no data:**

1. **It fits the problem.** Users aren't failing because they lack information. They're failing because the four settings interact and are hard to judge in the abstract. "Is 3–5 ft good?" or "What does a 15 kt offshore limit mean at my beach?" only makes sense next to real numbers. A live preview of today's conditions turns each setting into something they can see: "this range would have alerted you this morning, and this one wouldn't have."

2. **It's the only option where users do the task.** The video (a) and carousel (b) are passive. People skip them, forget them, or watch them before they have any context. With (c), the first alert is created during onboarding, so success means a working alert, not just an explanation delivered. That is also the metric you care about.

3. **It teaches at the moment of need.** Each setting is explained when the user is about to choose it, with the preview showing the effect right away. The video and carousel put all the explanation up front, before users have touched anything.

4. **It gives you the data you lack.** Instrument step completion, drop-off per setting, and how often users change the defaults. After one sprint you'll know which setting is the real problem. Neither (a) nor (b) gives you that.

**Trade-offs:**
- (c) is the most expensive to build. It needs a live data feed in the flow, sensible defaults per spot, and handling for flat or blown-out days, where the preview looks empty or alarming. If the real cost doesn't fit the sprint, fall back to (b), not (a). Cards are cheap and skimmable, and you can write them with concrete examples.
- (a) is the weakest bet. 90 seconds is long for a first launch, it's expensive to update when the UI changes, and users want to get to their beach.

**Ways to improve (c):**
- Pre-fill the settings with defaults based on the spot's typical conditions, so users adjust rather than start from scratch.
- Add a one-line explainer under each setting, which gets you most of what (b) would have given you.
- Let users skip to a default alert in one tap, so the flow doesn't become a barrier.

This is a judgment call from how people learn this kind of task, not from your users' data. Check it by tracking the share of new users who finish setup with an active alert, and compare that to your current baseline.
