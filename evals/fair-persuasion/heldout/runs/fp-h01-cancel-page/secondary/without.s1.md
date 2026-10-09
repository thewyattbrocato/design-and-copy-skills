Before the copy, one dependency: if pause isn't built, don't ship the pause option. Copy promising it would be a broken promise on the page where people are already deciding to leave. I've written the page with a pause option marked as conditional, and a version that works without it.

## Step 1: Ask why (keep this screen short)

**Headline:** Sorry to see you go. What's not working?

**Options (pick one):**
- It's too expensive right now
- I'm not cooking as much as I planned
- The meal plans don't fit how I eat
- I'm not shopping with receipts anymore
- Something else

**Button:** Continue

## Step 2: Tailored offer (one per reason)

**If too expensive → offer annual**
> **Switch to yearly and save $29.**
> Pay $79 for the year instead of $9/month ($6.58/month). Your plan and history stay the same.
>
> [Switch to yearly] [No thanks, cancel]

**If not cooking as much → pause (only if built)**
> **Take a break, not a goodbye.**
> Pause your plan for up to 3 months. Your saved recipes and receipt history stay put, and billing restarts on [date] unless you tell us otherwise.
>
> [Pause for up to 3 months] [No thanks, cancel]

*Fallback if pause isn't built:* Replace with a lighter-plan offer only if eng can build it. If not, show the annual offer here too, or skip the offer and go straight to confirmation. Don't invent a pause.

**If the plan doesn't fit → fix the plan**
> **Let's make it fit you.**
> Update your dietary preferences and household size. Most changes take effect on your next plan.
>
> [Update preferences] [No thanks, cancel]

**If something else → free text**
> Tell us more. It helps us improve.
> [text box]
>
> [Send and cancel] [Go back]

## Step 3: Confirmation

**Headline:** Your subscription is canceled.
> You'll keep full access until [end date]. After that, your plan stops renewing and you won't be charged again.
> Your receipt history is kept for [X days] in case you come back. Reactivate anytime from your account page.

**Button:** Done

Fill in [X days] only with a number eng and legal confirm.

## Notes

- **Keep the cancel button easy to find and finish in one flow.** Hiding it or adding several extra steps invites chargebacks and reviews, and some state auto-renewal laws (California's is the strictest) require cancellation to be about as easy as signing up. Have whoever handles legal check the flow.
- **Test the annual offer first.** It's the only offer here that needs nothing new from eng, and price-based saves usually move the most people. A/B test the copy against a control with no offer, and track saves per cancel attempt, not just total churn.
- **Avoid guilt copy** ("We'll miss you so much 😢"). It reads as pressure to people who've already decided, and it works worse than a plain, useful offer.
- **Watch month 2–3 specifically.** If the churn spike is tied to not having a grocery-receipt habit yet, a better onboarding nudge for the second week may do more than any cancel-page copy. Worth checking your data on what those users did in their first two weeks.

Want me to adjust the tone, or write the pause version once eng confirms the timeline?
