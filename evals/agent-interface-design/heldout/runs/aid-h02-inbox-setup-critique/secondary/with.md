**Assumption:** Quill Mail reads the freelancer's inbox and can archive, reply, and ignore on its own. I'm treating "Reply" as sending an email, not just drafting one, and the slider as controlling how much the assistant does without asking.

Overall the screen asks for the most decisions at the point where people know the least, and it hides the controls that matter most. The main problems:

**1. "Autonomy level 7" does not say what the agent may do.** A 1-10 number gives no way to know whether 7 means "archives newsletters" or "sends replies to clients." Replace it with a plain line that states the limit, and make the slider, if you keep it, move that line.

- When the person sets a level, show: "At this level it will archive and file mail on its own, draft replies for your approval, and never send a message or delete anything."
- Put any send or delete action behind an explicit cap, such as "send up to 5 replies a day, only to people you've already written to."

**2. "Reply" is a send action with no limit.** Choosing Reply for "client requests" would let it email clients unprompted, which is the riskiest thing on the screen. Make the default for Reply "draft for my approval," and add "send without asking" as a separate, later choice with a stated cap.

**3. The setup asks for too much before any value is shown.** Twelve dropdowns, a slider and a free-text tone box must all be answered before the first run. Ask only what gates safe operation, which is the caps above. Propose the rest and let the person correct it:

> "From your inbox I'd archive newsletters and cold pitches, ask you about invoices and client requests, and draft replies in your voice but not send them. Does that look right?"

Then show the tone box after the first draft exists, where the person can react to a real example instead of inventing a description of their voice from nothing.

**4. Run a dry run before going live.** Archiving and replying to someone's mail is hard to undo in the person's head even when the app can undo it. Before "Finish," show the last 30 to 50 emails and what the assistant would have done with each, with a one-line reason. This costs nothing and is where people find the wrong rule.

**5. "Archive" for cold pitches and newsletters hides things quietly.** That is acceptable only if the person can see what was archived. Batch it into a periodic digest ("14 newsletters and 6 pitches archived this week, Undo / Show") and make "Ignore" an alias for archive-with-a-record, not invisible deletion. The label "Ignore" suggests the assistant forgets, which is not true.

**6. Pause and status are missing and buried.** The grey note sends people to Settings > Advanced for changes, which is the wrong place for the one control they need when something goes wrong. Give the app a status home showing running or paused, the last action and when, and the next check, with a pause control one tap away. Keep the note, but point it to that home, not to Advanced.

**7. "Enable AI" on by default needs one more sentence.** It is the consent moment, so say what it reads: "Quill reads your inbox to sort it. It doesn't train on your mail." Only include the last clause if that is true, and don't leave it on by default unless the person has seen that sentence.

**8. No way to correct a mistake from the screen.** Mention on the setup screen, or in the first activity report, that every action can be undone, with "not this one" and "always or never for this kind" available on each item. Without these, the first wrong archive of a client email is the moment people uninstall.

**Suggested screen, in order:**

- "Quill Mail will sort your inbox and never send or delete anything without asking." (one-line promise, with a note that the caps can be changed)
- Caps: "Send replies on its own? Off / Only to people I've written to, up to 5 a day"
- Proposed starting rules, as a short sentence the person can accept or edit
- Dry run on recent mail, then "Start" and "Pause anytime from the status bar."
- Tone of voice, asked after the first draft

If you can share what the slider actually changes in the code, I can write the exact wording for each level.
