# Sensitive moments and automated messages

Load when a string sits near money, access, security, identity, family, health or loss; when a control needs a line saying what it will change; when a product reuses someone's own content or speaks for them (share text, resurfaced photos, summaries, milestones); when someone is told their name, content or account is flagged; or when software that acts on its own tells the person what it did. Examples are invented; adapt the pattern, not the words. The lines below are part of the requested strings, not notes beside them.

## Sensitive moments

Default to the plain pattern (what happened, what is safe, what to do next) for a string that:

- touches money, a locked or restricted account, a security check, or repeated sign-in failure;
- asks about or shows a name, age, health, weight, debt, family, relationship or a past event;
- tells someone they were flagged, declined, removed or refused;
- may reach a person who is grieving, ill or afraid.

Plain means no joke, mascot, emoji, exclamation mark or cheer, and no guess about the reader's mood, household or year. Change when the news is good and the person asked for it ("Your refund is on its way"): one warm sentence.

When the brand voice is playful, keep it in word choice (short sentences, familiar words) and let it go in the failure, decline and warning lines. It comes back on the next screen where the stakes drop.

| Moment | Reflex | Plain version |
|---|---|---|
| Payment declined | "Uh-oh, your card said no!" | "Your payment of $24 didn't go through. Your plan stays active until [date]. Try another card or ask your bank. [Update card]" |
| Several failed sign-ins | "Whoa, slow down!" | "Sign-in is paused for [minutes] after several failed attempts. Reset your password to get in now. If this wasn't you, [secure your account]." |
| Access removed | "Looks like you've been removed from the party!" | "Dana removed you from 'Harbor project' today. You can no longer open its files. Ask Dana to add you back, or contact your admin." |

## Consequence line at the control

Default to one line directly above the button, on the same screen and not in a tooltip, that says what changes now, what keeps working, who else is affected, and how and until when it can be reversed. Skip it when the action is undoable and an undo is offered right after.

- "Archive 'Harbor project'? It leaves the sidebar and stops sending reminders. Files and comments stay, and members can still open its link. Restore it from Archived any time. [Archive project] [Keep active]"
- "Remove Sam from the workspace? Sam loses access to all 14 shared folders now. Sam's own files stay with Sam. You can invite Sam again later. [Remove Sam] [Keep Sam]"

Say what continues to work, not only what stops: the worry is usually about what should not change. A reversal window gets its date ("restore until [date]"), and an action that cannot be reversed says so once, plainly, without capitals.

## Defaults that speak for the person

This covers pre-written share text, resurfaced photos or "on this day" cards, yearly summaries, birthday and anniversary prompts, streaks and milestones, and generated captions of their content.

- Default to a factual line: what and when ("Photos from 3 May 2021"), not how to feel ("Your happiest memories!"). Assume no partner, parent, child, pet, good year or weight goal. Change when the person has told the product that fact.
- Anything the product promotes from a person's own content gets a hide control that holds, and one plain acknowledgement: "Got it. We won't show this again." Add a short apology only after the person hid something, not before.
- A milestone states the true count ("24 of 30 days") and the next step. Never "Perfect month!" for an imperfect one, and no scolding for a missed day ("You broke your streak").
- Pre-filled share text is neutral, editable, and leaves out personal data the person did not choose to share.

## Flagged, held and declined notices

When a person's name, content or account needs checking:

1. Open with what was noticed, as an observation: "Another member reported your display name, and we need to check it." Not "Your name violates our rules" and not "fake".
2. Give one action to take (confirm or explain), a time frame as a placeholder unless supplied ("[N days]"), and what keeps working meanwhile. Say what happens if nothing is done only if the rule is given.
3. Offer a way to reach a person. Do not reveal who reported, and do not threaten.

A decline (payment, application, refund) gives its reason in one clause if the reason is known, says so if it is not, and names what the person can do next. Rules on notices, appeals and account actions differ by place and change over time; say once that the wording should be checked by whoever owns policy.

