**Why they skip**

1. **Step 1 promises nothing.** "Let's take a quick tour" tells a freelancer who just signed up to invoice someone that the next minutes are about Ledgerlark, not their work. Skip is the rational choice. The 80% skip rate on step 1 is mostly a verdict on the premise, not on the copy.
2. **The tour is an inventory.** Steps 2–4 name about 20 things (9 sidebar items, 5 top-bar items, 5 dashboard widgets) and ask people to remember them. Nobody can. Most of these labels are self-explanatory and need no teaching.
3. **It sits over the dashboard.** At first login the dashboard has no revenue, no invoices and no clients, so you describe widgets that are empty.
4. **The one useful step comes late.** The real task, creating an invoice, is step 5 of 7. Banking in step 6 is a separate job that belongs later.
5. **Step 7 is ceremony.** "You're all set!" teaches nothing and delays the work.

I'm inferring this from the copy, because the analytics show only the skip rate. People may also be skipping because the tour covers the screen, or because they're returning users on a new workspace. You can check both (see the last section).

**What I'd change**

Replace the tour with a guided first invoice. The goal sentence is: *"Afterwards they can create and send an invoice."*

- **Open on the task, not a tour.** Show one line on the dashboard or an empty state: "Send your first invoice. It takes about [N] minutes." Use two buttons, **Start** and **I'll explore myself**. Fill in `[N]` from real timing data. Skipping stays one click and can be undone later from the help center.
- **Teach in the real create-invoice screen,** with 3 short steps attached to the fields themselves:
  1. Add a client (or pick a labeled sample client, replaceable in one action).
  2. Add line items. This is where taxes and discounts live, so mention them here, in context.
  3. Set a due date and send, or copy the payment link.
- **Confirm what happened,** not "Great job!". For example: "Invoice sent to [client]. You'll see it under Outstanding on your dashboard, and it turns Overdue after [due date]." This ties the dashboard to something real, and the dashboard widgets then explain themselves.
- **Cut steps 2, 3 and 4 entirely.** The sidebar, top bar and dashboard labels are the interface. If a particular label confuses people in support tickets or session recordings, rename that label.
- **Move banking to a later, real moment.** Show it after the first invoice is sent ("Want payments matched automatically? Connect your bank in Settings > Banking") or as a dashboard prompt once an invoice is outstanding. Don't show it as step 6 of a tour.
- **Keep the `N` shortcut as a small hint** on the + button tooltip. It's for experts, not for a first-run script.
- **Resume later.** If someone skips, leave a small "Send your first invoice" item on the dashboard until they have sent one. Don't use streaks or nagging emails.

**How to judge it**

Don't use tour completion as the measure. Track:
- the share of new users who send an invoice in session 1,
- the share who send one without help within 7 days,
- support tickets about "how do I…" topics.

To test my guesses about the cause, A/B the new flow against the old tour. Also compare skip rates for users who arrive with an empty workspace against users who are joining an existing one.
