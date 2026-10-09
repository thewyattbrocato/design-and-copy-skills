**Ship (c), the interactive setup with a live preview.**

**Why**

1. **The problem is about relationships, not vocabulary.** Users probably don't fail because they don't know what "wind direction limit" means. They fail because they can't tell what a good value looks like. Is 3–5 ft right for my beach? Does offshore mean 90° or 270° here? A video or carousel defines the terms. A live preview shows what a setting does: "with these settings, today would be a match" or "this would never fire."

2. **It's the only option where the user ends up with a working alert.** (a) and (b) are passive. People skip, swipe through, and forget, and then still have to do the hard part from memory. In (c), the explanation and the task are the same step. The user finishes onboarding with the thing they came for.

3. **It gives you the data you currently lack.** You can instrument each step. You'll see where people drop off, which settings they change after seeing the preview, and how many finish with an alert. Neither (a) nor (b) tells you much beyond "viewed" or "skipped."

4. **The other two are weak at first launch.** A 90-second video asks for attention before the user has any context, and most people skip it. Carousels are the most commonly skipped onboarding pattern, and four cards of definitions get forgotten by the time the user reaches the form.

**Caveats**

- (c) is almost certainly the most expensive of the three. It needs a flow, a conditions fetch, and a preview that evaluates the settings. If your engineering estimate says it can't ship this sprint, (b) is the fallback. It's cheap and low risk, but I'd expect it to help least.
- Keep the first version small. Use one spot, sensible defaults pre-filled from the chosen beach (for example, offshore direction from the coastline orientation), and a single "would this fire today?" indicator. Don't build a rich forecast visualization yet.
- Add a skip option. Experienced surfers will find a forced flow annoying.
- My recommendation rests on reasoning about the mechanics, not on your data. Instrument it from day one, and if completion or first-alert-created rates are poor, that's your signal to revisit.
