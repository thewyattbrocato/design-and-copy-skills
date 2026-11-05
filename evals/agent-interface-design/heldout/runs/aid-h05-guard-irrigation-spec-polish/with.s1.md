**Greenline watering agent, v1 behavior**

**Promise:** While you're away, Greenline waters your zones at dawn within your town's restrictions. It never waters outside them, never edits them, and never orders anything.

**Setup**
Three questions only:
1. Which zones do you have?
2. What is each one (lawn, beds, pots)?
3. Do you have watering restrictions from your town? If yes, which days and hours?

Nothing else is asked. When setup ends, Greenline restates its plan in plain words, for example: "I'll water your lawn at dawn on allowed days. I'll skip a zone if rain is forecast above 60% or its soil sensor reads wet." You can correct the plan before anything runs.

**First week: suggest mode**
- Each morning it shows what it would have done and why. Nothing waters.
- After day 7 it asks once whether to switch on automatic watering. It shows the week's suggestions next to the actual weather.
- If you say not yet, it stays in suggest mode and doesn't ask again. You can switch it on from settings at any time.

**Daily run**
- It waters at dawn, inside your restriction windows.
- It skips a zone if rain is forecast above 60% or the soil sensor reads wet.
- The home screen shows its state (running or paused), the next run, and one line for the last run, for example "Watered lawn 18 min, skipped beds (rain)".
- A zone with no sensor uses the forecast only.
- If a sensor is offline, that zone uses the forecast only until the sensor is back. [Assumption: confirm with eng.]

**Interruptions**
It sends a notification only for:
- a suspected leak (water flowing while all zones are off)
- a sensor offline for more than 24 hours
- a conflict with your restrictions

Everything else goes in a weekly summary. The summary lists every run and skip with its reason, puts the doubtful ones first, and includes any adjustments Greenline made. Each notification type can be turned off. The weekly summary day is your choice.

**Control**
- The Pause button is on the home screen. It offers three choices: a day, a week, or until I resume.
- While paused, the home screen clearly shows "Paused until [date or you resume]". It lists any runs that would have happened, and offers Resume now.
- Any run can be stopped from its line on the home screen.
- A manual run always wins over the plan, and the agent picks the plan back up the next day.
- A manual run outside your restrictions shows a warning first. It starts only if you confirm. Greenline never starts one itself. [Needs eng sign-off.]

**Mistakes**
- If you cancel or override the same zone's run twice in a row, Greenline asks whether that zone got too much or too little.
- It adjusts that zone and tells you what it changed, for example "Beds: 12 min → 9 min."
- You can undo the change from that message or from the zone's settings.
- Adjustments stay within your restrictions and within a per-zone maximum run time. [Placeholder: set the limit.]

**Limits**
- Never waters outside your restrictions.
- Never edits your restrictions.
- Never orders anything.
- Never exceeds the per-zone daily maximum run time. [Placeholder.]

**Leaving**
Pause, turn off, and delete are reachable from the home screen. None of them asks for a reason. There is a route to a person from any alert.

---

**What I changed and why**
- **Manual run vs. restrictions.** "A manual run always wins" contradicted "never waters outside restrictions." I made the manual run win over the *plan*, with a warning and confirmation if it breaks restrictions.
- **Gaps I filled.**
  - A plan restatement at the end of setup.
  - A "not yet" outcome on day 7.
  - Sensor fallback behavior.
  - A visible paused state.
  - Undo for adjustments.
  - A run-time cap.
  - A way to leave.

**Open questions for eng**
- When a leak is suspected, does the agent close the valve or only alert?
- How is run duration calculated?
- What should the run-time cap be?
