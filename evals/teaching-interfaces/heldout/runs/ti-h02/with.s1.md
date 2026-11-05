**Why they skip**

Step 1 says nothing a person wants. "Let's take a quick tour" promises a lecture, and people who just signed up to send an invoice want to do that, not sit through a tour. The skip rate is also a verdict on the whole tour, because the Skip button is the only preview of what's coming. Seven steps is long, and the tour doesn't try to hide it.

The rest of the tour gives them the same reasons to skip:

- **It's an inventory.** Steps 2 to 4 list 9 sidebar items, 5 top-bar items and 5 dashboard widgets. That's about 20 things to remember, and the person hasn't done anything yet.
- **It covers the obvious.** A sidebar labelled "Invoices" doesn't need explaining.
- **It sits over the thing it describes.** Everything shows over the dashboard, and the dashboard is probably empty or sample data for a new user.
- **The one useful step comes late.** Creating an invoice is step 5, and step 5 itself packs in 6 features.
- **It ends on "You're all set!"** with nothing to do next.
- **It asks for a bank connection** before they've seen any value.

**What I'd change**

Fix first: if the sidebar needs a tour, the labels are the problem. Then replace the tour with a guided first task.

The sentence to aim for is: *afterwards they can send their first invoice.*

1. **Drop the welcome step.** On first login, show one line on the dashboard with a clear primary action: "Send your first invoice. It takes about [N] minutes." The buttons are **Create invoice** and a visible **Skip, I'll explore** link. I've left the time as a placeholder because I don't have a measured figure.
2. **Do the real task in the real product.** The invoice form opens with a few small coach marks, no more than three, and only on fields that aren't obvious: client, line items, and the send or payment-link action. Add taxes, discounts and due date as optional extras they can find later.
3. **Confirm with what happened.** After sending, say something like "Invoice sent to [client]. You'll see it under Outstanding, and you'll get a notification when it's paid." Point to the next real action. Skip the confetti.
4. **Move the bank connection** to a later prompt, once they have a sent invoice that a payment could match. Until then, an empty-state prompt on the relevant screen is enough.
5. **Handle the rest on demand.**
   - The `N` shortcut goes in the + button's tooltip.
   - The sidebar and top bar need no explanation.
   - Estimates, Expenses, Reports, Time Tracking and Tax Center each get an empty state that says what the area is for and offers one action.
   - A "Replay tour" or help entry stays available for people who skipped.

**How to check it**

Completion of the tour isn't the measure. Compare the share of new users who send an invoice within 7 days, and the share who create a second invoice unaided, between the old tour and the new flow. Skip rate on the new prompt is a useful secondary signal. I'm not predicting a number for any of these.

Two assumptions: the dashboard is empty for new users, and invoice creation is the core first success. If most people arrive to track time or expenses instead, aim the first task there.
