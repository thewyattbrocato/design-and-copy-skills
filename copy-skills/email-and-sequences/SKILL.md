---
name: email-and-sequences
description: Use whenever you write, plan, fix or judge email or direct messages to customers, subscribers or prospects, in any language and at any length - "write a drip campaign", "nobody opens our emails", "follow up without being pushy", "welcome email that doesn't overwhelm", "sound less like a mass blast". Covers subject lines, preview text and sender names; welcome, onboarding, trial, launch, newsletter, cart, win-back and renewal emails and series; cold outreach and follow-ups; sign-up and unsubscribe wording; cadence and stop rules. Not for receipts, resets and in-app notifications (ux-microcopy), the page an email links to (landing-page-copy) or checking claims (honest-claims).
---

# Email and sequences

An email is read in a crowded inbox by someone who owes the sender nothing. It works when the envelope says honestly what is inside, the body does one job, and the sender stops when the reader has answered. The usual failures are one email that does everything, follow-ups with nothing new, and envelope tricks that spend the reader's trust for one open.

## Do not produce

- "Just checking in", "Bumping this up", "Quick question" or any follow-up that adds nothing new.
- A fake "Re:", "Fwd:", order confirmation, invoice or internal-memo look on a promotion.
- "Last chance", a countdown or a stock limit without a real, given end.
- A personal detail, shared history or "I saw you looking at..." the user did not supply.
- Automation signed as a founder's personal note, unless that person wrote or approved it.
- A mystery subject whose body never pays it off.
- Several competing asks in one email, or a discount in every reminder.
- Alarm built on how common the bad behavior is ("most people haven't started"); say how many are on track, only if given.

## When not to use

- Receipts, resets, shipping notices and in-app messages: ux-microcopy, if installed.
- The page an email links to: landing-page-copy, if installed. Whether a claim is true: honest-claims, if installed.
- Deliverability setup, authentication records and legal compliance specifics.

## Before you write

Name the trigger (a sign-up, an action, an inaction, a date) and the one job of this email: a single ask sized to where the reader is. For a series, give each message one job, something new, and a first message that continues the exact promise the sign-up or ad made.

## Envelope

- **Sender:** a recognizable name that stays the same. A person only if that person stands behind the message.
- **Subject:** says what is inside or what to do. About 40 characters survives most phone inboxes; treat it as a default to check against any stated cap, not a law.
- **Preview text:** completes the subject with a detail, the deadline or the answer. Never "View in browser" or a repeat of the subject.
- **Envelope test:** show only sender, subject and preview to a stranger. Can they say what this is and what it asks?
- **Curiosity** is fine on a content email when the first lines pay it off. Not on billing, security, deadlines or promotions.
- When comparing subject lines, judge them on clicks that lead to the outcome and on replies or purchases, not opens.

## Body

- First line carries the point or the reader's situation, not a greeting paragraph or the company's history.
- One idea, short paragraphs, one primary link or button labelled with what happens. Repeat it rather than make the reader scroll back.
- Length follows use to the reader: short for promotions, reminders and outreach; longer is right for a story-led newsletter or teaching email where every paragraph earns its place. A supplied voice sample wins over these defaults.
- Bad news (price rise, shutdown, incident): the plain fact first with the date and amount, then the reason, then the reader's options.
- Personalization uses only data the person knowingly gave, with a graceful fallback when a field is empty; never a visible merge tag, never narrated tracking.

## Sequences

- Set the count and spacing from the reader's rhythm (workdays, pay cycle, trial length), not the sender's wish for one more touch. Several useful messages before an offer is a starting rhythm to adapt, not a law.
- Keep one voice and vary the format and opener across messages; do not repeat a template.
- Reminders escalate by helpfulness: reminder, then proof or an answer to the likely objection, then help, then an incentive only where earned (a first order, a long-lapsed customer).
- Every series states its stop rule: a reply, a purchase, an unsubscribe or a clear no ends it.
- Per-type jobs, spacing defaults and stop rules are in [sequence-patterns.md](references/sequence-patterns.md); load it for any series.

## Cold outreach

One true, specific detail about the recipient that the user gave, who the sender is and what they offer in a sentence, one small easy-to-answer ask; about four sentences. If no true detail was given, use a bracketed placeholder or leave it out. Default follow-ups: one that adds something new, then one short note that closes the loop and names the exit. Then stop, and stop at once at any no. Do not help buy, scrape or append lists; say so in one line and offer opt-in growth (a sign-up with a clear promise, a referral ask, a partner's list sent under the partner's name).

## Permission and exit

Say at sign-up what will arrive and how often, and keep to it. The unsubscribe link uses the plain word and works at once. For quiet subscribers, send less and better, then ask once plainly whether they still want the emails, then stop; never an ultimatum or guilt. Legal rules vary by place and change: say so and name nothing specific as current.

## If the email already works

Say so and change at most a word. Do not rewrite a clear subject, a good voice or a correct deadline to prove effort.

## When facts are missing

Never invent a number, quote, review, rating, customer, deadline, stock limit, discount or result. Where proof or a detail is needed, use a visible bracket (`[deadline]`, `[customer name]`) or a softer true sentence, and still deliver the email. Ask one question only if the session is interactive and the answer is cheap; otherwise deliver.

## Output

Deliver the requested text first, with nothing before it. When a count or set is asked for (three subject lines, a five-email plan), give exactly that, each with a one-clause reason only if reasons were asked. A sequence plan is a short list: send, timing, job, subject line; write the first email in full only if asked. Honor every length cap and count it yourself (`wc` if a shell is available); a limit counts spaces. Add at most two one-line notes, only for what the user must fill in or check. Suggest a test only when strategy was asked for, and then one change at a time. Answer in the user's language.

## Quick checks

- One ask per email; the first email continues the sign-up promise.
- The envelope alone says what is inside; preview text adds, not repeats.
- Nothing invented, no false urgency, no disguised sender.
- Each follow-up is new; the series says when it stops.
- Within every cap, counted.
