I wouldn't make it approve every filing. I'd have it ask only when it's unsure.

**Why not approve everything**
- Moving and renaming files is easy to undo, and nothing gets deleted or sent. That's the kind of action that's safe to automate.
- At 60 a week, you'd start clicking "approve" without reading. Then the prompts add friction but no safety, and the one wrong filing slips through anyway.

**What your cofounder is right about**
A misfiled receipt isn't catastrophic, but it can be a confidentiality problem. If client folders are shared with clients, one client could see another's receipt. If the folders are private to you, a misfile is just an annoyance. That's the main question for how strict to be.

**What I'd build**
1. **Start in shadow mode for 2–3 weeks.** The tool proposes each filing and you approve it. Track how often it's right. That's about 150 decisions, which should tell you whether it's trustworthy.
2. **Then auto-file only confident matches.** A match counts as confident when the sender, the client name, or a known vendor-to-client mapping points to exactly one client. Anything ambiguous, with no match or several, goes to a `Needs Review` folder or a short list for you to resolve.
3. **Never overwrite.** If a filename collision happens, add a suffix.
4. **Keep an action log.** Record the original filename, source email, destination folder, and timestamp. Then any misfile can be traced and reversed in seconds.
5. **Send a weekly digest.** One summary of what was filed where is a 2-minute skim instead of 60 clicks. It's also where you'd spot a pattern like "all receipts from vendor X are going to the wrong client."
6. **Keep the approval gate for new situations.** A new client, a new sender, or a low-confidence match should still ask you.

If the shadow period shows high accuracy, your cofounder gets the safety they want from the log, the review queue, and the digest. You skip the 60 weekly approvals.
