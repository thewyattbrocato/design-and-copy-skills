**Ship (c), the interactive setup.** It's the only option that teaches by doing, and the mistake you're describing is a comprehension problem.

- **It's the only option that teaches through the thing the user cares about.** A swell range, wind limit, and time window are abstract until you see them against real conditions. A live preview that says "Today this would have matched: no, swell is 1.2 ft, you asked for 2–4 ft" shows what each setting does. A carousel or video describes the settings but never shows their effect on this beach today.
- **It ends with a working alert.** The video and carousel finish with a user who understands the feature and still has to build an alert, which is where they currently go wrong. The interactive flow finishes with the alert set up.
- **Passive content is the weakest format for this.** Intro videos are commonly skipped on first launch, and four cards of settings text mostly get swiped past. Neither gives you feedback if the user is confused.

Risks to plan for:

- **Live preview is the expensive part.** It needs reliable forecast data for the chosen beach at setup time. If that's not solid yet, a simpler version works: fixed defaults, one screen per setting, and a preview that uses the last 7 days of data to show "this alert would have fired on 3 of the last 7 days."
- **It can add friction.** Keep it to the four settings, pre-fill sensible defaults, and let the user skip to a default alert at any point.
- **Empty previews are fine.** If today's swell doesn't match, that's useful information. Just word it as "no match today" rather than as an error.

Since you have no data yet, instrument it from day one: first-launch to first-alert-saved rate, the rate of users who skip setup, and whether the alert ever fires or gets edited within a week. That tells you in a few weeks whether it's working. If the new flow's completion rate is poor, the cheapest fallback is a short "what does this setting mean?" help link on each field, not one of the other two options.
