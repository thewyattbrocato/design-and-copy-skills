# Talking points: design system investment

*I read "a quarter of two people's time" as 25% of two people's capacity, about half an FTE. If you mean two people for a full quarter, change the cost framing in point 4.*

## 1. Open with the business problem
"We run one brand across a website and an app, built by three squads. Each squad currently solves the same problems on its own: how a recipe card looks, how checkout behaves, how we show a promo or an out-of-stock meal. I'm asking for a small, time-boxed investment so we build those things once and all three squads reuse them."

## 2. What they get, by audience
- **COO (speed and reliability):**
  - Features that touch shared pieces, like menus, delivery windows and checkout, ship faster because squads aren't rebuilding them.
  - Fewer "it works on web but not in the app" bugs and fewer rework cycles.
  - New hires and contractors get productive faster.
- **Head of sales (conversion and campaigns):**
  - Customers get the same experience on web and app, which builds trust at the moment they enter payment details.
  - Seasonal promos, new plans and partnership landing pages can launch faster because the building blocks already exist.
  - Fixes to checkout friction and accessibility land everywhere at once instead of three times.
- **Finance (cost and risk):**
  - We're paying for the same work multiple times. This moves that spend toward work that's reused.
  - It's a capped, defined investment, not an open-ended team.
  - Accessibility issues carry legal exposure, and a single source of truth lowers it.

## 3. Be upfront about the numbers
"I don't have a precise measure of the time we lose today, and I don't want to make one up. Here's what I'm confident in: squads are building similar things independently, and that's the kind of waste a design system removes. I'm proposing we measure it as part of the work."

Then offer a quick, credible estimate:
- Ask each squad lead: "In the last quarter, how many days went to rebuilding or fixing UI that another squad already had?"
- Count the visible inconsistencies. For example, how many different button styles or checkout error messages exist across web and app?
- Pull a few tickets tagged "UI bug" or "visual inconsistency" and add up the time they took.

You can say: "I can have a rough baseline within two weeks, and we'll use it to judge whether this worked."

## 4. Frame the ask as a bounded bet
- **Cost:** "About half of one person's capacity for one quarter. That's roughly [X] in loaded cost." Ask finance to fill in the figure so it's their number.
- **Scope:** Start with the 5 to 8 pieces used most, such as buttons and forms, the recipe card, the cart and checkout elements, and notifications. We won't try to cover everything.
- **Checkpoint:** At six weeks, show how many screens and flows use the shared pieces and what the squads report.
- **Exit:** "If the baseline shows the waste is small, we stop and you've lost a few weeks of part-time effort."

## 5. How we'll know it worked
Pick two or three, and avoid anything we can't measure:
- Time to build a new screen or promo page, before and after (a rough comparison is fine).
- Number of UI bugs and inconsistency tickets per sprint.
- Share of web and app screens using the shared pieces.
- Squad leads' own estimate of time saved, collected by survey.

## 6. What it costs to wait
"Every new feature adds to the inconsistency we'd have to clean up later. This is cheapest to fix while we have three squads. It gets more expensive as we add squads or features."

## 7. Likely questions
- **"Why not just hire for this?"** "A small start tells us whether the need is real before we commit headcount."
- **"What gets delayed?"** Decide this beforehand and name it. Leadership will trust the ask more if you've already thought through the tradeoff.
- **"Can you prove ROI?"** "Not yet. That's why the first two weeks produce a baseline, and why there's a checkpoint."
- **"Is this just a designer project?"** "No. It needs engineers from the squads. The benefit shows up as faster delivery for them."

## Closing line
"I'm asking for a small, capped investment to stop paying three times for the same work. In two weeks you'll have a baseline, at six weeks a progress check, and you can stop it at either point."

Tell me which squad pain points or recent incidents you can name, and I'll swap in a concrete example for each audience. One real story, such as a promo that took too long or a checkout bug that appeared on only one platform, will persuade this group more than the general argument.
