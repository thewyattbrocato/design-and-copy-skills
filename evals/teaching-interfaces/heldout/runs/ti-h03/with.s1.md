**Build (c), the interactive setup with a live preview of today's conditions.**

**Why**

- **It's the only option where users do the task.** People learn a setup by doing it. (a) and (b) ask them to remember four settings and apply them later, when they're at the real form. (c) has them make their first alert and get feedback as they go.
- **The live preview shows what each setting does.** Height range, wind direction limit and time window are abstract until you see them applied. "Wind limit: offshore only" is hard to picture. "Today at [beach], this alert would fire from 6–9am and not after, because wind turns onshore" is clear. The preview explains each setting using the user's own beach.
- **The video and carousel come before the product and teach by exposure.** The 90-second video is also the worst fit. It can't be skimmed, many people will skip it or watch it with the sound off, and it can't be fixed once it ships. The carousel is cheaper, but it is still a benefits-style tour that people swipe through to get to the app.
- **It's the safest pick when you have no data.** (a) and (b) only pay off if users watch or read, then remember, then apply it correctly. (c) has the fewest of those assumptions. If it underperforms, the user still ends up with a working first alert, which is the outcome you want.

**Design notes**

- Define the goal as "afterwards they can set an alert for their own break that fires when conditions are actually good." Keep everything in service of that sentence.
- Take one setting per step: beach, swell height, wind, then time window. That is four things, but only one at a time, with earlier choices staying visible on screen.
- Make the preview update as each control moves. It should say plainly what the alert would have done today, for example "This would fire at [time window] today" or "This would not fire today because [reason]."
- Offer a sensible default for each setting, such as a typical range for the chosen beach, so no one starts from a blank form. If you show example values, label them as examples and make them easy to replace.
- Add a visible Skip for experienced surfers, and a way to rerun the setup or reach short help later from the alert form.
- Skip the confetti and "You're all set!" screen. End with a line saying what now works, for example "You'll get an alert when [conditions]," and point to the next step.

**Main risk**

(c) costs the most to build, and the preview depends on forecast data being fast and reliable at first launch. If it's slow or fails, the step feels broken. Decide a fallback in advance, for example a static explanation of that setting.

**How to check it**

Since you have no data, measure it instead of guessing. Don't judge it by completion of the setup. Track these:

1. Whether new users create a first alert.
2. Whether that alert is still active, and not edited or deleted within about a week.
3. Whether they create a second alert without the guided setup.

If you can, run it against the current flow for a couple of weeks. Even a handful of 5-minute sessions with new users watching them set up an alert will show which settings still confuse them.
