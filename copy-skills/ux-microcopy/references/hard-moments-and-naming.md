# Hard moments and naming

Load for an apology, outage or incident notice, goodbye or unsubscribe page, canned support replies, a policy or legal-adjacent notice, or a request to audit or unify the terms across many strings. Examples are invented; adapt the pattern, not the words.

## Tone by reader state

Pick the tone from what the reader is feeling when the string appears, not from the brand's default.

| Reader state | Tone | Example |
|---|---|---|
| Blocked or losing work | Calm, direct, the fix first | "Your draft is saved. Reconnect to publish." |
| Money or security at stake | Exact figures and dates, no humor | "We stopped a sign-in from a new device. Was this you? [Yes] [No, secure my account]" |
| Loss, illness, grief | Plain and brief, no cheer, no cleverness | "We've closed the account. Contact support if you need a copy of the records." |
| Routine and unhurried | Neutral, one light touch at most | "Saved." |
| Real good news | Warm, one sentence, earned | "Your refund is on its way." |

## Apology

Use one when the failure cost the person something: a plain apology, what happened, what is fixed or safe, what they can do. Skip it for normal states (loading, empty, "no results") and never write "sorry for any inconvenience", which apologizes for nothing.

## Incident or outage notice

Order: what is affected and since when, what is not affected (data, charges), what to do now (or "nothing"), when the next update comes, where to follow it. Name the cause only if known. Do not promise a fix time that was not given: write "[expected end]" and say the time is unconfirmed.

Prepare in advance: a short template per incident type with blanks for time, scope and link, and a named person who approves the send. A drafted-in-a-hurry notice is where the filler and the guesses creep in.

## Goodbye, cancel, unsubscribe

Confirm the exit first, in the heading or first line: what ended, when, what the person keeps. Offer at most one lighter choice (fewer emails, a pause), once, below the confirmation, with a neutral decline. No "we're sorry to see you go", no gushing thanks, no countdown. An unsubscribe page needs no survey in the way.

## Canned support replies

A reply that reads as a template is the failure. Answer the actual question in the first sentence, give the one next step with the exact button or link name, link the long procedure instead of pasting it, and drop stock empathy openers. If a detail varies per customer, mark the blank, never fill it with a guess.

## Policy and legal-adjacent notices

Put a one-sentence plain summary first, then the binding text complete and untouched. Say what changes, for whom, and from when. Disclosures that matter to a choice (renewal, first charge, data use) sit beside the step where the choice is made, not only in the final terms.

## Naming audit

For a set of strings, a term table beats string-by-string polish. One row per thing:

| What users call it | What we call it | Where it appears | The pick |
|---|---|---|---|

Test every row with one question: if two strings name the same thing differently, users will assume two things. So pick the user's word over the internal one and use it everywhere, including the possessive ("your" or "my", not both). Keep paired actions as true opposites: archive / unarchive, not archive / restore; sign in / sign out, not log in / sign out. Plain before clever.

Output the term table first, then the rewritten strings.

## Flow review

For a multi-screen task, a table of screen, string and note beats prose. Walk it along the user's timeline and check what each stretch shows:

- Before: the entry point, the empty state, the permission ask.
- During: the slow state, the failure, the confirmation.
- After: the receipt or email, the off switch, the reminder.
- Coming back: what the person sees on a later visit.

## Before and after

- Outage. Before: "We're experiencing some issues and apologize for any inconvenience." After: "Uploads have failed since [start time]. Files already saved are safe. Nothing to do on your side; next update by [time], on the status page."
- Unsubscribe. Before: "Leaving already? Think of everything you will lose." After: "You're unsubscribed. No more weekly emails. Prefer one email a month? [Switch to monthly]"
- Canned reply. Before: "We understand how frustrating this must be and appreciate your patience." After: "Your refund was issued on [date] and usually appears within [days] of that. If it isn't there by then, reply with the last four digits of the card."
