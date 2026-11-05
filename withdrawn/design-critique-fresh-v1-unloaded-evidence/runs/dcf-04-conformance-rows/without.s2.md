The summary line and the report's own rows disagree. "Fully supports" can't be true if three criteria are "partially supports", so ask them to explain that first. All three remarks are vague, and each could affect your staff.

## Ask first
- Which product version, date and conformance level (A or AA) does the report cover?
- Was it a self-assessment or an independent audit? Can we see the test method and the assistive tech used (screen reader and browser combinations)?
- Why does the summary say "fully supports" when three rows say otherwise? Ask them to correct it or justify it.

## Row 3, keyboard (most serious)
Keyboard failures block screen reader users outright, not just make things harder.
- Which modules are "legacy"? Are the leave-request form, the rota view and the expenses screen among them?
- What exactly can't be done by keyboard: reaching controls, operating them, or escaping from them (a keyboard trap)?
- "Being updated" is not a commitment. What are the fix dates and the release version, and will they put those in the contract?

## Row 1, error identification
- Which forms use generic messages? Is the leave-request or expenses form one of them?
- Is the error identified in text and tied to the field, and does a screen reader announce it? "Generic" could mean "Invalid input" with no field named, which a screen reader user can't act on.

## Row 2, reflow
- Which data views? Is the rota one of them?
- Horizontal scrolling inside a genuine table or grid is often an accepted exception, so the rota may be fine. Ask whether the scrolling is limited to that kind of content, or whether ordinary text and forms also break at 400% zoom.
- Is there anything that needs two-dimensional scrolling to read a single line of text? That is what hurts your magnifier user.

## Before you sign
1. **Test it yourselves.** Ask for a trial and have your two screen reader users and your magnifier user complete real tasks on the leave-request form, the rota and the expenses screen. This will tell you more than the report.
2. **Put it in the contract.** Ask for accessibility warranties covering the named fixes, with dates, and a remedy if they slip (fee reductions or an exit clause).
3. **Ask about process.** How do they test new releases, and how do they handle accessibility bug reports? Is there a named contact?
4. **Ask for a workaround** for anything still open at go-live, such as an alternative way to submit expenses.

If they can't tell you which screens are affected, or if the answers put your three key screens in the "legacy" group, treat that as a serious warning before buying.
