# Review rule: Brindlemoor install guide

**Purpose:** No release ships an install guide whose steps nobody has run. Reviewers who don't answer can't block a release, but silence also can't count as approval of steps.

**Owner:** `[name]` owns the guide. The owner decides the wording, settles conflicting comments, and publishes.

**1. Run it (required, no silent approval)**
- Before each release, a named person `[name]` follows every step on the release build, on a clean machine or account. Reading the guide through doesn't count.
- They record the build version, the date, and pass or fail for each step.
- If a step fails, the owner fixes it and the same person re-runs that step and every step after it.

**2. Read-through review (silence means yes)**
- Send the draft to each reviewer at the same time, with a deadline of `[N working days]`. Each reviewer covers only their area (for example, support checks the troubleshooting section, product checks feature names).
- The owner merges all comments. If a reviewer hasn't answered by the deadline, the owner treats that as approval and publishes. Reviewers who stay silent get one reminder halfway through.

**3. Ripple check**
- If a release changes a value, limit, name, or step, the owner lists every page, screenshot, and example that states it, and updates them together. Product changes aren't done until their guide changes ship.

**4. If the run-through can't happen**
- Either the guide waits, or it ships with a visible "Not verified on this version" banner at the top. Only the owner can choose to ship it unverified, and they record why. The banner comes off when the run-through is done.

**5. After release**
- A customer-reported doc error is logged with the symptom, the page, and the fix. The owner triages it within `[days]`. If a wrong step got through, the owner adds it to the next release's run-through checklist.

**Notes**
- I assumed the install guide changes system setup or access, which is why it gets a mandatory run-through. If it's explanation only, drop section 1.
- Fill in the placeholders before you post it. Use real names for the owner and the person who runs the steps, and set the deadline and triage days to what your team can keep.
