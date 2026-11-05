**Design one (inline tracked changes) is better for your lawyers.** I'd add a few elements from design two.

**Why inline wins**

- **Traceability.** Tracked changes are already how lawyers record who changed what. With inline suggestions, each accepted edit is a discrete, attributable decision: "AI proposed, [name] accepted at [time]." In the chat-and-paste design, the document just shows text appearing. The record of the AI's involvement lives in a chat log that's separate from the document. Nothing links a clause to the person who approved it.
- **Review matches how lawyers work.** They are trained to read redlines, and they will review each change one by one anyway. Accept/reject per change gives them a familiar, low-risk way to stay in control. Copy-paste hides what changed, particularly when the AI rewrites an existing clause and the lawyer has to diff it by eye.
- **Fewer silent errors.** Pasting loses formatting, defined terms, numbering and cross-references. It also lets text get in without ever being reviewed as a change. A tracked change shows exactly what is being touched.
- **Trust builds gradually.** Slow-to-trust users do better when the tool can't act without them. Nothing in design one is applied until it is accepted, and a rejected suggestion leaves the document unchanged.

**Where design two is better**

- It suits open-ended questions ("what's the usual position on limitation of liability for SaaS?") and drafting from scratch, where there's no existing text to redline.
- It makes the AI feel optional and separate, which some cautious users prefer at first.

**Recommended approach**

1. Make inline tracked changes the main way the AI edits the document.
2. Mark AI-originated changes distinctly from human ones, for example a different author label such as "AI assistant (requested by J. Smith)". Record the requesting user, the time, and ideally the prompt or model version.
3. Never auto-apply. Require an explicit accept per change, and avoid a one-click "accept all AI changes" button, or at least make it hard to hit by accident.
4. Add a small side panel for questions and explanations, but have anything it drafts enter the document through the same tracked-change path, not by copy-paste. Insert-as-suggestion keeps traceability.
5. Show a short rationale with each suggestion, and cite the source (playbook clause, precedent) where you can. Careful reviewers want to know why.
6. Keep everything in the existing document history and audit trail, so accepted AI changes show up the way any other accepted change would.

**Risks to watch with design one**

- **Redline fatigue.** Large AI rewrites can bury reviewers. Keep suggestions scoped and small, and group them by clause.
- **Rubber-stamping.** Accepting many suggestions quickly undermines the "person's decision" record. Pacing, summaries, or flags on higher-risk changes (liability, indemnity, governing law) can help.
- **Attribution ambiguity.** Make sure that once a lawyer accepts a change, the record shows both that the AI originated it and that the lawyer made the decision.

I'd test this with a few of your lawyers on real redlines before committing, since the fatigue risk depends on how much the model suggests at once.
