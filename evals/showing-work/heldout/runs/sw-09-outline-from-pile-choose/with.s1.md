# Gridwalk offline mode: case study plan

## Sort of your material

**Lead (first screen and spine)**
- **Before and after screenshots.** They're your strongest visual, so they go first. Hiring managers should see the tiny grey icon next to the persistent banner with per-item sync states before they read anything.
- **Usability result (1 of 5 → 4 of 5 understood what had synced).** This is your only evidence, so put it directly beside the decision it supports. State that n=5 and that it was a short test. Candor about the sample reads better than overclaiming.

**Support (inside a decision section, one item each)**
- **2 or 3 inspector quotes** from the Notion notes. Choose the ones that explain why the old icon failed, such as not knowing whether work was saved.
- **The engineer's Slack comment** that sync conflicts were the hardest part. Use it as a short pull quote. It earns its place only if you show what you designed for conflicts.
- **3 to 5 Figma frames**, not 40. Pick the ones that show a decision changing between versions.
- **The competitor teardown**, only as one line or one small figure, and only if it changed something you did. Otherwise cut it.

**Drop**
- The other ~35 Figma frames and the version-by-version history.
- The full interview notes and any per-participant detail beyond the quotes.
- Teardown detail that didn't change a decision.
- A research, ideation and testing timeline, or a role and timeline table at the top.

## Outline

**First screen**
- **Title and one sentence:** "Gridwalk is a field-inspection app for utility workers. I redesigned its offline mode so inspectors can tell what has and hasn't synced." Add the facts you have, such as platform, your role and team size. `[platform, your role, timeframe]`
- **Visual:** before and after, same width, each side labeled. Pin the faults to the old version: "tiny grey icon, easy to miss", "no sign of which items are saved".
- **Why it mattered:** a short paragraph. Inspectors work where there's no signal, and unclear sync status means they can't trust their data.

**Section 1: A persistent banner replaces the easy-to-miss icon**
- **Claim:** inspectors couldn't tell they were offline, so offline status had to be always visible.
- **Proof:** the header close-up from before and after, plus one inspector quote.
- **Caption:** say what the banner does in each state, since the screenshot can't show that.

**Section 2: Per-item sync states show what's saved and what isn't**
- **Claim:** knowing you're offline isn't enough. Inspectors need to know which inspections are safe.
- **Proof:** the after screenshot of the list with states, then the usability result.
- **Result line:** "In a 5-person usability test, 4 understood what had synced versus not, up from 1 of 5 with the old design."
- **Caption:** name the task participants were given and say it was a small test.
- **Figma frames:** add 2 or 3 showing how the states changed between versions, if they show a real decision.

**Section 3: Designing for sync conflicts, the hardest part**
- **Claim:** `[what you decided: how conflicts are surfaced and resolved]`
- **Proof:** the Slack quote, then 1 or 2 frames of the conflict state. `[frames]`
- **Note:** I don't know how you handled conflicts. This section is only as strong as that answer. If you didn't fully solve them, say so here, which fits the ending too.

**Ending**
- **What's limited:** the test was 5 people, and there are no business metrics yet. Say what you'd measure next, such as support tickets or data-loss reports. `[planned measures]`
- **Credits:** `[credits: names and roles]`, including the engineer.
- **One action:** how to contact you.

## Things to fill in
- `[platform, your role, timeframe]`: from you.
- `[conflict decision]`: what the design actually does when two edits collide, and which frames show it.
- `[planned measures]`: what you'd track once there's data.
- `[credits]`: names and roles.
- **Quotes:** which 2 or 3 inspector quotes you want, and whether you have permission to use them.
- **Test task:** the task participants did in the usability test, for the caption.
- **Teardown:** whether it changed any decision. If not, drop it.

If you tell me how conflicts were handled and paste the inspector quotes you like, I can draft the section copy.
