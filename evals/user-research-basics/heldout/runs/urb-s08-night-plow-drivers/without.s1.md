# Research plan: why overnight plow drivers turn off voice directions

## Background and problem
Usage logs show many overnight-shift drivers disable spoken turn-by-turn within the first hour. So far, the only explanation comes from daytime supervisors, who say the voice is "just annoying." The supervisors don't work the overnight shift or drive the plows, so that's a hypothesis to test, not a finding.

## Goals
1. Explain why overnight drivers turn the voice off.
2. Find out whether turning it off is a problem. It might mean the feature is badly designed, or it might mean drivers don't need it.
3. Recommend changes backed by evidence.

## What we don't know yet
- **Does the voice fit the job?** Plow drivers often run fixed or coverage-based routes, not A-to-B trips. Directions built for "get me there fastest" may be wrong or useless for "cover every street."
- **Is the audio competing with something?** Overnight cabs have the plow engine, the blade and salter, and the dispatch radio. The app voice may talk over radio traffic.
- **Is the voice a safety or fatigue issue?** Drivers might find it startling or distracting at 3am, or it might mask sounds they need to hear.
- **Is it accurate?** Snow can cause GPS drift and closed or unplowed streets. The voice may give bad instructions at the worst times.
- **Is it a defaults or onboarding problem?** The volume, voice, or timing may be wrong, or drivers may not know how to adjust it.
- **Is it an experienced-driver problem?** Veterans who know their routes may find the voice patronizing, while newer drivers might want it.
- **Is it a logging artifact?** Cabs may be shared across shifts, so a setting could carry over from a previous driver. The toggle may also be per-device and not per-user, or the "first hour" may reflect a reset at shift start.

## Phase 1: Log analysis (week 1, desk work only)
- Compare overnight with day and evening shifts: what share turn off voice, and how fast?
- Break down by tenure, route type (fixed vs. dynamic), vehicle or device, and weather and storm severity.
- Check whether the toggle is per-user or per-device, and whether the setting persists between shifts.
- Check what happens before the toggle: a specific instruction, a reroute, a GPS jump, an incoming radio call.
- Check whether drivers turn it back on, and whether they do other things that suggest navigation trouble, like manual re-centering, off-route events, or app restarts.
- Output: a short list of which hypotheses the data supports, rules out, or can't speak to.

## Phase 2: Talk to the people who do the work (weeks 1–3)
- **Overnight ride-alongs:** 4–6 shifts, covering different routes, vehicles, and at least one actual snow event. Observe the cab environment, the radio, and when and how drivers interact with the app. Don't coach or ask questions while they're driving.
- **Driver interviews:** 10–12 drivers, 20–30 minutes, at shift start or end. Mix tenure, route type, and drivers who kept voice on and off. Ask them to walk through their last shift and tell the story of when they turned it off. Don't lead with "is the voice annoying?"
- **Others:** 2–3 dispatchers or overnight supervisors, 1–2 day-shift supervisors (to understand where their view comes from), and a fleet or IT person about cab hardware and audio.
- Have drivers show the app settings and any workarounds they use, such as a phone, paper maps, or memory.

## Phase 3: Synthesis (week 4)
- Cluster findings into causes (e.g., "talks over the radio," "wrong for coverage routes," "unnecessary on known routes").
- Check each cause against the log data to see how many drivers it plausibly affects.
- Separate "voice is badly done" from "voice isn't what these drivers need."

## Phase 4: Test changes (weeks 5–7)
Candidate changes depend on the findings. Examples:
- Voice that ducks or pauses for radio traffic
- Alerts only for exceptions: off-route, hazard, or unfamiliar segments
- A plow-route mode with coverage-oriented prompts
- Better defaults for volume and tone, plus easier one-touch controls
- A chime or visual cue in place of speech

Test the strongest 1–2 options with a small group of overnight drivers, either through a staged rollout or an A/B comparison. Track voice-off rate, off-route events, app use, and driver feedback.

## Success measures
- Better understanding: a ranked list of reasons, with evidence from logs and drivers.
- Lower early voice-off rate, **but only if** drivers also say the voice is useful. Fewer people turning it off isn't a win if they're just tolerating it.
- No increase in off-route events or driver complaints.

## Risks and ethics
- **Drivers may worry the research is about evaluating them.** Say clearly that it's about the app, keep notes unattributed, and bring the union or the drivers' supervisor in early if there's one.
- **Safety:** observers must not distract drivers. Follow the city's ride-along and PPE rules and get approval first.
- **Bias:** supervisors' opinions shouldn't steer interview questions. Interview drivers first.
- **Timing:** it's November 5, so winter storms are close. Book ride-alongs now to catch real snow events, and plan to do some of Phase 2 while Phase 1 is running.

## Deliverables
- Week 1: log-analysis summary
- Week 4: findings report with ranked causes and quotes or clips
- Week 5: recommendations and test design
- Week 7: test results and final recommendation

## What I need from you or your boss
- Access to the usage logs and someone who can explain how the toggle is recorded
- Permission and contacts for overnight ride-alongs and driver interviews
- A point person in fleet or IT for hardware and audio setup
- Whether there's a union or HR approval process
- How much of the timeline is firm, since I've assumed about 7 weeks

I can trim this to a one-page version for your boss, draft the interview guide, or write the log-analysis queries, if that would help before Friday.
