**Why they skip**

1. **Step 1 is a dead-end ask.** "Let's take a quick tour" gives no benefit, and the user doesn't know how long it is. A new user came to send an invoice, so they dismiss it. The 80% skip rate on step 1 mostly measures that they don't want the tour right now. It says little about whether the content is good.
2. **It looks like 7 steps of feature listing.** Steps 2–4 read out the UI (9 sidebar items, 5 top-bar items, 5 dashboard widgets). These are labeled and visible, and they're hard to remember. Nothing in them helps the user do anything.
3. **Timing is wrong.** On first login the dashboard is empty, so step 4 describes widgets with no data in them. The tour is also not tied to the user's goal.
4. **The valuable parts come late.** Creating an invoice (step 5) and connecting the bank (step 6) are the only actionable steps, and they come after three steps users have to click through to reach them. Most users never get that far.
5. **It's modal and blocks the screen.** It shows on first login, over the product, before the user has tried anything.

**What I'd change**

- **Cut it to 2–3 steps focused on one job: send your first invoice.** Drop the sidebar, top bar, and dashboard walkthroughs. People find those on their own.
- **Open with a benefit and a choice.** Something like: "Send your first invoice in about 2 minutes." The buttons would be **Create invoice** and **Maybe later**. Don't use Next/Skip.
- **Make it interactive.** Highlight the + button and have the user click it. Then guide them through the invoice form, covering client, line item, and send. Don't list features such as taxes, discounts, and payment links. Surface those as inline hints in the form.
- **Move the bank connection out of the tour.** Show it as a dismissible checklist item or a prompt after the first invoice is sent, when matching payments has a clear point.
- **Don't force the tour.** Keep a persistent "Getting started" checklist (create invoice, add client, connect bank) and a "Replay tour" link in the help menu.
- **Show the keyboard shortcut (N) later.** Use a tooltip or hint after the user has created a couple of invoices.

**How to measure**

Don't judge it by skip rate. Track the share of new users who send an invoice within 24 hours or 7 days, and compare the new flow with the old one in an A/B test. If the new flow has a higher skip rate but more first invoices sent, that's still a win.

I'm assuming the analytics are accurate. It's worth checking whether "Skip" is clicked at the same rate for users who arrived from an invite or a team workspace. Those users may not need an intro to the product at all.
