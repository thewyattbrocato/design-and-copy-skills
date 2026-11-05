# Greenline watering agent: v1 behavior

**What it does:** While you're away, it waters your lawn, beds, and pots at dawn when the soil and forecast allow. It never waters outside your town's restrictions, never edits those restrictions, and never orders anything.

## Setup

Three questions, in this order:

1. Which zones do you have? (one or more, free text)
2. What is each one: lawn, beds, or pots?
3. Do you have watering restrictions from your town? Yes (enter them) / No / Not sure

If the answer is "Not sure," it stays in suggest mode until you confirm the restrictions. *(Proposed.)*

Before week 1 starts, it restates its understanding on one screen: each zone and its type, the restrictions it will respect, and three example cases, such as "Lawn, rain forecast 70% at 5 a.m. → skipped." You confirm or correct it. *(Proposed.)*

## Week 1: suggest mode

- Nothing waters.
- Each morning, the home screen shows what it would have done for each zone and why, such as "Would water lawn 18 min. Soil dry, no rain forecast."
- Leak and sensor-offline notices stay on during suggest mode.
- After day 7, it asks once: "Turn on automatic watering?" The question shows that week's suggestions next to the actual weather for the same days.
  - Yes: automatic watering starts at the next dawn.
  - No: it stays in suggest mode and doesn't ask again unless you turn it on in settings. *(Proposed.)*

## Daily: automatic

- It runs at dawn in your local time zone.
- For each zone, it skips if the forecast rain chance is above 60% or the soil sensor reads wet. Otherwise it waters.
- If the soil sensor is offline (not yet past 24 hours), it uses the forecast alone and marks the line "(no soil reading)." *(Proposed.)*
- The home screen shows one line per day, such as "Watered lawn 18 min, skipped beds (rain)."
- Maximum run time per zone: **TBD**, set by product and eng.

## Interruptions

Only these three send a notification right away:

1. **Suspected leak** (water flowing while all zones are off).
   > "Water is flowing at [time] while all zones are off. I've paused all watering until you check. [Resume]"
   Pauses all scheduled runs until the user resumes. *(Proposed.)*

2. **Sensor offline for more than 24 hours.**
   > "Your [zone] soil sensor hasn't reported since [time]. Until it's back, I'm using the forecast alone."

3. **Restriction conflict** (a scheduled run would break your restrictions).
   > "Your restrictions say [rule]. I've held [zone] watering. I won't change restrictions. Update them yourself and the hold will clear."
   The hold can't be lifted from the app while the conflict stands.

Everything else goes into a **weekly summary** on a day you choose (**TBD**): runs, skips with reasons, sensor readings, and any corrections you made.

## Pause and stop

- **Pause** is on the home screen with three choices: 1 day, 1 week, until I resume. A banner shows "Paused until [date/time]" or "Paused until you resume." A 1-day pause ends at the same time the next day. *(Proposed.)*
- While paused, scheduled runs don't happen. Leak and sensor-offline notices still fire.
- When a scheduled run is skipped because of a pause, the home screen says so without blame ("Paused: skipped today's watering") and offers Resume now.
- **Stop** any run from its line on the home screen. It stops that zone's water at once.
- **Manual run** always wins: it starts now and replaces that zone's scheduled run for the day. It is allowed during a pause and doesn't end the pause. Restrictions still apply to manual runs. *(Proposed.)*
- After that, the schedule picks back up at the next dawn.

## Corrections

- The agent counts a stop or manual override of the same zone's scheduled run. After two in a row for the same zone (two consecutive scheduled runs), it asks:
  > "You've stopped lawn watering twice in a row. Did I water too much, too little, or was this just one time?"
  - **Too much:** reduces that zone's run time by **TBD**%.
  - **Too little:** increases it by **TBD**%.
  - **Just this time:** no change.
- It shows the new value before saving, then tells you what changed and offers Undo.

## Limits

- It never waters outside your restrictions. If they're unknown ("Not sure"), it doesn't water automatically.
- It never edits your restrictions.
- It never orders anything or buys supplies.
- It never contacts anyone but you.
- Water already applied can't be undone. The activity record shows what ran and when.

---

*Changes: added the setup restatement, pause and manual-run rules, a defined correction trigger with a "just this time" option, and what the leak and restriction notices do. Items marked TBD need product decisions before eng builds them: forecast time window, run-time cap, adjustment size, summary day, and how location and time zone are obtained.*
