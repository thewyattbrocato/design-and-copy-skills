**Pick: the left sidebar, with each group as its own page.** Group the sidebar's nine entries under three small headings.

**Why not the other two**
- **Top tabs:** you have nine groups, and tabs run out of room at about five. On a phone they turn into a scrolling strip with hidden tabs.
- **One long page:** the 40 settings aren't all short form fields. Team, vehicles and drivers, and invoices are tables or lists, and integrations is six cards. Stacked on one page, they bury each other. Anchor links also leave people scrolling through billing to reach alert rules.
- **Sidebar:** nine groups is what side navigation handles well, and the sidebar always shows where you are. The designer's pick fits the content best.

**Sidebar contents**
- **Account:** Company profile, Billing & invoices, Team & roles
- **Operations:** Vehicles & drivers, Alert rules, Notification channels, Integrations
- **Data & security:** Data export, Security

**Laptop**
- The page has the app header on top. Below it is a sidebar about 15rem wide that stays in place while the content scrolls.
- The selected item is highlighted. The sidebar's left edge lines up with the header logo.
- The content area shows one group at a time: a title, a one-sentence purpose line, then the controls.
- Form groups like Company profile and Security stay in a column about 40 to 60 characters wide, with labels above the fields. Leave the extra width empty instead of stretching the fields.
- Table groups like Team, Vehicles & drivers, and Invoices use the full content width.
- Integrations is a wrapping grid of six equal cards. Each shows the logo, the name, a status, and a Connect or Manage button.
- Save sits in a bar that stays visible, and it appears only when something has changed.

**Phone**
- The sidebar becomes its own screen. Tapping Settings opens a full-width list of the nine groups under their three headings, with a chevron on each row.
- Tapping a row opens that group as a single column with a back arrow to the list. This is better than a hamburger drawer, because the list is the menu and nothing is hidden.
- Tables become stacked rows: a name, a role or status, and a chevron that opens a detail view.
- Integration cards go to one column.
- Save is pinned to the bottom of the screen when there are unsaved changes.

**What to give the others**
- **Dev:** every group gets its own URL, such as `/settings/billing`, so links and deep links work. Within a long group like Security or Alert rules, anchors can still jump to a section.
- **PM:** if a group such as Alert rules later has distinct subareas (rules, schedules, history), use tabs inside that group. Local tabs work well there, but they shouldn't be the top-level navigation.
