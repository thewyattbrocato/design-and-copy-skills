The summary line and the rows disagree. "Fully supports" can't be true if three criteria are "partially supports", so ask the vendor to correct or explain it. Beyond that, the remarks are vague, so the aim is to turn them into specifics about your three screens.

## Questions for the vendor

**Across the whole report**
- Which standard and version is this (for example WCAG 2.1 or 2.2, level AA), and which product version and date was it tested against?
- Who tested it (internal team or third party), and with what assistive technology? Ask for named screen readers and browsers, and whether the testing was manual or only automated.
- Were the leave-request form, the rota view and the expenses screen specifically tested? If not, can they test them now and share the results?
- Are there other criteria marked "supports" that depend on these same legacy modules?

**Row 1: error identification ("some forms use generic messages")**
- Which forms? Are the leave-request and expenses forms among them?
- What does a generic message look like, for example "Invalid input" with no field named? Which field is wrong, and what needs fixing, must be stated in text.
- When validation fails, how is it announced to a screen reader? Ask whether focus moves to the error or a summary, whether fields are marked invalid, and whether error text is programmatically linked to its field. Your two screen reader users will miss errors if the message is only visual or isn't announced.
- What is the fix, and when will it ship?

**Row 2: reflow ("certain data views may need horizontal scrolling at high zoom")**
- Which views? Is the rota view one of them?
- Is it needed at 400% zoom (the usual test, equivalent to a 320px-wide viewport)? Does content get clipped, overlap, or force scrolling in two directions on anything other than a true data table?
- A wide grid like a rota can reasonably scroll sideways. Ask whether the row and column headers stay visible and usable, because that's what matters for your magnifier user.
- Can your magnifier user try the rota view at their usual settings before you sign?

**Row 3: keyboard ("legacy modules are being updated")**
- Which modules are the legacy ones, and are leave, rota or expenses among them?
- What exactly fails? Can some controls not be reached or operated by keyboard? Are there keyboard traps? Is the focus indicator missing?
- What is the date for the update, and will they commit to it in the contract? "Being updated" isn't a commitment.
- Keyboard access matters for screen reader users too, so this is the highest-risk row for you.

## Before you sign
- Run a trial with your three staff members on the three screens. A vendor report can't replace that.
- Ask for a dated remediation plan and put it in the contract, with a remedy if the dates are missed (a fix at no charge, a price reduction, or a right to exit).
- Ask for a written warranty that the three core workflows are fully usable with a keyboard and screen reader, and with a magnifier at 400% zoom.
- Ask how accessibility bugs are reported and prioritised after you buy, and whether the vendor retests each release.

If they can't tell you whether your three screens are affected, treat that as a significant finding in itself.
