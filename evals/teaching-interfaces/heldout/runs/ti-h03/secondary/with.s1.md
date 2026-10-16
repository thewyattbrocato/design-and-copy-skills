**Ship (c), the interactive setup.**

- **It teaches the part people get wrong.** The hard part isn't knowing what a swell height or wind limit is. It's combining four settings so the alert fires at the right times. A carousel explains each setting alone, and users can read all four cards and still set the wrong combination.
- **The live preview gives feedback on the actual choice.** Seeing "today, this setup would have fired at 7am" or "no matches this week" shows whether the alert is too strict or too loose before the user saves it. That's the feedback loop the other two options don't provide.
- **It delivers value in the first session.** The user leaves with a working alert, not just an understanding of one. Video and carousels are passive, and first-launch content is often skipped.

**Why not (a) or (b):** Both are cheap, but both depend on users choosing to watch or swipe and then applying what they learned. A 90-second video is also expensive to produce and hard to update when settings change.

**Risks with (c):**
- It's the most work, and the live preview depends on your conditions data being reliable and fast. Check that before committing.
- Handle the empty states: no matching conditions today, no data for a beach, and the user changing settings mid-flow.
- Let users skip it with sensible defaults, so it doesn't become a new onboarding wall.

**Since you have no data yet, measure it from day one:**
- First-session completion rate of the alert setup
- Share of users who create an alert within 7 days
- Edits within 24 hours of creation (a proxy for "the first setup was wrong")
- Alerts that fired vs. were dismissed or turned off

If the preview data isn't dependable enough to build in one sprint, fall back to (b). It's the lowest-risk option, and it can be written in a day.
