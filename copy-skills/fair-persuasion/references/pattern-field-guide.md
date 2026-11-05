# Pattern field guide and governance

Load for an audit of a flow that touches money, consent or exit, when someone asks to add a pressure device, and for any test, optimizer, generated variant or agent that steers a choice. Every example is invented. [patterns-and-fixes.md](patterns-and-fixes.md) holds the common devices by choice; this file adds how to spot subtler ones, a test for what is acceptable, and rules for experiments and automation.

## Audit a flow

Default: walk the journey as someone with one goal and compare four pairs: join against leave, accept against decline, first price against final price, and what a label or heading says against what the body commits to. Every gap is a finding. For an audit, give each finding as where it is, who it costs, and the fair version that serves the same goal. Change when the request is one line or one screen: check only the pair that touches it.

## The four-part test

Default: influence is acceptable when all four hold, judged by what the person can see and do, not by what the team meant.

1. **True and checkable.** The claim, count, deadline or reason can be shown to be so.
2. **Consequence visible before the act.** Price, recurrence, who pays, what is shared and the date are at the control, not after it.
3. **Decline as easy as accept.** Same steps, weight and place for "no", "skip", "not now" and the cheaper option.
4. **Reversible as easily as done.** Cancel, undo, remove and export take no more effort than the act did.

One failure is enough to change the device; fix that part and keep the goal. Change when friction protects the person (a confirmation before wiping an archive): it fails the fourth on purpose, so it stays if it says why and costs seconds.

## Cues and fair forms

Devices already in [patterns-and-fixes.md](patterns-and-fixes.md) are not repeated. The cue is what a reviewer can find on the screen or in the spec.

| Cue | Why it works | Fair form |
|---|---|---|
| The option the business dislikes is smaller, paler, below the fold, or a text link beside a filled button | People take the loudest path, so contrast decides, not content | Same size, weight and position. Test: cover the words; do both look equally pressable? |
| A double negative, a bold line about something else, or a checkbox whose label does not say what ticking does | Reading is skipped and the bold line is taken as the choice | One positive sentence saying what happens if chosen; the control's name matches its commitment |
| An everyday action creates a recurring charge (invite as editor, "continue", share, add a collaborator) with no price at the control | The cost arrives after the decision | Price, recurrence and who pays at the control, the free option preselected, a receipt afterwards |
| An account, contact list or location is required for a task that does not need it | Refusing costs the task itself | Ask when a feature needs it, allow a guest or skip path, say what is shared and when |
| The prompt returns after "no": next visit, next screen, every launch | Repetition wears refusal down | Ask once, remember the answer, ask again only after a long, stated gap or when the person does something that needs it |
| No export, or something switched off remotely after purchase | Leaving costs the person's own data and work | Export before and after cancelling; say what keeps working |
| One-tap purchase on a stored card, or in-game currency that hides the real price | There is no deliberate moment | A confirm showing the amount above a size the team sets, a receipt, a plain refund route |
| "N looking now", "booked minutes ago", "only 3 left" with no scope, window or source | A borrowed crowd stands in for a reason | A true figure with its scope ("for your dates", "in the last day") or nothing; whether it is true belongs to honest-claims |
| A review request that rewards only top ratings, lower ratings held back or delayed, or free product not disclosed | The public sees a curated crowd | Ask everyone, show all, put any incentive next to the review |
| "We value your privacy" beside a tracking control | Reassurance stands in for a choice | Say what is collected and why, with equal accept and decline |
| Endless feed, autoplay with no pause point, loss-of-streak warnings, random paid rewards, paying to skip a grind | They remove the stopping point and reward unpredictably | A natural end, autoplay off or one tap to stop, streaks that forgive, odds and spending limits wherever chance is paid for |
| Pressure that varies with what the system infers (urgency for those predicted to hurry, a harder exit for someone who seems alone or short of money) | It aims at a weak moment, not a reason | The same message for everyone in the same situation; personalization stays when it serves their goal and has a neutral version |

## Keep the legitimate versions

Default: these stay, so the skill does not over-ban.

- **Deadline:** real, shown as a date and its cause, the same for everyone, never reset.
- **Scarcity:** read from the inventory or seat count and scoped to what the person is viewing.
- **Retention offer:** one, once, on the cancel screen, a real change in terms, never delaying the exit.
- **Protective default:** security on, backup on, saying so and reversible in one step.
- **Account needed:** fine when the service is personal (saved orders, history), not to read a page.
- **Prominent call to action and honest social proof:** a clear primary button and a real, sourced "most chosen" label are design, not trickery.

Change when a "legitimate" version fails one of the four parts: a real deadline that is secretly renewed is a fake one.

## Experiments and automation

- **Guardrails.** Default: a test aimed at conversion also tracks refunds, early cancellations, complaints and support contacts, and a variant that wins on conversion but loses on these does not ship. Change when the test touches no money, data, consent or exit; a headline test needs none.
- **Why it matters.** Honest variants usually move behavior a few points; deceptive ones move it much further. A test that scores only conversion therefore selects the deception. When asked to hit a target, say the fair version may lift less and do not promise the pushy figure; change that only when the user supplies measured results for both.
- **Optimizers and generated UI.** Default: an optimizer or model that writes or picks variants gets a ban on the devices in this guide, a person who reviews a winner before everyone sees it, and a log of each variant and why it exists. Change to sampled review for a surface with no money, consent or exit.
- **Targeting.** Never vary pressure by inferred debt, illness, grief, age, loneliness or the hour. Helpful personalization (language, saved preferences) is fine and keeps a neutral version.
- **Owner.** Default: each money, consent and exit flow has a named owner and a recorded reason for every default. Skip for a one-off page.

## Agents acting for a person

Whole-product design of such agents is agent-interface-design; the levers below are the persuasion part.

- **Whose pick.** Paid or partner placement in an agent's recommendations is labelled at the pick, and the person can sort by their own criteria. Change when there is no commercial tie; say so rather than leaving it unstated.
- **Grants.** Default: ask for the narrowest scope that works, with a named maximum for spending or sending, off until switched on; widen only on the person's later yes.
- **Human path.** Cutting support cost never means hiding the person: improve self-serve answers and offer a scheduled callback, but keep a visible way to a human in the automated flow.
- **Persona.** A name, voice and warm tone are fine; claiming to be human, or using the persona to win data or compliance, is not. Say it is automated where trust is being asked for (account access, payment).
- **Check-ins.** A "just checking in" that is really a promotion is marketing; label it as one. For a person who went quiet, send one note that offers something useful and how to stop it.
- **Feeds.** A feed built only from past clicks narrows what the person sees; give a way to look beyond it.

## Vulnerable contexts

Default: test the flow as a tired person on a phone, interrupted, on a slow connection, in a second language. The bar rises when the person is in debt, ill, bereaved, young or has just had a payment fail: remove pressure there instead of tuning it. Change when the audience is verified professional and the context is not a stress moment; keep the other checks.
