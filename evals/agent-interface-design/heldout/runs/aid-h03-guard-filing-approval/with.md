**Don't approve all 60 a week. Let it file on its own, but make every filing easy to review and undo, and send only the uncertain ones to you for approval.**

Your cofounder wants to prevent a wrong filing from going unnoticed. That's a fair goal, but per-item approval doesn't achieve it. At 60 a week you'd be tapping "yes" by about day three, and then the approvals protect nothing while still costing you time. Your actions are also cheap to reverse: nothing is deleted or sent, and a misfiled PDF is just in the wrong folder. That's the situation where act-and-report is the right setting.

**The promise:** "While you're away it will move and rename receipt PDFs into the matching client folder, and it will never delete, send, or touch anything that isn't a receipt PDF."

**What I'd build**

1. **Confidence split.**
   - **Clear match:** it files the receipt. Examples are a known sender, a client name or account number in the PDF, or a vendor you've mapped to that client.
   - **Doubtful or unmatched:** it leaves the file in an "Unsorted" folder and puts it on a short list for you. This is the only approval you do, and it should be a small fraction of the 60.
2. **Dry run first.** For the first week or two, run it in suggest-only mode. It shows where it would file each receipt and why, and you approve in bulk. That's your cofounder's approach, but limited to a trial period. When you see a clean run, switch to act-and-report. I haven't tested this tool, so I can't tell you how accurate it will be. The trial will show you.
3. **One weekly digest** (or daily, if you prefer) listing every filing: file, client, the reason for the match, and an **Undo/Move** button on each. Put doubtful items first. A bare total like "60 filed" doesn't let you check anything.
4. **Undo.** Log the original name and location for each file so any single filing, or a whole batch, can be reversed. Keep the log long enough to catch mistakes you notice late. Drive's version history helps as a backup.
5. **Two kinds of correction.** "Not this one" fixes a single file. "Always/never for this sender" creates a rule, and the tool shows you the rule in plain words before saving it. After you fix the same sender twice, it should suggest the rule.
6. **Status and pause.** Show a simple status (running or paused, last filing, next check) with a one-tap pause. Alert you right away only when something breaks, such as lost Drive access or a failing inbox connection. Silence should never mean "broken."
7. **Rules for new things.** A receipt that matches no client, or a client with no folder, always goes to the review list. It never creates a folder or guesses.

**The one real risk** is a receipt filed into the wrong client's folder when you later share that folder with the client. That's an exposure risk, not just a tidiness problem. If any client folders are shared, require approval for those clients until you trust the matching, or keep the filing in an internal staging folder that you share from. It's the only place I'd keep approval permanently.

**To tell your cofounder:** "Approval on everything gives us the feeling of control, but not the protection. We'll approve the uncertain ones, review everything else in a digest, and be able to undo any of it." If a week of the trial shows frequent mistakes, then tighten the setting.

If you tell me how you identify clients today (sender, vendor, or a name in the PDF), I can sketch the matching rules and the digest layout.
