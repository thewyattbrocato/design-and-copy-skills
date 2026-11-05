I've only got your description to go on, not the app or code, so this critique is based on that. Your two complaints share one cause. The agent works for five hours in a black box, and the client can only correct it or check it at the end.

## What's wrong

**1. Start commits five hours to a guess.**
"Top three rivals", "Europe" and "pricing" are each ambiguous. Rivals could mean by revenue, by overlap with the client's product, or by who the client already loses deals to. Europe could mean the EU, the EU plus UK and Switzerland, or the EEA. Pricing could mean list prices, discounts, packaging or contract terms. The agent picks an interpretation silently, and the client first sees that choice 30 pages later. A wrong guess at minute 2 costs the full run.

**2. The spinner and percentage give no information.**
Open-ended research has no real percentage, so the number is invented. It tells the client nothing about direction, which is the thing they worry about. It also trains them to ignore the page. The overnight timing makes it worse, because nobody is watching when the agent drifts.

**3. There's no way to steer once it's running.**
Even if a client notices a problem, the only option is to cancel and start over, throwing away sources the agent already read.

**4. The report doesn't show how much was verified.**
A 30-page PDF where every sentence has the same confident tone hides what's solid and what's inferred. Clients can't tell a pricing figure from a filing apart from one the agent guessed from a blog post. That makes them distrust the whole report, including the parts that are right.

**5. The report doesn't say what it assumed.**
If it's wrong, the client has to work out why. If it's right, they still can't tell it answered their question.

## What to change, in priority order

1. **Add a scoping step before Start commits (2–3 minutes).** The agent restates the question as a plan the client can edit:
   - the named rivals and why it chose them
   - the exact region
   - the time window
   - what "pricing" covers
   - the source types it will use

   Show sensible defaults and ask only about what's materially ambiguous. A client who can fix "Rival C should be X, and include the UK" in 30 seconds removes most of your wrong-road complaints.

2. **Add a direction check at about 20–30 minutes.** The agent emails or notifies a short preview: the rivals confirmed, the first few findings, and the outline. It keeps running on its best guess while it waits, so an unanswered check doesn't stall the overnight job. If the client replies with a correction, the agent redirects and **reuses what it already gathered**.

3. **Replace the percentage with a real activity view.** Show milestones and counts, such as rivals identified, sources read, claims gathered, claims cross-checked and sections drafted. Give the time estimate as a range. Add an "Adjust scope" button that works mid-run.

4. **Label every claim with its verification status.** Use a small fixed set:
   - **Verified**: from a primary source (a filing or the rival's own price page) or from two independent sources.
   - **Single source**: one source only.
   - **Inferred**: the agent's own conclusion.
   - **Not found**: the agent looked and couldn't find it.

   Each claim should link to its source, with the retrieval date and the supporting quote. Put a "what we checked and what we couldn't" summary on page 1. Reporting gaps honestly is what builds trust.

5. **Restructure the report.**
   - Put a one-page summary first, with the assumptions stated at the top ("Rivals: A, B, C. Region: EU + UK. Period: 2025–26").
   - Make the main deliverable a web report with expandable evidence, and offer the PDF as an export. Evidence trails fit badly in a PDF.
   - Add a "Change an assumption and re-run" link that reuses cached research.

6. **Handle failure with a recovery path.** If a client finds a wrong turn late, a partial re-run should be cheap and fast, and you could offer a credit. Without that, a wrong guess still costs them a full day.

## How to tell it's working
- Share of runs where the client edits the plan at scoping (the plan is useful if this is non-trivial).
- Share of runs redirected at the 20–30 minute check.
- Re-run and refund rate, which should drop.
- How many clients open the evidence links, which shows whether the verification labels are used.

If you want, I can draft the scoping screen, the claim-label design, or the activity-view copy next. If the app code is available, point me to it and I can check what the current progress UI actually reports.
