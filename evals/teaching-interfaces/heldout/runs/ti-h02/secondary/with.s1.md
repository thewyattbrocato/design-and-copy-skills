**Verdict:** The tour is an inventory of the product, shown before anyone has a reason to care. Step 1 gives the user nothing to do and a seven-step promise of more of the same, so 80% leave at the first click.

**Why people skip**

- **No task.** Every step says "this is X" and asks for nothing. The user never does anything in the product, so the tour teaches nothing they'll remember.
- **It blocks the screen.** It sits over an empty dashboard, so the user can't see what the tour is describing.
- **It duplicates the interface.** Step 2 reads the sidebar aloud, and step 3 does the same for the top bar. Those labels are already on screen.
- **It front-loads features they don't need yet.** Step 6 (bank connection) and the invoice options in step 5 matter only after a first invoice exists.
- **Length signals a chore.** "Quick tour" followed by seven steps reads as a gate, not a help.

**What I'd change**

1. **Replace the tour with one guided first task.** Goal: "After this, you can send an invoice." The empty Invoices area has one primary button, "Create your first invoice," and the form is pre-filled with a sample client and line item, labeled *Sample*, with a one-click replace.
2. **Cut steps 1, 2, 3 and 7.** Labels don't need a tour. Keep "Skip" visible, and don't show the tour again once it's been dismissed.
3. **Move step 4 into the dashboard's empty state.** Say what fills each card once there are invoices, and hide cards that have no data yet.
4. **Move step 6 to the moment it matters.** After the first invoice is sent, show a single prompt: "Connect your bank so paid invoices mark themselves." Keep it dismissible.
5. **Keep step 5's content, but put it in the form.** Show line items, taxes, discounts and the payment link as the user reaches each field, not as a list up front. Mention the `N` shortcut in the button's tooltip.
6. **Use at most three anchored tooltips, each on the element it describes,** and only if the user stalls.

**How to measure it:** Track the share of new users who send a first invoice within their first session, and again at day 7 without any help. Skip rate alone doesn't tell you whether the change worked.

**Caveat:** The analytics show *that* people skip, not *why*. Watch five or so first-login sessions, or ask the first few skippers one question, before you commit to the redesign.
