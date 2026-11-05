**Go with the designer's left sidebar, but make each group its own page rather than one scrolling list.** The sidebar picks a group, and the main area shows only that group's settings.

**Why not the other two**
- **Top tabs:** You have 9 groups, which is too many for a tab row. On a phone they'd scroll sideways and hide the later ones. Tabs also look the same as your app's main navigation, so people can't tell which level they're on.
- **One long page:** 40 settings on one page means a lot of scrolling and no sense of where you are. It also has a single Save problem: it's unclear what a button covers. Anchor links only fix the first of those.

**Sidebar groups (9, in four clusters)**
- Account: Company profile, Billing & invoices, Team & roles
- Operations: Vehicles & drivers, Alert rules, Notification channels
- Connections: Integrations, Data export
- Security

**Laptop**
- A sidebar about 15rem wide sits on the left, under the app header. Its left edge lines up with the header's left edge. It has a small search box at the top, since people will look for a specific setting.
- The main area holds one group at a time, with the group name as a heading.
- Forms and toggles sit in a column about 40–45rem wide, so labels and fields stay close together. Sections inside a group get subheadings and their own Save button.
- Table-style groups use the full main width: Team & roles, Vehicles & drivers, and Alert rules.
- Integrations is a list of 6 rows. Each row has a name, a status, and a Connect or Manage button, and Manage opens that integration's detail.
- If a group has two distinct halves, use tabs inside that group only. Billing could split into Plan and Invoices. That gives the PM their tabs in the one place they fit.

**Phone**
- The sidebar becomes the first screen. "Settings" opens a full-width list of the 9 groups, with the clusters as small labels and a chevron on each row. The search box sits at the top.
- Tapping a row opens that group as a single-column screen with a back arrow to "Settings". I'd avoid a hamburger drawer, because it hides the only map of the area.
- Fields stack full-width. Tables become cards or compact rows, such as a vehicle name with its driver and status.
- Save sits in a bar fixed to the bottom of the screen, and it only appears once something has changed.
- The source order is the list, then the group, then its sections. The back button is always at the top, so nothing important ends up below the fold.

**For your dev**
- Give every group its own URL, such as `/settings/billing`, and every section an anchor, such as `/settings/billing#invoices`. Links from emails, support, and alerts then land exactly where they should. Anchor links still work, just inside a group instead of across the whole page.
- Build the sidebar as a plain list of links. The same component then renders as the laptop sidebar and as the phone's first screen.
