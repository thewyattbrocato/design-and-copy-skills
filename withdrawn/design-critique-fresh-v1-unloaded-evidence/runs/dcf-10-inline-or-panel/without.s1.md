**Design one, inline tracked changes, is better for your lawyers, with one caveat about how you build it.**

**Why inline wins**

1. **Traceability is built in.** Tracked changes already record who changed what and when, and lawyers already rely on that record. With inline suggestions, every AI edit is a pending change that a named person must accept or reject. With a chat panel, the lawyer copies text over, so the document shows a human paste. Nothing in the document links that text to the AI output or to a decision. You would have to build a separate audit trail, and it would be easy to bypass.

2. **It matches how lawyers already work.** Redlines, accept/reject, and reviewing a counterparty's markup are routine. Inline suggestions use that habit, which matters for people who are slow to trust new tools. A chat panel asks them to learn a new workflow and trust output they must verify elsewhere.

3. **Review happens in context.** A clause is only right relative to the definitions, the governing-law section, and the surrounding terms. In a diff, the lawyer sees exactly what would change in place. In the chat panel, they judge a clause in isolation and then paste it, which is where inconsistencies get in.

4. **It keeps the lawyer's judgment in charge.** Per-change accept/reject makes the lawyer the decision-maker on each edit. Copy-paste makes it easy to take a whole block without reading it closely, and it leaves no sign that the text was machine-generated.

**The caveat**

Inline has its own risks, so build it with these in mind:

- **Mark AI authorship clearly.** Attribute suggestions to "AI assistant" as a distinct author, separate from human collaborators. Record who accepted each one.
- **Don't allow "accept all."** Or at least make it deliberate, with a confirmation step. Bulk acceptance undermines the careful review you want.
- **Keep suggestions small and explainable.** Each one should carry a short rationale, such as "aligns with your playbook's limitation-of-liability position". Large rewrites are hard to review and erode trust.
- **Make it user-initiated at first.** Let the lawyer invoke the helper on a selection, rather than having suggestions appear unprompted. That respects their cautiousness and keeps the decision with them.

**Where chat does help**

Chat suits open-ended questions, like "what's the usual market position on indemnity caps?" or "explain this clause". You can add a small chat or prompt box later, as long as any text it proposes enters the document as a tracked suggestion, not by copy-paste. That keeps the audit trail intact.

**Recommendation:** Ship inline tracked changes first, with AI authorship attribution and per-change acceptance logged. Treat chat as an optional add-on that feeds into the same tracked-change flow.
