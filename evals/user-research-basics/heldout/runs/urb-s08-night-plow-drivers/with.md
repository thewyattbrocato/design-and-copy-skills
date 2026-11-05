# Research plan: why overnight plow drivers turn off spoken directions

**Draft for [boss], due Friday**

## 1. Decision and stakes
- **Decision:** what to change about voice guidance for overnight drivers. Options include different defaults, different content, different timing, or leaving it alone. Product owns this.
- **Current assumption:** the voice is "just annoying" (daytime supervisors). This comes from people who don't work the overnight shift and aren't in the cab. Treat it as one hypothesis among several.
- **Cost of a wrong guess:** we could spend a release on a quieter or friendlier voice when the real cause is something else. Examples are directions that don't fit plow routes, clashes with the dispatch radio, or drivers who already know their routes. Turning voice off may also be a safety signal rather than a preference.

## 2. What we already have (use first)
- **Usage logs.** Before talking to anyone, cut them by:
  - time into shift when voice goes off, and whether it is ever turned back on;
  - route type (assigned plow route, deadhead or transit, return to depot);
  - weather and road conditions, and time of night;
  - driver tenure, and repeat versus new routes;
  - device and volume settings, if logged.
- **Support tickets, feedback and dispatcher notes** mentioning voice, audio or directions. [to collect]
- **Why this matters:** the logs show *what* and *when*. The cut by route type and tenure will likely rule several explanations in or out before any interview.

## 3. Research questions
1. **Log analysis:** produce a table of when and in what situations voice is turned off, and whether it stays off. Done when we can say which situations account for most switch-offs.
2. **Interviews:** produce a list of the reasons overnight drivers give, from their last real shift, for turning voice off. Each reason should have a count of how many drivers gave it.
3. **Ride-along (optional):** observe what the voice does in the cab, such as what it says and when, and what else is competing for attention. Done when we have a list of specific moments where voice and the job conflict.

## 4. Method (smallest version)
| Step | What | Size |
|---|---|---|
| A | Log analysis (section 2) | Existing data, no participants |
| B | Short conversations about the last shift, before or after the shift, at the depot | About 6–8 overnight drivers, then add a few if new interviews are still changing the picture |
| C | Ride-along observation, only if the city allows it and the driver agrees | 2–3 shifts |
| D | Short contrast sample: 3–4 daytime drivers and 2 supervisors | Checks whether this is an overnight issue or a general one, and tests the "just annoying" claim |

