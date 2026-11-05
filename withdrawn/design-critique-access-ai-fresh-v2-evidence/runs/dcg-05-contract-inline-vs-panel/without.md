**Inline suggestions are better for most of a lawyer's drafting work.** I'd keep a lightweight chat entry point for open-ended requests, but the inline edit should be the primary surface.

**Why inline wins**

- **It matches how lawyers already work.** Redlines and tracked changes are the native format of contract review. A proposed edit shown next to the clause, with accept and reject, fits that habit. Nobody has to learn a new one.
- **Review is the bottleneck, and inline makes it cheaper.** A lawyer is accountable for every word, so they must read every change. A diff against the existing clause shows exactly what changed. A chat answer makes them compare two blocks of text by eye, which is slow and easy to get wrong.
- **Context comes for free.** The assistant already knows the clause, the defined terms, the surrounding sections and the document's governing law. In a chat panel the lawyer has to paste in or describe that context, and any gap produces a plausible but wrong answer.
- **Copy-paste adds risk.** Moving text across by hand can drop a word, break numbering or cross-references, or lose formatting. It also leaves no record of what came from the assistant. Inline edits can flow into the document's existing track-changes and audit trail.
- **It keeps attention on the document.** Switching between a panel and the text breaks concentration, and lawyers are paid for sustained attention.

**Where the chat panel is better**

- **Open-ended questions.** Examples are "what's our exposure under this indemnity?" or "how does this compare to market?" These need an explanation, not an edit.
- **Exploration before drafting.** A lawyer may want to talk through options before committing to wording.
- **Whole-document tasks.** Summaries and issue lists don't attach to a single clause.

**Recommendation**

Make inline the default for anything that changes the text. Each suggestion should be a tracked change with a short rationale and accept, reject and modify controls. Let the lawyer invoke it from a clause, for example with "tighten this" or "make this mutual". Add a chat panel for questions and analysis, and let it hand its output back as an inline suggestion instead of making the lawyer copy it across.

**Caveats**

- I'm reasoning from how legal workflows typically run, not from your users. A few sessions with your lawyers would test it. Watch whether they reach for the panel when they have a drafting task.
- Inline can get noisy. If the assistant proposes too many edits, lawyers will ignore them or resent them. You'd need to limit suggestions to ones the lawyer asked for, or to high-confidence ones.
