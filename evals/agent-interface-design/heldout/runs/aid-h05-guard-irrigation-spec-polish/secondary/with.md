# Greenline watering agent: v1 behavior

**What it does, and never does:** While you're away, Greenline waters your zones at dawn and skips any zone that is too wet from rain or soil moisture. It never waters outside your restrictions, never edits your restrictions, and never orders anything.

## Setup

Three questions, and no others:

1. Which zones do you have?
2. What is each zone: lawn, beds, or pots?
3. Do you have watering restrictions from your town?

After the third answer, Greenline shows a one-screen summary of what it understood (zones, types, restrictions, dawn schedule). This is a display only, with no further questions. Restrictions are stored as entered. Greenline reads them and never writes them.

## First week: suggest mode

- Nothing waters automatically during days 1 to 7.
- Each morning, the home screen shows what Greenline would have done that day and why. These suggestions do not send notifications.
- After day 7, Greenline asks once whether to switch on automatic watering. The question shows the week's suggestions next to the actual weather for the same days.
- If you say no, Greenline stays in suggest mode and does not ask again. *(Assumed; confirm.)*

## Daily: automatic mode

- Greenline waters each zone at dawn.
- It skips a zone if either of these is true:
  - Forecast chance of rain is above 60%.
  - The soil sensor reads wet.
- The home screen shows one line per day, with the reason for each skip, for example: "Watered lawn 18 min, skipped beds (rain)."

## Notifications

Greenline sends a notification only for:

1. **Suspected leak:** water is flowing while all zones are off.
2. **Sensor offline:** the soil sensor has been offline for more than 24 hours.
3. **Restriction conflict:** a scheduled run falls inside your restrictions. Greenline does not run it and tells you why.

Everything else goes into the weekly summary. The summary includes watering totals, every skip with its reason, a list of skipped runs so you can see what was missed, pauses, manual runs, and sensor status.

## Control

**Pause** (home screen button). Choices: a day, a week, or until I resume.
- *Assumed:* a day is 24 hours from when you choose it, and a week is 7 days.
- While paused, the home screen shows a persistent "Paused until ___" banner. Runs skipped during a pause are labeled "Paused" and do not blame the user.
- Resume is a button on the same banner.

**Stop a run.** Any run can be stopped from its line on the home screen. This stops only that run. The next scheduled run still happens. *(Assumed.)*

**Manual run.** A manual run always wins. If you start a zone manually, that zone's scheduled run for that day is skipped. Greenline resumes its plan the next day.

## Mistakes

If you cancel or override the same zone's run twice in a row:

1. Greenline asks: did this zone get too much water or too little?
2. It adjusts that zone's run length.
3. It tells you what it changed, for example: "Beds: 12 min to 9 min."

*(Assumed: a run you did not cancel or override resets the count. Stopping a run from its line counts as a cancel.)*

## Open questions

These need decisions before build:

1. **Rain forecast:** which time window, and which data source?
2. **Soil sensor:** what reading counts as "wet"? While the sensor is offline (under 24 hours), does Greenline water on schedule or skip?
3. **Leak:** does Greenline only notify, or also shut off the water?
4. **Restriction conflict:** what exact rule defines a conflict?
5. **Weekly summary:** which day and time?
6. **Pause:** can a manual run happen during a pause?
7. **Suggest mode:** can you run a zone manually in suggest mode? Does that count as an override?
8. **Corrections:** how large is each adjustment, and what are its limits? Is it applied immediately or after you confirm? What happens if you answer "neither"?
9. **Turning on later:** after declining automatic watering on day 7, how do you turn it on? How do you edit your restrictions? (You can, Greenline can't.)
