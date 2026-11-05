**Verdict:** The queue is built to produce approvals, not to check the model. The under-3% change rate mostly measures how easy it is to agree, so it says little about accuracy. The speed-oriented layout (Enter to approve, a pre-filled dropdown, one-click approve all) is a good fit for throughput, and it's the reason the number looks so good.

*I'm assuming this is a shipped internal tool. I haven't seen the screen, only your description, so the findings come from that.*

## Findings, ranked

**1. [Blocker] Approve-all-on-page removes the review.**
- **Seen:** A green, top-right "approve all on this page" button.
- **Why it matters:** One click approves every row on the page unread. Those rows count as "approved, no change", so they push the change rate down. Insurance claims affect real payouts and denials, so a wrong category that nobody notices costs someone money.
- **Change:** Remove it. If a bulk action is needed, limit it to rows the reviewer has opened, or to rows where the model is highly confident and a sampled audit backs it up. Make it a neutral secondary button, not green and primary.

**2. [Major] The pre-selected answer anchors the reviewer.**
- **Seen:** The model's category is already in the dropdown. Doing nothing, or pressing Enter, means agreeing.
- **Why it matters:** Reviewers tend to go with the default, and the work is a skim for obvious errors. Reviewers don't have to commit to anything, so an Enter press can't be told apart from a considered "yes". The 3% mixes real agreement with rubber-stamping, and you can't separate them.
- **Change:** For a sampled subset (for example 5–10% of rows, chosen at random), hide the model's suggestion until the reviewer picks a category. Compare their answer to the model's. That gives an unanchored accuracy figure that is a much better basis for the claim management wants to make.

**3. [Major] The speed counter and target bar reward not looking.**
- **Seen:** The header counter reads "claims reviewed today", and a bar compares it to the team target.
- **Why it matters:** The only visible measure is volume. Changing a category costs time (open the dropdown, choose, confirm), so every correction pulls a reviewer away from their target. That pressure pushes the change rate toward zero whatever the model's real accuracy. If staff are measured on this bar, the 3% tells you about the incentive.
- **Change:** Put a quality measure next to the counter, such as agreement with a seeded gold-standard set. Drop the target bar, or pair it with that measure so corrections never count against someone.

**4. [Major] Two lines of claim text are often too little to judge a category.**
- **Seen:** Each row shows the claim number and the first two lines only.
- **Why it matters:** Category-deciding details (cause of loss, coverage, amounts) are often further down. A reviewer can only confirm that the suggestion is plausible against the opening lines. Where the category is wrong but plausible, they will approve.
- **Change:** Let the row expand in place (a key such as Space) to show the full text, and log whether it was opened. Show the model's reason, such as the phrases that drove the choice, so the reviewer can check the evidence and not just the label.

**5. [Major] Nothing shows doubt, and approvals look alike.**
- **Seen:** Every row looks the same, whether the model is sure or guessing. There's no confidence signal and no "unsure" state.
- **Why it matters:** Reviewers can't spend attention where it's needed. Close calls get the same half-second as obvious ones.
- **Change:** Mark low-confidence rows where they sit, and sort or filter by them. Add an explicit "can't tell / escalate" option, so a reviewer isn't forced to choose between approving and guessing. A confidence badge by itself isn't enough, since it needs to be backed by calibration data.

**6. [Minor] Enter approves and advances immediately, and no undo is described.**
- **Seen:** One keypress commits the row and moves on.
- **Why it matters:** An accidental or double press approves a claim the reviewer hasn't read. This is a plausible slip at speed.
- **Change:** Add a short undo (a toast with "Undo" for a few seconds, or a Backspace/Z key) and a visible approved state on the row.

## What works
- **Keyboard-first flow:** Enter to approve and advance suits repeat work, and I'd keep it.
- **Table with one claim per row:** It's easy to scan and compare, so keep it.
- **Model answer shown in context:** It saves typing for the many correct rows. The problem is that it's the only thing shown, not that it's there.

## What to tell management
The 3% can't be read as accuracy. It's the share of rows where a reviewer, under a volume target, with the answer pre-filled and an approve-all button, chose to change something. It puts a floor under the error rate only for rows people actually inspected. To get a real number, use the blind sample from finding 2. Add a small set of claims with known-correct categories (including some with deliberately wrong suggestions) and measure how many reviewers catch. If they miss many of those, the 3% is mostly rubber-stamping.

**Not checked:** I haven't seen the live screen. Nothing here covers contrast, target sizes, focus order or screen-reader behavior. Whether reviewers get time to read claims is also unknown. Watching three to five reviewers work a queue without prompting would show how often they read past the first two lines.
