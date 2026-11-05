# Deepfield critique: Start to report

Both complaints have the same root cause. The client gives you one sentence, the agent interprets it alone, and the client sees nothing of that interpretation until five hours later. The fix is to surface the agent's interpretation and its evidence at the points where the client can still act on them.

## 1. Before Start: the question is taken at face value

"Top three rivals in Europe on pricing" hides at least four decisions: which rivals, what "Europe" means (EU, UK, Nordics?), what time window, and which pricing facet (list price, packaging, discounts, changes over time). The agent guesses all four, and a wrong guess on any of them wastes the run.

**Change:**
- Replace the free-text box and Start button with a short **scoping step**. The agent restates the brief as structured fields the client can edit: named rivals, regions, time window, and what counts as "pricing". Start stays disabled until the client confirms.
- Pre-fill the rivals from the client's account or CRM where possible. Have the agent propose candidates ("I'd pick A, B, C because…") instead of asking an open question.
- Keep it to one screen. If it feels like a form, people will click through it, so default everything and make the edits the exception.

## 2. First 20 minutes: no early checkpoint

This is the biggest fix. Rival selection, region and year are all settled in the first few minutes of work, but you only find out they were wrong in hour five.

**Change:**
- Add a **checkpoint at about 15–20 minutes**. Email and notify the client with a one-screen summary: "Here's who I'm analysing, where, which period, and my research plan. Reply to adjust, or I'll continue in 30 minutes."
- Make it **proceed-by-default**. The run shouldn't stall overnight waiting for a click. It should continue unless the client objects, so you keep the "set and forget" promise.
- Add a **cheap redirect**. If the client corrects the brief at the checkpoint, restart from there. That costs 20 minutes instead of 5 hours.
- Consider a second, lighter checkpoint at about 50% with preliminary findings, so a wrong turn in the analysis can still be caught.

## 3. During the run: a spinner and a percentage

For an open-ended agent the percentage is made up. It stalls, jumps, or sits at 90% for an hour, and that erodes trust. It also tells the client nothing they could act on.

**Change:**
- Drop the percentage. Show **stages** (Scoping → Gathering sources → Analysing → Verifying → Writing) with the current one highlighted.
- Add a **live findings feed** with concrete items: "Found 14 sources on Rival A's EU pricing," "Rival B's pricing page changed in March, reading the archive." This shows the work is real and exposes drift early.
- Add a visible **"Something look wrong?" button** that opens the same edit flow as the checkpoint, so the client can steer at any point.
- Show an honest estimated finish time as a range, and say so when it changes.
- Let the client close the tab with confidence. State plainly that email arrives when it's done, and send a short "still running, on stage 3" note if it goes long.

## 4. Verification: invisible to the client

Clients can't tell what the agent checked, so they have to treat the whole report as unverified and recheck it themselves. That removes much of the value of paying for the research.

**Change:**
- Give every substantive claim a **status**: *Confirmed* (two or more independent sources, or a primary source such as a filing or the company's own pricing page), *Single-source*, or *Inferred/estimated*. Show it inline, and keep the labels few and visually distinct.
- Attach a **citation with date retrieved** to each claim. Link to a saved snapshot, because pricing pages change.
- Add an **"Unverified / couldn't find" section** listing what the agent looked for and failed to confirm. Clients trust a report more when it admits gaps.
- Put a **verification summary** on page one: "41 claims: 29 confirmed, 8 single-source, 4 inferred."
- Be careful not to overclaim. A "verified" label must reflect a check that actually happened, so define what each status means in the pipeline and enforce it there.

## 5. The deliverable: a 30-page PDF

A PDF is hard to interrogate, and it fixes the report's shape before the client's real question is answered.

**Change:**
- Lead with a **one-page answer** to the original question, plus the assumptions used (rivals, region, period). A wrong assumption is then visible in ten seconds.
- Make the **web version the primary report**, with the PDF as an export. It can have collapsible detail, click-through citations, and verification filters ("show only single-source claims").
- Put **"Scope used"** at the top of the report, mirroring the confirmed brief from step 1.
- Offer **follow-up actions** from the report: "Add a fourth rival," "Redo for UK only." Cheap incremental reruns beat a fresh five-hour run.

## 6. After delivery: no feedback loop

You learn about wrong turns from complaints, not from data.

**Change:**
- Add a one-click "Was this the right scope?" prompt on the report, with a reason picker (wrong rivals, wrong region, wrong period, other).
- Log the checkpoint edits too. If many clients correct the same thing, such as the agent's rival choice, fix that default.

## Priority order

1. **Scoping confirmation plus the 20-minute checkpoint.** This addresses the wasted-hours complaint directly, and it's the cheapest to build.
2. **Per-claim verification status and citations.** This addresses the second complaint, but it needs pipeline work to make the labels truthful.
3. **Replace the percentage with stages and a findings feed.**
4. **One-page answer and web report.**
5. **Feedback loop.**

## Metrics to track

- The share of runs where the client edits the scope at the checkpoint.
- The share of runs that are redone or restarted after delivery. This should drop.
- Support complaints about "wrong direction."

One question affects the design: is the five-hour runtime fixed, or could the agent do a quick 20-minute "scout" pass first? If so, the checkpoint can show real preliminary findings and not just a plan. That makes it far more useful to the client.
