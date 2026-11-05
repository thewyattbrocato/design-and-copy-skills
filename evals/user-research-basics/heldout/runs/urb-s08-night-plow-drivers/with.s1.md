# Research plan: why overnight plow drivers turn off spoken directions

**Assumptions:** you have the usage logs, access to the drivers through the city's fleet or operations office, and a few weeks. I haven't invented any numbers. Anything not yet known is marked `[to collect]`.

## 1. Decision and stakes

- **Decision:** what to change about voice guidance for overnight drivers. The options are the defaults, the content, the timing, the volume and ducking, or leaving it alone.
- **Who acts:** your boss and the product team.
- **Current assumption:** the voice is "just annoying" (daytime supervisors). This is a hypothesis, not a finding. The supervisors don't work overnight and don't drive the cabs.
- **Cost of a wrong guess:** we might tune the voice (tone, frequency) when the real problem is something else. Examples are that it clashes with the dispatch radio, repeats directions on routes drivers already know, or tells them things that don't fit plowing. If drivers turn it off for a reason we haven't found, they may also be missing the alerts that matter.

## 2. Evidence already in hand

Use these before talking to anyone.

| Source | What to pull | Answers |
|---|---|---|
| Usage logs | When in the shift the voice goes off (minutes in, which screen, during a route or at start). Whether it's turned back on. Whether this is the same drivers each time or many drivers once. Overnight vs. day, same metrics. | What exactly happens, and whether it is really specific to overnight |
| Same logs | Voice off vs. on: route completion, off-route events, missed segments, manual re-routes | Whether turning it off is harmless or a symptom |
| Support tickets, app feedback, dispatcher notes | Anything mentioning voice, volume, audio, radio, "talking" | Unprompted complaints in drivers' own words |
| Fleet info | Cab hardware (speaker, Bluetooth, tablet), radio setup, shift structure, route types (plow vs. salt vs. deadhead) | Context for the hypotheses below |

**Check first:** whether the voice defaults to on, and whether turning it off is one tap. If it's easy and visible, the log shows a choice. If it's buried, it may show something else.

## 3. Research question

> Produce a ranked list of the reasons overnight drivers turn off voice guidance in the first hour. For each reason, note what the driver does instead and what it costs them.

**Result that would change the plan:** if the logs show the same drop-off in day shifts, the question is not about overnight and the supervisors' read gets a closer look. If voice-off correlates with worse route outcomes, the priority moves from comfort to safety.

## 4. Hypotheses to test (not conclusions)

These come from the situation, not from data. The interviews should be able to rule each of them out.

1. **Competes with the radio.** Dispatch traffic and the voice overlap. The driver has to pick one.
2. **Wrong content.** Directions designed for road trips don't suit plowing. Drivers may follow assigned routes they know, so prompts are redundant, or the prompts are wrong for plow work (turn prompts for a lane they're clearing, for example).
3. **Too frequent or badly timed.** It speaks during tricky maneuvers, such as backing, raising or lowering the blade, or low visibility.
4. **Cab audio.** Engine and plow noise, speaker placement, or no way to adjust volume. At night, a voice that's too loud or too quiet.
5. **Night-specific factors.** Fatigue, quiet streets, and the voice startling or irritating a driver who is alone for hours.
6. **Just annoying.** The supervisors may be partly right. Keep it in the list and test it like the others.
7. **Something else we haven't thought of.** Leave room for it in the guide.

## 5. Method (smallest version that answers it)

**Step 1: Log and ticket review (about 3–4 days).** Section 2. Do this first, because it shapes the interview questions.

**Step 2: Interviews with overnight drivers (6–8 people, about 30–40 minutes each).**
- Conversations about the last real shift, not opinions about the app.
- If you can get city approval, a ride-along or cab observation for 2–3 of them would be worth more than the rest. You see the noise, the radio and the moments when the voice goes off.
- Also talk to **2 dispatchers or overnight supervisors**. They know what drivers say to each other.
- Add **3–4 day-shift drivers** as a comparison. They aren't the focus, but they tell you whether this is overnight-specific.

**Step 3: Check with supervisors (1 short meeting).** Share what you found and ask what they'd expect. Don't defer to them, but they will have to act on any change.

Stop adding interviews when new ones stop changing your list of reasons. Add a few more if they still do. With 6–8 people, report "5 of 7", never percentages.

## 6. Who to recruit

