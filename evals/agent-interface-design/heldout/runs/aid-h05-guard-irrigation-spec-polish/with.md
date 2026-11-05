Here's the polished version. I tightened the wording, resolved a few ambiguities, and filled gaps. Anything I added that is a product decision rather than wording is marked **[confirm]**.

---

# Greenline watering agent, v1 behavior

**In one line:** While you're away, it waters your zones at dawn within your town's rules. It never waters outside those rules, never edits them, and never orders anything.

## Setup
Three questions, nothing else:
1. Which zones do you have?
2. What is each one (lawn, beds, pots)?
3. Do you have watering restrictions from your town?

At the end, it restates the plan in plain words with an example, such as "Lawn: dawn, skipped if rain is forecast above 60% or the soil reads wet." You can correct it before it starts.

## First week: suggest mode
- Each morning it shows what it would have done and why. Nothing waters.
- After day 7, it asks once whether to switch on automatic watering. It shows the week's suggestions next to the actual weather.
- If you say no or don't answer, it stays in suggest mode. You can switch to automatic at any time from the home screen. **[confirm]**

## Daily behavior
- It waters at dawn.
- It skips a zone if rain is forecast above 60% or the soil sensor reads wet.
- The home screen shows one line, for example: "Watered lawn 18 min, skipped beds (rain)."

## Notifications
It interrupts you only for:
- a suspected leak (water flowing while all zones are off)
- a sensor offline for more than 24 hours
- a conflict with your restrictions (for example, your restrictions leave no allowed window for a zone's scheduled run)

Everything else goes in a weekly summary. The summary lists each run and skip with its reason, plus any adjustments the agent made. Leak alerts still fire while paused.

## Control
- **Pause** is a button on the home screen with three choices: a day, a week, or until I resume. While paused, the home screen says so, and skipped runs are noted without blame.
- **Stop:** any run can be stopped from its line on the home screen.
- **Manual runs:** a manual run always wins. The agent resumes the plan the next day.

## Mistakes
If you cancel or override the same zone's run twice in a row, the agent asks whether that zone got too much or too little water. It adjusts, tells you what it changed (for example, "Beds: 12 min → 9 min"), and offers an undo.

## Limits
It never waters outside your restrictions, never edits your restrictions, and never orders anything.

---

**Open questions for eng and product**
1. **Run-length cap.** Nothing limits how long a zone can run, and a runaway run is the worst case for a watering agent. Set a maximum per run (I didn't invent a number), and decide whether the agent may shut off water when it suspects a leak or only alert.
2. **Offline sensor.** Should it fall back to forecast-only, or skip that zone, until the sensor returns? The draft doesn't say.
3. **Manual runs vs. restrictions.** I read "never waters outside restrictions" as covering the agent's own runs only. Should a manual run during restricted hours be blocked, warned about, or allowed? **[confirm]**
4. **Leaving.** The draft has no off or delete path. I'd add "turn off automatic watering" to the home screen, with no reason required.
