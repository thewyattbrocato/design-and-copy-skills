# Talking points: design system investment

## Opening (the framing)

"We have a website, an app, and three squads, and each one currently builds its own version of the same things: buttons, forms, product cards, the cart, checkout. I'm asking for two people for one quarter to build those once, properly, so every squad can reuse them. That's about half a person-year, and I want to explain what we get back."

Avoid the words "components," "tokens," and "Figma library." Say "shared building blocks" or "one way of doing things."

## What it means for each person in the room

**COO (speed, predictability, operations)**
- Each squad rebuilds common pieces, so the same work gets paid for three times.
- Once the building blocks exist, new features, seasonal menus, and promotions go out faster because squads assemble them instead of building from scratch.
- Fixes happen in one place. A bug in the address form gets fixed once, not three times on web and app.
- New hires and contractors get productive sooner because there's one clear way to build things.

**Head of Sales (customer experience, conversion, campaigns)**
- Customers use us on both web and app. If ordering, swapping a recipe, or checking out feels different on each, it creates friction and erodes trust.
- Campaigns and promos (holiday boxes, referral offers, new-customer discounts) can launch consistently across channels without three separate builds.
- Accessibility and quality get fixed in the shared pieces, so every screen benefits.

**Finance (cost, return, risk)**
- Cost is bounded: 2 people × 1 quarter, with a defined scope and an end date.
- The return is recovered engineering and design time, fewer rework cycles, and fewer inconsistency bugs. I'll be upfront that I'm still quantifying this (see below).
- It's an investment that compounds. The cost is front-loaded, and the savings recur with every feature shipped afterward.

## Be upfront about the numbers

Leadership will trust you more if you say this yourself:

"I don't have a precise figure for the time we lose today. I'd rather tell you that than invent one. Here's what I'm doing about it:"
1. **Before the build:** a short audit of our most important flows (sign-up, menu browsing, checkout) to count how many different versions of the same element exist across web and app.
2. **Ask each squad** to estimate how much of their last two releases went to rebuilding or reconciling UI that already existed elsewhere.
3. **Track after:** time-to-build for comparable features before and after the system exists.

If you can do #1 and #2 before the meeting, even rough numbers ("we found 11 button styles," "squad leads estimate 15–25% of UI work is duplicate") will land far better than the argument alone. Only use numbers you actually gather.

## The ask, made safe

- **Scope:** start with the pieces used in the highest-value flows (menu, cart, checkout, account), not everything.
- **Checkpoint:** a mid-quarter review where I show what's built and which squad has adopted it.
- **Success measures** (pick two or three you can actually track):
  - Number of screens/flows using shared pieces
  - Time to build a comparable feature, before vs. after
  - Number of UI inconsistency bugs reported
  - Squad feedback on whether it's saving them time
- **Exit option:** if adoption or early results aren't there at the checkpoint, we reassess rather than continue by default.

## The cost of not doing it

"If we don't do this, each squad keeps building its own version, the web and app drift further apart, and the cleanup gets more expensive the longer we wait. The company is growing, so every new feature adds to the pile."

## Likely questions

- **"Why two people for a whole quarter?"** Because the first version has to be solid enough for three squads to trust it. A half-built system doesn't get adopted.
- **"What are we not shipping in that time?"** Have a direct answer ready. Name what those two people would otherwise work on, and be honest about the tradeoff.
- **"When do we see payback?"** Be careful here. Say the first benefits show up when squads start using the shared pieces, probably the quarter after, and that you'll report on it. Don't promise a payback date you can't support.
- **"Can't the squads just do this alongside their work?"** That's been the default, and it's how we got to the current state. Nobody owns it, so it keeps losing out to feature deadlines.

## One-line close

"This isn't a design project. It's a way to ship customer-facing changes faster and more consistently across web and app, and I'm asking for a bounded quarter to prove it."

If you tell me which two roles are involved and what they'd otherwise be working on, I can tighten the tradeoff section. I can also draft a one-page version to send ahead of the meeting.
