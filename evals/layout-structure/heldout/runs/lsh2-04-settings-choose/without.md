**Pick: the left sidebar, with each group as its own page (not one long scroll).**

Forty settings across about ten groups is too much for top tabs, and too much for one undivided page. The sidebar scales as you add groups, and it's the layout people already expect in admin tools.

**Why not the other two**
- **Top tabs:** Ten-plus groups won't fit in a row. You'd end up with overflow menus or two rows of tabs. Tabs also suit 3–6 peer views, and this isn't that.
- **One long page with anchors:** It works for about 10 settings. At 40, people lose their place, the page loads slowly, and one Save button has to cover everything. It also gets awkward for billing and security, which need their own confirmations and permission checks.

**Grouping**

I'd collapse the list into about 8 sidebar items so it doesn't feel like 10+ flat links:

1. Company profile
2. Billing & invoices
3. Team & roles
4. Vehicles & drivers
5. Alerts & notifications (alert rules and channels together, since they're configured together)
6. Integrations
7. Data export
8. Security

Under Integrations, show the 6 integrations as a card grid. Each card has a connect/configure button that opens a detail view. They don't need to be 6 sidebar items.

**Laptop**
- A fixed left sidebar about 240px wide, with the 8 items. The active item is highlighted.
- The content area to the right has a page title and a max width of about 720px, so forms stay readable.
- Settings within a page are split into labeled sections with a divider between them.
- Save is per section or per page. Put a sticky save bar at the bottom only when something has changed.
- Search at the top of the sidebar ("Search settings…"). At 40 settings, this is the thing that rescues people who don't know which group holds what.

**Phone**
- Opening Settings shows a full-screen list of the 8 groups, each with a chevron and a one-line summary (for example, "Billing & invoices: Plan, card, invoices").
- Tapping a group pushes that page full-width, with a back arrow in the header that returns to the list.
- Forms are single column, and the save bar sticks to the bottom of the screen.
- The same search field sits above the list.

This is one navigation model that adapts. The sidebar on a laptop is the same list that becomes the first screen on a phone. You build it once, and the designer's structure holds on both sizes.

**What each person gets**
- **Designer:** the sidebar, as proposed.
- **Dev:** each group gets a stable URL (`/settings/billing`), which gives the deep-linking that anchors were meant to provide. They can still link to a section within a page (`/settings/security#two-factor`).
- **PM:** the sections within a page can use tabs where a group has distinct views. Billing could have Plan, Payment method, and Invoices as sub-tabs. That keeps the PM's tab idea in the one place where it fits.
