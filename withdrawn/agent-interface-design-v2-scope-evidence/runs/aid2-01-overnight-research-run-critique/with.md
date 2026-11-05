**Assumption:** each run is a one-off, read-only job. It reads the web and never contacts anyone, so the risk is wasted hours and unearned trust, not harm. The client usually leaves the page after clicking Start.

## Diagnosis

Deepfield is judged once, at the end, so a wrong turn at minute 10 compounds unseen for five hours. A spinner and a percentage hide that. The percentage also says nothing about direction, so "62%" can mean 62% of the wrong report. Reports that don't separate verified from inferred claims make the problem worse, because clients can't tell what to trust.

## Walking the experience

**1. Before Start: a free-text question goes straight into a five-hour job.**
"Top three rivals … Europe" has at least three unresolved choices: which rivals, which countries (EU, EEA, UK?), and what period. The agent silently picks, and that is exactly what clients complain about.

- Change: after the question is typed, show **how Deepfield read it** in plain words before Start is enabled:
  > Rivals: Acme, Borealis, Corvid (picked because they rank highest in your category; swap any). Region: EU-27 + UK. Period: 2025 to date. Pricing means list prices, plan changes and promotions. Not covered: channel partner pricing.
- Each item is editable. Where the agent guessed, mark it "my guess" and make it one tap to change.
- Show a plan the client can cut or reorder, with the stop-and-ask points marked. Include a line like "While you're away it will read public sources and will never contact anyone or log in to anything."
- Ask about only what is ambiguous, not a long intake form. If the rival choice is truly uncertain, say so.

**2. First 15–20 minutes: the cheap checkpoint is missing.**
The scoping phase (identify rivals, region, period, sources) is the one that decides whether the next five hours are wasted. Make it a gate.

- Change: run scoping first, then pause and send a short **seam check-in** (email and in-app): "Here's what I'm about to research. Rivals, region, year, and the 5 sources I'll lean on most. Reply 'go' or fix anything." Set a timeout, for example it proceeds on its reading after N hours of silence (N is yours to choose), and say so in the message. Don't make the client's inbox a blocking dependency.
- Add a second, lighter seam after the first findings (for example, after the first rival's pricing page is analyzed): "This is what I found for Acme. Is this the level of detail you want?" Wrong depth is the next most likely complaint.
- Between later phases, give a two-line statement: goal as it now reads, assumptions, what's next. A phase can then be rerun without the bad assumption carried forward.

**3. During the run: the spinner and percentage.**
They carry no information the client can act on, and they train people to ignore the page.

- Replace them with one watch view: current phase, phases done, a running list of **findings so far** (even rough), sources read, and an on-demand log.
- Show pause and stop one step away. They differ: pause keeps state and accepts new direction (including "drop Corvid, add Delta"). Stop ends now, keeps what's finished, and says what was half-done. Acknowledge any new instruction at once, even if it applies at the next phase.
- Drop the percentage, or relabel it as phase progress. Don't show an ETA you can't back; if you show one, label it an estimate.
- Notifications: one at the scoping gate, one if something needs the client (a rival is ambiguous, sources are blocked, the question can't be answered as asked), and one on completion. No per-step pings. A problem found early ("I can't find European pricing for Borealis") should interrupt then, not appear in the PDF as a footnote.

**4. The report: 30 pages with no map of what's solid.**
This is where "I can't tell what it verified" comes from.

- Open with a one-page summary that begins with the **scope as run** (rivals, region, period, exclusions) so a mismatch is spotted in seconds.
- Mark every claim with a status, visible in the PDF and the web view:
  - **Verified**: found in a primary source (price page, filing) and the agent shows the link and date accessed.
  - **Corroborated**: two or more secondary sources agree.
  - **Single-source or inferred**: stated with its basis.
  - **Not found**: say what was looked for and where. A gap is information, so don't paper over it.
- Put the doubtful items first, in a short "check these before you use them" list near the front, not buried in an appendix.
- Include a "what I assumed" list, including every guess the client confirmed or didn't correct at the gate.
- Show sources per claim (footnote or margin), with archived snapshots where possible, because pages change.
- Don't invent a confidence score or "95% verified" figure. Counts of claims by status are fine because they are real counts.

**5. After reading: the only remedy today is another five-hour run.**
- Add **refine, not rerun**: from any section, "this is the wrong rival / wrong region / go deeper here," which reruns only that part. Keep the rest.
- Let the client accept or flag individual sections, with flagged ones feeding the refine. Keep a record of what was accepted.
- Offer "always" versus "this time" for preferences ("always treat Europe as EU-27 + UK"), shown as a plain-language saved rule that the client can see and edit.

## Priorities

1. **Restate the question and get confirmation before Start.** This is cheap and likely removes the largest class of complaints.
2. **Scoping gate at the first 15–20 minutes** with a reply-to-fix path and a stated timeout.
3. **Claim-level verification status** and a doubtful-first list in the report.
4. **Replace the spinner and percentage** with findings-so-far, pause, stop and steer.
5. **Section-level refine** instead of full rerun.

## Caveats

- The gate adds friction and some clients won't answer. Measure how often the confirmed scope differs from the first reading, and how often the timeout path is taken. Those are the numbers to track, and I haven't assumed any values.
- Verification labels are only worth showing if the pipeline can really tell primary from secondary sources. If it can't yet, ship "sources per claim" first and add labels once they're trustworthy. A wrong "Verified" is worse than none.
- I haven't seen the app or the report, so this is based on your description. If you share a sample PDF and the current Start screen, I can make the changes concrete, including exact screen text.
