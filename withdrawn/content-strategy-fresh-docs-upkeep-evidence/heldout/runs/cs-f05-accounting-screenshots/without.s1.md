**Pick: drop the screenshots.** Replace them with numbered text steps that use the exact on-screen labels, like "Settings → Connected apps → Create API key".

**Why drop rather than keep or change:**
- **Screenshots fail silently.** After a redesign, a stale screenshot looks authoritative and sends people to the wrong place. A text step with a renamed button still gets someone close, because they can search the page for the words.
- **Text is cheap to maintain.** Fixing a label is a one-line edit. Fixing a screenshot means re-capturing, re-cropping, and redrawing the arrow, which is why the pages go stale.
- **Text also gives you search, translation, and screen-reader support.** Annotated images give you none of these.

**What to do instead:**
1. Write each connection as numbered steps: the exact menu path, the field names, and what to paste where.
2. Keep screenshots only of Marlowpine's own UI, such as the "connected" success state. You control that UI, so those images won't surprise you.
3. Add a "Last verified: <date>" line to each page, and link the vendor's own help page for the step. When their UI changes, their docs change too.
4. Fix the real problem, which is that you hear about redesigns from customers. Put a quarterly reminder on someone's calendar to walk through all three connections end to end. If any vendor offers a sandbox account, run that walkthrough there.

**When I'd choose differently:** if one step is truly hard to describe in words, like finding a control hidden in an unlabeled icon menu, keep a single screenshot for that step only. Mark it with the capture date and don't draw an arrow, since the arrow makes it look more precise than it is.
