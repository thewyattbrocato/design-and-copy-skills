# What's wrong with this design

**The queue measures compliance, not accuracy.** The 3% override rate tells you how often a reviewer chose to fight the default. It doesn't tell you how often the model is wrong. Nearly every feature pushes toward approval.

## Design problems

1. **Pre-selected answers cause anchoring and automation bias.** With the model's category already in the dropdown, the reviewer confirms instead of judging. Confirming is easier than deciding, and people confirm more than they should, even when they're trying.
2. **Enter approves and advances.** The fastest path is the default one. Overriding takes a mouse or keyboard trip into a dropdown, and approving takes one keystroke. A held or double-tapped Enter becomes a silent approval, and there's no undo.
3. **Two lines of claim text isn't enough to verify a category.** Insurance categories often depend on details further down, such as cause of loss, dates, or exclusions. A reviewer under time pressure can't catch those errors without opening the claim, and the layout discourages that.
4. **"Approve all on this page" is a green, top-right button.** It's styled as the primary action, and it turns review into a rubber stamp. Any rows it covers count as human-approved but got no human judgment.
5. **The counter and team-target bar reward throughput.** "Claims reviewed today" goes up fastest by approving quickly. Nothing rewards catching errors, so reviewers are pushed away from the careful work the queue exists for.
6. **There's no reject or "unsure" path.** You described the task as approve or reject, but the UI only lets people change the category. A claim that is ambiguous, miscoded in a way the dropdown can't express, or needs escalation has nowhere to go. It gets approved or forced into a wrong category.
7. **There's no confidence signal or prioritization.** Every row looks equally trustworthy, so reviewers can't spend attention where the model is likely wrong.

## Why the 3% figure is misleading

- It mixes model accuracy with reviewer attention, and you can't separate them from this data.
- The design predicts a low override rate whether the model is 99% accurate or 85% accurate.
- Only errors a reviewer noticed and bothered to fix show up. Errors on rare categories, subtle ones, and ones in rows that went through approve-all are all counted as correct.
- If approved labels feed back into training or evaluation, the model's mistakes get recorded as ground truth and the metric looks better over time.

## How to find out the real accuracy

- **Blind audit sample:** Randomly pick a few percent of claims and have a senior reviewer label them without seeing the model's prediction. Compare against the model's category. This is the real accuracy number.
- **Seeded known-wrong items:** Insert claims with known wrong suggestions into the queue. The share that reviewers catch is your reviewer catch rate, which tells you how much to trust the 3%.
- **Behavioral data you probably already have:** Time per row, how often approve-all is used, whether rows were opened, override rate by reviewer, by hour, and by model confidence. Reviewers with near-zero overrides and sub-second dwell times are rubber-stamping.

## Fixes

- Make the primary action require a choice, or hide the model's suggestion on a random subset of rows.
- Show more claim text, with an expand option, and show model confidence. Sort or flag low-confidence rows.
- Remove approve-all, or limit it to rows above a high confidence threshold with an audit sample still held out.
- Add "reject / unsure / escalate" with a reason.
- Add a short confirmation or undo for Enter-approve.
- Replace the throughput target with quality-weighted metrics, such as catch rate on seeded items and agreement with audits. If you keep a volume target, don't show it as a per-person race.

Management's conclusion should be "we don't know the model's accuracy yet", and the audit sample is the quickest way to find out.
