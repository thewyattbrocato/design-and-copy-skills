The spec is solid. The scope limit in (2), the abstain behavior in (3) and the undo in (4) are the right core. Before building, I'd change or add these:

**Must settle before building**

1. **Enforce the "only sets categories" limit in the system, not in the categorizer.** Give the job a credential or service role that can write only the `category` field (and its run metadata). That way a bug or bad model output can't touch amounts, and "can't delete" is a guarantee rather than an intention.
2. **Only touch transactions with no category.** Say explicitly that it never overwrites a category a user or accountant set, or an earlier run's category the user has confirmed. Make runs idempotent so a retry or double-fire can't change anything twice.
3. **Define undo precisely.**
   - Record the previous value and a run ID on every change.
   - "Undo all from last night" must skip any transaction the user has edited since, rather than clobber it.
   - Decide what happens in reconciled or closed periods, or after an export to an accountant. I'd suggest the categorizer never touches those, and undo there warns.
4. **Define "unsure" as a number.** Use a calibrated confidence threshold, checked against real data before launch. Consider forcing "needs you" for high-stakes categories: owner draws, transfers, payroll, anything tax-sensitive. The cold start for new users with no history should be very conservative.

**Gaps in the user-facing pieces**

5. **Morning list at scale.** "Short" breaks when there are 300 changes. Group by merchant, sort by lowest confidence first, and show a total count. Keep the "needs you" queue separate from the "what I changed" list.
6. **Status line failure states.** Cover "partial" (some committed, some not) and "hasn't run in N days" as well as finished/failed. Say which changes from a partial run were kept. Also settle what "nightly" means across user time zones.
7. **Turning it off.** Specify that it stops future runs but leaves existing categories alone. Say what happens to anything pending, and keep the undo available for the last run.

**Learning from corrections**

8. **Scope and visibility.**
   - Learn per business, never across customers.
   - Treat a correction as a rule ("always Staples → Office Supplies") only when it's clearly consistent, and let users see, edit and reset what it has learned.
   - Never apply learning retroactively to past transactions without showing the user first.
   - Count an undo as negative feedback.

**Worth adding**

- **Audit log** of every run and change, visible to the user and their accountant.
- **Kill switch** on your side, plus metrics: accept rate, undo rate, share left as "needs you". A rising undo rate should page someone.
- **Data handling.** If an external model sees transaction descriptions, check that against your privacy terms and what you tell users.
- **Rollout.** Start with a shadow mode (propose, don't write) or a small cohort, so you can measure accuracy before it writes anything.

If you want, I can turn this into a revised spec with acceptance criteria.
