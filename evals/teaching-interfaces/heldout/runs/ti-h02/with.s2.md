**Verdict: people skip because step 1 offers them nothing, and the other six steps tell them it won't get better.**

**Why they skip (from the script itself)**
- **Step 1 has no value.** "Let's take a quick tour" is a cost to the user, with no payoff. They came to do a job, and this stands between them and it.
- **It's an inventory, not a path.** Steps 2–4 name about 19 things (9 sidebar items, 5 top-bar items, 5 dashboard widgets). Nobody retains that, and most of it is self-explanatory, like "Search" or "Notifications". Seeing the bulk of it coming, people leave early.
- **The tour blocks the thing it describes.** It sits over the dashboard, so people can't try anything. The one useful step, creating an invoice, is fifth. The bank connection in step 6 is a task you're asking them to do later, not something they can do now.
- **Step 7 is ceremony.** "You're all set!" teaches nothing and delays the work.
- **Skip is probably a rational choice.** An 80% skip rate on step 1 means the tour is working as a gate people dismiss. I'd treat that as a design signal and not try to "fix" it by hiding Skip.

**What I'd change**

*Goal sentence:* "Afterwards, they can send their first invoice."

1. **Replace the tour with a guided first task.** On first login, show one line of context and one action: "Send your first invoice. It takes about [N] minutes." Use a button such as **Create invoice** with a quiet **Skip, I'll explore** link. Fill in the time only if you've measured it.
2. **Walk through the real invoice form**, with at most three coach marks on the fields that matter: client, line items, and send. Taxes, discounts, due date and payment link stay optional and unmarked until they reach them. Offer a sample client, labeled as sample and replaceable in one action, so nobody has to invent data to get started.
3. **Confirm with what happened.** For example: "Invoice sent to [client]. You'll see it under Outstanding on your dashboard." That points to the next step without confetti.
4. **Teach the dashboard when it has something to show.** Once they have an invoice, one tip on the Outstanding tile ("This updates when [client] pays") explains it in context. Until then, show an empty state that says what the area is for and offers one action.
5. **Move the bank connection to the moment it matters.** Show it after the first invoice is sent, as an offer: "Connect your bank to match payments automatically", linking to Settings > Banking. Don't put it in a tour.
6. **Cut entirely:** the sidebar and top-bar walkthroughs, the dashboard widget list, the keyboard shortcut (show "N" as a hint on the + button instead), and the "You're all set!" step.
7. **Keep a way back.** Put "Replay the first-invoice guide" in the help center so skipping isn't final.

**Fix before you teach.** If the sidebar's 9 items or the top bar need explaining, that points to navigation problems. Check labels and grouping before you write more help text.

**How to judge the new version**
- Don't measure tour completion. Measure the share of new users who send an invoice within their first session, and the share who create a second invoice unaided within about a week.
- Compare against the current flow as a baseline. I don't have your numbers, so I'm not predicting a lift.
- Check where people abandon the guided invoice (which field), because that shows what to fix in the form itself.

**Assumption:** Ledgerlark's core first success is sending an invoice. If your activation data points elsewhere, such as connecting a bank, swap that in as the goal.
