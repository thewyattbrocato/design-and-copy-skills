The summary and the rows contradict each other. Where they differ, trust the rows. "Partially supports" means some criteria fail somewhere, so ask the vendor to correct or explain the summary line. The rows appear to map to WCAG 3.3.1 (Error Identification), 1.4.10 (Reflow) and 2.1.1 (Keyboard). Check the criterion numbers in the report.

## Questions for all three rows

1. Which specific screens and modules are affected? Ask for a list, not "some" or "certain" or "legacy".
2. Are your three screens (leave request, rota, expenses) on that list? Ask for a written yes or no on each.
3. What was tested, and how? Ask for the date, product version, and whether it was automated only or included manual testing with a screen reader (NVDA, JAWS, VoiceOver) and a magnifier.
4. Is there an independent audit or just a self-assessment?

## Row-specific questions

**Keyboard (most serious).** This is a Level A criterion. If something can't be operated by keyboard, a screen reader user is usually blocked entirely, not just inconvenienced.
- Which functions can't be completed by keyboard alone? Is any of it in leave, rota or expenses (date pickers, dropdowns, drag-and-drop on the rota, file upload for receipts)?
- What does "being updated" mean? Ask for a dated roadmap with release versions, and whether it's contractually committed.
- What's the workaround in the meantime? Is it accessible too?

**Error identification.** This matters for the forms, especially the leave and expenses forms.
- Are the generic messages on those forms? What do they say?
- Are errors announced to screen readers (for example through live regions or by moving focus), and do they name the field and the problem?
- Are errors indicated by colour alone?

**Reflow.** This affects your magnifier user.
- Is the rota a data view? Rotas are often wide grids, so this is a likely problem.
- Does the horizontal scrolling happen at 400% zoom or 320px width? Are the headers and the row or column context kept visible while scrolling?
- Is the rest of the page, apart from the table, free of two-dimensional scrolling?

## Before you sign

- **Test it yourself.** Ask for a trial or sandbox and have your three users do their real tasks: submit a leave request with deliberate errors, read the rota, and file an expense with a receipt. This will tell you more than the report.
- **Get commitments in the contract.** Ask for remediation dates for the three gaps, a requirement to keep conformance for the whole term, and a remedy if they miss the dates, such as a fee reduction or a right to terminate.
- **Ask for the full report.** Check whether the other criteria are marked "supports" and whether any are "not evaluated". Ask who wrote the report and when.
- **Ask about support.** Do they have a process for accessibility bug reports, and what response times apply?

If they can't say whether your three screens are affected, treat that as a warning sign. If the keyboard gap touches those screens and has no firm fix date, I wouldn't sign.
