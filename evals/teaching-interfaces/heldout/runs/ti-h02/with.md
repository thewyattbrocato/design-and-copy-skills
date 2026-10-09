**Verdict:** People skip because step 1 asks for their attention and gives nothing back. They've just signed up to send an invoice, and a modal covers the dashboard with "let's take a quick tour." The rest of the tour confirms the instinct. Steps 2–4 list parts of the screen they can already see. Steps 5–6 are the only useful ones, and they sit behind four steps of inventory.

The 80% skip rate on step 1 is evidence about the opening. It says nothing about the later steps, because almost nobody gets that far. The next check is how many skippers create an invoice in their first session.

**Why it fails**
- **It blocks the job.** The tour covers the dashboard before they've done anything.
- **It's an inventory.** Steps 2–4 name about 19 items (9 sidebar entries, 5 top-bar items, 5 dashboard widgets). Nobody retains that, and sidebar labels like "Invoices" and "Clients" explain themselves.
- **The useful content is buried.** The one thing a freelancer came to do, create an invoice, is step 5. Step 5 also packs in six features.
- **Step 1 and step 7 are filler.** "Welcome" and "You're all set!" teach nothing, and "all set" is false because they haven't sent anything.
- **Bank connection is mistimed.** It's a setup chore, and it's pitched before they have any invoices to match.

**What I'd change**

1. **Cut the tour and use a guided first task.** The goal is: *afterwards they can send their first invoice.*
2. **Replace the modal with a dashboard empty state.** Say what the dashboard is for and give one action, "Create your first invoice." Hide or mute the zeros in the revenue, overdue, and cash-flow widgets until there's data. Don't show fake numbers.
3. **Make the invoice form the lesson.** Pre-fill it with clearly labelled sample content that can be replaced in one action, such as a sample client and line item. Add one-line hints beside only the fields that need them: due date, tax, and payment link. Put discounts and extra line-item options behind "more options."
4. **Confirm with what now works.** After sending, say something like "Sent to [client]. You'll see it under Outstanding, and it turns Overdue after [due date]." That also introduces the dashboard widgets, in context.
5. **Move the shortcut and bank link to later.** Show "press N" as a small hint on the + button, or after the second invoice. Offer bank matching once they have a sent invoice: "Connect your bank to mark this paid automatically."
6. **Keep help available.** Put a "Take a tour" or "Getting started" link in the help center for people who want the sidebar and top-bar walkthrough. Never make it mandatory.

**If you must keep a tour**, use three steps tied to that first success: (1) the + button to create an invoice, (2) where it appears afterwards, and (3) bank matching. Make Skip obvious and let people come back to it.

**How to judge it:** Compare first-session invoices created, and invoices created in days 2–7 without help, between the old and new flows. Tour completion rate isn't the right measure.

*Assumptions: I haven't seen the actual UI, so I'm inferring from the copy. A sample client and invoice are a suggestion, and the form fields should match whatever your invoice form really has.*
