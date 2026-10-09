**Why people skip**

1. **It's a wall of 7 modal steps over the dashboard.** Users arrive with a goal (send an invoice, see what's owed). Step 1 promises "quick" but offers no value, so skipping is the rational choice. Skip on step 1 is basically a reaction to the format, not a judgment on the content.
2. **Step 1 says nothing.** "Let's take a quick tour" asks for time and gives nothing in return.
3. **The content is a feature inventory.** Steps 2-4 list nine sidebar items, five top-bar items and five dashboard widgets. Nobody retains that, and most of it is self-explanatory labels. It also covers the UI, not the user's job.
4. **It's front-loaded with orientation and back-loaded with value.** The two things that matter to a freelancer (create an invoice, get paid) are steps 5 and 6, after three steps of navigation trivia.
5. **It's shown over a dashboard that is probably empty.** Revenue, overdue invoices and the cash-flow chart show zeros on first login, so describing them is abstract.
6. **Step 6 asks for a high-trust action (connect your bank) as a passing tip.** Users need a reason first.

**What I'd change**

- **Cut it to 2-3 steps, or drop the tour.** Keep only what leads to the first outcome: a sent invoice.
- **Make step 1 the hook.** Replace it with something like: "Send your first invoice in about 2 minutes." Buttons: **Create invoice** / **Explore on my own**. Skip then becomes a choice between two real options.
- **Turn the tour into doing.** Launch the user straight into the invoice form with contextual hints (client, line items, due date, payment link). A real first invoice teaches more than a description does.
- **Drop the inventory steps (2-4).** Self-explanatory navigation doesn't need narration. If something truly isn't obvious, use a one-time tooltip when the user first reaches it.
- **Defer the bank connection.** Prompt it after the first invoice is sent or paid ("Want payments matched automatically?"), when the benefit is obvious.
- **Add a persistent checklist instead** (Create invoice, Add a client, Send it, Connect bank). It's resumable, non-blocking and shows progress.
- **Keep it re-launchable** from the help center, and mention the `N` shortcut in the invoice flow where it will actually be used.
- **Segment if you can.** Users who import data or were invited to a team workspace need a different path from a solo freelancer.

**How to check it worked**

Measure the share of new users who send an invoice within 24 hours or 7 days, not tour completion. A tour that nobody finishes but that leads to more sent invoices is fine. A tour with 90% completion and no change in activation isn't. I'd A/B the new flow against the current one on that metric. Also check whether the 80% who skip on step 1 activate at a different rate from those who don't. If they activate just as well, the tour may be unnecessary.
