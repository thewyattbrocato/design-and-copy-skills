# Gridwalk offline mode: case study outline

## What leads, what supports, what goes

| Tier | Material | Why |
| --- | --- | --- |
| **Lead** | Before/after screenshots | This is the work, and it's the first screen. A hiring manager sees the change in five seconds. |
| **Lead** | Usability result (1/5 → 4/5) | This is your only evidence. Put it right next to the decision it proves. |
| **Support** | 3–5 Figma frames | Use them to show the decisions, not the process. Pick frames where a choice is visible, such as the sync-state variants or the conflict screen. |
| **Support** | Interview notes (6 inspectors) | Use them as the reason behind the decisions. Take one or two findings, or short quotes, and put each inside the decision it explains. |
| **Support** | Engineer's Slack comment | It explains why conflicts are a section of their own. Paraphrase it, or quote it with the engineer's permission. |
| **Support** | Competitor teardown | Give it one sentence or one small comparison, and only if it changed a decision. |
| **Drop** | Most of the 40 frames and the version history | Showing all three versions reads as process. Keep one "what I tried and rejected" frame at most. |
| **Drop** | Persona, timeline and role-table style framing | It pushes the work below the fold. |

Two of your pieces carry the most weight: the before/after pair and the test result. Everything else only explains why those two exist.

## Outline

**First screen (no heading, just the work)**
- **Title and one sentence:** "Gridwalk offline mode: a redesign so utility inspectors can tell what has and hasn't synced. For field inspectors on [platform], working in areas with [connectivity constraint]."
- **Visual:** the before and after screenshots side by side at the same width. Label each side. Pin short callouts to the old one: "Tiny grey icon, easy to miss" and "no way to see which items saved." Callout the new one the same way: "Persistent banner" and "per-item sync state."
- **One short paragraph on why:** inspectors couldn't tell whether their work was safe. Back this with one finding from the interviews.
- **Result line:** "In a 5-person usability test, 4 understood what had synced, up from 1 before." Say it's a small test.

**1. A persistent banner instead of a tiny icon**
- **Claim:** offline status should be impossible to miss, because inspectors are working with gloves, glare and divided attention.
- **Proof:** the before/after header crop. Add an interview finding or quote on how inspectors noticed (or didn't notice) they were offline. `[quote or finding: what inspectors said]`
- **Caption:** say what the old icon looked like in the field, or what the banner does in each state. Don't just repeat the paragraph.

**2. Per-item sync states to answer "is my work safe?"**
- **Claim:** a global status isn't enough. Inspectors need to know which specific inspections are saved, pending or failed.
- **Proof:** one frame showing the list with each state. If you have a small Figma comparison of an option you rejected, add it here. Then give the test result: 1 of 5 → 4 of 5 understood what had synced.
- **Caption:** state how the test worked, for example "5 participants, same task before and after."

**3. Sync conflicts: the hardest part**
- **Claim:** conflicts were the hardest problem, and the engineer said so. Here's how the design handled them.
- **Proof:** the Figma frame(s) of the conflict flow. `[what the design does when two edits collide, and the tradeoff you and the engineer weighed]`
- **Note:** I don't know what you decided here, and it's probably your strongest section for hiring managers, because it shows collaboration and a real constraint. Write it in your own words. If the conflict handling was only partly designed or tested, say so.

*Merge or cut section 3 if the Slack comment is all you have.* Don't build a section on a design you can't describe.

**4. What didn't work, and what's still limited**
- The test had 5 participants and measured comprehension, not task success or error rate.
- There are no business metrics yet. Say what you'd measure next. `[e.g. support tickets, data-loss reports, time to sync; only what is real]`
- Anything you'd change.
- If the competitor teardown changed a choice, mention it here or in the relevant decision.

**Close**
- `[credits: names and roles]`, and your role.
- One action: "Get in touch" or "See the prototype," repeated from the top.

## Rules for the text
- Section titles are decisions, not phases. Avoid "Research," "Ideation" and "Testing."
- Each paragraph makes one claim (about 15–60 words) and is followed straight away by its figure.
- Every figure gets a caption that adds something the paragraph doesn't, like a condition, a number or the platform.
- If you can link a prototype or a short clip of the sync states changing, include it. It needs a replay control and shouldn't autoplay.

## Still to fill in
- `[platform and connectivity constraint]` for the opening sentence.
- `[quote or finding]` from the interviews for sections 1 and 2.
- `[conflict handling decision and tradeoff]` for section 3.
- `[next measures]` for section 4.
- `[credits: names and roles]`.
- The engineer's permission to quote the Slack comment, if you want to use their words.

I didn't invent any numbers or quotes. The only figures here are the 1/5 and 4/5 you gave me.
