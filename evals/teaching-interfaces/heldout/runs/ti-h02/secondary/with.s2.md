**Verdict:** The tour teaches the interface by inventory, so step 1 asks for a full minute of reading before anything useful happens. Skipping is the rational response. Fix the first run rather than polishing the copy.

**Why people skip**

- **Step 1 gives no reason to stay.** "Let's take a quick tour" promises nothing the person wants. They came to make an invoice, and the tour stands between them and that.
- **It names the parts of the product, not the job.** Steps 2 to 4 list nine sidebar items, five top-bar controls and five dashboard figures. Nobody can hold that, and none of it says what to do first.
- **It points at things that may be empty.** I'm assuming a new account's dashboard shows zeros and no invoices. A tour that highlights "revenue this month" and "overdue invoices" over empty figures teaches nothing.
- **Stacked steps with no skip on the way.** Seven full-screen-style overlays make the person feel they must finish or dismiss each one, so the cheapest exit is Skip on step 1.
- **Step 5 is the only action in the tour, and it's buried.** The one thing they need is in the middle of a list of features.
- **Step 7 is ceremony.** "You're all set!" comes after nothing they did.

**What I would change**

1. **Delete the tour.** Don't replace it with a shorter tour.
2. **Make the empty dashboard the teacher.** Each empty area says what it is for in one line and gives one action: "Create your first invoice" as the primary button. Hide controls that do nothing yet, and don't show zeroed charts as if they were data.
3. **Offer a guided first task.** "Create your first invoice" opens a draft with a sample client and a sample line item, both labelled as sample and replaceable in one action. The person edits the draft and sends it. Put the `+` and `N` hints on screen during this task, next to the button they refer to, not in a tour.
4. **Introduce the bank connection when it matters.** After the first invoice is sent, show a single prompt: "Connect your bank to match payments automatically." Link it to Settings > Banking. Payment matching is meaningless before anyone has an invoice to match, so step 6 is the wrong moment.
5. **Keep the sidebar and top bar unexplained.** Labels already name them. Explain a term only when it's unclear, like "workspace" if your product uses it in a way people won't guess.
6. **Keep skip and return paths.** Skip should take them to the empty dashboard with the first-invoice action still visible, and Help Center should hold the walkthrough for anyone who wants it.

**How to measure it**

Don't judge the new flow by tour completion. Measure whether people create and send an invoice in their first session, and whether they come back a week later and do it again without help. Compare that with the current cohort's numbers.

**Assumptions:** I haven't seen your empty-state or sample-data behaviour. If the dashboard already has useful sample figures, I'd still keep the sample clearly labelled, and I'd check that no plausible-looking numbers could be mistaken for the person's real data.
