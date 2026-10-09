I'd group the 14 settings by **what the notification is about**, and use a **topic × channel grid** instead of a flat list of switches. Most of the overwhelm comes from the list having no structure, and the two master toggles are doing a job the layout should handle.

**Proposed layout**

1. **Top: Pause and quiet hours**
   - Replace the two master toggles with a single "Pause all notifications" control, or keep them as "Push" and "Email" channel headers.
   - Quiet hours goes right below, as a time-range row, since it governs push timing and is more than a switch.

2. **Garden care** (the core value, so it comes first)
   - Watering reminders, frost alerts, harvest windows
   - Show Push and Email checkboxes per row. Most of these are push-only, so one cell may be empty.

3. **Community**
   - Friend requests, comments on my beds, shared bed invites

4. **Ideas and discovery**
   - New plant suggestions, plant of the week

5. **Email updates** (lowest priority, so it goes last and can be collapsed)
   - Weekly summary, product news, sale announcements

**Why the grid helps**

Each row is a topic and each column is a channel (Push, Email). That reduces 14 switches to about 10 cells, and the user sees "what do I get and where" at a glance. Empty cells mean that channel isn't offered for that topic, which is clearer than a disabled switch.

**Details that matter**

- **Hide marketing from the default view.** Put product news and sales under a "Marketing emails" disclosure, off by default, so the main screen is only the garden and social items.
- **Use a sensible default for the whole list.** Pre-enable garden care and social, and leave marketing off. Users who see a long list of "on" switches tend to feel they've been signed up for everything.
- **Gray out, don't hide, children of a master switch.** If push is paused, the push column should show as disabled with a note like "Paused in quiet hours" or "All push paused," so users understand why.
- **Add a one-line summary** at the top, such as "You'll get 4 push and 2 email notifications," so the screen reads as a status rather than a form.

If you tell me the platform (iOS, Android, web) or your component library, I can sketch the markup or a component structure for the grid.
