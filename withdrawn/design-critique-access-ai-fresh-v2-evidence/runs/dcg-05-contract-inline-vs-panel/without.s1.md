**Inline suggestions are better for most lawyer workflows**, with a small chat affordance kept as a secondary path.

**Why inline wins**

1. **It matches how lawyers already work.** Redlining and tracked changes are the native review format. A proposed edit shown next to the clause, with accept or reject, fits the way lawyers already review a counterparty's draft or a junior's markup. Nobody has to learn a new habit.
2. **It removes the copy-paste step, which is where errors creep in.** With a side panel, the lawyer has to find the right clause, paste the answer, and reconcile it with the surrounding text. Each of those steps risks a wrong paste, a dropped qualifier, or formatting and numbering drift. In contracts, a small slip such as a changed defined term or a lost "not" can matter a great deal.
3. **Showing the diff makes review faster and safer.** Lawyers are accountable for every word. A proposed edit shown as a diff against the existing text lets them see exactly what changed. A chat answer is usually a fresh block of text, so they have to compare it to the original by eye.
4. **Context is built in.** An inline suggestion is anchored to a specific clause. The assistant knows what it is editing, and the lawyer knows what the suggestion applies to. In a chat panel the lawyer has to describe the clause or paste it in, and the answer can drift from the document's defined terms and cross-references.
5. **It gives an audit trail.** Accepted and rejected changes can be attributed, logged, and reversed. This matters for professional responsibility and for explaining later why the text says what it says.

**Where chat is still useful**

- Open-ended questions, such as "What are typical indemnity caps for SaaS deals?" or "Summarize the termination rights in this agreement."
- Exploratory drafting, when the lawyer doesn't yet know which clause they want.
- Questions about the whole document rather than one clause.

**Recommendation**

Make inline suggestions the primary surface. Let the lawyer trigger them from a clause, using a selection, a right-click, or a short prompt box anchored there. Keep a lightweight chat panel for questions and exploration, and let it push its output into the document as a proposed edit. That way the lawyer never has to copy and paste.

**Caveats**

- Inline works only if suggestions are unobtrusive. If every clause carries a suggestion, lawyers will tune them out. Make them on demand, or trigger them selectively.
- This is a reasoned judgment, not a tested result. If you can, test it with a few lawyers on a realistic task, such as revising a limitation-of-liability clause. Compare time to finish, errors introduced, and how much they trust the output.
