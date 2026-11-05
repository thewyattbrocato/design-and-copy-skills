# Research Plan: Why Overnight Plow Drivers Turn Off Voice Guidance

## 1. Problem statement

Usage logs show many overnight-shift drivers disable spoken turn-by-turn directions within the first hour. We don't know why. The only explanation so far comes from daytime supervisors, who don't drive the cabs and don't work that shift. Their view ("it's just annoying") is a hypothesis, not a finding.

**Goal:** Find out why drivers turn off voice guidance, decide whether that's a problem, and recommend changes backed by evidence.

**Open question:** Is turning off voice a *symptom* (the voice is badly suited to plowing) or a *reasonable choice* (experienced drivers don't need it)? The fix differs completely, so we need to separate the two.

## 2. Hypotheses to test

| # | Hypothesis | What would support it |
|---|---|---|
| H1 | **Guidance is designed for the wrong task.** Plows follow assigned service routes (often covering every street, with deadheading and repeated passes). The app may give commuter-style directions that conflict with the actual job. | Drivers say prompts are wrong or irrelevant. Mute rates are higher on service-route segments than on transit segments. |
| H2 | **Drivers already know the routes.** The voice adds nothing for veterans. | Mute rates fall with tenure and with how many times the driver has run the route. |
| H3 | **Audio competes with safety-critical audio.** Dispatch radio, the engine, the blade and the hydraulics all add noise. The voice may talk over radio traffic or be inaudible. | Mutes cluster around radio activity. Drivers describe missing or talking over calls. |
| H4 | **Cognitive load and startle.** At night, in whiteout conditions or with low visibility, unexpected speech is distracting or fatiguing. | Mutes cluster in bad weather or in the low-visibility hours. Drivers describe being startled. |
| H5 | **Content and timing problems.** Prompts come too late at plow speeds, repeat too often, mispronounce street names, or announce things that don't matter. | Drivers cite specific bad prompts. Ride-alongs show prompts arriving after the turn point. |
| H6 | **Hardware or setup.** Volume defaults, speaker placement or device differences make the voice unpleasant or unusable. | Mute rates vary by vehicle or device model. |
| H7 | **Setting friction.** Mute is the only control available, so drivers pick it over finer adjustment (volume, fewer prompts, alerts only). | Drivers say they'd keep some voice if they could tune it. |
| H8 | **Supervisors' view: it's annoying.** | Drivers independently describe the voice as irritating, and can say why. |

We'll treat these as competing explanations. More than one is likely true, and the mix may differ between experienced and new drivers.

## 3. Approach

### Phase 1: Mine the data we already have (Week 1–2)
No new fieldwork needed.
- Segment mute events by shift, vehicle, device model, app version, driver tenure, route type, weather, time since shift start, and what the driver was doing at the moment of muting (plowing, deadheading, stopped, mid-prompt).
- Check whether muting is **the first action** in a session, or comes after a specific event, such as a prompt, a reroute or a long stretch of prompts. This distinguishes "never wanted it" from "something set them off."
- Check whether muted drivers still follow the route correctly, via deviations, late arrivals and missed segments. That gives a first read on whether muting causes harm.
- Compare to day shift. If day drivers also mute, the issue isn't specific to nights.
- Check whether any mute events cluster right after a prompt. A pattern of "prompt, then immediate mute" is a strong sign of a specific bad prompt.
- Data caveats to check: Is voice on by default? Does the toggle also affect other audio? Could "muted" include accidental taps or the device being shared between drivers?

### Phase 2: Listen to drivers (Week 2–5)
This is the core of the study. Drivers are the experts on this and haven't been asked.
- **Interviews:** 12–16 overnight drivers, 30–45 minutes each, at shift change or in the yard. Cover a mix of tenure, route type (arterial, residential, hills), and those who mute versus those who keep voice on. Interview some day-shift drivers too for contrast. Ask them to walk through the last time they turned it off. Ask about the radio, route knowledge, and what they do instead. Avoid leading questions like "is the voice annoying?"
- **Ride-alongs:** 4–6 overnight shifts, ideally during real snow events, since conditions are the whole point. Observe without directing: when the voice speaks, what is the driver doing, how do they react, and when do they mute? Note noise, radio traffic and display glare. Ride-alongs need approval from the department and driver consent, and safety rules apply to our observers.
- **Short follow-up survey** (5–7 questions) for the whole overnight roster, to size what we learn from interviews. Keep it anonymous and say clearly it's not tied to performance review.

### Phase 3: Test what we learn (Week 5–8)
- Turn the top candidate fixes into low-cost prototypes. Options might include a "key turns only" mode, quieter or ducking audio around radio traffic, route-type-aware prompts, and a volume or prompt-frequency control in place of an on/off switch.
- Run a small field trial with willing overnight drivers (ideally with an A/B or before/after design). Measure mute rate, time to mute, route adherence and driver-reported satisfaction.
- If winter timing doesn't allow a trial this season, run bench tests in a parked cab with recorded radio and engine noise.

## 4. Stakeholders and ethics
- **Drivers and their union or representatives** should hear about the study before we show up. If drivers suspect the interviews feed discipline or surveillance, we'll get guarded answers. Make it explicit that responses are confidential and that mute logs won't be used to evaluate individuals.
- **Fleet operations and safety** should review the ride-along protocol. We should also decide upfront what we do if we observe an unsafe situation.
- **Daytime supervisors** are still useful for operations context (what the app is meant to do, what complaints reach them). They shouldn't be treated as a proxy for driver experience.

## 5. Success measures
- We can name the top 2–3 reasons for muting, ranked by how many drivers they affect.
- We know whether muting hurts route performance or safety, or is harmless.
- Each recommended change links to a specific finding.
- After any change ships, the early-mute rate drops. Define the target with the team (for example, a share of overnight sessions still on voice after one hour). Keep in mind that a high mute rate isn't automatically bad if the voice is truly unneeded.

## 6. Timeline

| Week | Activity |
|---|---|
| 0 (by Friday) | Plan approved, access and consent requests sent |
| 1–2 | Log analysis, interview guide, recruitment through ops |
| 2–5 | Interviews, ride-alongs during storms, survey |
| 5–6 | Synthesis, prioritized findings and recommendations |
| 6–8 | Prototype and field trial or bench test |
| 8–9 | Final readout, with a ship list and measurement plan |

Ride-alongs depend on weather. We're early in snow season, so if we schedule now we can catch real events, and delays could push this into the next storm cycle.

## 7. Deliverables
1. Log analysis summary (mid-point)
2. Findings report with driver quotes and observation notes
3. Ranked recommendations with expected impact and effort
4. Trial results and a measurement plan for rollout

## 8. Risks
- **Small or unrepresentative sample:** recruit across tenure, route and mute behavior, not just volunteers.
- **Drivers guarded about speaking candidly:** use a neutral interviewer, confidentiality and union buy-in.
- **Weather doesn't cooperate:** keep a bench-test fallback.
- **Logs can't distinguish accidental from deliberate muting:** triangulate with interviews.
- **Fixing the wrong thing:** the plan tests alternatives (H1–H8) before committing to a redesign.

## 9. What I need from you or your boss
- Access to the raw usage logs and the fields available
- Confirmation of who approves driver access and ride-alongs (ops and the union)
- Any budget or time limit on the field trial
- Whether there's a mute-rate target or safety concern leadership already has in mind

I can also shorten this to a one-page version for your boss, or draft the interview guide and survey questions. Which would help most before Friday?
