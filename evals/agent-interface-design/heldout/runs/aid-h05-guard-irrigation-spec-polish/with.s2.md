**Greenline watering agent, v1 behavior**

While you're away it waters your zones at dawn within your town's rules. It never waters outside your restrictions, never edits them, and never orders anything.

**Setup**
Three questions, nothing else:
1. Which zones do you have?
2. What is each one (lawn, beds, pots)?
3. Do you have watering restrictions from your town? If so, what are they?

Before anything goes live, the agent restates what it understood. Example: "Lawn waters at dawn on allowed days. Beds skip when rain is likely. Pots follow the same rules."

**First week: suggest mode**
- Each morning it shows what it would have done and why. Nothing waters.
- After day 7 it asks once whether to switch on automatic watering. It shows the week's suggestions next to the actual weather.
- If the user says no, it stays in suggest mode and doesn't ask again. The user can switch on automatic watering at any time from settings.

**Daily**
- It waters at dawn.
- It skips a zone if the chance of rain in the forecast is above 60%, or if the soil sensor reads wet.
- Each run has a maximum length per zone: [value to be set by eng].
- The home screen shows one line, for example "Watered lawn 18 min, skipped beds (rain)". It also shows whether the agent is running or paused, and when it next checks.

**Interruptions**
Only three things send a notification:
- A suspected leak: water flowing while all zones are off.
- A sensor offline for more than 24 hours.
- A conflict with the user's restrictions.

Everything else goes in a weekly summary. The summary lists every run and every skip with its reason.

**Control**
- Pause is a button on the home screen. It offers three choices: a day, a week, or until I resume.
- While paused, the home screen clearly says "Paused" and when it ends. The three notifications above still go out.
- Any run can be stopped from its line on the home screen.
- A manual run always wins, and the agent picks the plan back up the next day. The agent never starts a run outside the restrictions. If a manual run falls outside them, the user gets the restriction-conflict notification, but the run isn't blocked.

**Mistakes**
If the user cancels or overrides the same zone's run twice in a row, the agent asks whether that zone got too much or too little, then adjusts. It tells the user what it changed (for example, "Beds: 12 min → 9 min") and offers a one-tap undo.

**Limits**
- It never waters outside the user's restrictions.
- It never edits the restrictions itself.
- It never orders anything.

Two things the spec leaves open that eng will ask about:
- What the agent does on a suspected leak: notify only, or also shut off the water.
- What it does for a zone with no soil sensor, or whose sensor has been offline for more than 24 hours: forecast only, or skip the zone.

I added the per-run maximum as a placeholder rather than picking a number.
