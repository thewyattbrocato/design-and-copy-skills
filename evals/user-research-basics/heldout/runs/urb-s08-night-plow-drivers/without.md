# Research Plan: Why Overnight Plow Drivers Turn Off Voice Directions

## 1. Background and problem
Usage logs show many overnight-shift drivers disable spoken turn-by-turn directions within the first hour. So far, the only explanation comes from daytime supervisors, who say the voice is "just annoying." Supervisors aren't the users, and they don't work the overnight shift. Their explanation is a hypothesis, not a finding.

**Goal:** Understand why drivers turn off voice guidance, whether that's a problem, and what to change.

## 2. Research questions
1. What is the real pattern? Who turns voice off, when, and how does it differ from day shift and by route type?
2. What are drivers doing and hearing in the cab when they turn it off?
3. Is the voice failing them (wrong content, timing, volume), or is voice the wrong tool for this job?
4. Does turning it off cause problems, such as missed turns, wrong-way entries, or reliance on the screen at night?
5. What change would drivers adopt, and how will we know it worked?

## 3. Hypotheses to test
Each hypothesis predicts something different, so the research can tell them apart.

| # | Hypothesis | What we'd expect to see |
|---|---|---|
| H1 | **Drivers already know the route.** Plow routes are repetitive and assigned, so directions are redundant. | Mute rates fall with route familiarity and with repeat runs. Veterans mute more. |
| H2 | **The voice isn't designed for plowing.** Directions assume A-to-B driving, but plowing means coverage patterns, dead ends, and U-turns. The app may call out turns that don't apply. | Mute follows irrelevant or wrong prompts. Mute rates are higher on coverage routes than on transit or deadhead legs. |
| H3 | **Audio conflicts with safety-critical sound.** Drivers need to hear the radio and dispatch, the engine and blade, the spreader, and warning signals. | Muting follows radio traffic. Drivers describe the voice "talking over" things. |
| H4 | **Overnight context.** Fatigue, a quiet cab, and volume that is fine by day but jarring at 3 a.m. | Mute timing clusters at specific points in the shift. Volume complaints come up. |
| H5 | **Accidental or friction-driven muting.** Gloves, cab vibration, or a bad button location. | Mutes happen right after screen touches. Drivers re-enable it, or don't know it's off. |
| H6 | **Timing and quality.** Prompts arrive late at plow speeds, in snow-covered or unplowed streets, with GPS drift, or with mispronounced street names. | Mutes follow bad prompts. Drivers cite specific incidents. |
| H7 | **Supervisors are right.** It's simply irritating, for example repetitive or too chatty. | Drivers say so unprompted, and a quieter voice or fewer prompts fixes it. |

## 4. Approach
Use mixed methods. The logs tell us what happens, and field research tells us why.

### Phase 1: Analyze existing data (week 1–2)
- Break down mute events by shift, route type, driver tenure, vehicle, weather, time into shift, and prior prompt.
- Check whether the setting is persisted per driver or per session. A logging artifact or default-state bug could explain part of the pattern.
- Compare day shift with overnight shift. Day shift is the baseline.
- Find what happens right before a mute: a prompt, a radio event, or a screen tap.
- Check whether drivers re-enable voice later, and whether routes completed without voice show more deviations or off-route events.
- **Output:** a short list of patterns that sharpens the hypotheses.

### Phase 2: Listen to drivers (week 2–4)
- **Overnight ride-alongs (6–8 sessions):** Observe the full shift, including what's audible, what the driver does with the app, and when and how they mute. Cover a mix of route types, tenures, and vehicles. This is the most important step.
- **Interviews (10–15 drivers):** Ask about their last shift, not about the voice in general. Ask when they last muted it and why. Include drivers who keep it on.
- **Short follow-up diary or text check-in (optional):** Drivers log each time they mute it and why during one week.
- **Supervisor interviews (3–5):** Day and overnight leads, to understand how they see the issue and what operational constraints exist, such as dispatch protocol and radio rules.

### Phase 3: Test candidate fixes (week 4–7)
Choose based on what Phases 1 and 2 show. Possible options:
- Fewer or smarter prompts, such as only on non-obvious turns or deviations
- Plow-specific logic for coverage routes, dead ends, and U-turns
- Ducking or pausing around radio traffic
- Night-specific volume and tone defaults
- A protected mute button or an easier toggle
- Replacing voice with a tone, a visual cue, or haptics

Test with a small group of overnight drivers, either A/B or sequential, and watch both the logs and feedback.

## 5. Success measures
- **Primary:** Voice retention at 1 hour and at end of shift, among overnight drivers.
- **Safety and quality:** Off-route events, missed turns, and driver-reported distraction.
- **Experience:** Driver-rated usefulness, with a short post-shift question.
- **Guardrail:** Retention alone isn't the goal. If drivers know the route and the screen works, voice off may be fine. Forcing it on would be the wrong answer.

## 6. Practical and ethical considerations
- **Driver candor:** Drivers work for the city, and the people asking are tied to management. Make clear that the research is about the app and not about them. Keep interview notes anonymous, don't share individual names with supervisors, and talk to the union rep if there is one.
- **Safety on ride-alongs:** Get city approval, wear required PPE, follow the vehicle's passenger rules, and stay out of the driver's way. Don't distract them during operation.
- **Weather:** Overnight shifts depend on storms. Build in scheduling flexibility and a fallback of interviews before or after shifts.
- **Sample bias:** Don't recruit only volunteers or people who like talking. Include quiet or skeptical drivers.
- **Logs:** Confirm that data use for analysis is covered by your existing terms and city policy.

## 7. Timeline (about 7 weeks)
| Weeks | Activity |
|---|---|
| 1–2 | Log analysis, recruit participants, get approvals |
| 2–4 | Ride-alongs and interviews |
| 4 | Synthesis and a findings readout |
| 4–7 | Prototype and test changes |
| 7 | Final recommendations and report |

## 8. Deliverables
- A findings summary: causes ranked by evidence, with driver quotes
- A prioritized list of recommended changes with expected impact
- A test result for the most promising change
- A recommendation on whether voice should default on, off, or adapt by context

## 9. What I need from you or your boss
- Access to the logs and their schema
- Permission and contacts for overnight ride-alongs
- A point of contact in the city's operations or union
- Budget for driver time or incentives, if applicable
- Product and engineering availability for the Phase 3 prototypes

## 10. Open questions for you
- How is the mute event logged? Is it a user action, or could it be a default or crash?
- Do you know of any recent app changes, such as a new voice or update, that line up with the drop?
- Are routes assigned or chosen by drivers?

---

I can turn this into a one-page summary for your boss, or draft the interview guide and ride-along observation sheet. The first thing I'd draft is the interview guide.
