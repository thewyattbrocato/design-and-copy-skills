**Fix these four: #2, #4, #9, #1.**

**1. #2, error shown after the locker opens (2 of 6, step 3).**
- Both users abandoned their bags, and it only resolved when staff stepped in. That is a complete task failure.
- The cause is probably a simple status-message bug: the door opens, but the screen says "error."
- Across 30 stores, each occurrence is a customer who leaves without their groceries and a staff intervention.

**2. #4, chilled and frozen items in a separate locker (3 of 6, step 4).**
- Two of the three went home without their frozen items. That is a failure with real cost: spoiled food, a refund or redelivery, and an unhappy customer.
- The fix is cheap: show a clear "You also have items in locker X" prompt, and don't allow "finish" until it's acknowledged.

**3. #9, order code vs. PIN confusion (4 of 6, step 1).**
- This was the second most common problem. Two people made the mistake twice, so it's a real barrier at the very start of the flow.
- No one failed outright, but it will cause repeated errors and support calls at scale.
- Fixes: clearer labels, an example of each, and a message like "That looks like a PIN, not an order code."

**4. #1, finding where to scan the code (5 of 6, step 1).**
- It affected almost everyone and cost about 40 seconds each. Everyone found it eventually.
- It's a first-step problem, so it shapes the first impression. Better signage or a lit scanner area is likely a cheap fix.
- Fixing #1 and #9 together cleans up step 1.

**Why not the others?**
- **#12 (wheelchair user couldn't reach the top row):** This is a serious failure, and an accessibility one, so it should not be dropped. It's likely a hardware or layout change rather than a software fix. I'd put it on the roadmap as a separate item. A near-term mitigation is to assign accessible users to lower lockers.
- **#5 (language icon):** It caused one abandonment, but only 1 of 6 hit it. It's a quick fix if there's capacity, and it's the first one I'd add if you can fit a fifth.
- **#8 (screen timeout):** 2 of 6 had to rescan, which is annoying but recoverable. Extending the timeout is probably trivial.
- **#6 (fear of double charge):** 3 of 6 hesitated, but all finished. Better wording on the finish button would help.
- **#3, #7, #10, #11, #13, #14:** These are either preferences, had no failures, or are a different kind of fix (a staff process for #13, a feature request for #14). Revisit them after the rollout.

**Caveat:** With 6 sessions, the counts are rough. I ranked mainly by whether people failed to get their groceries, then by how many hit the problem. I treated #12 as a hardware item rather than one of the four software fixes. If it can be fixed in software, for example by directing accessible users to lower lockers, it should replace #1.
