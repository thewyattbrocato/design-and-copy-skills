Here's my critique, ordered by impact. This is based on your description only. I haven't seen the table.

## Biggest problems

**1. Hover-only row actions: change this first.**
- Touch and tablet users can't see them at all.
- Keyboard users can't reach them unless they're also revealed on focus.
- Nobody can discover them without mousing over the row.
- Suspend and delete sit next to each other, so a slip on a hover target is costly.

*Fix:*
- Keep a visible, quiet affordance on every row. A "⋯" overflow menu works, or an Edit button plus a "⋯" menu.
- Put suspend and delete in the menu, not as adjacent icons.
- Delete should ask for confirmation or offer undo, and should be styled as destructive.
- If you keep hover reveal as a secondary treatment, also reveal on `:focus-within`.
- Give icon-only buttons `aria-label`s.

**2. Blank cells for "no last login."**
- A blank is ambiguous. It could mean never logged in, missing data, or a render failure.
- "Never logged in" is useful admin information. It usually means an invited user who hasn't activated, or a stale seat.

*Fix:*
- Show "Never" in muted text, or a "Never signed in" or "Invited" status.
- Use an em dash only if the value is truly unknown, and say which case it is in a tooltip.
- Make the column sortable and filterable so admins can find these users.

**3. 11px text.**
- It's below comfortable reading size, especially for dense data with names and emails.
- It fails most accessibility expectations for admins who aren't young or who work on small laptop screens.

*Fix:*
- Use 13–14px for body cells, with 12px as the floor for secondary text such as emails or timestamps.
- At about 40 rows you don't need that much density. Normal row height with 13px text still fits comfortably with pagination or a sticky header.

## Smaller problems

**4. Centered numbers.**
- Centered numbers can't be compared by scanning a column, because digits of different lengths don't line up (e.g. 9, 120, 1,045).

*Fix:*
- Right-align numeric columns, and right-align their headers to match.
- Use `font-variant-numeric: tabular-nums`.
- Format consistently: thousands separators, and storage in one unit or with an auto-scaled unit (e.g. "1.2 GB") plus a used/limit comparison if relevant.
- Left-align text columns such as name, email, and role.

**5. 1px border on every cell.**
- The full grid adds visual noise and competes with the data. At 8 columns × 40 rows that's roughly 320 boxes.

*Fix:*
- Remove vertical borders and use only light horizontal row dividers, or subtle zebra striping, but not both.
- Use more cell padding (about 12px horizontal and 10px vertical) instead of lines to separate columns.
- Keep a slightly stronger border under the header.

## Things to add or check

- **Sticky header** so the column labels stay visible while scrolling.
- **Sort and filter** for status, role, and last login. Admins mostly look for exceptions, such as suspended users, inactive users, or seat overuse.
- **Status as a labeled badge** (Active, Suspended, Invited), with text and not color alone. Suspended rows could also be visually muted.
- **Last login as a relative time** ("3 days ago") with the exact timestamp on hover.
- **Bulk selection**, if admins ever act on more than one user at a time.
- **Narrow screens:** 8 columns won't fit on a small screen, so decide which columns to hide or collapse and allow horizontal scroll with a pinned name column.
- **Empty and loading states** for the table.

## Suggested priority

1. Make row actions visible, and move destructive ones behind a menu with confirmation.
2. Replace blanks with an explicit "Never."
3. Raise text size to 13–14px.
4. Right-align numbers with tabular figures.
5. Drop the vertical borders.

If you share the markup or a screenshot, I can give concrete CSS and component changes.
