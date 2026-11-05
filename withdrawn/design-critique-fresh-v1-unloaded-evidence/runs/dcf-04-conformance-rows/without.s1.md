The summary line and the rows contradict each other. A product with three "partially supports" rows doesn't fully support the standard. Ask them to correct the summary, and treat the remarks as the real picture.

I'm assuming the report follows WCAG, so these rows would be 3.3.1 Error Identification (Level A), 1.4.10 Reflow (AA) and 2.1.1 Keyboard (A). Check the criterion numbers in the report to confirm.

## Questions for the vendor

**Across all three rows**
- Which exact screens, forms and modules does each "partially supports" cover? Ask for a list. "Some", "certain" and "legacy" aren't scoped.
- Can you test the leave-request form, the rota view and the expenses screen, with a screen reader and a magnifier, before signing? Ask for a trial or sandbox for this. Also ask which screen readers and browsers they tested with.
- Was the report based on a full audit, and by whom (internal or independent)? What's the date and product version?
- Will you correct the summary line, and will you put the accessibility commitments in the contract?

**Row 3, keyboard (your biggest risk)**
- Which modules count as "legacy", and are the leave, rota or expenses screens among them?
- Can every function on those three screens be completed by keyboard alone? That includes date pickers, dropdowns, modals, rota drag-and-drop or calendar controls, and file upload on expenses.
- Is there any keyboard trap, or any control that can't take focus?
- "Are being updated" is a plan, not a conformance claim. What is the dated roadmap, which release will fix this, and what remedy applies if it slips?

Keyboard failures usually mean screen reader failures too, since a screen reader user navigates by keyboard. This row matters most for your two screen reader users. If any of your three core screens is affected, I'd treat it as a blocker until it's fixed.

**Row 1, error identification**
- Which forms use generic messages? Is it the leave or expenses forms?
- Does the error text say which field is wrong and what's wrong with it? Is the error announced to screen readers (for example via an alert or focus moved to the error), or only shown visually or by colour?
- Can you show me the actual messages for a missed required field, a bad date and an invalid amount?

**Row 2, reflow**
- Which "data views" are affected? The rota view is the obvious candidate, because it's a wide grid.
- At 400% zoom (a 320px-wide viewport), can a user read the rota without scrolling in two directions? Is there an alternative view, such as a list or agenda?
- Do the leave and expenses forms reflow properly at that zoom?

The exception for data tables in the reflow criterion is narrow, so ask whether they're relying on it. Horizontal scrolling inside a rota may be acceptable, but only if the page as a whole still works. Have your magnifier user try it, since they'll know quickly whether it's usable.

## Before signing
- Ask for the full report, not just the summary, and for a statement of which screens are out of scope.
- Run a short test with your three affected staff on the real screens: submit a leave request, read the rota, and file an expense, each with their own tools.
- Get written commitments: remediation dates for these three issues, a named contact for accessibility defects, and a remedy if fixes slip, such as a price reduction, termination rights or a holdback.

If the vendor can't say which screens are affected, or won't let you test, take that as a warning sign about the rest of the report.
