I'd make these changes, in this order. The first four are small and fairly safe to ship without testing. The fifth is the biggest change.

**1. Save settings automatically and drop the Save button.**
- Each toggle or field applies as soon as it changes, and the "Discard changes?" popup goes away.
- For number fields, commit when the field loses focus or the user taps Done, not on every keystroke. Otherwise a half-typed threshold like "3" (on the way to "35") could trigger alerts.
- Show a brief "Saved" indicator or an Undo snackbar so people can see it worked.
- Today's flow makes people hold unsaved state in their heads, and the discard popup punishes them for it.

**2. Remove the "Are you sure?" on the temperature unit.**
- It's trivially reversible, so the prompt only adds doubt.
- Store thresholds in one canonical unit and convert for display. Switching units then never changes what an alert means.
- Keep confirmations for actions that can't be undone, like Reset.

**3. Turn on sensible alerts for new hives.**
- Make the defaults conservative, such as hive temperature out of range, a sharp weight drop (possible swarm), and low battery. Only enable alerts for sensors the hive actually has.
- During add-hive, show the defaults as a short checklist ("We'll alert you about: …") that people can adjust.
- Ask for notification permission at that moment, when the reason is obvious.
- Keep the defaults to a few high-value alerts. Turning everything on would cause alert fatigue, and then people would mute the app.

**4. Rework Reset.**
- Move it to the bottom of an "Advanced" section, well away from the primary controls.
- Rename it to say what it does. If it only resets alert thresholds, call it "Reset alert thresholds to recommended."
- Give it a specific confirmation that names what will be lost. Better still, split it into scoped resets, like one per section.

**5. Reorganize the 38 controls by task instead of by when engineering added them.**
- The top level should be about 5–7 rows that lead to sub-screens:
  - **Hives:** per-hive alerts and sensors.
  - **Alerts and notifications:** with thresholds shown inside each alert, not as separate fields far away.
  - **Units and display**
  - **Sync and devices**
  - **Account**
  - **Advanced:** Reset, diagnostics.
- Put per-sensor notification toggles next to that sensor's threshold. A threshold and its on/off switch should never be on different parts of the page.
- On number fields, add the unit, a valid range, and a "Recommended: X" hint. Most beekeepers won't know what a good humidity threshold is.
- Plain-language labels help, for example "Tell me if the hive gets too cold" instead of "Temp low threshold."

**Reducing risk without user testing**
- **Check what you already have first.** Tag the "confusing" reviews and support tickets by which part of settings they mention, and look at analytics for where people exit, how often the discard popup appears, and how many hives end up with zero alerts. That tells you whether the changes above match the real complaints. I haven't seen the reviews, so I'm assuming settings is the main source.
- **Do an in-house sort.** Have 3–5 people who don't work on the app (not testing, just sorting) put the 38 items into groups. Compare the groups to your proposed structure.
- **Stage the rollout.** Ship behind a flag to 10–20% of users and watch these metrics:
  - Support contacts about settings.
  - Reset taps.
  - Share of new hives with at least one alert on.
  - Alert mute rate, to catch the new defaults being too noisy.
- **If time is short,** do 1–4 now and the regrouping in the following release. Autosave and sensible defaults will likely remove the most friction.
