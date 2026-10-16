**Verdict:** Remove the tour. Step 1 is the first thing standing between a new user and their task, and its only promise is more of the same. Skipping it is a reasonable response to that.

**Why people skip**

- **Step 1 is a gate with no payoff.** "Let's take a quick tour" asks for time before anything useful happens, and the user has no reason yet to believe the tour is quick or worth it.
- **Steps 2 to 4 describe what is already on screen.** They list nine sidebar items, five top-bar items and four dashboard metrics. That is an inventory, and nobody can remember it, so the effort buys nothing.
- **The one useful action is buried.** Creating an invoice (step 5) is the task that matters, but it comes after four passive steps.
- **Step 6 asks for a setup task inside a tour.** Connecting a bank needs credentials and time, so it is a poor fit for a passive walkthrough.
- **Step 7 has no next action.** "You're all set!" ends the tour without pointing anywhere.

**What to change**

1. **Replace the tour with a first task.** The first-login goal is "one invoice created." Put the user straight into the invoice form, with a single sentence saying what they're doing, and show the + button or the N shortcut in context.
2. **Make the empty dashboard explain itself.** Say what the area is for, and give one action such as "Create your first invoice." Hide or disable controls that have no data yet, such as the cash-flow chart. Don't make an illustration the largest element.
3. **Offer sample data only if you have it.** A "use a sample invoice" option is useful, but label it as sample and make it removable in one action. Don't show plausible numbers that could be mistaken for the user's own.
4. **Explain fields where they appear.** Line items, taxes, discounts, due date and payment link are visible in the form, so give short hints beside the fields that need them. Don't list them in a tour.
5. **Move bank connection out of onboarding.** Prompt for it after the first invoice is saved, with "Connect now" and "Later." Say what it does in their terms: "Connect your bank so payments match invoices automatically."
6. **Keep skip and return paths visible.** Anything you do show needs a skip, and help should be findable later from the help center.

**What to measure**

Track whether people create an invoice in their first session, and again within a week, without help. That matters more than whether they finish a tour. I don't have your baseline numbers, so set the target from your current data before you ship the change.

**Assumptions**

- I haven't seen the product. I assumed the dashboard is empty for a new user and that the Welcome screen is the only gate before the tour.
- If the 80% skip figure comes only from step 1, check how many people reached step 5 before you judge the later steps.
