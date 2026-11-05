**Ship (c), the interactive setup with a live preview.**

**Why**

1. **It teaches by doing.** The goal is that a new user can finish a spot alert that fires when they'd want to surf. In (c) they build their real first alert, so the onboarding and the task are the same thing. (a) and (b) both put explanation before the task and rely on people remembering it. Four settings plus a video is a lot to hold in memory.

2. **The live preview teaches what the text can't.** "Swell 3–5 ft, wind limit offshore, 6–9am" is abstract. Seeing "today at [their beach], this alert would have fired / wouldn't have, because wind was onshore" shows what each setting does. The feedback is also in their terms, not "Great job!".

3. **It fixes the real problem.** You said people get setup wrong, which is different from not knowing the app exists. A video or carousel explains the settings. A guided flow can also prevent bad choices with sensible defaults, a starting range for the chosen beach, and plain-language labels like "wind that blows onshore" next to the compass limit.

4. **(a) and (b) are the weaker bets.** A 90-second video is passive and easy to skip. It's also costly to produce, hard to update, and needs captions. A 4-card carousel shown before the app opens is the "benefits before product" pattern. It covers four new ideas at once, away from the controls they describe.

**How to build it**

- Order the steps: beach, then swell height, then wind, then time window. Each step has one control, one sentence of context, and the preview updating beside it.
- Keep earlier choices visible as the user goes.
- Put a sensible default on each setting so they can finish in under a minute.
- Add an obvious skip for experienced surfers, and a way to rerun the guide from the alert screen.
- If the preview has no data for a beach, say so plainly. Don't show plausible-looking numbers.

**What to measure, since you have no data**

Don't judge it by completion of the flow. Judge it by:
- the share of new users who create an alert in the first session
- the share who still have that alert enabled after 7 days
- the share who edit or delete it within a day, which suggests they set it up wrong

Run it against your current onboarding as a holdout if you can. That gives you the data you don't have yet, and it will show whether a cheap card or two is worth adding later.

**Assumptions and trade-off**

- I assumed the preview can use forecast or recent data you already have. If it can't, (c) is much more expensive, and (b) becomes the fallback, but with each card placed beside its control rather than shown as a carousel up front.
- (c) costs the most engineering of the three. It's the only one that tests the behavior you care about.
