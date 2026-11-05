**Change them: drop the annotated screenshots and replace them with a short "what Marlowpine needs" table for each tool.**

Screenshots with arrows are the most expensive thing you can maintain for someone else's product. You don't control when they change. Nothing tells you when they have, and every redesign makes the page wrong without any sign. Dropping everything isn't right either, because readers still need to know where to go in the vendor's app.

**What replaces them, per tool:**
1. **A table of the settings Marlowpine needs, in the vendor's own terms.** For example: "Create an API key with read access to invoices," "Copy the client ID," "Paste the redirect URL: `[ours]`." Menu paths shift less than layouts do, and the values are what readers actually get wrong.
2. **A pointer to the vendor's own help page, plus a search phrase.** Use something like "search 'create API key' in [vendor] help." The vendor then keeps the walk-through current, not you.
3. **Screenshots only of Marlowpine's side.** You control that UI and can update it with your releases.

**Exception:** if a vendor has no usable help page and readers can't get through the connection without a walk-through, keep full steps for that one tool. Even then, make them text steps, not arrows on screenshots.

**To stop learning about changes from angry customers:**
- **Owner:** whoever on your team handles integrations or support for each tool. A page with no named person is the one that goes stale.
- **Check:** each of the three connections is run end to end on the current vendor version. These steps touch accounts and access, so someone should actually do them, not just reread the page. Do it on a set date, such as the first of each month `[confirm cadence]`, and also when a customer reports a mismatch.
- **Freshness:** show "last verified `[date]`" on each page, not "last edited," with a feedback link that reaches the owner.
- **Defect log:** log each reported error as a product bug (symptom, page, fix) so you can see which vendor changes most.

**Two notes:**
- I've assumed you have no way to get advance notice of vendor redesigns. If any of the three publishes release notes or a changelog, subscribing to it is the cheapest trigger you can add.
- I haven't seen your pages or support tickets. If you can pull a list of the tickets that came from stale screenshots, it would show which tool to convert first.
