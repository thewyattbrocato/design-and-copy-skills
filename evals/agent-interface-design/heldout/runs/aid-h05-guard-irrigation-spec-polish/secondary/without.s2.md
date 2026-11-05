# Greenline watering agent: v1 behavior

**Setup**
Setup asks three questions only:
1. Which zones do you have?
2. What is each zone? (lawn, beds, or pots)
3. Do you have watering restrictions from your town?

Nothing else is asked.

**First week (suggest mode)**
The agent runs in suggest mode. Each morning it shows what it would have watered and why. Nothing waters during this period.
After day 7, it asks once whether to turn on automatic watering. The question shows the week's suggestions next to the actual weather.

**Daily operation**
- The agent waters at dawn.
- It skips a zone if the chance of rain is forecast above 60%, or if the soil sensor reads wet.
- The home screen shows one line per day, for example: "Watered lawn 18 min, skipped beds (rain)."

**Notifications**
The agent sends a notification only for:
- A suspected leak (water flowing while all zones are off)
- A sensor offline for more than 24 hours
- A conflict with the user's town watering restrictions

Everything else goes into a weekly summary.

**Pause and manual control**
- The home screen has a Pause button with three options: for a day, for a week, or until resumed.
- Any run can be stopped from its line on the home screen.
- A manual run takes priority over a scheduled run. The scheduled plan resumes the next day.

**Corrections**
If the user cancels or overrides the same zone's run twice in a row, the agent asks: "Did this zone get too much or too little water?" It then adjusts that zone's schedule and tells the user what it changed.

**Limits**
- The agent never waters outside the user's town watering restrictions.
- The agent never edits those restrictions.
- The agent never orders anything.

---

**What I changed**
- Made the setup and first-week sections state the rules directly instead of using fragments.
- Changed "above 60%" to "the chance of rain is forecast above 60%" so the threshold is clear.
- Standardized on "until resumed" (the original mixed "until I resume" with "resume").
- Clarified the manual-run rule. "Picks the plan back up the next day" was ambiguous, so it now says a manual run takes priority and the scheduled plan resumes the next day.
- Rewrote the mistake rule so the question and the action are explicit.
- Made "restrictions" consistently "town watering restrictions."

**Open items for the eng team**
- **Pause vs. manual run:** The spec doesn't say whether a manual run is allowed during a pause. I'd suggest allowing it, since the user chose to run it, but you should confirm.
- **"Never orders anything":** This is ambiguous. I assume it means no purchases or supply orders. If it also means the agent can't reorder supplies in any form, say so explicitly.
- **Threshold boundary:** I kept "above 60%," so exactly 60% still waters. Confirm that's intended.
