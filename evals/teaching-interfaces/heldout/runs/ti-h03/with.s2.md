**Build (c), the interactive setup with a live preview of today's conditions.**

**Why (c) over (a) and (b)**

- **It's the real task.** Users get the alert wrong, so the fix is to have them make one correctly. With (c) they leave onboarding with a working first alert. With (a) and (b) they leave having watched or read something, and then still have to set up the alert unaided.
- **The preview explains the settings.** "Swell height range" and "wind direction limit" are abstract until you see them applied to a real beach. If the preview says "with these settings, today at [beach] would/wouldn't trigger", the effect of each choice shows up right away. A card or video can only describe that effect. The preview also catches mistakes immediately, for example a wind limit set so tight that the alert never fires.
- **It has no memory load.** A video or carousel asks people to remember four settings and apply them later on a different screen. In (c) the instructions and their earlier choices stay on screen while they work.
- **(a) is the weakest.** Ninety seconds is long for a first launch. People skip it, can't scrub back to the one setting they're unsure about, and it needs captions and a no-audio version to be usable. Surfers opening the app on a beach car park will rarely sit through it.
- **(b) is a fallback, not a fix.** A four-card carousel is cheap, but it's a benefits-style explainer shown before the product opens. It's the option most likely to be swiped through without reading.

**Design points that matter for (c)**

1. **The goal is one sentence:** "Afterwards they can set an alert that fires on the days they'd want to surf."
2. **One setting per step**, in the order beach, swell height, wind direction, time window. Keep the running summary and the live preview visible throughout.
3. **Start from a default.** Pre-fill sensible values for the chosen beach, labelled as suggested, so users edit rather than build from blank. Don't invent the defaults: base them on the beach's actual exposure or let them come from your surf-forecast data.
4. **Explain only what's Swellwise-specific.** For example, what "wind direction limit" means (offshore versus onshore) in plain words next to the control. Skip explaining things like dragging a slider.
5. **Give feedback in their terms**, such as "This alert would have fired on [n] of the last 7 days", rather than "Great job!". Only include that history line if your data supports it.
6. **Add a skip for experienced users** and a way to re-run the guide later.
7. **Fix labels in parallel if they're confusing.** If testing shows people misread "wind direction limit", rename or redesign it. That's cheaper than teaching around it.

**Since you have no data, this is how to check it worked**

- Instrument two measures: the share of new users who finish creating a first alert, and the share who still have an active alert, unedited or deliberately edited, a week later. Completion of the guide itself is not the target.
- Before or during the sprint, watch 3–5 new users do the setup. If they stumble at the same step, that tells you which label to change.
- If you can afford it later, A/B (c) against (b) on that week-one measure.

**Notes**

- I assumed (c) is feasible within the sprint, since the preview needs conditions data you already display. If the preview is the expensive part, a static "this range means roughly X to Y ft at [beach]" line is the cheaper variant. It keeps most of the benefit.
- The main trade-off is build effort: (c) is the most work of the three, but it's the only one that gets people to a working alert.
