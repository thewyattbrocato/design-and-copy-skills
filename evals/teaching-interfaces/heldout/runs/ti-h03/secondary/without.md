**I'd ship (c), the interactive setup with a live preview.**

The part users get wrong is the combination of settings, not what the settings mean. A carousel or video can explain "wind direction limit" well and still leave someone guessing whether 15 knots offshore is a reasonable number for their beach. Only the live preview lets them check the setting against real conditions, which is where the mistake happens. If today's wind would already fail the filter, the preview shows that before they save an alert that never fires.

The other two options are cheaper, but they're passive:

- **(a) The video** has the highest drop-off. Most people skip a 90-second intro on first launch, and what they remember is vague.
- **(b) The carousel** is quick to build and easy to skim. Four cards of explanation still leave the user to apply the settings to their own beach without any feedback.

(c) also gives you the most useful early signal. A completed first alert is a concrete activation event you can measure, which the other two can't give you.

Risks with (c):

- **Length.** Keep it to the four settings and make each step skippable with sensible defaults, so it doesn't feel like onboarding homework.
- **Dependency on live data.** The preview needs location permission and a forecast for the chosen spot. Define a fallback for when either is missing, such as showing the last cached forecast or a plain "conditions unavailable" state with the setup still completable.
- **Build cost.** It's the most work of the three. If that's a real constraint this sprint, the cut that keeps most of the value is a single-screen preview that updates as the user adjusts the swell range and wind limit, without the full step-by-step flow.

Since you have no data, I'd track first-alert creation rate and whether that first alert ever triggers a notification. Those two numbers will tell you more than any of the three could guess in advance.
