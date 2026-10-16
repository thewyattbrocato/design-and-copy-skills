# Talking points: design system investment

## The one-sentence version
"We're building the website and app three times over, once per squad. I'm asking for a quarter of two people's time so we build things once, ship faster, and stop shipping inconsistencies customers notice."

## Open with the problem
- We have a website, an app, and three squads. Each squad makes its own decisions about how buttons, forms, checkout steps, and error states look and behave.
- Customers don't experience three squads. They experience one Orchard & Pine, and they notice when the app and the site disagree.
- Today, the same problem gets solved several times, and fixes don't carry over. A fix in one place has to be rediscovered and redone in the others.

## Why each leader should care

**COO (speed, efficiency, predictability)**
- This is a capacity play. Every hour a squad spends rebuilding something that already exists is an hour not spent on features.
- Shared parts make delivery more predictable because fewer things are built from scratch.
- It makes onboarding and cross-squad work easier. Someone moving between squads isn't relearning how everything works.

**Head of Sales (customer experience, conversion, credibility)**
- The signup, menu selection, and checkout flows are where customers decide to subscribe or leave. Inconsistency there erodes trust.
- When we want to launch a promo, a seasonal menu, or a new partnership look, we change it in one place, not in three squads' code on three timelines.
- Accessibility and quality become the default instead of something each squad has to remember.

**Finance (cost, risk, return)**
- This is a bounded, visible investment: two people for one quarter, with defined checkpoints.
- The return is recovered engineering and design time, fewer rework and bug-fix cycles, and lower risk on things like accessibility compliance.
- I'll bring numbers at a set checkpoint rather than ask you to take the benefit on faith.

## Be upfront about the gap in evidence
Say this directly. It builds credibility with a finance audience:

> "I don't have a precise number for how much time we lose today. That's partly because no one has measured it. Part of this quarter's work is to establish that baseline, so by the end we can say what we saved, not guess."

Then show you're not hand-waving. Offer a quick way to get a rough number before the quarter starts:
- Ask each squad lead for their best estimate of how often they rebuild or restyle something that exists elsewhere.
- Count visual inconsistencies across the site and app in a short audit (a screenshot comparison of the key flows works well).
- Look at the last few months of design-related bug tickets and rework.
- Even rough figures, like "about 10% of front-end time", are enough to frame the trade-off.

## The ask, made concrete
- **What:** about 25% of two people's time for one quarter.
- **Cost framing:** this is roughly half of one person's capacity. Say that plainly; it's a smaller number than "two people" sounds.
- **Scope:** don't build everything. Start with the parts used in the highest-traffic customer flows (signup, menu browsing, checkout, account management) and the pieces all three squads already duplicate.
- **Not in scope:** a full redesign or a big-bang rewrite. Squads keep shipping and adopt shared pieces as they touch each area.

## What success looks like (so Finance can hold you to it)
Pick two or three and commit to them:
- A baseline measurement of rework and inconsistency, taken in the first few weeks.
- Percentage of the key customer flows using shared parts by end of quarter.
- Time to build a comparable new screen, before vs. after.
- Reduction in design-related bug tickets.
- A short check-in at the midpoint where you report on progress and can stop or adjust.

## Anticipate the pushback

**"Why not just keep shipping features?"**
Because the duplication cost grows with every feature. It's cheaper to fix now with three squads than later with more.

**"Can't we do this in the background?"**
That's what has happened so far, and it's why we have the inconsistencies today. Without dedicated time it gets deprioritized every sprint.

**"How do we know it's working?"**
The measures above, with a midpoint check-in. If the baseline shows the problem is small, I'll say so and we can stop.

**"Why a quarter?"**
It's long enough to cover the highest-traffic flows and get the squads adopting, but short enough to be a contained bet.

## Close
> "I'm not asking you to care about components. I'm asking for a small, time-boxed investment to make us faster, more consistent for customers, and easier to change. And I'm committing to bring back numbers so you can judge whether it paid off."

---

Two things would make this stronger. If you can share anything you know (rough headcount per squad, a recent example where the app and site disagreed, a feature that took longer than it should have), I can swap in concrete Orchard & Pine examples. I can also turn this into a one-page handout or a short slide outline.
