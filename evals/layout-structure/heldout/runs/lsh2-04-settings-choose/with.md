**Pick: the left sidebar, with one change. Only one group's content shows at a time, and the sidebar becomes a drill-down list on phones.**

The PM's tabs and the dev's single page both break down at your size.

- **Top tabs** work for about 5 flat destinations. You have about 10 groups. Several of them (integrations, team and roles, alert rules) have their own sub-lists. Tabs would overflow on a laptop and become a horizontal scroll on a phone, and a user can't tell what's hidden.
- **One long page** with anchors gives you about 40 controls in one scroll. Users would have to remember where things are, and anchor links would only help them jump. Save behavior also gets muddy, because it's unclear what "Save" covers. The dev's idea does have one good use, described below.

The sidebar scales to the 10 groups and nests if you add more. It shows the whole map at once, so people can find "where do I change alert thresholds?" without hunting.

## Laptop (about 1280px wide)

- **Header:** the app's global nav, with "Settings" as the page title.
- **Sidebar:** about 15rem wide, left-aligned with the app's content edge and sticky while the main area scrolls. It lists the groups in this order:
  - Company profile
  - Team and roles
  - Vehicles and drivers
  - Alert rules
  - Notification channels
  - Integrations
  - Billing and invoices
  - Data export
  - Security
- **Order:** it follows how often people visit and what they do. Daily-ish operations come first, billing and security later. Putting a small divider before the account-level items (Billing, Data export, Security) is optional, but I'd do it. Style the sidebar quieter than the global nav so the two don't read as the same thing.
- **Main area:** one group at a time, with a page title and a one-sentence purpose. The form column is capped at about 40–60ch, with labels above fields. Leave the extra width empty. Don't stretch fields across it.
- **Wide content:** tables are the exception to the cap and can fill the width. That covers team members, vehicles and drivers, and alert rules. Give them frozen name columns.
- **Save:** each group has its own save bar, pinned at the bottom of the main area and always visible. It's disabled until something changes.
- **Integrations:** a grid of 6 equal cells, each with logo, name, status and Connect/Manage. A cell opens its own detail view.
- **The dev's idea, used well:** inside a long group such as Alert rules or Security, an "on this page" list can sit at the top, or on the right on wide screens. That gives the dev anchor links where they help.

## Phone (about 390px wide)

- **First screen:** the sidebar becomes the screen. Settings opens as a full-width list of the 9 groups, with a one-line summary under each name (for example "Alert rules · 12 active") and a chevron.
- **Tapping a group:** it pushes a full-screen view with a back arrow labeled "Settings". The group's page title is next to the arrow.
- **Forms:** single column, full width, labels above fields, tap targets at least 44px.
- **Tables:** they become stacked cards (one per person, vehicle or rule), not sideways-scrolling grids.
- **Save:** a sticky bar at the bottom of the screen, shown only when there are unsaved changes. Leaving with unsaved changes asks first.
- **Integrations:** one column of 6 cells instead of a grid.
- **Why not a hamburger or a dropdown:** a list as the landing screen keeps the map visible and keeps the main action near the top. A drawer would hide it.

## Things to settle before building

1. Per-group save versus per-field autosave. I'd use per-group save for anything with consequences (roles, billing, security) and apply toggles immediately only for simple on/off switches.
2. Whether Security needs its own re-authentication step on entry. That's common for this kind of group.
3. Search across settings. At 40 items it isn't required, but a small search box at the top of the sidebar is cheap and would settle the designer/dev/PM debate for users who don't know the group names.
