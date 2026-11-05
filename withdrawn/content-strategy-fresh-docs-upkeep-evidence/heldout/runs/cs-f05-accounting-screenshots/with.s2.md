**Pick: change them. Replace the screenshots-with-arrows with written steps, and drop most of the images.**

Screenshots break the moment a vendor moves a button, and the arrow makes it worse because it points confidently at the wrong place. Written steps that name the menu path and the label ("Settings → Integrations → API access → Create key") usually survive a redesign, or need a one-word edit. Dropping everything would lose the check that a customer is on the right screen, so keep a little visual help.

**New page shape, per tool**
1. Before you start: what you need, such as admin role, plan tier, and what to copy from Marlowpine.
2. Numbered steps in text, naming the menu path and button labels.
3. "You'll know it worked when…" Describe what the customer sees in Marlowpine, which you control. This is the most useful line on the page.
4. At most one screenshot of **your own** Marlowpine screen. Don't use vendor screenshots, or use one only for orientation, with no arrow, cropped to the page area rather than the full UI.
5. A "Last verified: [date]" line and a "This doesn't match what I see" link that reaches whoever owns the page.

**Stop angry customers being your alarm**
- **Owner:** one named person per tool. Use whoever handles that integration's support tickets today, and give them the right to pull a page.
- **Trigger:** that owner subscribes to the vendor's release notes or changelog and rechecks the page when a UI or API change appears.
- **Backstop:** once a month, someone walks each of the three flows end to end in a test account and updates the "Last verified" date. This takes about as long as a coffee, and it replaces the customer complaints.
- **Retire rule:** if a vendor change breaks a flow and the page can't be fixed within [your agreed time], put a visible "under review" notice at the top instead of leaving wrong steps up.

**This week:** pick the tool whose screens changed most recently, rewrite its page in this shape, and see how long it takes. Then do the other two.

Notes:
- I assumed the three vendors don't offer a stable, official setup guide you could link to. If one does, link to it for the vendor-side steps and only document the Marlowpine side.
- To see how well this is working, count the tickets that say "the docs don't match" per month before and after. I didn't have that number, so I haven't estimated it.
