The spec is solid. The safety shape is right: it can only set categories, it abstains when unsure, and every change is visible and undoable. I'd change or add these things before building.

**Change**

1. **Enforce "only sets categories" in the system, not the prompt.** Give the job a write path that can touch only the `category` field (and the "needs you" flag). It should have no access to payment, amount, or delete operations. Also decide what the job does with locked or reconciled periods, and with transactions already exported to accounting or tax tools. I'd say it should skip those. A category change there can quietly alter reports someone has already filed.

2. **Define undo precisely.** Log each change with the previous value, new value, run ID, and confidence. If the user has edited the category since, "undo all from last night" should skip that transaction, not overwrite their edit. Undo should be idempotent, and it should say what it did ("Reverted 41, skipped 3 you'd already changed").

3. **Split "learns from corrections" into separate behaviors.** Undoing a change means "wrong." Recategorizing to X means "X is right." Both are useful signals, but they aren't the same. Specify these points:
   - Learning is per business, never shared across customers.
   - Users can see and delete what it has learned, for example as "Always categorize 'Shopify payout' as Sales."
   - A single correction shouldn't create a hard rule.
   - Anything the user categorizes manually is never overwritten.

**Add**

4. **Define the confidence threshold.** Say how "unsure" is measured and who sets it. Start conservative and track the share left as "needs you" and the share of changes undone. Undo rate is your main quality metric. Also decide what happens to "needs you" items that sit for weeks.

5. **Make the status line honest about failure.** "Finished" needs more states than yes and no:
   - Partial run, such as "Categorized 120 of 300, then stopped."
   - Failed.
   - Never ran. This is the dangerous one, because a dead job can't report itself. Use an external check, such as "last run was 3 days ago," so the line goes stale visibly.

6. **Make runs idempotent.** A retry or double-fire must not categorize twice or create duplicate undo entries. Process only transactions that are uncategorized and not already handled.

7. **Define the off switch.** Decide what happens to past changes (I'd keep them, with undo still available), whether an in-progress run stops, and whether the default for new users is on or off. For launch I'd suggest a suggest-only or shadow mode for the first week or two. That builds trust and gives you real accuracy data before it writes anything.

8. **Handle the morning list at scale.** "Short" breaks at 400 changes. Show a summary with counts, list the lowest-confidence changes first, and let users expand the rest. Use the user's timezone for "overnight" and "morning."

9. **Keep an audit trail.** Record who or what made each change, plus the model or rules version. You'll need it for support questions like "why was this categorized as Travel?"

10. **Check data handling if a third-party model is involved.** Transaction descriptions are sensitive. Confirm what leaves your infrastructure and that it fits your privacy commitments.

Items 1, 2, and 5 are the ones I'd settle before writing code. The others can be decided during the build.
