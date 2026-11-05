**Why they skip**

Step 1 says nothing useful, and it's the only thing people see before the Skip button. It's a "Welcome" with no reason to continue. The tour also looks like a long one: seven steps, stacked over the dashboard they came to use. People skip to get to the product.

The other steps would earn the same reaction if people got that far:
- **It's an inventory.** Steps 2, 3 and 4 list every sidebar item, top-bar control and dashboard widget. Nobody remembers a list of nine items. They can read the same labels on the screen.
- **Nothing is done.** The tour describes the product but never has the person do anything. Step 5 describes invoice creation and lists five options, but doesn't let them create one.
- **The tour covers the whole dashboard.** A new user has no invoices, so the dashboard probably shows empty or zero values. Describing "revenue this month" and "overdue invoices" gives them nothing to look at.
- **It comes too early.** Step 6 (bank connection) is a setup chore, and it comes before they've seen any value.
- **"You're all set!" is empty.** They haven't done anything yet.

Skipping step 1 is a sensible reaction. It isn't a sign the users are uninterested.

**What I'd change**

Replace the tour with a guided first task. For a freelancer's invoicing tool, the one thing they should be able to do afterwards is: **send their first invoice.**

1. **Fix the interface first.** If people can't find "create invoice", make the + button labeled ("New invoice") and put it in an obvious place. Make the empty dashboard say what it's for (see 4).
2. **Drop steps 2, 3, 4 and 7.** The sidebar, top bar and dashboard labels already explain themselves. Search, notifications and help need no tour.
3. **Replace the tour with a short guided path.** On first login, show one dismissible card, not an overlay on top of everything:
   > **Send your first invoice**
   > Add a client, a line item and a due date. Takes about [X] minutes.
   > [Start] · Skip for now
   
   Fill the time estimate in from real timing, since I don't have it.
   Then open the real invoice form with a sample client and line item, clearly labeled "Sample", replaceable in one action. Show only the few fields that matter (client, line item, due date) and tuck taxes, discounts and the payment link behind "More options". Mention the N shortcut when they next return to the dashboard, as a tooltip beside the + button, not in the first run.
4. **Give the empty dashboard a purpose.** Instead of zeroed widgets, show something like: "Your revenue and overdue invoices will appear here once you send an invoice. [Create invoice]". Hide the cash-flow chart until there is data.
5. **Confirm with what changed.** After sending: "Invoice sent to [client]. You'll see it under Outstanding on your dashboard, and we'll mark it paid when [payment method works]." Fill this in according to what the product really does. That confirmation points to the next step, not confetti.
6. **Offer bank connection later.** Prompt it when the first invoice is sent or when payment matching would help, as a card with the reason ("Match payments to invoices automatically"), not as step 6 of a tour.
7. **Keep skip and a way back.** An obvious "Skip for now", and a "Get started" checklist or help entry that stays reachable.

**How to judge it**

Don't measure tour completion. Measure the share of new users who send an invoice in their first session, and the share who create a second invoice within [N] days without any prompts. Compare against the current flow with an A/B test. Skip rate is a poor measure here, since someone who skips and then sends an invoice anyway is fine.

**Assumptions:** I assumed that most new users' main job is sending invoices, and that the dashboard is empty on first login. If most people arrive with imported data, the dashboard guidance changes. I also haven't seen the actual screens, so check the fixes in step 1 against them.
