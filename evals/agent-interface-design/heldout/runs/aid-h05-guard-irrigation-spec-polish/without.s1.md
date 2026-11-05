Here's the polished version. Below it are two contradictions I didn't resolve, because they're product decisions.

---

# Greenline watering agent: v1 behavior

**Setup**
Setup asks three questions and nothing else:
1. Which zones do you have?
2. What is each zone (lawn, beds, or pots)?
3. Do you have watering restrictions from your town?

**First week (suggest mode)**
- For the first 7 days the agent only suggests. Each morning it shows what it would have done and why. Nothing waters.
- After day 7 it asks once whether to switch on automatic watering. It shows the week's suggestions next to the actual weather.

**Daily run**
- The agent waters at dawn.
- It skips a zone if the rain forecast is above 60% or the soil sensor reads wet.
- The home screen shows a one-line summary, for example: "Watered lawn 18 min, skipped beds (rain)".

**Notifications**
The agent sends a notification only for:
- a suspected leak (water flowing while all zones are off)
- a sensor offline for more than 24 hours
- a conflict with the user's restrictions

Everything else goes in a weekly summary.

**User control**
- The home screen has a Pause button with three choices: one day, one week, or until the user resumes.
- The user can stop any run from its line on the home screen.
- A manual run always takes priority over the agent's plan. The agent resumes the plan the next day.

**Learning from corrections**
If the user cancels or overrides the same zone's run twice in a row, the agent asks whether that zone got too much or too little water. It then adjusts the zone and tells the user what it changed.

**Limits**
The agent never:
- waters outside the user's restrictions
- edits the restrictions itself
- orders anything

---

**What I changed**
- Rewrote "until I resume" as "until the user resumes", since the rest of the doc is third person.
- Split the setup questions into a list.
- Made the headings parallel and the sentences more direct.
- Left the substance alone.

**Questions for the eng team**
1. **"A manual run always wins" conflicts with "never waters outside restrictions."** What happens if the user starts a manual run during a restricted window? Either the restriction wins and the app warns the user, or the user can override it. This is also probably the "conflict with restrictions" notification, so it's worth stating explicitly.
2. **Setup doesn't ask about soil sensors, but the daily rule depends on them.** Say what happens for zones with no sensor (forecast only, presumably). Also say how run duration, like the "18 min" in the example, is determined, and what "adjusts" means after two overrides.

I can add a draft answer to either question if you tell me which way you want to go.
