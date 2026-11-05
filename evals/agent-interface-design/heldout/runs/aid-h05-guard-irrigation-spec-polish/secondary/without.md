# Greenline Watering Agent: v1 Behavior

**Setup**

The agent asks three questions and no others:
1. Which zones do you have?
2. What is each zone? (lawn, beds, or pots)
3. Do you have watering restrictions from your town?

**First week: suggest mode**

- The agent runs in suggest mode. Nothing waters.
- Each morning, it shows what it would have watered and why.
- After day 7, it asks once whether to turn on automatic watering. The question shows the week's suggestions next to the actual weather.

**Daily operation**

- The agent waters at dawn, local time.
- It skips a zone if rain is forecast above 60% or the soil sensor reads wet.
- The home screen shows one line per day, for example: "Watered lawn 18 min, skipped beds (rain)."

**Notifications**

The agent sends a notification only for:
- A suspected leak (water flowing while all zones are off)
- A sensor offline for more than 24 hours
- A conflict with the user's watering restrictions

Everything else goes into a weekly summary.

**Pause and control**

- The home screen has a Pause button with three options: for one day, for one week, or until the user resumes.
- Any run can be stopped from its line on the home screen.
- A manual run takes priority over the agent's scheduled run for that zone. The agent resumes its plan the next day.

**Corrections**

If the user cancels or overrides the same zone's run two times in a row, the agent asks whether that zone got too much or too little water. It then adjusts and tells the user what it changed.

**Limits**

The agent:
- Never waters outside the user's restrictions
- Never edits the restrictions
- Never orders or buys anything

---

**Changes I made**

- Tightened the wording in each section and made the sentences parallel.
- Clarified "at dawn" as local time.
- Clarified that a manual run overrides only that zone's scheduled run for that day.
- Changed "cancels or overrides the same zone's run twice in a row" to "two times in a row," since the original could be read as two different days or two different actions.
- Changed "orders anything" to "orders or buys anything" to cover purchases as well.

**Gaps eng will likely ask about (not in the doc)**

1. **Soil sensor setup.** The leak, sensor-offline, and wet-soil rules all depend on a soil sensor, but setup never asks whether the user has one. Should setup ask, or should the agent run without wet-soil checks if there isn't one?
2. **Declining automatic watering.** What happens if the user says no after day 7? Does the agent stay in suggest mode?
3. **Weekly summary timing.** What day and time does it arrive?
4. **Rain threshold.** Is it "above 60%" or "60% or higher"? I kept "above 60%" as written.
5. **Pause in suggest mode.** Does the Pause button apply during the first week? Nothing waters then, so it may not matter, but the behavior should be stated.

If you tell me the answers, I'll fold them into the doc.
