# Install Guide Review Rule: Brindlemoor

**Applies to:** Every release that changes or republishes the Brindlemoor install guide.

**1. No sign-off, no publish.** The guide doesn't go out until a named reviewer has approved it in writing (PR approval or a ticket comment). Silence is not approval.

**2. Assign a reviewer early.**
- The author requests review at least **3 business days before** the planned publish date.
- The request names one primary reviewer and one backup. "Anyone on the team" doesn't count.

**3. The reviewer runs the steps.** Reading the guide isn't enough. The reviewer follows every step, in order, on a clean machine or fresh VM, using only the guide. Approval comment must include:
- the OS and version tested
- the Brindlemoor version tested
- "All steps completed as written," or a list of the steps that failed

**4. Response deadline: 2 business days.**
- If the primary reviewer hasn't responded by then, the author pings the backup.
- If the backup hasn't responded within 1 more business day, the author escalates to [manager/release owner]. That person must assign a reviewer or explicitly delay the release.

**5. Waiting is not a reason to publish.** If review isn't done by the publish date, the release of the guide slips. Only [release owner] may approve an exception. They must record it in the release ticket along with the risks. Anything published under an exception gets a walkthrough within 1 business day after publishing.

**6. Changes after approval need re-review.** Any edit to a step after sign-off needs the reviewer to re-run that step and everything after it.

**7. Record it.** Link the approval comment in the release ticket. If a published guide turns out to be wrong, note in the post-mortem whether this rule was followed.

---

**Things to fill in or confirm with your manager:**
- The names or roles for **[release owner]** and the escalation contact.
- Whether 3 / 2 / 1 business days fits your release cadence. I picked these as defaults.
- Whether you want rule 5's exception path at all. Dropping it is stricter, but it leaves no way out in a real emergency.

I didn't see your current rule, so this is written from scratch. If you paste it, I can edit it into the same format your wiki uses.
