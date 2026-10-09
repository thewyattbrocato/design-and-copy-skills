**Rewrite: a short welcome, then a checklist that stays on screen**

The original asks a new admin to remember nine steps from a modal they'll only see once. It also lists a dozen features before they've done anything. Par levels (step 3) come before the item import (step 8), so the order is wrong too. I'd split it into a short welcome and a persistent checklist.

**Welcome modal (about 25 words)**

> **Welcome to Stackwell**
> Let's get your clinic ready to place its first purchase order. It takes four short steps, and you can finish the rest later.
>
> [Start setup]  ·  [Skip, I'll explore]

**Setup checklist (a side panel or page that stays open while they work, with progress saved)**

> **Get ready for your first order**
>
> 1. **Set your currency and time zone**
> 2. **Add your locations**: for example front desk, exam rooms, storage
> 3. **Import your items**: upload your spreadsheet of supplies
> 4. **Add a vendor**: include their payment terms
>
> ✓ *When these are done:* **Create your first purchase order**
>
> **Set up when you're ready**
> - Set par levels for your items
> - Set approval rules for purchase orders
> - Invite your team and assign roles
> - Connect your accounting software
> - Schedule weekly cycle counts

**Short confirmation after each step (say what now works, then point to the next step)**

> Example after step 3: "214 items imported. You can now add them to orders. Next: add a vendor."

**What changed and why**
- **One goal:** after setup, they can place a real purchase order. Everything else is secondary.
- **Four steps up front, five later:** the first four are the minimum an order needs. Approval rules, team, accounting, par levels and cycle counts matter, but none of them blocks a first order. The nine steps stay available under "Set up when you're ready."
- **No feature list:** they'll meet lot tracking, expiration alerts, cost reports and audit logs when those features become relevant. Listing them now teaches nothing.
- **Fixed the order:** items are imported before par levels, since par levels apply to items that already exist.
- **Help stays reachable:** the checklist stays visible and can be skipped or reopened. I'd put a "Help Center" link in its footer rather than burying it in the last sentence.

**Notes**
- I assumed the step order and four-step minimum from your list. If a vendor must exist before items can be imported in Stackwell, swap steps 3 and 4.
- "214 items" is a placeholder. The real count should come from the import. Also check that "Import your items" and "Create your first purchase order" match your actual button labels.

To judge whether it works, measure how many new admins place a real order within their first week without opening the Help Center, not how many click Finish.
