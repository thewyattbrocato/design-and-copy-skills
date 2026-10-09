---
name: ux-microcopy
description: Use whenever you write or fix the words inside a product or a transactional message, in any language and at any length - "what should this button say", "make this error friendlier", "this sounds robotic", "word this so people don't panic", "is this confirmation clear". Covers buttons, links, empty states, toasts, dialogs and delete confirmations, system and network errors, loading text, permission prompts, tooltips, banners, push notifications, onboarding, settings, cancel and pause screens, 404 pages, receipts, resets and outage or price-change notices. Not for form fields and validation (form-design), marketing pages or email sequences, or ARIA and focus.
---

# UX microcopy

Interface words are read in a hurry, mid-task, often under stress. Each string should say what happened, what is safe, and what to do next, in the user's words, with the button saying what it will do.

## Do not produce

- "Submit", "OK / Cancel" on a destructive action, "Click here", a bare "Learn more".
- "Oops!", "Something went wrong" or an error code with no cause and no next step.
- "Are you sure?" without naming the object and what will happen.
- A decline that shames (a decline phrased as a confession of a bad choice) or a goodbye that guilts.
- Celebration for a routine save; jokes in errors, billing, security or anything irreversible.
- Fault assigned to the user ("You entered an invalid card"): the system, not the person, failed to accept it.
- Two names for one thing.
- Fake progress stages, an invented time estimate, or urgency with no real deadline.

## When not to use

This skill covers every string outside a form, plus short transactional messages. Hand off:

- Field labels, hints, placeholders, validation messages and submit buttons: form-design if installed. This skill follows the same rules (one sentence, what is wrong and how to fix it, no blame).
- Roles, ARIA and focus: detailed component accessibility work. Which states a screen needs: the last polish pass on a nearly finished screen. Whether a flow steers people unfairly: fair-persuasion.
- Marketing pages and message sequences: landing-page-copy and email-and-sequences. Help articles and docs.

If a neighbor is not installed, use ordinary judgment. A platform's native dialog wording and button order, and an existing design system's string patterns, win over everything here.

## Method

1. **Name the moment**: what the user was doing, what just happened, their likely state, and the component's limits. A single string can start at step 2.
2. **Lead with the answer.** What happened or what to do comes first; put a condition before its instruction ("If the card is declined, try another card"). Order by moment:
   - **Failure**: what happened, what is safe ("Nothing was charged", "Your draft is saved"), what to do next, where to get help if it persists. A code goes last as a reference. Say "We couldn't reach the server", not "You lost connection". If a second failure follows the first, word it differently, not the same line again.
   - **Empty**: what belongs here, why it is empty, the one action that fills it. Say so when empty is good news.
   - **Destructive or costly**: name the object and the consequence, with who is affected and whether it can be undone. Buttons are verb plus object, equal in weight, the decline neutral ("Delete budget" / "Keep budget").
   - **Success**: confirm what happened and what comes next. Plain unless the voice and moment both allow lightness.
   - **Permission**: why it is needed, what it enables, that it can change later; "Turn on" / "Not now".
   - **Waiting**: what is really happening, an honest estimate if you have one, whether the user can leave.
   - **Notification**: one point, front-loaded, one action; urgent only for a real deadline.
   - **Cancel, downgrade, pause**: a plain heading, what happens to data and billing and when, the cancel action; at most one alternative, offered once.
   - **Bad news** (price change, removed feature): the fact with date and amount, then the reason, then the options. No euphemism.
3. **Choose the words.** The user's terms, not internal ones, one per concept. A button starts with a verb, says what happens, and matches the title of the screen it opens; label the consequence on anything that costs money ("Pay $24", not "Continue"). A link says where it goes. Sentence case, common words, exact numbers, absolute dates for deadlines.
4. **Set tone by stakes.** The voice stays constant and the tone shifts: calm and direct for failures, money, security and anything irreversible; light only in low-stakes moments and only if the brand voice has it. When the user is likely distressed (loss, illness, money trouble), plain and kind. One plain apology when a failure cost the user something; none for normal states; no "sorry for any inconvenience". "Please" only where the user must do something that costs effort or an apology is due, never as padding.
5. **Check.** Read it aloud. Each button and link still makes sense out of context, since screen readers list them. Meaning never rests on color or an icon alone. No idiom or pun that will not translate, and leave room for longer translations. The decision-critical condition sits before the button, in plain text, not in a tooltip or fine print.

Required legal text stays complete: put a one-sentence plain summary before it instead of cutting it. Starting lengths, to test against the real component: a functional button one to three words, a tooltip one or two sentences, a push notification front-loaded so the first words survive truncation. A stated limit always wins; count characters instead of guessing.

## Judgment calls

- **Subject**: "we" for what the product did or failed to do; "you" for everything else, never as the doer of a fault. Passive only when naming an actor would blame the user.
- **Length**: as short as complete, and complete includes the next step. Anything longer than two tooltip sentences belongs in help content.
- **Personality**: plain by default; playful only when the brand voice is playful and the stakes are low. A flat "no jokes" and "be funny" are both wrong; the situation decides.
- **Urgency**: none by default; with a real deadline, give the date and the consequence plainly.
- **Conversion button versus functional button**: a button that sells may name the value and run longer; a functional one stays short and standard.
- **Generated or templated text** (suggested replies, auto-drafts): never congratulate or cheer in a context that might be bad news; label a draft as a draft.

## Quick checks

- Every failure has a cause in plain words and a next step.
- No fault is placed on the user.
- Every button says what happens; destructive confirmations name the object and the consequence.
- Declines are neutral and equal in weight.
- One term per thing; every string fits its limit.

## Missing facts

Never invent a fix, a time, a price, a deadline, a feature, a count or a policy the user did not give. If the message needs one, write the sentence you can stand behind ("We couldn't save your changes. Try again in a moment.") or leave a visible bracket such as [restore time] and still deliver the strings. Ask one question only when the session is interactive and the answer changes the wording; otherwise deliver, with the brackets.

## If the text already works

Say so and change at most a word. Keep strings that are clear, specific and on-voice; do not rewrite for taste, and do not flatten a deliberate brand voice.

## Output

Deliver the strings first, labeled by where they appear, nothing before them. When a number or set is asked for (three variants, one button, a notification under a limit), give exactly that, and verify counts and limits rather than asserting them. Add at most two one-line notes, only when they change what the user does. For a critique, quote each failing string, say why in a clause, and give the fix.

## References

- [messages-by-moment.md](references/messages-by-moment.md): load when writing a moment you have not written before, or a full flow (cancellation, permissions, outage notices), for short before-and-after pairs.
