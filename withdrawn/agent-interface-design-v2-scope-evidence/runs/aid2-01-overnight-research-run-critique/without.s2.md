# Deepfield experience critique, from Start to report

Your two complaints have the same root cause. The product treats a five-hour job as a single unobserved transaction: the client commits once at Start, hears nothing useful for five hours, then gets one artifact with no provenance. Everything below is about changing that.

## 1. Before Start: the question is under-specified, and the system never checks

"Top three rivals in Europe on pricing" hides at least five decisions:
- **Which rivals?** The client may have meant the three they worry about, not the three the agent finds largest.
- **Which Europe?** EU, EEA, UK, or Russia and Turkey too.
- **Which period?** Current list prices, the last 12 months, or the trend.
- **Which products and segments?**
- **What counts as pricing?** List price, discounting, packaging, or contract terms.

A free-text box followed by Start means the agent guesses at all five. A wrong guess on any one wastes the whole run.

**Change:** Add a two-minute **scoping step** before Start.
- The agent restates the question as a structured brief the client can edit:
  - Named rivals, with the agent's reasoning for each.
  - Geography.
  - Time window.
  - Report sections.
  - Exclusions.
- Ask only what the agent can't resolve itself, in one to three questions. Rival identity is the one you must confirm.
- Make the brief the contract. Start becomes "Approve brief and start."
- For repeat clients, prefill from past briefs and company profile.

This is the highest-leverage fix. It targets wrong rivals, wrong region and wrong year directly.

## 2. During the run: a spinner and a percentage tell the client nothing

- **The percentage is probably fiction.** Agent work isn't linear, so it will stall at 40% or jump. Nothing in it lets the client judge whether the run is on track.
- **There's no chance to catch a wrong turn.** The client is the only person who knows immediately that "Acme" is the wrong rival, but they have no way to say so.
- **There's no sense of what's happening.** Silence for five hours reads as either "stuck" or "magic," and neither builds trust.

**Change:**
- **Replace the percentage with named phases:** identify rivals, collect sources, extract pricing, cross-check, draft. Show the current phase and a rough time estimate.
- **Add an early checkpoint at roughly 15–20 minutes.** The agent has by then settled on its rival list, sources found and working outline. Email or notify the client: "Here's what I'm investigating. Reply to adjust, or do nothing and I'll continue." Pause only if you need a hard confirmation. Otherwise default to proceeding after a timeout, so overnight runs don't stall waiting for someone asleep.
- **Show a live findings feed**, such as "Found 14 sources on Rival B's EU price page" and "Rival C changed pricing in March 2026." It proves progress and lets clients spot errors early.
- **Allow mid-run steering.** "Drop Rival C, add Rival D" should reuse completed work and redo only what's affected, not restart.
- **Allow cancel or pause without losing results,** with partial output delivered.

Make sure the checkpoint is cheap to act on. A client who must log in, read a long page and fill a form won't use it. Aim for one-click confirm and one-line correct.

## 3. Delivery: the report hides what was verified

A 30-page PDF presents every sentence in the same confident voice. Clients can't tell a figure read off a rival's current price page from one inferred from a two-year-old press article. That's the "can't tell what was verified" complaint, and it's a trust problem as much as a UX one.

**Change:**
- **Label every claim by evidence level.** Three tiers is enough:
  - *Verified:* seen directly in a primary source, such as the rival's own site or a filing.
  - *Reported:* from secondary coverage.
  - *Inferred or estimated:* the agent's own synthesis.

  Use a visible mark, not a footnote.
- **Cite each claim with a source, retrieval date and link,** not a bibliography at the end.
- **Add a "Confidence and gaps" page at the front.** It should cover what couldn't be found, which pages were paywalled or blocked, and where sources conflict. Admitting gaps is the strongest trust signal you have.
- **Include an "Assumptions used" section** that echoes the approved brief, so any mismatch is obvious right away.
- **Lead with a one-page summary,** with key figures and their evidence labels.
- **Deliver an interactive web version alongside the PDF.** Clicking a claim shows the source excerpt. PDFs can't do that, and a 30-page document is hard to audit.

One caution: the labels must reflect something real. Have the pipeline record provenance as it works, and don't ask a model to guess afterward which claims it verified. Otherwise the labels will be wrong and do more damage than having none.

## 4. After the report: no feedback loop

If the report is 80% right, the client has to start over, and that's another five hours. Add:
- A "refine this" action, such as "add Rival D" or "redo section 3 for 2026," that reruns only the affected parts.
- A quick per-section rating, which tells you where the agent goes wrong.
- A follow-up question box that answers from the already-collected research.

## Suggested order

1. **Scoping brief plus approval** (biggest reduction in wasted runs).
2. **Early checkpoint email** (catches what scoping misses, and is cheap to build).
3. **Evidence labels and inline citations** (addresses the verification complaint; needs pipeline provenance work).
4. **Phase-based progress and findings feed** (replaces the percentage).
5. **Partial reruns and mid-run steering** (the hardest to build, so do it last).

## How to know it worked
- Share of runs where the client says the report went the wrong way (your current complaint rate).
- Share of runs rescoped at the checkpoint, and how many of those would have been wasted runs.
- Rerun rate within 48 hours of delivery.
- Whether clients open the sources behind claims. High usage suggests they trust the labels enough to check them.

I can draft the scoping-brief screen, the checkpoint email, or the evidence-label scheme next. Tell me which would help most. If you can share a few example complaints, I can also check whether the wrong turns cluster around one decision, like rival selection, which would show where to focus first.
