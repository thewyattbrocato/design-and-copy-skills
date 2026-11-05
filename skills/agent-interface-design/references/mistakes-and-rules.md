# Mistakes and rules

Load when designing how people correct an agent that acted wrongly, find what it should have done and did not, edit its instruction, or review what it skipped. Names and numbers are invented; adapt the pattern.

An agent interprets literally and meets cases its designers never pictured. Plan the failure path before the success path: the person who has one bad experience and no way to say "not this" turns it off.

## Two ways to be wrong

- **Acted when it should not have** (a wrong filing, an unwanted booking). The person sees it, so give them a fix.
- **Did not act when it should have** (a missed renewal, a thing left in the pile). Usually nobody sees it, so the interface has to surface it.

For every action the agent takes, name both failures and where each shows up.

## Fixing a wrong action

Put the fix on the item itself, in the report or the activity record, where the person noticed the problem.

| Control | Meaning | Detail |
|---|---|---|
| Undo this | Reverse this one | Always present; see the reversal rule in `SKILL.md` |
| Not this one | Skip this item, leave the rule | Optional duration or place ("not for this client", "not this week") |
| Always or never for this kind | Make a durable rule | Shows the rule it will create before saving |
| Flag for later | Capture context in one tap | For when the person cannot tune now; the agent or a reviewer sees it with the item |

- After the same correction twice, propose the durable rule instead of waiting: "You've moved three invoices from this supplier out of Archive. Always keep them in Billing? [Yes, always] [Just those]". If the rule is cheap and reversible, apply it and say so.
- Confirm a rule change when it affects a lot or the agent is unsure of the pattern; apply it at once when it is narrow and reversible.
- A thumbs-down that changes nothing is worse than no control, because it teaches the person that feedback is ignored. If a control has no effect, remove it; if it has one, say which ("Okay, I'll stop sorting these into Archive").
- Keep a visible, editable list of exceptions and rules so that the person can see and clear them. Name them in plain sentences.

## Finding what it missed

- Keep a list of what the agent skipped or rejected, with the low-confidence ones first and a filter for "almost qualified". Link it from the report.
- Let a person pull an item back with "include this anyway", with an optional reason, which also teaches the rule.
- Now and then let a borderline item through, flagged as such. It reminds people the filter exists and checks that it is not too strict.
- Show near-misses periodically, not only on request: "5 messages came close to your rule this week."

## Editing a rule

Rule editing fails in two ways: a form of operators the person must memorize, and a save that shows nothing about its effect.

- **Restate it as a sentence, editable in place.** "Alert me when a listing in Harbour Street is under [$1,200], ignoring [commercial] listings." Highlighted parts open menus; the person chooses instead of recalling. A person may also type the change in their own words; show how the agent read it, in the same sentence form, before saving.
- **Edit from the case that went wrong.** "Change the rule that did this" opens the rule with the offending item attached and highlighted.
- **Preview the edges, not a random sample.** Show three groups after any edit: items the new rule would now catch that it did not before, items that only just qualify, and items that only just miss. A random ten rarely contains the cases that decide whether the rule is right. Label each group so a person can accept or reject the edit by looking at it.
- **Use real items** from the person's own history, never invented samples that look like theirs.
- When the instruction is plain language and the agent infers the trigger, the same applies: show the interpretation, the list of things it would act on now, and the edge cases, before it takes effect.

## An instruction that is quietly wrong

A right result for the wrong reason survives until the day it does not. Offer "why did you do this?" on any action, answered in a sentence with the cue it used ("filed here because the sender matched the supplier you tagged on 3 June"). If it cannot say why, say that and offer to reverse it.

## Worked example: a print shop's proof-checking agent

It reads incoming artwork files and rejects those that will print badly, holding them for the customer.

Weak: it sends "Your file has issues" and logs a count. A false rejection can only be fixed by emailing the shop.

Better:

- Each rejection card lists the reason in the customer's terms ("text is 5 pt, below the 6 pt print minimum"), with **Print it anyway** (with an optional reason), **Not for this job type** and **Never check this**, the last showing the rule: "Stop checking minimum text size for all your jobs".
- The weekly report carries "9 rejected, 4 almost passed" with a filter for the near ones, and one borderline file released with a note.
- Editing the minimum-size rule shows real files from the last month in three labeled groups: 6 that the new limit would now reject, 4 that are rejected by less than half a point, 4 that pass by less than half a point. The owner can tell whether the setting is right by looking.
