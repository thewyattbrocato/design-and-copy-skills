**Ship (c), the interactive setup with a live preview.**

The confusion is about what the settings *mean* for a real beach. "Is 4 ft too big? What does a wind limit of 15 kt do to my Tuesday?" A video or carousel can define each setting, but users still have to picture how it plays out. The live preview answers that with today's actual surf, wind, and tide at the spot they picked.

- **Video (a)** is the weakest fit. Users skip 90-second intros, it can't reflect their beach or today's conditions, and it goes stale every time you change a setting.
- **Carousel (b)** is the cheapest and easiest to test, but it's passive. Four cards of explanation teach vocabulary, not judgment. Users often swipe through without absorbing it and then guess when they reach the real screen.
- **Interactive setup (c)** does the job the user came for, creating the first alert, and teaches each setting while they make it. It also surfaces the failure mode directly: if the preview shows the alert would have fired zero times last week, the user can see that before they save a useless alert.

Its risks are real. It's the most work, the preview depends on forecast data being fast and reliable for the chosen spot, and some users will just want to get out of the way. To manage those:

- Pre-fill sensible defaults so a user can finish in one or two taps.
- Keep it to the four settings. Don't add more.
- Let people skip it and finish later, with a visible way back in.
- Use the preview to show how often the alert would have triggered over the past week. That's more useful than showing only today.

Since you have no data, make the decision measurable whichever you ship. Track the share of new users who create an alert in their first session, and whether that alert is still active or has fired a notification after 7 days. Those numbers will tell you more than the design debate.

If you can't ship (c) in one sprint, ship (b) as a fallback, but add the live "would this have fired?" preview as soon as you can. The carousel without it still leaves users guessing.
