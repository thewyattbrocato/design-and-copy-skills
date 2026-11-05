# Questions to ask before you sign

**First, the contradiction.** "Fully supports the standard" can't sit alongside three "partially supports" rows. Ask them to correct the summary, or explain which one is accurate. Also ask which standard and version the report covers (for example WCAG 2.1 or 2.2, level AA) and when it was last tested. A vague or stale report is a risk in itself.

## Row 3, keyboard (WCAG 2.1.1, Level A): the most serious

"Legacy modules are being updated" doesn't say which modules, how they fail, or when they'll be fixed.

- Are the leave-request form, rota view and expenses screen "legacy modules"? Ask for a module-by-module list.
- What exactly fails? Examples are controls you can't reach or operate, keyboard traps, date pickers, drag-and-drop on the rota, and custom dropdowns.
- What is the committed fix date, and will it be written into the contract?
- Is there an interim workaround that doesn't depend on a mouse?

Keyboard access is the foundation for screen reader use, so this affects your two screen reader users directly.

## Row 1, error identification (WCAG 3.3.1, Level A)

"Generic messages" could mean errors that don't say which field is wrong or what's wrong with it. For screen reader users, it could also mean errors that are never announced.

- Which forms? Is the leave-request form or expenses form one of them?
- Are errors programmatically tied to the field and announced by assistive technology, or only shown visually (for example red text)?
- Can they show you the actual error behaviour on the forms you use?

## Row 2, reflow (WCAG 1.4.10, AA)

"Certain data views" is probably the rota view, and possibly the expenses tables. Your screen magnifier user will hit this most.

- Which views need horizontal scrolling at 400% zoom (a 320px-wide viewport)?
- Is the rota one of them? If so, is there an alternative such as a list view?
- Is scrolling needed only for genuinely two-dimensional content like a table, which WCAG allows, or for ordinary content?

## Across all three

1. **Test your workflows.** Ask for a trial or sandbox, and have your three staff run the leave-request, rota and expenses tasks with their own tools (for example NVDA, JAWS or VoiceOver, and their magnifier). A report can't replace this.
2. **Ask about testing method.** Was it a self-assessment or a third-party audit? Was it tested with real screen readers? Can you see the underlying audit results?
3. **Ask for a remediation roadmap.** You want dated commitments for these three rows, and an answer on whether other rows are overstated.
4. **Get it in the contract.** That means a stated conformance level, a fix timeline, and a remedy (such as price reduction or exit rights) if they miss it.
5. **Ask about regression.** How do they check accessibility in each release?

If they can't say clearly that your three screens are unaffected, treat the keyboard row as a blocker until you've tested it yourselves.
