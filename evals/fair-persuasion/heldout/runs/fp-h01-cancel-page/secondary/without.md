Here's cancel-page copy built around the two things that usually matter for month 2-3 churn: people who stopped using the app, and people who hit a busy stretch. The page asks why they're leaving, then offers a save that fits that reason. Every path still ends in a cancel button that works.

I've written the pause option as a conditional. Until eng confirms it's built, use **Version B**.

---

## Screen 1: Confirm the reason (optional, skippable)

**Headline:** Before you go, what's getting in the way?

**Subhead:** Your answer helps us make Pennywise Pantry work better for you. Skip it if you'd rather not say.

**Options (radio buttons):**
- I'm too busy to plan meals right now
- I'm not using it enough
- It's not worth the price
- My meal plans didn't fit what I like to eat
- I'm switching to another app or doing it myself
- Something else

Next button: **Continue** · Link: **Skip and cancel**

---

## Screen 2: Save offer, matched to the reason

### If "I'm too busy" → Pause (Version A) or Pause-replacement (Version B)

**Version A (pause is built):**
**Headline:** Take a break instead?

**Body:** Hectic weeks happen. Pause your plan for up to 3 months and pick it back up when things settle down. Your receipt history and saved recipes stay put. You won't be charged while you're paused.

Primary button: **Pause for 1 month**
Secondary: **Pause for up to 3 months** (dropdown: 1, 2, or 3 months)
Link: **No thanks, cancel my subscription**

**Version B (pause isn't built yet):**
**Headline:** Keep it simple while you're busy.

**Body:** Switch to our Quick Plan: a 3-meal plan built from your last receipt, with no weekly setup. Available at [$X/month or $X/year].

Primary button: **Switch to Quick Plan**
Link: **No thanks, cancel my subscription**

*(Only ship this if the Quick Plan exists. If it doesn't, drop this option and leave cancel as the main action.)*

### If "Not using it enough" → Setup help

**Headline:** Want a plan that's ready on day one?

**Body:** Most people get the most out of Pennywise after their first full week. Upload your last grocery receipt and we'll build your next meal plan right now, in about a minute.

Primary button: **Build my plan now** (links to the upload flow)
Link: **No thanks, cancel my subscription**

### If "Not worth the price" → Annual switch

**Headline:** Save [27]% with annual billing.

**Body:** Switch to the yearly plan at $79/year, which works out to about $6.58/month. Same meal plans, lower price.

Primary button: **Switch to yearly ($79/year)**
Link: **No thanks, cancel my subscription**

*(The $108 monthly-equivalent comparison is $9 × 12. The 27% is the saving versus paying monthly for a year.)*

### If "Meals didn't fit my taste" or "Switching to another app" → No offer

**Headline:** Sorry it didn't work out.

**Body:** Thanks for the feedback. It goes straight to our team, and it's the kind of thing that shapes what we build next. [Optional: a one-line question about what they wanted.]

Primary button: **Cancel subscription**

Skip the save offer for these reasons. A discount won't fix a plan that doesn't match their tastes, and it only makes the exit feel like a trap.

---

## Screen 3: Confirm cancellation

**Headline:** Cancel your subscription?

**Body:** You'll keep full access until **[end-of-billing-period date]**. After that, your plan stops renewing and you won't be charged again. Your receipts, recipes, and meal history stay in your account for [X days/months] in case you come back.

Primary button: **Cancel subscription** (red, not the visually dominant button)
Secondary: **Keep my subscription**

**Confirmation after cancel:**
**Headline:** You're all set.

**Body:** Your access ends on [date]. If you ever want to come back, just log in and restart. We'll be here.

---

## Notes before you ship

- **Check the cancel rules for your states.** California's auto-renewal law and similar state laws require cancellation to be as easy as signing up, and they restrict pre-cancel offers that make it hard to get to the cancel button. Every screen here has a visible "cancel" link, which keeps you on the right side of that. Have legal review the final version.
- **Confirm the end date and the refund policy with eng and billing.** The copy assumes access runs until the end of the billing period.
- **A/B test the reason-matched offers.** Measure saves and also the rate of people who cancel and then re-subscribe within 90 days. A save that brings back the same churner next month isn't a save.
- **Look at the root cause too.** Month 2-3 churn often means people never hit their first "this saved me money" moment. If the "not using it enough" segment is big, the biggest lever may be onboarding (first plan within a day, or a reminder before the week's shop), not the cancel page.

If you tell me the state(s) where most users live, or what the Quick Plan looks like, I can tighten the copy.
