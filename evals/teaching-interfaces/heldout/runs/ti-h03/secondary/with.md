**I'd ship (c), the interactive setup with a live preview.**

**Why:** New users get alerts wrong because they pick values that don't match how their beach actually behaves, like a swell range that's too narrow or a wind limit that rules out every good session. That's a judgment problem, not a comprehension problem, and only (c) addresses it.

- **The video (a)** explains concepts passively. Users who see it may still set a 0.5 m swell minimum on a beach that only breaks at 1.5 m. Ninety seconds is also long for a first-launch screen, so many people will skip it.
- **The carousel (b)** is better than the video because it's skimmable, but it explains each setting in the abstract. Reading "wind direction limit: choose the offshore range" doesn't tell someone what their beach looks like under that rule.
- **The interactive setup (c)** puts the setting in front of the user with a consequence attached. If they drag the swell minimum up and the preview shows today's 1.2 m swell is now excluded, they learn the tradeoff by doing it. It also finishes with a working alert, which is the outcome you actually want. The other two options end with a user who understands the feature and still hasn't set one up.

**Risks to plan for:**
- **Flat-day preview:** If today has no surf, the live preview looks broken. Show the last 7 days with markers for when the alert would have fired, so there's always something to look at.
- **Build cost:** (c) is the biggest of the three. Keep the first version to the four settings, with sensible defaults so "Create alert" works without any edits.
- **Data dependency:** The preview needs reliable per-beach conditions. If that feed is patchy for some beaches, fall back to the carousel for those.

**Without data, I'd test before committing fully.** Five or six moderated sessions with new users, or a prototype clickthrough, would show quickly whether people can set a sensible first alert. Track one metric to decide later: the share of new users who create an alert in their first session. Use the carousel as the fallback if (c) turns out to be too costly this sprint, since it's the cheapest way to fix the concept gap.
