**Why people skip**

- **It asks for time before giving anything.** "Let's take a quick tour" with seven modal steps reads as a chore. Someone who just signed up wants to make an invoice, so Skip is the fastest way back to the task.
- **Step 1 is pure ceremony.** Nothing on screen is useful yet, so people decide the tour isn't worth their attention. The 80% number is mostly about step 1's value, not the later steps.
- **It describes instead of showing.** Steps 2 and 3 list nav items and top-bar buttons the user can already see. Step 4 describes revenue and overdue charts that are probably empty for a new account, so it talks about data they don't have yet.
- **It's generic.** Nothing connects to what a freelancer actually needs: get the first invoice sent and paid.
- **It blocks.** A modal stack over the dashboard interrupts the user before they've decided to explore, and Skip is the obvious way out.
- **The bank step is premature.** Connecting a bank before the user has an invoice has no payoff yet.

**What I'd change**

1. **Replace the tour with a setup checklist** on the dashboard, something like "Get paid in 3 steps": add business details, send your first invoice, connect your bank. Each item is a real action, progress saves, and the user can dismiss it or come back to it. It respects that people arrive with a goal.
2. **Make the first step an action, not a message.** Highlight the + button with a short tooltip: "Create your first invoice (or press N)." Advance when they actually click it. Doing it teaches more than reading about it.
3. **Use contextual tooltips, not a modal sequence.** Show one hint the first time someone reaches a feature (e.g., the first visit to Settings > Banking shows "Connect your bank to match payments automatically"). Anchor each to the element it describes.
4. **Use empty states as onboarding.** The dashboard with no invoices should say "No invoices yet. Create your first one" with a button, not show a chart of zeros. This is where most of the teaching should happen.
5. **Keep Skip, but make it low-stakes.** Show the checklist as a non-blocking card, and if you keep any modal, make "Skip" and "Start" equally visible.
6. **Measure activation, not tour completion.** The metric that matters is whether users send their first invoice within 7 days, and whether the checklist or tour changes that. Analytics on who skipped step 1 won't tell you that.

If you want a quick test, run the checklist against the current tour for a cohort of new signups and compare time-to-first-invoice. Since I haven't seen the actual UI, check whether Skip is visually more prominent than Next, because that alone can drive a lot of the skip rate.
