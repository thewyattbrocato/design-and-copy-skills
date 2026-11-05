# Install Guide Review Rule: Brindlemoor

**Purpose:** No install guide change is published until a named reviewer has approved it. A missing reply never counts as approval.

**1. Assign reviewers when the draft is ready**
- The author names one primary reviewer and one backup in the review request. Don't send it to "the team."
- The reviewer must be someone who can run Brindlemoor (engineering, support, or QA), not only someone who proofreads.

**2. Reviewer checklist (required)**
- Follow every step, in order, on a clean machine or fresh environment. Reading the steps is not enough.
- Confirm that commands, paths, version numbers, and screenshots match the release being published.
- Reply with **Approved** or **Changes needed**, plus the environment tested (OS and version).

**3. Timeline**
- The review request goes out at least **3 business days** before the planned publish date.
- If the primary reviewer hasn't replied after **1 business day**, the author pings them and tags the backup.
- If there is still no reply after **2 business days**, the author escalates to the manager, who assigns a reviewer.

**4. No silent publishing**
- Silence is not approval. Don't publish without a recorded **Approved**.
- If the deadline arrives without approval, the publish date moves. The release owner can override only by writing down the risk and accepting it. The override is logged on the review ticket with their name.
- For any step that changes how the product is configured or installed, the override isn't available. Those steps need a completed run-through.

**5. After publishing**
- Record the reviewer, the date, and the environment tested on the review ticket.
- If a customer reports an error in the guide, fix it within 1 business day and add the miss to the next retro.

---

**Notes**
- I haven't seen your current rule, so I wrote this from scratch. Adjust the timelines (3, 1, and 2 days) to match your release cadence.
- The core fix is two things. Reviewers must run the steps, since a read-through probably wouldn't have caught a wrong step 6. And no reply means the publish date moves, not that you publish anyway.
- If you paste your current rule, I can edit it into this shape instead.
