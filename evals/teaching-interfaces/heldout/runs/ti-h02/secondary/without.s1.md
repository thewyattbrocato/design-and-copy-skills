**Why people skip**

- **It delays the product without offering anything in return.** "Let's take a quick tour" promises nothing. People arrive to make an invoice, and the tour stands between them and that.
- **It's a menu read-out, not a set of tasks.** Steps 2 to 4 list nav items and dashboard widgets that are labeled on screen. Nobody needs them explained, and a list of nine names is hard to retain.
- **It's passive.** The user clicks Next nine times and does nothing. Nothing they do in the tour carries over into real use.
- **The valuable steps are buried.** Creating an invoice (step 5) and bank matching (step 6) are the reasons to stay, and they sit behind four steps of inventory.
- **The skip decision happens before any value is shown.** 80% skipping on step 1 means the pitch failed, not that the later steps are bad. Those who continue are likely the people who were already engaged.
- **It ends with no next action.** "You're all set!" leaves the user staring at the dashboard with no idea what to do first.

**What I'd change**

1. **Remove the modal sequence.** Replace it with an empty-state dashboard that has one clear primary button: "Create your first invoice."

2. **Add a persistent setup checklist instead of a tour.** For example:
   - Add your business details
   - Create your first invoice
   - Connect your bank to match payments automatically

   It's visible, shows progress, can be dismissed without losing its place, and can be reopened from the help center. People who skip the checklist still see it, so skipping costs them nothing.

3. **Trigger tips at the moment of need.**
   - On first visit to Invoices: point at "+" and note that N works too.
   - After the first invoice is sent: "Payments not matching? Connect your bank to match them automatically."
   This teaches the same content, but when the user can act on it.

4. **Cut steps 2 to 4.** The sidebar and dashboard are self-explanatory. If you want to keep one orientation moment, make it a single line on the dashboard, not a tour.

5. **Make the opener specific.** For example: "Send your first invoice in about 2 minutes." Give a button that does the thing, not "Next."

6. **Don't block the UI.** An overlay that describes things the user can't touch feels like a wait. Let them click around while the tip is visible.

7. **If you keep a tour at all,** make skip say "Not now" and make it resumable from Help. "Skip" reads as a dismissal of the whole product.

**How to measure it**

Stop using tour completion as the success metric. Track activation instead: percentage of new users who create an invoice within 7 days, and who connect a bank within 14 days. Then compare skippers and completers. If skippers activate at the same rate, the skip rate isn't the problem. If they don't, the checklist-and-tips version should close that gap, and an A/B test against the current tour will show it.
