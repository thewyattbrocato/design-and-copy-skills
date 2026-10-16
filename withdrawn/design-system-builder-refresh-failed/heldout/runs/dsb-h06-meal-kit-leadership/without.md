# Talking points: Design system investment

## The one-sentence version
"We're building the same things three times, on two platforms, and we want to spend a quarter of two people's time so each thing is built once and works everywhere. That makes us faster at shipping changes and keeps the experience consistent for customers."

## 1. Open with the problem in their terms
Skip "components" and "tokens." Talk about what they feel:
- **Speed:** When we want to change something customers see everywhere (a promo banner, the checkout button, the "skip a week" flow), how many places do we touch? Three squads, web and app, means the answer is often "several, by different people."
- **Consistency:** A customer who orders on the website and manages their box in the app should feel like it's the same company. Today that depends on squads happening to make the same choices.
- **Rework:** Each squad solves the same problems independently (forms, date pickers, error states, empty states), and they solve them slightly differently.

## 2. Say plainly what you don't know
This builds credibility with finance. Something like:
> "I don't have a measured number for how much time we lose today, and I'd rather tell you that than invent one. What I have is a strong pattern from how teams like ours work, and a plan to measure it in the first few weeks so you can see whether this is paying off."

## 3. The ask, framed as a bounded bet
- **What:** About 25% of two people's time for one quarter. That's roughly half of one person-quarter in total. Fill in the real cost with finance's loaded rate.
- **What it's not:** An open-ended program or a redesign. It's a scoped effort with a checkpoint at the end of the quarter.
- **What we stop doing:** Be ready to say what gives (e.g. "those two people take on less squad work, which means X slips or slows"). Leadership will respect you naming the tradeoff.

## 4. What they get, by audience

**COO (operations, delivery, risk)**
- Fewer one-off builds and fewer "why does this look/behave differently here" bugs reaching QA and support.
- Squads can ship changes without waiting on each other, which makes planning more predictable.
- New hires and contractors get productive faster because there's one way to do common things.

**Head of Sales (growth, conversion, partnerships)**
- Faster turnaround on seasonal menus, promos, and landing pages. This is the most tangible benefit for a meal-kit business, because so much of it is time-sensitive.
- A consistent, polished experience across sign-up and checkout, where trust and conversion matter most.
- Accessibility baked in once, which widens who can order and reduces legal exposure.

**Finance (cost, return, risk)**
- A defined, capped cost with a measurable checkpoint.
- Savings come from less duplicated work and less rework. This is capacity we get back, not new headcount.
- Lower risk of expensive inconsistencies, like a pricing or legal-copy change that gets missed in one place.

## 5. How you'll prove it (since you have no baseline yet)
Offer to measure this in the first 2–3 weeks, cheaply:
- **Audit:** Count how many different versions of the same elements exist today (buttons, forms, cards) across web and app. It's a concrete, visual number, and it takes a few days.
- **Squad survey or short interviews:** "How many hours last sprint went to rebuilding or reconciling UI that exists elsewhere?" Rough numbers are fine as a baseline.
- **Pick one or two tracked flows:** For example, the time to ship a change to checkout or a promo module, before versus after.
- **Quarter-end review:** Show the audit, the survey, and the before/after on those flows. If the numbers don't justify continuing, say you'll stop.

## 6. Likely questions and short answers

- **"Why now?"** Three squads means the duplication grows with every new feature. It's cheapest to fix before it gets bigger.
- **"Can't the squads just coordinate?"** They can, and they do, but coordination costs time every sprint. This replaces the ongoing coordination cost with a one-time investment.
- **"What if we don't do it?"** Nothing breaks tomorrow. The cost is a slow tax: slower changes, more inconsistency, and more rework as we grow.
- **"How do we know it worked?"** The quarter-end review above: fewer duplicate elements, faster time on the tracked flows, and squad feedback.
- **"Why a quarter?"** Long enough to cover the highest-traffic flows (sign-up, checkout, box management). Short enough to reassess before committing more.

## 7. Close
> "I'm asking for a small, capped investment with a built-in checkpoint. If we measure and it isn't paying off, we stop. If it is, we'll have the evidence to decide whether to do more."

---

**Before the meeting**
- Get the loaded cost for two people at 25% from finance, so you can state the dollar figure yourself.
- Pick one or two specific examples from your own product (a recent promo or checkout change that took longer than it should). A real story lands better than any general argument.
- Decide in advance what work you'd deprioritize, so you aren't improvising it in the room.

If you tell me a recent example or two from Orchard & Pine, I can work it into the opening so it's specific to your product.