**Not recommended:** a survey now (we don't yet know the options to offer), focus groups, or asking supervisors to speak for drivers. After B we could send a short survey to count which reasons are most common, but only once the themes are known.

## 5. Hypotheses to test (labeled assumptions, not findings)
- H1: Drivers know their routes, so the voice adds nothing after the first pass.
- H2: Instructions are built for road navigation, not plowing, so they conflict with the actual job (for example, wrong turns, one-way or lane assumptions, or not following the assigned pattern).
- H3: The voice competes with the dispatch radio or other audio, or masks sounds the driver needs.
- H4: Voice is a distraction in poor visibility and heavy workload.
- H5: Timing, repetition or volume is poor at night (too loud in a quiet cab, too late or too early for a turn at plow speed).
- H6: It is turned off by habit or by a setting that doesn't persist.
- H7: It really is just annoying (the supervisors' view).

Interviews should surface reasons we haven't listed. The list shapes the analysis but not the questions, so we don't lead.

## 6. Who to talk to
- **Overnight shift plow drivers who used the app in the last two weeks.** Include a mix of tenure and of route types (arterial, residential, deadhead). Include people who turned voice off *and* people who kept it on.
- **Leaves out:** drivers who stopped using the app entirely, contractors (if any), and anyone we can't reach on their shift schedule. Say so beside every conclusion.
- **Screener:** short. Ask what they did on their last shift (among several tasks), and confirm they used the app. Don't mention voice or the study topic in the invitation. Describe it as "a chat about how you use tools in the cab."
- **Exclude:** product, design and support staff for this app. Avoid supervisors in the room during driver sessions.

## 7. Interview guide (outline, about 20–30 minutes)
Goal (for the team): learn what happened with voice guidance on recent shifts, in drivers' own words.
1. Intro, consent, recording permission, anonymity (section 9).
2. Warm-up: route, how long on the job, how long on overnight.
3. "Walk me through your last shift from the time you got in the truck."
4. "Tell me about the first time that shift you did something with the app." (Follow with what they did next, what they were looking at, and what they heard.)
5. "Tell me about the last time you changed a setting or turned something off in the cab." (Probe: what was happening just before, and what changed after.)
6. "What else is going on in the cab while you work?" (Radio, plow controls, mirrors, phone.)
7. "Tell me about a time the app told you something that didn't match what you needed to do."
8. "What did you do on the shift before, and how was that different?"
9. Close: "Anything I should have asked?" Permission to follow up.

Probes: "say more," "what happened next," and silence. Use their words, not ours ("voice," "directions"), until they say them.

## 8. Roles and what a human must do
- **Product/research lead (you):** owns the plan, the checklist and the analysis.
- **Interviewer:** someone who did not design the voice feature, with a second person taking notes. Notes are coded by participant letter.
- **Needs a human, in this order:**
  1. Get sign-off from the fleet/depot manager, and the union rep if there is one, so drivers know this is not a performance review.
  2. Recruit and schedule around shift times.
  3. Handle consent and recording permission.
  4. Run the sessions.
  5. Store notes and recordings in a shared location (study, participant code, date).

## 9. Safety, consent and trust
- **Never interview or observe while the person is driving** a plow on a call or route. Talk at the depot, in a break or at shift change. For ride-alongs, the driver and the city decide whether it's allowed. We stay out of the way and don't ask questions while the truck is moving.
- Say plainly what's recorded, who sees it, how long it's kept, and that they can skip questions or stop.
- Drivers work for the city, so say clearly that individual answers go to the product team only and nothing is reported to supervisors by name. Keep participant IDs out of anything shared widely.
- Pay or time allowance: check city rules. [to confirm]

## 10. Schedule (proposed, adjust to the winter season)
Dates are placeholders; I don't know your constraints.
- **Week 1:** log cut, ticket review, sign-off, screener out.
- **Week 2:** interviews begin, with the contrast sample (Step D) at the end.
- **Week 3:** ride-alongs (if approved), synthesis.
- **Week 4:** readout with a ranked list of reasons and options.

**Fallback if recruiting is slow:** relax one criterion (such as route type) first, then interview fewer people now and more later. Overnight scheduling will probably be the slowest piece, so ask for access early.

## 11. What would change the plan
- If the logs show switch-offs concentrated on **deadhead or return legs** or on **repeat routes**, the problem is relevance, not tone. Prioritize interviews on H1 and H2.
- If drivers mostly give a **radio or audio-clash** reason, look at audio priority and ducking, not the voice itself.
- If **most drivers** say the content doesn't match plow work, the fix is the instructions, not the delivery.
- If the reason is mainly **"annoying"** or voice quality, a tone and frequency change is justified, and the supervisors were right.
- If **daytime drivers** show the same pattern, the cause isn't specific to the night shift.

## 12. Limits
- 6–8 interviews give a list of reasons and rough counts (reported as "n of N"), not percentages.
- Drivers who agree to talk may differ from those who don't.
- Logs show that voice went off but not why.
- Findings should stay as problems and evidence. Solutions come after the readout.

## 13. Output
A short readout: the log findings, the ranked reasons with counts and source (n of N), what we still don't know, and the cheapest next check. Options for changes come from that, not before.

*Assumptions:* the app logs voice on/off events with timestamps, and you can reach drivers at the depot. If the logs don't capture those, step A becomes a small instrumentation change.
*What a human must do:* get depot/union sign-off, recruit, handle consent and run the sessions. I can't do those.
