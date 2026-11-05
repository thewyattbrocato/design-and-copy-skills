# Research plan: why overnight plow drivers turn off voice directions

**Assumptions:** you can reach drivers through the city's fleet or operations contacts, and the usage logs have timestamps and per-driver or per-session records. The plan has no dates because I don't know your season or access. Confirm with your boss which week plowing ramps up, since that sets your window.

## 1. Decision and stakes
- **Decision:** what to change about the voice guidance. The options include defaults, content, timing, volume, a night mode, or leaving it alone.
- **Who acts:** your boss and the product team.
- **Risky assumption:** that the voice is "just annoying," which is the daytime supervisors' view. If it's wrong, we could spend months tuning a voice when the real problem is that the directions are wrong for plow routes.
- **Cost of being wrong:** a shipped fix that doesn't change the mute rate. There is also a safety risk. If drivers mute guidance because it's distracting or wrong, they're driving in snow at night with less support.

## 2. Evidence in hand
- **Usage logs:** they show what happens (the mute) and when. They can't say why.
- **Supervisor opinions:** these are second-hand. Day supervisors aren't in the overnight cabs, so treat their view as one hypothesis.

## 3. Research questions
1. **When, where and for whom** do overnight drivers mute the voice? The output is a profile of mute events by time into the shift, route type, location and driver.
2. **What is happening in the cab and on the route** at the moment of muting, in the drivers' own words? The output is a list of reasons, grouped.
3. **What do drivers do instead** (memory, paper, radio, a partner, silent screen)? The output is a description of how navigation actually works on a night route.
4. **Which change fits the reasons we find?** The output is a candidate change, tested with a few drivers.

## 4. Hypotheses to test
These are labeled guesses, not findings.
- **H1: Wrong content.** Plow routes are assigned and repetitive, and drivers know them. Turn-by-turn directions built for point-to-point trips add nothing, or conflict with how plow routes work, such as deadheading, partial passes and repeating streets.
- **H2: Competing audio.** The voice competes with dispatch radio, engine and blower noise, or a partner's talking.
- **H3: Alertness and startle.** At night the voice is jarring or fatiguing, or drivers prefer quiet to stay alert.
- **H4: Bad guidance.** GPS drift or snow-covered roads produce wrong or late prompts, so drivers learn to distrust the voice.
- **H5: Plain annoyance.** This is the supervisors' view. It stays in the list and gets tested like the others.
- **H6: Muting is fine.** It's a rational choice by experienced drivers, and the only change needed is a better default.

**What would change the plan:**
- If the logs show muting concentrated on repeat routes, that points to H1 or H6.
- If muting follows specific locations, that points to H4.
- If drivers mostly describe noise or radio conflicts, that points to H2.

## 5. Method, smallest version first

**Step 1: Mine the logs (a few days, no drivers needed).**
- Slice mute events by minutes into the shift, route familiarity (first time on a route versus repeat), location and speed, app version and device, and driver tenure if available.
- Compare overnight with day shift, and the mute against any later re-enable.
- Check whether "within the first hour" is real or an artifact. For example, drivers may mute at startup because the voice defaults on at an awkward moment.
- Report counts as n of N. Say what the logs can't see, such as the reason for the mute and what the cab was like.

**Step 2: Interviews with overnight drivers (the core of the study).**
- Talk to 6 to 8 overnight drivers. Include a mix of tenure and route types, and people who muted and people who didn't.
- Add 2 to 3 day-shift drivers as a comparison.
- Add 1 or 2 overnight dispatchers or night supervisors, who see the shift but aren't the daytime view.
- Run them as 30 to 45 minute conversations about the last shift, at the depot or by phone.
- Stop adding people when new interviews stop changing the reasons list. Add a few more if they still do.
- If the city allows it, add one or two ride-alongs. The cab is where the competing audio and the real route use show up.

**Step 3: Test a candidate change (only after steps 1 and 2).**
- Show 3 to 5 drivers a revised version, such as different content, a night mode or changed defaults, on real tasks.
- Compare mute behavior in a pilot. A live comparison needs one metric chosen in advance, such as the mute rate in the first hour. It also needs whole weeks of data, and enough drivers to mean something. A handful of drivers is a lead, not a result.

**Not recommended:** a survey now, because we don't yet know the options to put in it. Also avoid focus groups, and avoid asking drivers what they want or whether they like the voice. Ask about the last shift instead.

## 6. Who to recruit
**Screen on behavior:**
- Worked an overnight plow shift in the last month.
- Used the app on that shift.
- A mix of muted and not muted, according to the logs.

**Sample limits:**
- Volunteers skew toward the talkative.
- Supervisor-picked drivers skew toward the favored or compliant.
- Sample from the logs and ask the depot to invite, rather than letting supervisors choose.

## 7. Interview guide (core prompts)
Cover these as stories about a recent shift, in this order:
1. Walk me through your last overnight shift, from when you got in the truck.
2. Tell me how you knew where to go on that route.
3. Tell me about the last time you turned the voice off. What was going on just before?
4. What was on in the cab at that moment (radio, engine, other people)?
5. Tell me about a time the directions were wrong or late.
6. What do you do for a route you've never driven?
7. Tell me about a shift when you left the voice on. What was different?
8. Who else is involved when you're navigating, such as dispatch or a partner?
9. Anything I should have asked?

Don't mention the voice until prompt 3, and don't suggest reasons ("is it annoying?"). Use their words when you follow up.

## 8. Consent and safety
- **Driving:** never run a session, call or app task while someone is driving. Phone interviews happen before or after a shift, with the person parked or off duty. Ride-alongs need the city's sign-off and a safety briefing, and the researcher must not distract the driver.
- **Employer power:** drivers work for the city. Say plainly that participation is voluntary, that nothing said is attributed or goes to their supervisors, and that you'll share findings only in grouped form.
- **Recording:** get explicit consent before recording, and say who will hear it and how long it's kept. Code participants by letter or number and store files in one shared place.
- **Supervisors:** keep them out of the room.
- **Pay:** check whether the city allows incentives or paid time for participation.

## 9. Roles and what a human must do
- **Needs people:** one person who asks, and a second who takes notes (can be the same person for phone calls). Neither should be the designer of the voice feature.
- **You must do:** get access to the logs, arrange the city's permission and contacts, recruit and schedule, obtain consent, run and record the sessions, and store the files.
- **Fallback if recruiting is slow:**
  - Relax one criterion first, such as route type.
  - Then talk to fewer people now and more later.
  - Either choice delays step 3.

## 10. Output for your boss
- A short log profile with counts and its limits.
- A grouped list of reasons, with each tied to n of N drivers and its source.
- A ranked set of candidate changes, each linked to the reasons behind it. Anything from a single source is marked as a lead.
- What's still unknown, and the cheapest next check.

## 11. Limits
- Interviews show what reasons exist, not how common each one is. Counts from 8 to 10 people describe those people, not all drivers.
- The logs show behavior but not intent.
- If the findings point to a design change, test it with new drivers before shipping. Drivers who have seen the revised design are tainted for the test.

**Note:** I don't have your log schema, shift counts or driver numbers, so I left them out. Fill in `[to collect]` values once you pull the logs.
