**Why they skip**

1. **Step 1 asks for time and offers nothing.** "Let's take a quick tour" is a cost with no stated payoff. Users are in the middle of a goal, which is probably to send an invoice, and a modal over the dashboard blocks it. Skip is the quickest way to get on with that goal.
2. **They can see the length and the content type up front.** Most tours show "1 of 7" or imply it. Seven steps is a lot for a first login.
3. **The tour is a feature inventory, not a path to value.** Steps 2–4 read out UI that is already visible: the sidebar items, the top bar, the dashboard widgets. Nobody retains a list of nine nav items. It's also the wrong moment, since a new user's dashboard is empty.
4. **The one useful step comes too late.** Creating an invoice is step 5, and the bank connection is step 6. Step 7 ("You're all set!") adds nothing.
5. **It fires at the worst time.** It pops up on first login, before the user has any context or intent.

Step 1 gets 80% skips partly because it's the only step most people ever see. It tells you the tour as a whole isn't wanted, but not whether the content is bad. Check how many users click through step 1 and then drop off at steps 2–4. That would confirm the inventory steps are the problem.

**What I'd change**

- **Cut it to a goal-driven flow of 2–3 steps.** Freelancers come to send an invoice and get paid, so build the tour around that.
  1. Spotlight the **+ New invoice** button: "Send your first invoice in about 2 minutes." The button is the call to action, and clicking it starts a real invoice instead of advancing a slide.
  2. After the first invoice is sent, offer the payment link and bank connection: "Get paid faster: add a payment link / connect your bank."
- **Drop steps 2, 3, 4, and 7.** Labeled, visible UI doesn't need narration. If you want discoverability, use small hotspots or tooltips on first hover.
- **Make the first screen a choice.** For example: "Create an invoice" (primary) and "Look around first" (secondary). That replaces a Skip that feels like rejecting the product with a path that serves the user's goal.
- **Don't block the screen.** Use a non-modal checklist or a dismissible card on the dashboard, such as "Send your first invoice / Add a client / Connect your bank". Users can do these when they're ready, and progress is visible.
- **Move the keyboard shortcut and the long feature list into contextual hints.** Show the "N" tip after they've created an invoice by clicking, when it's relevant. Put the invoice details (line items, taxes, discounts, due date) in the invoice form itself.
- **Use empty states to teach.** An empty Invoices or Clients page with a clear "Add your first client" button teaches more than a slide.

**How to measure**

Don't judge it by Skip rate. Track activation: the share of new users who send a first invoice within 24 hours or 7 days, and time to first invoice. Run the new flow against the old tour as an A/B test, with a no-tour control if you can, because the tour may not be helping at all.
