The spec is solid. Your constraints (2), (3) and (4) are the hard ones, and you've already got them. I'd change these things before building:

**1. Say exactly what it may touch.**
- Add "never changes a transaction that already has a category, whether the user set it or it's a bank-supplied or rule-set one." "New" should mean uncategorized.
- Also exclude reconciled transactions, closed periods and anything already exported to an accountant. Otherwise a nightly job quietly changes numbers someone has filed.
- Decide what undo restores. I'd say it restores uncategorized, and the item then goes to "needs you."

**2. Add a cap on how much it does in one night.**
- If a run would change far more than usual (a first run, or a bulk import), hold the changes as suggestions instead of applying them. The threshold is a placeholder to tune, not a number I'm proposing.
- Consider launching the first week or so in suggest-only mode. The user accepts a batch, and the categorizer goes live once they've seen how it reads their business. Applying changes is cheap to reverse, so this is optional, but it's the cheapest way to build trust.

**3. Make the morning report an item list, not a count.**
- Put "needs you" first, then changes. Group changes by merchant so a long list stays scannable.
- Each row shows the merchant, the category it chose, a one-line reason ("matched your 3 earlier Staples purchases") and its own undo.
- Keep "undo all from last night." State how long undo stays available. Say plainly that undoing doesn't reverse anything the user did later, such as edits or exports.

**4. Make "learns from corrections" visible and controllable.** This is the biggest gap. A hidden learner can widen its own behavior without anyone noticing.
- Offer two choices on a correction: "just this one" and "always do X for this merchant." The second shows the rule in plain words before it saves.
- Add a "Rules it has learned" page where users can view, edit and delete rules.
- Decide who teaches it. In a workspace with several users or an accountant, I'd have learned rules be workspace-wide but attributed ("added by Sam"). Otherwise one person's correction silently changes everyone's books.
- Propose a rule after the same correction twice, rather than learning from a single correction.

**5. Define the status line states.**
- "Finished" alone isn't enough. Use: finished (N categorized, M need you), finished with nothing new, partial, failed, skipped (off) and overdue (missed its expected time).
- "Nothing new" must look different from "broken."
- A failed or missed run is the one thing that should interrupt, with an in-app banner or email. Routine completions stay in the morning list.

**6. Spell out what turning it off does.**
- Pausing and turning off should be one step from the status line, not buried in settings. Show a visible "paused" state.
- State what happens to existing changes and "needs you" flags. I'd keep them and keep them undoable.
- Transactions that arrive while it's off stay uncategorized, and the status line says so.

**7. Small additions.**
- Mark auto-categorized transactions in the ledger ("auto"), so an accountant can tell them apart.
- Log every change with the old value, new value, run ID and reason. Undo and the audit trail both depend on this.
- Decide the "unsure" threshold and what counts as "unsure" (no match, a tie between two categories, a new merchant), and write it into the spec. Don't leave it as a model detail.

Also write the one-line promise into the settings page and onboarding: "While you're away it will assign categories to new transactions. It will never move money, change amounts, delete anything or touch a transaction you've already categorized."

I'd build in this order: the change log and undo, then the report and status line, then the categorizer. The categorizer is safe to ship only once the other two work.
