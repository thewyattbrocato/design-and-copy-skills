The spec is solid. Its strongest points are that it can only set categories, that it leaves anything doubtful alone, and that every change has a one-click undo, including a batch undo. Here is what I'd change before building, most important first.

**1. Say what undo can't reach.**
- Categories feed reports, tax prep, and possibly exports to an accountant or accounting software. Undo is only safe if nothing downstream has consumed the category.
- Add a rule that it never touches transactions in a closed or exported period.
- Add a rule that it never overwrites a category the user set themselves.
- If categories sync out, state what "undo" does after a sync.

**2. Define "unsure" and show what it skipped.**
- Name the threshold as a tunable value, not a vague idea. Don't commit to an accuracy number you haven't measured.
- Give "needs you" its own list, because missed items go unnoticed.
- Show that list in the morning view, next to the changes.

**3. Start with a dry run.**
- For the first few nights, have it suggest categories without applying them.
- Show the user how it read their situation, with a few example transactions and why each got its category.
- Let the user switch it to live when they're ready. Don't apply changes silently on night one.

**4. Make the morning list reviewable at any volume.**
- "Short list" breaks on a big night. Don't truncate it. Group by merchant or category, put the lower-confidence changes first, and give each row its own undo.
- Decide what "undo all from last night" does when the user has since edited some of those items. I'd have it skip the edited ones and say so.

**5. Make the status line tell different outcomes apart.** It should separate these cases:
- Ran and found nothing new.
- Finished.
- Failed or stopped partway, with how many transactions were done and how many weren't.
- Paused or off.

A failed run should reach the user directly, because the plan can't be that they'll notice a stale line. It's a real problem, so it should be the one kind of message that interrupts.

**6. Split corrections into two kinds.**
- "Not this one" is a one-off fix.
- "Always do this for this merchant" creates a rule.
- Treat an undo as the first kind, not as a lasting rule.
- Show any learned rule in plain words, such as "Shell → Fuel", so the user can see and edit it. Preview what it would newly catch before saving.
- Suggest a rule after the same correction repeats. Don't create one silently.
- Say whether learning is per account only. I'd keep it per account.

**7. Put the off switch where the status line is.**
- Settings is fine, but also put pause one step from the dashboard status.
- A paused state should be clearly visible, not just an absent "last ran".
- Say what happens to past changes when it's turned off. I'd keep them.
- Say what happens to the nights it missed when it's turned back on. I'd have it catch up on the skipped transactions, then show the usual list.

**8. Add one line stating the promise.** Put this in settings and in the first-run screen: "Overnight it will assign categories to new transactions and never change amounts, move money, or delete anything."

**Open questions that affect the build**
- Does it only handle transactions that arrived since its last run, or can it re-categorize old ones? I assumed only new ones.
- Do categories sync to other systems, and are there closed periods? This determines how big item 1 is.

I can turn this into a revised spec or break it into build tasks next. Which would you like?