## Asking a sensitive question

Default to one sentence saying why it is asked, who sees the answer, and that skipping is fine, with what skipping changes ("We'll show general tips instead"). If the reason needs three sentences, the question may not be needed; ask the user whether it is. Field mechanics belong to form-design.

## Read-aloud check

Read each sensitive string aloud as if to a person who just heard bad news, then as a synthetic voice would say it. Nothing may depend on an emoji, color or tone of voice; spell out abbreviations; write dates unambiguously ("3 May"). Where one string runs on screen and by voice, use one pronoun rule: "we" for the product, "you" and "your" for the person's things, never the product's "my" for the person's account or library.

## Words for software that acts on its own

Which messages exist and when they fire is a design decision (agent-interface-design if installed). The words:

- **Activity summary** (what it did, and why). Past tense, real stage, count and scope, the reason in the person's terms (their rule or request), doubtful items first, the undo beside it. "Archived 38 promotions overnight because of your 'archive promotions' rule. 3 looked uncertain: [Review them]. [Undo all]"
- **What was not done.** Name items left alone or skipped, with the reason. Scheduled is not sent: say "Scheduled for tomorrow morning", not "Sent". Say "Checked 12 messages, nothing needed action" only when proof of life is wanted; otherwise stay silent.
- **Heading toward a limit.** What is drifting, against which limit, what the system is doing about it, when the next update comes, and what the person can do. "Groceries are at $410 of your $500 limit with 11 days left. Orders pause at $500. Next update on Friday. [Raise limit] [Pause orders]"
- **Could not finish.** What it tried (rounds, attempts), what it did not do, who must act and by when if that is real. The line shown while it is still trying names the stage ("Checking calendars for a shared time"), with no invented estimate.
- **First message and limits.** Default to one line on what it can do (two or three things), one on what it cannot, and how to reach a person. Not "I can help with anything".
- **Edge of capability.** Say it can't do that here, name the nearest thing it can do, and offer the human route. Each fallback differs from the last: first a rephrase with the nearest options, then two or three options as buttons, then a handoff to a person with the conversation attached. Never the same line twice.
- **Recurring status messages** lead with the fact and drop the cheer after the first time ("Your order is on its way"). Keep the wording stable enough to scan.
- **Hedges.** "Appears to" only for an unconfirmed state; confirmed states use flat verbs.
- **No borrowed feelings.** An automated message claims no memory, effort or feeling ("we're working hard") it cannot show.

## Who acts in a notice

Default to the company as the subject of its own act and the act as a verb. Change when the doer is unknown: say so, with a bracket for what is being found out.

| Evasive | Direct |
|---|---|
| "A duplicate charge occurred." | "We charged you twice for the March invoice. We refunded the second charge; it should arrive [refund timing]." |
| "An issue was identified with some exports." | "Exports from 1 to 4 June are missing rows. We're re-running them and will email you by [time]." |
| "Fees may be adjusted." | "We will raise the fee from $4 to $5 on 1 September." |

- Order: the reader's stake first, the cause second, the action third. Required legal text follows a one-sentence plain summary.
- Replace "not ... unless ... not" with the instruction: "Cancel before 5 June to avoid the charge."
- When the company benefits (renewal, data use, upsell), state that use beside the choice.
- Kindness spares the reader's fault, never the company's.

## Quick checks

- Failure, decline, warning and flag lines have no joke, emoji, cheer or guessed mood; a requested brand voice lives in word choice.
- Every button that restricts, removes or pauses has a line above it naming what changes, what continues, who is affected, and how and until when to reverse it.
- Promoted personal content has factual wording, a hide that holds, and a plain acknowledgement.
- A flag notice describes what was noticed without a verdict, with one action, a time frame (a placeholder if unknown) and a human route.
- An activity summary says what it did, why, how many, what it left alone and how to undo; nothing says "sent" or "done" for what is only scheduled; no fallback repeats a line.
- The company is the subject of its own act.
