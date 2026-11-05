The spec is solid. The main safeguards are already in it: write access limited to category, an "unsure" path, a visible change list with undo, and an off switch. I'd change or add these before building, most important first.

**Must settle before building**

1. **Enforce "only sets categories" in the system, not the prompt.** Give the job a credential or API path that can write only the `category` field. A bug or bad model output then can't touch amounts or delete anything.
2. **Define which transactions it may touch.**
   - Only uncategorized transactions.
   - Never overwrite a category a user or accountant set.
   - Skip reconciled transactions and anything in a closed or filed period.
   - Categories feed reports, tax prep and exports, so a wrong one isn't harmless.
3. **Define what undo restores and what happens if the user has edited since.**
   - Restore the prior state, which is uncategorized.
   - If the user has since changed the transaction, "undo all" should skip it, not clobber it.
   - Keep an audit log of every change (old value, new value, run ID, reason).
4. **Make runs idempotent and resumable.** A crash halfway, or a retry, must not double-apply or leave partial changes with no record. The status line should distinguish these states:
   - Finished.
   - Partial (X of Y done).
   - Failed.
   - Didn't run.
   - Stale. If the last run is more than about 36 hours old, flag it.

**Should add**

5. **Confidence threshold.** "Unsure" needs a number. Calibrate it on real labeled data and favor precision over coverage, because a wrong auto-category costs more trust than a "needs you" item. Consider launching in suggest-only (shadow) mode first, then auto-apply once accuracy is measured.
6. **Learning rules.**
   - Scope it per business, with no cross-customer leakage.
   - Show the user what it learned (for example, "Always categorize Stripe as Income") and let them edit or reset it.
   - Require more than one correction, or an explicit "always do this" choice, before it generalizes.
   - Decide whether an undo counts as a correction (I'd say yes, as a weaker signal).
7. **Off switch semantics.** Say what "off" means: it stops categorizing and stops learning, but keeps existing categories and undo history. Also decide who can toggle it on multi-user accounts (owner, accountant).
8. **Morning list at scale.**
   - "Short" breaks down at 300 transactions, so group by merchant or category.
   - Show a one-line reason and the confidence for each change.
   - Put "needs you" items first.

**Edge cases to cover**

- **"Overnight" is per user timezone.** Run staggered, not all at once.
- **Pending transactions** can change amount or merchant when they post. Categorize only posted ones, or re-check on change.
- **Data handling.** Transaction data goes to a model provider, so check that against your privacy policy and any bank-data agreements. Say so in settings.
- **Ops.** Add a global kill switch, rate and cost limits, and alerting on spikes in undo rate. A high undo rate is your best live signal that quality dropped.

**Suggested success metrics:** auto-apply precision, share routed to "needs you", undo rate, and time users spend in the morning review.

I can turn this into a revised spec or a build plan if you'd like.
