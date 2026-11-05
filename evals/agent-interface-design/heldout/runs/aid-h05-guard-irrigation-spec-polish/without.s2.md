Here's a polished version. I tightened the wording and fixed the "until I resume" voice slip, which should be "until the user resumes". I didn't invent behavior to fill gaps. The open questions are listed below the doc so you can resolve them before it goes out.

---

# Greenline watering agent: v1 behavior

**Setup**
Three questions only:
1. Which zones do you have?
2. What is each zone (lawn, beds, or pots)?
3. Do you have watering restrictions from your town?

Nothing else is asked.

**First week (suggest mode)**
For the first 7 days the agent only suggests. Each morning it shows what it would have done and why. Nothing waters. After day 7 it asks once whether to switch on automatic watering, showing the week's suggestions next to the actual weather.

**Daily run**
The agent waters at dawn. It skips a zone if rain is forecast above 60% or the soil sensor reads wet. The home screen shows one summary line, for example: "Watered lawn 18 min, skipped beds (rain)."

**Notifications**
The agent sends a notification only for:
- a suspected leak (water flowing while all zones are off)
- a sensor offline for more than 24 hours
- a conflict with the user's restrictions

Everything else goes in a weekly summary.

**User control**
- **Pause:** The home screen has a Pause button with three choices: one day, one week, or until the user resumes.
- **Stop a run:** Any run can be stopped from its line on the home screen.
- **Manual runs:** A manual run always takes priority over the plan. The agent resumes the plan the next day.

**Learning from corrections**
If the user cancels or overrides the same zone's run twice in a row, the agent asks whether that zone got too much or too little water. It then adjusts the zone and tells the user what it changed.

**Limits**
The agent never:
- waters outside the user's restrictions
- edits the restrictions itself
- orders anything

---

**Open questions for the eng team**
1. **Manual runs vs. restrictions:** "A manual run always wins" conflicts with "never waters outside restrictions." Does a manual run bypass restrictions, or does it warn or block?
2. **Setup vs. data needs:** Setup asks only three questions, but the forecast needs a location and the soil check needs sensors. Where do those come from (account, device, or permissions)? What happens to a zone with no sensor?
3. **"Override":** What counts as an override: a manual run on that zone, a changed duration, or something else? Does a pause count?
4. **Adjustment mechanics:** What does "adjusts" change (duration, frequency, or both), and by how much?
5. **Rain rule:** Over what window is the 60% rain chance measured: the day, the next 24 hours, or the next 12?
6. **Declined auto mode:** If the user says no after day 7, does the agent keep suggesting, and does it ask again?
7. **Suggest mode alerts:** Do leak, sensor and restriction alerts fire during the first week? I assumed yes.
8. **Paused state:** Do alerts still fire while the agent is paused? I assumed leaks should.
