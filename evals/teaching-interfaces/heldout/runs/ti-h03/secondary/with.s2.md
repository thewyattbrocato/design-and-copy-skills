**Ship (c), the interactive setup with a live preview.**

- **It teaches the thing people get wrong.** Users misconfigure alerts because the settings interact. A 3 ft swell limit means little until you see that today's swell is 4 ft and the wind would block it anyway. A live preview shows that relationship with real numbers. A video or carousel can only describe it.
- **Passive intros get skipped or forgotten.** By the time a user reaches the alert screen, a 90-second video or four cards has faded. The user has to remember the explanation while making the choice, which is hard. Building the alert while looking at real conditions avoids that.
- **Videos go stale.** Beach names, conditions, and UI change. The live preview uses current data, so it stays accurate without re-shooting or rewriting copy.
- **The carousel is the cheapest option, but it's the easiest to ignore.** If you want a fallback, a short version of (b) could be placed inside (c)'s steps as inline help.

**The risks with (c):**
- It's the most work. If the sprint is tight, cut it to three steps and a static preview of the last 24 hours' conditions at the chosen beach. Skip the live forecast.
- The preview has to handle bad cases: a flat day, no data for the beach, or a time window with no forecast. Each needs a clear message, or new users will think the app is broken.
- Users may still change the defaults after the first alert. That's fine, but it means the setup has to explain what each setting does, not only pick values.

**This is a reasoned choice, not a measured one.** You have no data, so the case for (c) rests on how the mistake happens, not on evidence that it converts better. To check it after shipping, track:
1. Share of new users who create an alert in their first session.
2. Share of first alerts edited or deleted within 7 days. This is your best proxy for misconfiguration.
3. Whether a small group that sees the old flow does worse on those two numbers.

If you can't ship a test group, at least record these metrics before launch so you have a baseline.
