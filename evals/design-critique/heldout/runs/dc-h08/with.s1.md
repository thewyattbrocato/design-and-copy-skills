I'd group the toggles by what they're about, put the two master switches at the top, and collapse the rest into sections. Here's the layout I'd use.

**Top: delivery channels (2 rows)**
- Push notifications (master)
- Email notifications (master)
- Quiet hours, as a row that opens a time picker rather than a plain toggle. It's a schedule, not an on/off setting, so it shouldn't look like the others.

When a master is off, grey out and disable the child toggles that depend on it. Show a one-line note like "Push is off, so these won't be delivered." That alone removes much of the confusion.

**Section 1: Garden care** (the core value of the app)
- Watering reminders
- Frost alerts
- Harvest windows

**Section 2: Community**
- Friend requests
- Comments on my beds
- Shared bed invites

**Section 3: Discover and news**
- New plant suggestions
- Plant-of-the-week
- Weekly summary email
- Product news email
- Sale announcements

**Why this works**
- **Five groups instead of 14 flat items.** Each section has 3–5 rows, which people can scan.
- **Order by importance.** Garden care comes first because those alerts are time-sensitive, and the marketing items go last.
- **Defaults carry the weight.** Garden care and community can default to on. Promotional items (sale announcements, product news) should default to off or be opt-in, so most people never need to visit them.
- **Channel per row.** If you want to cut the list further, make each row a single item with small Push and Email chips (for example, "Frost alerts: Push ✓ Email ✗"). That removes the need for separate email toggles and could shrink the screen to about 10 rows. The weekly summary and product news are email-only by nature, so they'd show only the Email chip.
- **Optional.** Collapse Discover and news by default, with a summary like "3 of 5 on".

**Watch for**
- Use plain labels with a short description under each. "Harvest windows" on its own is vague. "Tells you when crops are ready to pick" is clear.
- Keep each section's header visible while scrolling.
- Add a single "Pause everything" action, which is what most overwhelmed users actually want.

If you tell me whether this is iOS, Android, or web, I can adjust the pattern. For example, iOS conventionally uses grouped inset lists with a drill-down for the channel details.