- **Include:** drivers who worked at least one overnight plow shift in the last month, with a mix of experience (new to the app vs. long-time users) and route types.
- **Screen on behavior, not opinion.** Ask what shifts they worked and what they did on them. Don't ask whether they like the voice, and don't mention voice in the invitation. Describe the study as "how you use the app on your shift."
- **Exclude:** anyone who helped build or test the app.
- **Who this leaves out:** drivers who quit the app entirely, and contractors if they're outside the city's pool. Note this beside any conclusion.
- **Recruit through** the city fleet or operations office. This is the main thing you need your boss to unlock. Drivers may be wary of an interview that could look like an evaluation of them. Make clear it's about the app.

## 7. Interview guide (draft)

*Goal (for the team, not read aloud): find out what happens around the moment the driver turns the voice off, and what they do afterward.*

1. **Intro and consent.** Purpose in plain words, that this is about the app and not about them, what's recorded, who sees it, that they can skip or stop. Ask permission before recording. Name participants by code (D1, D2…) in notes.
2. **Warm-up.** Tell me about your usual shift. How long have you been doing overnights? What do you drive?
3. **Last shift.** Walk me through your last overnight shift from when you got in the cab.
4. **First hour.** What did you do with the app in the first hour? What did you set up? What did you look at?
5. **Audio.** What were you hearing in the cab? *(Let them list it: radio, engine, app. Don't name the voice first.)*
6. **The moment.** Tell me about the last time you changed a setting on the app, or wanted to. What was going on? What happened next?
7. **Without it.** What do you do for directions when the app isn't talking? *(Their answer shows what the voice is replaced by.)*
8. **Missed or wrong.** Tell me about a time the app told you something that was wrong or didn't fit what you were doing.
9. **Other people.** What do other drivers say about the app? What do dispatchers say?
10. **Close.** Is there anything I should have asked? May I follow up?

Probes: "say more about that," "what happened next," "why was that," then wait.

**Don't ask:** "Do you like the voice?" "Would you use it if it were quieter?" "What features do you want?" These get opinions and guesses, not what happens.

## 8. Safety and consent

- **Never interview a driver who is driving or about to.** Schedule before or after shifts, at the depot, or on breaks. This applies to phone calls as well.
- Cab observation needs the city's approval and the driver's explicit consent. The observer stays quiet and out of the way, and the session ends if the driver is distracted.
- Keep notes anonymous. Say clearly that nothing goes to supervisors with names attached.
- Store recordings and notes in one shared location after each session, named by study, participant code and date.

## 9. Roles and what a human must do

You can own all of these; it's just tasks.

- **Get access and approval** through the fleet office. *Your boss may need to open this door.*
- **Recruit and schedule** (about a week of lead time).
- **Facilitate** and **take notes**. Ideally two people, with someone other than the app's designer asking the questions.
- **Synthesize:** code notes by participant, group by reason, count as "n of N", and rank by how often each came up and how much it matters to safety and route completion.

## 10. Schedule (rough; adjust to your dates)

| When | What |
|---|---|
| Week 1 | Logs and tickets; get fleet access; draft screener |
| Week 2 | Recruit; run 2–3 pilot interviews and fix the guide |
| Weeks 2–3 | Remaining interviews and any cab observation |
| Week 4 | Synthesis; check-in with supervisors; recommendation |

**Fallback if recruiting is slow:** do fewer interviews now (4–5 overnight drivers) and add more later. This pushes the recommendation back about a week. Or relax the experience criterion rather than the overnight one.

## 11. What the output will be

A short write-up with:
- The ranked list of reasons, each with "n of N" and its source.
- What drivers do instead, and whether it costs them anything.
- Open questions and the cheapest next check.
- Decisions to take to your boss, such as default, content, timing and volume.

Solutions come after the findings, kept separate from them. Any change you make should be tried with drivers who weren't in the study.

## 12. Limits

- Six to eight interviews show *why*, but not *how many* drivers have each reason. If you need counts, follow up with a short survey built from the reasons you found.
- Self-reports are weaker than observation. That's why the ride-along is worth pushing for.
- Drivers who turn the voice off may not remember exactly why. The "last shift" questions help, but treat single-source reasons as leads.

---

*Two notes:* (1) Whether you can get ride-along approval is the biggest unknown, and it's worth asking your boss about it now. (2) Once you have the log numbers, I can help sharpen the question or turn this into a one-pager for Friday.
