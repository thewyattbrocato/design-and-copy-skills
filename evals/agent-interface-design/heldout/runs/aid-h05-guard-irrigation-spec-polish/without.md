Here's the polished version, followed by what I changed and what I left open.

---

# Greenline watering agent: v1 behavior

**Setup**
Setup asks three questions and nothing else:
1. Which zones do you have?
2. What is each zone (lawn, beds, pots)?
3. Do you have watering restrictions from your town?

**First week (suggest mode)**
- For the first 7 days the agent only suggests. Each morning it shows what it would have done and why. Nothing waters.
- After day 7 it asks once whether to switch on automatic watering. It shows the week's suggestions next to the actual weather.

**Daily run**
- The agent waters at dawn.
- It skips a zone if rain is forecast above 60% or the soil sensor reads wet.
- The home screen shows a one-line summary, for example: "Watered lawn 18 min, skipped beds (rain)".

**Notifications**
The agent sends a notification only for:
- a suspected leak (water flowing while all zones are off)
- a sensor offline for more than 24 hours
- a conflict with the user's restrictions

Everything else goes in a weekly summary.

**User control**
- **Pause:** a Pause button on the home screen offers three choices: one day, one week, or until the user resumes.
- **Stop:** any run can be stopped from its line on the home screen.
- **Manual runs:** a manual run always takes priority over the agent's plan. The agent resumes the plan the next day.

**Learning from corrections**
If the user cancels or overrides the same zone's run twice in a row, the agent asks whether that zone got too much or too little water. It then adjusts the zone's schedule and tells the user what it changed.

**Limits**
The agent never:
- waters outside the user's restrictions
- edits the restrictions itself
- orders anything

---

**What I changed**
- I reformatted it into headed sections with lists, so engineers can scan it.
- I fixed "until I resume" to "until the user resumes". It was the only first-person slip.
- I renamed "Interruptions" to "Notifications" and "Mistakes" to "Learning from corrections", since those names say what the sections cover.
- I made "a day, a week" explicit as one day and one week.
- I made "adjusts" more specific: it adjusts that zone's schedule.
- I added the "(suggest mode)" label and kept the wording otherwise.

**Open questions to settle before sending**
1. **Setup says "nothing else is asked", but the agent needs a location for the forecast.** Should that come from the device or account? The spec should say so, along with how sensors get paired.
2. **A manual run "always wins", but the agent "never waters outside restrictions".** Does a manual run override the restrictions? If it does, the limit is no longer absolute. If it doesn't, the manual run should trigger the restriction-conflict notification.
3. **The rain rule needs a time window.** Is it above 60% today, or over the next 24 hours?
4. **What happens to a zone with no soil sensor?** Presumably only the forecast rule applies.
5. **A pause covers scheduled runs.** Can it also suppress notifications such as a leak alert? I'd suggest it shouldn't.
6. **"Cancels or overrides" needs a definition.** Does a manual run on that zone count as an override?

I left these as questions because they're product decisions, and I didn't want to guess the answers.
