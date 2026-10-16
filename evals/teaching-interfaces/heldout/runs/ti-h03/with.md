**Ship (c), the interactive setup with a live preview.**

**Why**

- **It's the only option where users do the real task.** The problem is that new users set up alerts wrongly. A video or carousel can only describe the four settings. Option (c) has them build their first real alert, so they finish with a working alert and the skill to make another.
- **The live preview shows what each setting does.** Height range, wind direction limit and time window are abstract until you see them against today's conditions. "Your alert would have fired 3 of the last 7 days" or "this would trigger now" tells users whether their settings make sense. A carousel can't show that, and a video would be out of date the next day.
- **Users don't have to remember anything.** With (a), someone watches 90 seconds and then has to recall wind limits and swell ranges later on a different screen. With (b), the cards disappear before the setting is used. In (c) the explanation sits next to the control, and earlier choices stay visible while they work.
- **Both alternatives sit between the user and the task.** People tend to skip videos and swipe through carousels. Neither one changes the alert form itself, so the confusion is still there afterwards.

**How to keep it small enough for one sprint**

- Take the four settings one at a time, in your order: beach, swell height, wind, time window. Give each a one-line "what this does" beside the control, and a sensible default so nobody starts from a blank form.
- Make the preview a single strip or card that updates as they change a value. Use today's real conditions at the chosen beach, and a plain sentence such as "Right now: 4 ft, offshore. This alert would fire."
- Include a visible skip for experienced surfers, and keep a way to reopen the guidance later from the alert screen.
- End by confirming what the alert will do ("You'll be notified when…") and not with a celebration screen.
- Fix confusing labels and defaults as you go. For example, wind "limit" may be unclear without saying whether it means offshore or onshore. Label changes can fix some of the confusion without any teaching.

**How to check it worked**

Since you have no data, treat this as a bet and measure it. Track these:

1. The share of new users who save a first alert.
2. Whether they create or edit an alert unaided about a week later.
3. How often their alerts fire, and how often they're deleted or edited soon after. Frequent deletions would mean the settings are still wrong.

Compare these against your current cohort. Don't use "completed the tutorial" as the measure.

**Assumptions and trade-offs**

- I assumed the preview can use data you already fetch, such as the forecast for the chosen beach. If it can't, a simplified preview is still better than none.
- (c) is the most engineering work of the three. If it won't fit, a cut-down version (defaults plus one live line of conditions) still beats a video.
