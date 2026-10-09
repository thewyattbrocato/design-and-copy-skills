**Why people skip**

- **Step 1 asks for time before giving anything.** "Let's take a quick tour" is a promise of work with no payoff. A new freelancer who just signed up wants to send an invoice, so Skip is the obvious click.
- **It's a passive lecture.** Steps 2, 3, and 4 describe UI that's already on screen: the sidebar, the top bar, the dashboard. Reading a list of nine menu names teaches almost nothing, and people can see the menu themselves.
- **The one useful step is buried.** Step 5, creating an invoice, is the only action that matters, and it's the fifth of seven screens. Most people will have quit by then.
- **Step 6 is a setup task in the wrong place.** Connecting a bank needs a few minutes and credentials, so it doesn't belong in a first-session walkthrough. It's the kind of step people skip or resent.
- **It blocks the screen.** Showing every step over the dashboard in sequence makes the app feel locked until they've clicked through, so Skip becomes the escape hatch.
- **The ending is flat.** "You're all set!" gives no next action, so the tour finishes without leading anywhere.

I'm inferring these reasons from the copy and structure. The 80% number only tells you where people leave, not why. Watching a few session recordings of skippers would confirm or correct this.

**What I'd change**

1. **Replace the slideshow with a task.** Drop the tour and make the empty dashboard say: "Send your first invoice." One primary button, with the `N` shortcut shown as a hint. This keeps step 5 but makes it the whole onboarding.
2. **Use a persistent setup checklist instead of a modal.** It stays in the sidebar or dashboard header and can be collapsed or dismissed:
   - Create your first invoice
   - Add a client
   - Set up a payment link
   - Connect your bank (*moved here, and optional*)
   Each item checks off when done, so people can come back to it without feeling blocked.
3. **Teach the UI in context, not in advance.** Show a short tooltip the first time someone opens Invoices, Settings, or Reports, pointing at what that page does. Explaining the sidebar before anyone needs it is wasted effort.
4. **Move bank connection to a moment of need.** Prompt for it after the first invoice is sent or the first payment is expected, with the benefit stated: "Match payments automatically so you don't have to."
5. **Make the end of the flow lead somewhere.** When the first invoice is sent, say "Sent! Want to get paid faster? Connect your bank," rather than "You're all set."
6. **Keep Skip, but don't make it the only way out.** Skip should dismiss the checklist, not hide the product. Dark-pattern skip buttons tend to hurt trust with freelancers, who are your core audience.

**How to measure it**

Stop using "clicked Skip" as the success metric. Track whether new users send their first invoice within 24 hours, and compare that across the current tour and the new version. Also check whether skippers return to the checklist later. Completing the tour may correlate with activation, but it's still not proof the tour caused it, so run an A/B test if you can.
