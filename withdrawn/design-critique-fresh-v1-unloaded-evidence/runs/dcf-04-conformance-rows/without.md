The summary line and the rows contradict each other. "Partially supports" means some criteria fail, so ask the vendor to reconcile them in writing. These are the questions I'd put to them.

**Overall**
- Which version of the standard and which product version does the report cover? When was it tested, and by whom (self-assessed or independent)?
- Does "fully supports" mean something different from the table, or is the summary wrong? Ask them to correct whichever is inaccurate.
- Were the leave-request form, the rota view and the expenses screen tested? Which of the three rows affect them?

**Row 3: Keyboard (highest priority)**
Keyboard failures are usually the most serious. They block screen reader users entirely, and the standard treats this as a basic (Level A) requirement. The remark is also the vaguest of the three.
- Which modules are "legacy"? Are the leave form, rota and expenses among them?
- What specifically fails? Common problems are keyboard traps, controls that can't be reached or activated, and missing focus indicators.
- What is the committed fix date per module? Will they put it in the contract?
- Can our screen reader users test those three screens with the keys they use (NVDA/JAWS/VoiceOver, whichever applies) before we sign?

**Row 1: Error identification**
- Which forms use generic messages? Does that include leave requests and expenses?
- When validation fails, does the message name the field and say what's wrong, such as "End date is before start date" rather than "Invalid input"?
- Are errors announced to screen readers, and is focus moved to the error or an error summary? Visual-only red text would fail our two screen reader users.

**Row 2: Reflow**
- Which "data views" need horizontal scrolling? The rota is almost certainly one.
- Does the scrolling affect the whole page, or only the table, with the rest of the page still reflowing?
- At 400% zoom, can our magnifier user still see the row and column headers while reading a rota? Can they reach every action without losing their place?
- Do they offer an alternative view, such as a list view of the rota?

**Contract protections**
- A remediation roadmap with dates for these three items.
- A warranty that the product meets the stated conformance level on our key screens, or a right to exit or get a refund if it doesn't.
- Fresh conformance reporting after each major release.
- A named accessibility contact and a support route for accessibility defects.

**Before you sign**
Run a short trial with your three users on the three screens, whatever the vendor says. Their results will tell you more than the report does. If the vendor won't allow that, treat it as a red flag.

If the answers on keyboard access are vague, I'd treat that as a blocker, since it affects the two screen reader users most directly. Reflow and error messages are more likely to be fixable with workarounds.
