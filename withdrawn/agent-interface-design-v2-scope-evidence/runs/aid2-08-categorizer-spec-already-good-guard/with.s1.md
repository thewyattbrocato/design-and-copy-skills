The spec is already strong. Your constraints (set-only, uncertain items left alone, one-click undo, visible run status, off switch) are the right ones. I'd change these things before you build.

**Change before building**

1. **Define what undo can't reach, and protect user edits.**
   - Never touch a transaction the user has already categorized or edited, or one in a reconciled or closed period.
   - If the user has edited a transaction since the run, "undo all from last night" should skip it and say so, rather than overwrite their edit.
   - Say what categories feed downstream, such as reports, tax exports and an accountant's view. Undo should show that those figures change back too.

2. **Make the failure state more than a status line.**
   - "Whether it finished" needs more than ok or failed. Use ran, partial (X of Y done), failed, paused and off, plus the next scheduled run.
   - A failed or partial run is a problem. It should interrupt the user, not wait on the dashboard.
   - The failure message should say what happened to the unprocessed transactions. They stay uncategorized and get picked up next run.

3. **Order the morning list by doubt, not time.**
   - Put the least-confident changes first, then "needs you" items, then the routine ones collapsed.
   - On a big night the list stops being "short", so cap it and group the confident changes, with each item still reversible.
   - The "needs you" items need their own place with a one-click category picker. If they exist only as a marker, they'll be ignored.

4. **Split corrections into three.**
   - "Undo" reverts one change.
   - "Not this one" is a one-off correction.
   - "Always or never for this kind" creates a rule, for example "Stripe payouts → Income". The rule is shown in plain words.
   - Right now "learns from corrections" is invisible. Add a "What it has learned" page where each rule can be viewed, edited or deleted, and a reset option. Show a rule before it takes effect, or propose it after the same correction twice.
   - Decide whether a bare undo counts as a teaching signal. I'd say yes, weakly, and I'd ask once.

5. **Add a gentler first run.**
   - Categorizing is cheap to reverse, so acting from day one is defensible. For a new user with no history, though, I'd start with a dry run or suggest-only for the first night or two. They'd see "here's what I would have done" and approve it.
   - Then restate what it does, in one line: "While you're away it will assign categories to new transactions, and it will never move money, edit amounts or delete anything."

6. **Spell out what "off" does.**
   - Turning it off should be reachable from the status line, not only from settings.
   - It should say what happens to past changes (kept, unless the user chooses "undo all") and to learned rules (kept but inactive, or deleted).
   - Pause, which skips runs, is separate from off, and the status line should show it clearly.

**Smaller points**
- State that it can only choose from existing categories, or whether it may create new ones. I'd say it can't.
- "Unsure" needs a threshold. Leave the number as a placeholder to tune on real data, and don't promise an accuracy figure in the UI or marketing.
- Say how learning is scoped: per user, not shared across customers, unless you've decided otherwise and tell users.
- A person should be reachable from the failure and "needs you" screens.

These are spec edits only. None of them changes the architecture.
