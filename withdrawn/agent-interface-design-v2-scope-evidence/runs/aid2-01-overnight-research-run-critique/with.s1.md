**Assumptions.** The client is a business user who types one sentence and leaves. A wrong turn is only visible at hour five. The cost is five hours plus a missed morning deadline. Nothing here is sent or spent on the client's behalf, so the risk is wasted time and false confidence, not harm. I haven't seen your actual screens, so this critiques the flow as you described it.

## The core problem

Deepfield is judged once, at the end, and the client has no say in between. A one-line question is badly under-specified: which three rivals, which countries, which year, pricing of what. The agent guesses silently, the spinner hides the guesses, and the PDF arrives with them baked in. A percentage is the weakest possible status, because it shows the agent is busy but not whether it is going the right way.

## Click to Start

**Problems**
- Start commits five hours of work on an unchecked reading of the question.
- Nothing tells the client how the agent interpreted "top three rivals", "Europe" or "pricing".
- The client can't see what the agent will do, or what it will skip.

**Change**
1. **Add a two-minute interpretation step before the run starts.** Don't make it a form. Restate the question the way the agent understood it, and let the client correct it:
   > "I'll compare **Acme, Birch, Corvo** (picked as the three largest by revenue in your category; swap any) on **list and enterprise pricing**, in **EU-27 plus UK**, covering **2025–now**. I'll leave out: marketplace resellers, non-public quotes."
2. Make every bolded item editable inline. Mark the guessed ones ("picked by me") differently from the ones the client stated.
3. Ask at most two or three questions, and only the ones the agent can't reasonably infer. Rivals, region and time window are the ones your clients keep getting wrong. Propose a default for each instead of leaving a blank.
4. Show the plan as editable steps, with the points where it will pause marked (see the next section). This is the "plan before it starts" pattern for long, costly jobs, and Deepfield qualifies.
5. Give a plain-language promise: "Over the next ~5 hours I'll read public sources only. I won't contact anyone. I'll check in with you at 20 minutes."

## While it runs

**Problems**
- A spinner and a percentage. The client can't tell whether it is on track, stuck, or reading the wrong company.
- No way to redirect, and no way to stop without losing everything.

**Change**
1. **Replace the percentage with a status page.** It should show the current phase, phases done, the rivals and sources covered so far, and the first findings as they appear. Put the detailed log behind a click. Don't invent a percentage. If you show a time estimate, label it as an estimate.
2. **Add an early checkpoint, at roughly the first 15–30 minutes (a starting value to test).** Send a short "here's what I've found so far" message. Include the rivals it settled on, the sources it's using, and a sample of two or three findings. Ask one question: "Is this the right road?" The wrong-rival, wrong-region and wrong-year failures all show up here, at about 10% of the cost. Make the email and the in-app page carry the same check-in.
3. **Add shorter check-ins at phase boundaries,** each a two-line statement: the goal as it now reads, what it's assuming, and what it will do next. The client can correct it, and the agent reruns the affected phase without carrying the bad assumption forward. Don't interrupt within a phase.
4. **Don't wait for an answer.** If the client doesn't respond, the agent continues on its stated assumptions and says so in the report. An overnight service can't block on a person who's asleep.
5. **Offer both Pause and Stop,** one step from the status page. Stop keeps what's finished and says what was left half-done. Pause accepts a new direction ("drop Corvo, add Delta") and resumes.
6. **Acknowledge redirections immediately,** even when they apply later.
7. **Warn about trouble early.** If the agent finds it can't find a rival's EU pricing, or the sources contradict each other, that is a "problem" message sent right away. Don't let it surface at the end as a thin section.
8. **Keep notifications few.** Completions go into the final email, problems interrupt, and the checkpoint is the one scheduled check-in. Don't send per-step pings.

## Report: what was verified

**Problems**
- A 30-page narrative with uniform confidence. Every sentence looks equally trustworthy, so the client can't tell what's checked and what's inferred.

**Change**
1. **Tag every claim with its basis.** For example:
   - *Confirmed*: from a primary source, such as the rival's own pricing page or a filing, with a link and the retrieval date.
   - *Reported*: from press or a third party, not corroborated.
   - *Inferred*: the agent's estimate or extrapolation, with the reasoning.
   - *Not found*: searched for and not found, with where it looked.
2. **Put a one-page "how sure are we" summary up front.** It should list the assumptions the agent made, the claims it was least sure of first, and the gaps. Don't give an overall confidence score. Show counts per tag with the underlying claims behind them, because a bare percentage hides which way it fails.
3. **Link every figure to a source,** with a date, and note staleness: "pricing page captured 3 Nov".
4. **Report what it didn't do,** with reasons: "Could not access Birch's German price list (login-gated)."
5. **Review the output as separable parts.** In the web app, let the client accept, flag or reject each section, with the doubtful ones first. Add a one-step "redo this section with X" instead of forcing a full five-hour rerun. Keep the PDF as the deliverable, but make the web version the working copy.
6. **Offer "this was wrong" at the claim level,** with two options: "wrong for this report" and "always treat X this way" (for example, "never use reseller prices"). Show the rule it creates.

## Priority

1. **Interpretation step before Start.** It's the cheapest change and prevents most of the "wrong road" complaints.
2. **Early checkpoint at ~15–30 minutes.** It catches what the first step misses.
3. **Evidence tags and the "assumptions and gaps" page.** This directly answers the verification complaint.
4. **Replace the spinner with a findings-so-far status page, plus Pause and Stop.**
5. **Section-level redo.** This helps most once the rest is in place.

## How to tell whether it worked

- Track the share of runs where the client edits the interpretation, and the share where they redirect at the checkpoint. If the checkpoint edits are high, your interpretation step is asking too little or proposing poor defaults.
- Track full reruns requested after delivery. That is the number your clients are complaining about today, so use it as the baseline. I have no figure for it.
- Check whether clients open the source links. If they never do, the tags aren't earning their space.

One caution: the interpretation step adds friction to a flow that is currently one click. Keep it to a single screen with good defaults, so a client who agrees with the guesses can still start with one click.
