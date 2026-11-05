# Greenline watering agent: v1 behavior

**Setup**

The agent asks three questions and no others:
1. Which zones do you have?
2. What is each zone: lawn, beds, or pots?
3. Do you have watering restrictions from your town?

**First week (suggest mode)**

For the first 7 days the agent runs in suggest mode. Each morning it shows what it would have done and why. Nothing waters.

After day 7 it asks once whether to turn on automatic watering. The question shows the week's suggestions next to the actual weather.

**Daily operation**

- It waters at dawn.
- It skips a zone if the forecast chance of rain is above 60%, or if the soil sensor reads wet.
- The home screen shows one summary line, for example: "Watered lawn 18 min, skipped beds (rain)."

**Notifications**

The agent sends a notification only for:
- A suspected leak: water flowing while all zones are off.
- A sensor offline for more than 24 hours.
- A conflict with the user's watering restrictions.

Everything else goes in the weekly summary.

**Control**

- The home screen has a Pause button with three choices: pause for a day, pause for a week, or pause until the user resumes.
- Any run can be stopped from its line on the home screen.
- A manual run takes priority over the scheduled plan. The agent resumes its normal plan the next day.

**Corrections**

If the user cancels or overrides the same zone's run twice in a row, the agent asks whether that zone got too much or too little water. It then adjusts and tells the user what it changed.

**Limits**

The agent:
- Never waters outside the user's restrictions, including during manual runs.
- Never edits the user's restrictions.
- Never places an order for anything.

---

**What I changed**
- Reorganized into sections so eng can find each rule quickly.
- "Rain is forecast above 60%" became "the forecast chance of rain is above 60%," since the original was ambiguous about what was being forecast.
- "Never orders anything" became "never places an order," which is clearer.
- "Picks the plan back up the next day" now says what the agent does after a manual run.
- Added "including during manual runs" to the restrictions limit. The original had "manual run always wins" and "never waters outside restrictions," which conflict. I resolved it in favor of restrictions. If that's wrong, change the limit and tell me.

**Open questions to settle before sending**
1. **Manual runs vs. restrictions:** I resolved this as above. Confirm it.
2. **"Twice in a row":** Does this mean two consecutive scheduled runs of the same zone, or two consecutive days? Does a cancel made through Pause count?
3. **Rain boundary:** Is the threshold "above 60%" or "60% or higher"? The current text leaves exactly 60% unspecified.
4. **Manual run and the schedule:** Does a manual run replace that zone's scheduled run for the day, or add to it?
