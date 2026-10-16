**Pick: the left sidebar, with each group as its own page.** Don't make it one long scroll, and don't use tabs.

**Why the other two lose**
- **Top tabs:** you have 9 groups, and Team, Alert rules and Integrations will grow. Nine tabs don't fit across a laptop, and on a phone they become a horizontal scroll strip where people miss the ones off-screen.
- **One long page with anchors:** 40 settings with different save behavior makes a very long scroll. Saving gets ambiguous ("did my billing change save when I edited alerts?"). Vehicles, drivers and alert rules are lists that grow, and they would push everything below them down the page. Your dev's instinct for deep-linkable sections is still right: give each group its own URL, like `/settings/alerts`.

**Sidebar grouping (9 items, under 3 quiet headings)**
- **Account:** Company profile, Billing & invoices, Team & roles
- **Operations:** Vehicles & drivers, Alert rules, Notification channels, Integrations
- **Data & security:** Data export, Security

**Laptop**
- The app's top bar is unchanged. Below it, a sidebar about 15rem wide sits on the left, aligned with the logo's left edge. It stays in view while the content scrolls. The current group is highlighted.
- The content area has a page title, a one-sentence description, then the controls. Form groups (Company profile, Security, Notification channels) use a column about 40–60ch wide, left-aligned, with labels above fields. Leave the empty space to the right empty.
- List-type pages (Vehicles & drivers, Team & roles, Alert rules) fill the width as tables with search and filters.
- Integrations is a list of 6 rows, each with a name, a status (Connected or Not connected) and a Connect or Manage button. Clicking one opens its detail.
- Each page has its own Save bar, which is always visible and only enabled when something has changed.

**Phone**
- `/settings` shows the 9 groups as a full-width list of rows with chevrons, under the same 3 headings. It doesn't show a sidebar or a form.
- Tapping a row opens that group full-screen with a back arrow and the group's title in the header. Forms stack in one column.
- Tables become cards or rows. A sticky Save button sits at the bottom of the screen.
- The URLs match the laptop's, so a link to Alert rules works on both.

**Worst cases to check before building**
- A translated label that's 40% longer.
- A company with 200 vehicles.
- An empty Integrations list.
- A non-admin user. Hide or lock the groups they can't edit, such as Billing, instead of leaving them as dead links.

I haven't built anything yet. If you'd like, I can sketch the sidebar and page as HTML or React.
