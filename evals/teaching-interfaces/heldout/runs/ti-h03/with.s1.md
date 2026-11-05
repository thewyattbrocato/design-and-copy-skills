**Build (c), the interactive setup with a live preview.**

**Why, given no data:**

1. **It teaches by doing.** The task is to build one alert. Option (c) is that task with guidance. (a) and (b) teach before the person acts, so they have to remember four settings when they reach the form. In (c) each setting is on screen while they choose it, and their earlier choices stay visible.

2. **The preview explains the settings.** Swell range and wind limit are abstract until you see them against real conditions. For example, "this alert would fire today" or "this alert wouldn't fire, because wind is 18 kt offshore and your limit is 12." A video or card can only describe the thresholds. The preview shows what each one does, and it updates the user's mental model in their own terms.

3. **It's the safest bet without data.** The video is the weakest option. It's passive, people skip it, and nobody can replay it at the moment they're stuck. The carousel is the typical "benefits before the product opens" pattern, and it's usually swiped through without being read. (c) is the only option where a user ends up with a working alert, so you get the outcome you care about whether or not they absorb any explanation.

**Shape it so it stays small:**

- **One sentence of goal:** "Afterwards, they can set an alert that fires on days they'd want to surf."
- **Order:** beach, then swell height, then wind direction limit, then time window. Add one line of context per step, shown beside the control.
- **Defaults:** prefill sensible values, such as a swell range and wind limit typical for the chosen beach. Users adjust them instead of starting from a blank form. Label them as suggested.
- **Preview:** show today's conditions for that beach, with a plain verdict on whether the alert would trigger now and why. Consider showing the next few days too, if the data is already available.
- **Control:** allow Back and an obvious Skip. Experienced users shouldn't be forced through it.
- **Confirmation:** end with a statement of what now works ("You'll be notified when swell is X–Y and wind isn't Z"), not confetti.
- **Later:** reuse the same live preview in the edit-alert screen, so the help is there whenever someone changes a setting.

**Trade-offs and assumptions:**

- (c) costs the most engineering, mainly the preview logic, which needs forecast data wired into the setup flow. If that's too heavy for one sprint, a cut-down version still beats (a) and (b): the step-by-step flow with one-line hints and a static verdict line. Add the live preview after.
- I'm assuming you already have today's conditions data in the app. If you don't, the cost changes the calculation.

**How to check it:** you have no data, so build in the measurement. Track these three things:
- Share of new users who finish a first alert.
- Share who edit or delete it within a week, which suggests they set it wrong.
- Share who create a second alert unaided a few days later.

The last one is the real test of whether they learned it. Completion alone only shows they got through the flow.
