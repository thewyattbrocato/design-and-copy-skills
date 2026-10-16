**Pick: the left sidebar.** It's the designer's option, with one borrowing from the dev's. The sidebar lists the groups, and each group is a single scrolling page of sections with its own anchor links.

**Why not the other two**
- **Top tabs:** you have 9 groups (company, billing, team, vehicles and drivers, alerts, notifications, integrations, export, security). That's too many for a tab row. On a laptop they'd crowd or truncate, and on a phone they'd become a horizontal scroller where people miss the tabs off-screen. Tabs also can't nest, so integrations (6 of them) would need a second tab row.
- **One long page:** with 40 settings, people would have to scroll past billing to find a security toggle. Browser find and deep links work, but the page has no sense of place. Long forms also make "unsaved changes" ambiguous.

**Laptop (about 1280px)**
- **Sidebar:** about 14–16rem wide, fixed in view, with the 9 groups in the order people use them. Put the rarely changed ones (company, billing) and the sensitive ones (security) toward the ends. The active group is clearly marked.
- **Content column:** it starts at the same left edge as the page title. Forms are capped at about 40–60ch, with labels above fields. Extra width stays empty rather than stretching the controls.
- **Inside a group:** a heading and a one-sentence purpose, then the controls. Big groups get a small "On this page" list at the top. Alerts, team and integrations are the likely ones. This is the dev's anchors idea, applied locally.
- **Integrations:** a list of 6 equal rows or cards, each with a status and a Connect or Manage button. Each opens its own detail view instead of adding more controls to the page.
- **Team members and vehicles/drivers:** these are tables, not forms. They can use the full content width.
- **Saving:** either each section saves on its own, or a sticky save bar appears when something changes. Pick one pattern for the whole area.

**Phone (about 390px)**
- **Level 1:** the settings screen opens as a plain list of the 9 groups. Each row has an icon, a name, a one-line summary and a chevron. Nothing else is on screen.
- **Level 2:** tapping a row opens that group full-screen with a back arrow and the group name in the header. This is a standard drill-down, so the sidebar doesn't become a hamburger menu.
- **Within a group:** a single column with full-width fields. The "On this page" list collapses into a jump menu at the top. Tables turn into stacked cards, one per member or vehicle.
- **Saving:** the save button sticks to the bottom of the screen, above the keyboard.

**Checks before you build**
- **Worst case:** a long company name, a team with 100 members, zero integrations connected, and German labels about 35% longer. The sidebar and rows should survive all of these.
- **Roles:** if non-admins can't see billing or security, hide those rows for them instead of showing a locked page.
- **Search:** at 40 settings, a search box above the sidebar (and at the top of the phone list) is worth adding. It's the only thing here that removes the need to know which group a setting lives in.

**For the meeting**
- **Designer:** gets the sidebar.
- **Dev:** gets anchor links and deep-linkable URLs for every group and section (`/settings/alerts#escalation`).
- **PM:** the top-level navigation stays flat and quick to scan. If they want tabs, use them inside a group, for example Members / Roles / Invitations under Team.
