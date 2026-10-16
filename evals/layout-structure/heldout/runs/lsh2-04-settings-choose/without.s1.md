**Pick: left sidebar with grouped sections, one group per page.** It collapses to a drill-down list on phones.

**Why not the others**
- **Top tabs:** You have 8+ groups, and some of them (Integrations with 6 items, Team with roles) are deep. Tabs run out of width at about 5–6 labels and then turn into a scroll or overflow menu. They also give you no second level.
- **One long page:** 40 settings on one page is hard to scan, and the anchor links are really just a sidebar. Each section needs its own save and error state, which gets awkward on a single scroll. Deep-linking to a section is also less reliable than a real route.

The sidebar is the designer's pick, but I'd change one thing: each group gets its own URL (`/settings/billing`). That keeps the dev's linkability and gives the PM a visible top level.

**Sidebar groups (about 8)**
1. Company profile
2. Team & roles
3. Vehicles & drivers
4. Alert rules
5. Notifications
6. Integrations
7. Billing & invoices
8. Data & security (export plus the security items)

If you want a visual break, put a divider before Billing and Data & security so the list reads as "fleet setup" and "account admin."

**Laptop**
- A fixed sidebar about 240px wide sits on the left, with the group names and the current one highlighted.
- The content pane is on the right, capped at about 720px so form fields don't stretch.
- Each page has a title, short sections with headings, and a save bar. Settings that apply immediately, like toggles, don't need one.
- Integrations is a list of 6 cards, each with a Connect or Manage button. Team members is a table.
- A search box at the top of the sidebar jumps straight to any of the 40 settings.

**Phone**
- `/settings` shows only the list of groups, as full-width rows with chevrons. Nothing else is on screen.
- Tapping a row opens that group's page with a back arrow and the group name in the header. That's the standard iOS and Android settings pattern.
- Forms are a single column. Tables, such as team members, turn into stacked cards.
- The save button is pinned to the bottom of the screen when a form has unsaved changes.
- Search stays at the top of the group list.

**Build note:** it's one layout component. At 768px and wider it shows the sidebar and content together. Below that it shows either the list or the page, depending on the route. That's a small amount of extra work compared to tabs.
