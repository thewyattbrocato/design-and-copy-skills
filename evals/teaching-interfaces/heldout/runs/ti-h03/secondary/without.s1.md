**Build (c), the interactive setup with a live preview.**

The mistake new users make is choosing values, like a swell range that never fires or a time window that misses the good hours. Only (c) helps with that directly. The user sets each value while seeing what it would have done today, for example "this range would have matched 0 of today's 3 windows." That teaches the tradeoff in context, and it gets the user to a working alert before they leave.

Why not the other two:

- **(a) Intro video:** Passive, 90 seconds is a lot to ask of someone who just opened the app to check waves, and it's watched once and forgotten. It explains settings without showing their effect on the user's beach.
- **(b) Swipe carousel:** Cheaper and less intrusive, but it explains each setting in the abstract. Users often swipe through it and still face the same blank form. It's the best fallback if (c) doesn't fit the sprint.

Risks with (c) to plan for:

- **Live data dependency.** If conditions fail to load on first launch, the preview breaks. Show cached or last-known conditions, or a clear fallback state.
- **Empty previews feel like failure.** "No matches today" can read as the app being broken. Phrase it as "this setting would have skipped today's surf," and show the nearest-match option.
- **Drop-off.** Keep it to four short steps, pre-fill sensible defaults for the beach, and let users skip to "use recommended settings."
- **Cost.** It's the largest build of the three. Scope it to one spot and one alert type first.

Since you have no data, run a cheap check before or during the build. Watch the share of new users who create a first alert within 24 hours and whether that alert fires within the first week. Five or six interviews with surfers who've used the app would also show whether they understand "wind direction limit" without help. If (c) is too big for the sprint, ship (b) and use the same metrics to decide whether (c) is worth the next one.
