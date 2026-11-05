**Why they skip**

Step 1 says nothing and costs a click, and it's the only place the skip decision gets made. Anyone who signed up to send an invoice sees a modal over their dashboard and a "quick tour" of unknown length, so they dismiss it. That 80% probably isn't a verdict on steps 2–7. It's a reaction to step 1 and what it implies.

Steps 2–7 give people more reason to skip:

- **It's an inventory, not a task.** Steps 2–4 read out the sidebar (9 items), the top bar (5) and the dashboard (5). That's about 19 names to remember, and none of it helps anyone do anything. Most of it is self-explanatory, such as "Settings" or "search".
- **It comes before action.** People retain what they do, not what they're shown. The tour sits on top of the dashboard and blocks the thing it describes.
- **Step 5 is the only valuable one, and it comes fifth.** It also packs in 4 more nouns (line items, taxes, discounts, payment link) plus a shortcut.
- **Step 6 is a different job.** Bank matching is a setup task. It's out of context here, and people can't act on it while a modal is open.
- **Step 7 is ceremony.** "You're all set!" teaches nothing and just delays the exit.

**What I'd change**

The goal: *after the first minute, they can create and send an invoice.*

1. **Drop the tour. Replace it with a guided first task.** On first login, the dashboard shows one clear prompt, such as "Create your first invoice", and the user's real work starts there. Skip stays visible, and so does a way to get help later.
2. **Guide only the parts of the invoice form that aren't obvious.** Use a small number of inline hints beside the field itself:
   - client (pick one or add one)
   - line items
   - due date and payment link
   - the send button

   Taxes and discounts can stay as ordinary optional fields. Their labels should carry the meaning.
3. **Confirm with what happened.** After sending, say something like "Invoice sent to [client]. You'll see it under Outstanding when it's unpaid." That points to the next step and doesn't need confetti.
4. **Move bank connection to its moment.** Show it as a prompt or empty state once there's an invoice that could be matched: "Connect your bank to mark invoices paid automatically." It then comes as a real task at a relevant point, not as step 6 of a lecture.
5. **Give an empty dashboard a purpose.** Before any data exists, the revenue and cash-flow widgets should say what they'll show and offer the one action that fills them (create an invoice). Don't show sample numbers that could be mistaken for the user's own. If you add a sample, label it "Sample" and make it removable in one click.
6. **If the team insists on a tour, cap it at 3 steps,** all tied to that first invoice: the **+ New invoice** button (and N), the invoice's status in the list, and where payments show up. Open with a useful line like "Let's send your first invoice (about 2 minutes)", not "Welcome".
7. **Keep the sidebar and top bar self-explanatory.** If people can't tell what "Tax Center" or the workspace switcher does, fix the labels or add a tooltip that appears on hover. Don't bring them up in a tour.

**How to measure it**

Don't use tour completion. It only shows who clicked Next. Better measures:

- Share of new users who send an invoice within their first session and within 7 days.
- Whether they create a second invoice unaided, without the prompt.
- Bank-connection rate after the contextual prompt compared with step 6 today.
- Support or help-center questions about the features the tour used to cover.

I'd A/B test the guided first task against the current tour on these.

*Assumptions: I only had the tour text, with no screenshots or funnel data, so the diagnosis is inferred from the copy. Whether step 1's skip rate also reflects a timing or layout problem, such as the modal appearing before the dashboard loads, is worth checking.*
