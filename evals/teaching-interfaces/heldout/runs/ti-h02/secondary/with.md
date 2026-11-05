**Why people skip:** the tour asks for trust before it gives anything back. Step 1 is a greeting with no outcome, so a new user who doesn't yet know what they'll get from the product has no reason to sit through six more Next clicks. Steps 2 to 4 are an inventory of controls, and step 5 describes creating an invoice without letting them do it. Step 6 asks them to connect a bank, which they aren't ready for on first login. Step 7 is ceremony. Skipping at step 1 is the rational response to this structure. The skip rate is a symptom of the tour itself, not of impatient users.

**What I'd change:** replace the tour with a guided first task.

1. **Step 1 names one outcome.** Something like "Send your first invoice in about two minutes." Keep the Skip button, and add a visible way back ("Replay the tour" in Help).

2. **The task is the tour.** Pre-fill a sample client and one line item, both labeled "Sample" and removable in one click. Put the `+` button and the `N` shortcut on screen, pointing at the real control, with one line on what each field is for. The person creates the invoice, previews it, and sends or saves it. Confirm the win in one line: "Invoice #1 is ready. Clients who pay faster usually have a due date set." Then offer the next step.

3. **Sidebar and top bar become hints at the point of use.** Don't explain nine menu items up front. When someone first hovers or visits Invoices, Expenses or Tax Center, show a short tooltip with what it's for. Ignore and dismiss are both easy.

4. **The dashboard's empty state explains itself.** Instead of a card for each metric, say what the numbers will show once there are invoices, with one action: "Create your first invoice." Hide report and chart controls that have no data yet.

5. **Bank connection moves out of the tour.** Show it after the first invoice is sent and unpaid, as a banner: "Connect your bank to mark invoices paid automatically." This is the moment it matters, and it's a real task with a real result.

6. **Cut step 7.** The confirmation in step 2 already does that job.

**Measure the right thing.** Track whether people create and send an invoice unaided in their first week, not whether they finish the tour. Step 1 skip rate tells you little on its own. Compare first-week invoice creation before and after the change.

Two notes: I haven't seen your analytics beyond the 80% step 1 skip figure, so I can't say whether a sample invoice or a different entry point would be best for every user segment. And if most of your users arrive with a specific reason, such as clients or a migration from another tool, a short branch on the first question might beat a single path.
