**Assumptions:** I'm working from your description, not the app itself. I'm assuming the agent only reads public sources and doesn't contact anyone or spend money. I'm assuming the client is asleep or away for most of the run. Anything marked "placeholder" is a number for you to set.

## The core problem

Deepfield makes its most expensive commitment at the moment it knows the least. A free-text question goes straight into a five-hour run. "Top three rivals", "Europe" and "pricing" all have several reasonable readings, and the agent picks one without telling anyone. The client then finds out which one at the end, when a wrong turn can't be fixed cheaply.

The verification complaint has the same cause. The report is one finished object, and its 30 pages look equally certain.

The priority order is:
1. Confirm the brief before Start.
2. Show real progress and checkpoints while it runs.
3. Make the report reviewable claim by claim.

## 1. Before Start: confirm the brief

**Now:** the client types a question, clicks Start, and the agent decides what it meant.

**Change:** Start doesn't launch the run. It opens a short "How I read your question" screen, with a draft already filled in from the question and the client's account. The client only corrects it. Don't ask them a list of questions.

> **Before I start, check I've understood.**
> **Rivals:** Acme, Borealis, Cortex. *I picked these as your closest competitors by [reason, e.g. overlap in your product category].* [Change] [Add one I should include]
> **Region:** EU-27 plus UK. *Switzerland and Norway are not included.* [Change]
> **Period:** pricing as published now, compared with [year]. [Change]
> **"Pricing" means:** public list prices, plan tiers and recent changes. *Not negotiated or private discounts.* [Change]
> **What I'll do:** read public websites, filings and press coverage. I won't log in anywhere or contact anyone.
> [Start research] [Edit plan]

Why each part is there:
- **Name the rivals and say why.** "Top three" is the most likely cause of the wrong-rivals complaints. The agent's choice becomes something the client can see and overrule.
- **State the exclusions.** For region, year and pricing scope, what's left out is where clients get surprised.
- **Keep the promise line short.** It says what the agent will do and what it won't. It covers paywalled sources too. If you ever buy access to them, that needs its own cap and approval.
- **Offer the plan as an edit option.** Show the phases (identify rivals, gather pricing per rival, cross-check, write up) and let the client reorder or cut them. Mark where the agent will stop and ask.

This costs the client about a minute. A wrong reading costs five hours. Track how often clients edit this screen. If almost nobody does, your drafts are good enough to shorten it.

## 2. While it runs: replace the spinner and percentage

A percentage of an unknown-length research task is a made-up number. It also hides the one thing the client wants, which is whether it's on the right road. Replace it with one status view:

- **Current phase**, with the phases done and the phases left.
- **Findings so far:** rivals confirmed, countries covered, number of sources read, and the gaps found.
- **Assumptions in force.** The same list as the brief, plus anything the agent decided along the way.
- **Next checkpoint** and an estimated finish, labeled as an estimate.
- **Pause and Stop**, one click from this view. They are different actions:
  - Pause keeps the working state and accepts new direction.
  - Stop ends work, keeps what's finished, and says what was left half-done.
- **A "Redirect" box.** The agent acknowledges it immediately, even if it will apply at the next phase.

**Checkpoints.** The main checkpoint is the confirmation screen at Start, because the client is there and awake. Don't plan on a mid-run approval overnight, because nobody will answer it and the night is lost.

Mid-run, the agent should do two different things depending on the cost of a wrong guess:
- **Cheap and recoverable** (a minor ambiguity): choose, log it as an assumption in the report, and move on.
- **Costly** (a rival turns out to have been acquired, or has no European pricing at all): send a message and apply a default the client picked at Start. Offer the choice at Start: "If I hit a fork like this, [wait for me / continue on my best reading and flag it]."

**Messages.** Sort them into kinds so the client isn't pinged for everything:
- **Problem** (interrupts now): a rival has no findable pricing, or a major source is blocked.
- **Concern** (a note, not an interruption): coverage for one country is thin.
- **Completion:** one email at the end, not one per phase.

## 3. The report: make verification visible

"30 pages, trust us" is the second complaint. Fix it in the report itself, not with a disclaimer.

**Page one is a "What I did" summary.** It restates the brief, lists every assumption the agent made, and lists what it couldn't find. Put the gaps and doubtful items first. Gaps are the part clients most need and most rarely get.

**Mark every claim with a status that has a fixed meaning.** Define the labels once in the report, for example:
- **Confirmed:** from a primary source (a filing or the company's own pricing page), with the retrieval date.
- **Single source:** one source only, and what it is.
- **Inferred:** worked out from other data, with the reasoning shown.
- **Not found:** searched and nothing turned up.

Don't add a percentage confidence score unless you can show how it's calculated and what its error rate is. Clients will read an invented one as a measurement.

**Make every claim traceable.** Each one links to its source with a retrieval date. This is also the cheapest way for the client to spot a wrong-year source.

**Deliver the report in the web app, with the PDF as an export.** The email links to the web version. There, the client can:
- Accept or reject each section on its own, with doubtful sections shown first.
- Ask for one section to be redone ("redo Germany for 2026") in a few minutes, not a full rerun.
- Keep a record of what they accepted.

The PDF carries the same status marks for people who read it offline.

## 4. When it's still wrong

The goal isn't zero misreadings. It's making a misreading cheap to fix.

- **Rerun only the affected part.** If one rival was wrong, swap it and redo that rival's sections. Reuse everything still valid.
- **Give two kinds of feedback**, not just a thumbs-down:
  - "Not this time" (this brief only).
  - "Always for this company", for example "Europe means EU plus UK". Show the saved rule in plain words, and reuse it to pre-fill the next brief.
- **Record which version of the brief each report ran on**, so an old report isn't judged by new rules.

## 5. Cancelling and getting help

At any point, the client should be able to cancel without giving a reason. The screen should say what they keep (the partial findings) and what happens to billing. I don't know your billing, so check that this is clear. A route to a person should be visible from the status view and from the report. A client whose run has gone wrong shouldn't have to hunt for it.

## What to do first

1. **The confirmation screen before Start.** It targets the wrong-rivals, wrong-region and wrong-year complaints directly, and it's the smallest build.
2. **Per-claim status and source links in the report.** This answers the verification complaint. It depends on the agent already recording its sources, so check that first.
3. **The status view with real phases and Stop/Pause.** Do this once the first two are in.
4. **Section-level accept/reject and partial rerun.** This is the biggest build and the biggest saving, so schedule it as a second step.

To judge whether this works, track how often clients edit the brief, how often they ask for a partial rerun, and how often they ask for a full rerun. If full reruns don't fall, the confirmation screen isn't catching the misreadings.
