**Greenline watering agent, v1 behavior**

**Promise:** Once automatic watering is on, it waters each zone at dawn unless rain or wet soil says to skip. It never waters outside your town's restrictions, never changes those restrictions, and never orders anything.

**Setup (three questions, nothing else asked)**
1. Which zones do you have?
2. What is each one: lawn, beds, or pots?
3. Do you have watering restrictions from your town? If yes, you enter them now. [OPEN: how restrictions are entered and how the user updates them later, since the agent never edits them.]

After setup, the agent restates its understanding in plain words with three example cases, such as: "Lawn is watered at dawn unless rain is forecast above 60% or its soil reads wet. You'll hear from me only about leaks, a sensor offline for more than 24 hours, or a conflict with your restrictions."

**First week: suggest mode**
- Nothing waters.
- Each morning, the home screen shows what it would have done and why. This is not a push notification.
- On day 7, it asks once whether to turn on automatic watering. The question appears next to the week's suggestions and the actual weather. If the user declines, it stays in suggest mode. [OPEN: whether and when it asks again.]

**Daily (automatic mode)**
- Waters each zone at dawn. [OPEN: how dawn is set, by location and time zone.]
- Skips a zone if rain is forecast above 60% or its soil sensor reads wet.
- [OPEN: what happens for a zone with no sensor, and while a sensor is offline for less than 24 hours.]
- The home screen shows one line per day, for example: "Watered lawn 18 min, skipped beds (rain)."

**Home screen**
- Status: running, scheduled, or paused, with last action, its time, and next check.
- Pause is one step from the home screen. Choices: for a day, for a week, until I resume. The paused state is clearly visible. If a scheduled run is skipped while paused, the home screen says what was skipped, without blame, and offers "Resume now" or "Resume on [date]."
- Each run has a Stop control on its line. Stop ends that run. Water already applied is not reversed, and the line says so.

**Manual runs**
- A manual run overrides the schedule and pause. [Proposed: it also overrides the rain and soil skips. Confirm.] It never overrides watering restrictions.
- After a manual run, the agent resumes its plan the next day.

**Notifications**
Push notifications are limited to these kinds:
- **Problem (sends at once, cannot be turned off):**
  - Suspected leak: water flowing while all zones are off. [Proposed: stop all zones and say so in the notification. Requires a flow sensor. Confirm the hardware exists.]
  - Sensor offline for more than 24 hours.
  - Conflict with restrictions. [OPEN: define what counts as a conflict and what the agent does, which is to skip that zone until it is resolved.]
- **Completion (weekly, batched, can be turned off):** the weekly summary, covering runs and skips with reasons.

The day-7 question and the mistake question are in-app prompts, not notifications.

**Mistakes**
- Trigger: the user cancels or overrides the same zone's run twice in a row. [OPEN: whether suggest-mode days count.]
- It asks: "Did [zone] get too much water or too little?"
- It proposes the change in plain words, for example "Beds: 10 min less per run." The change applies only when the user confirms. [Changed from the draft, which had it adjust first.]
- Bounds: [OPEN: step size and limits, for example ±[X] min per run, never above [Y] min.]
- Every change appears in the activity record, with an undo.

**Limits**
- Never waters outside restrictions, including manual runs.
- Never edits restrictions.
- Never orders anything.
- Caps daily water per zone at [OPEN: [X] min]. A stuck valve or a misread sensor must not run a zone for hours.

Notes: [OPEN] items need a product or engineering decision before build. I proposed defaults where the draft was silent, and bracketed numbers are placeholders, not tested values.
