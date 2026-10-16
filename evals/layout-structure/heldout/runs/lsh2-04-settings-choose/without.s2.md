**Pick: the left sidebar.** On phones it collapses into a drill-down list. Use real URLs per group, such as `/settings/billing`, and not one long page.

**Why the sidebar wins**
- You have about 10 groups and 40 settings. Top tabs break down at that size. Ten tabs overflow on a laptop and need a scrolling tab strip on a phone, where people don't notice the hidden tabs.
- One long page with anchors is fine for 40 simple toggles. Yours include team and role tables, invoice lists, and six integrations. The page gets very long, saving is ambiguous (one Save button, or one per section?), and it loads everything at once.
- Separate pages let you load each group on its own and link straight to it ("fix this in Alert rules"). Permissions also get simpler: hide Billing from non-admins by hiding one route.
- The dev's idea still helps inside a group. A long group like Integrations can have anchors or cards.

**Sidebar groups (about 7 to 8, not 10)**
- **Company:** profile
- **Billing:** plan, payment method, invoices
- **Team:** members and roles
- **Fleet:** vehicles and drivers
- **Alerts & notifications:** alert rules and channels together, since people think of them as one job
- **Integrations:** the 6, as a card grid
- **Data:** export
- **Security**

Put Billing and Security last or in a separate "Admin" cluster. The designer wanted every group listed, and this keeps that.

**Laptop (about 1280px)**
- The app's main nav stays on top or far left. Next to it is a settings sidebar about 220px wide, with the group names and the current one highlighted.
- The content area on the right is capped at about 720px so forms stay readable. It has a page title, short sections with headings, and a Save bar pinned at the bottom only when something has changed.
- Integrations shows a 2×3 card grid, each card with a Connect or Connected state. Team and Billing use tables.

**Phone**
- `/settings` shows the groups as a full-width list. Each row has an icon, a name, a one-line summary ("3 channels on"), and a chevron.
- Tapping a row opens that group full screen with a back arrow and the group name in the header. There is no sidebar on the phone.
- Forms are single column. The Save button sticks to the bottom. Tables turn into stacked rows, such as a member with their role and a menu.
- Integrations becomes a single-column list.

**Add search**
Put a search field at the top of the settings area on both layouts. With 40 settings, "where do I change the invoice email?" is the most common question, and search answers it faster than any navigation pattern.

**How to answer each person**
- **Designer:** you got the sidebar with every group.
- **Dev:** it's one route per group, so there's no giant page to build or maintain, and anchors still work inside long groups.
- **PM:** tabs are the right idea for 4 to 6 sections, and you have more than that. If Alerts later needs sub-views like Rules and Channels, use tabs inside that group.
