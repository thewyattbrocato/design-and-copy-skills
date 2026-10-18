**Group the toggles by what they're about, and move the global controls to the top.** The problem is that 14 identical rows give no hierarchy. Sorting them into a few labeled sections fixes most of it.

**Suggested layout**

**Top: global controls**
- **Pause all notifications** (or the two master switches, shown together)
- **Quiet hours**: a row that opens a time picker, not a bare toggle

**Garden care** (things the user acts on)
- Watering reminders
- Frost alerts
- Harvest windows

**Inspiration**
- New plant suggestions
- Plant of the week

**Community** (social)
- Friend requests
- Comments on my beds
- Shared bed invites

**Summaries**
- Weekly summary email

**News & offers** (collapsed by default, since it's the least essential)
- Product news email
- Sale announcements

This gives 3 global, 3 + 2 + 3 + 1 + 2 = 11 per-topic toggles, grouped under 5 headings that a person can scan in seconds.

**Details that matter more than the grouping**

- **Make the masters hierarchical.** When "Push" is off, grey out the push-based rows and say why ("Turned off in Push settings"). Don't let people flip a toggle that does nothing.
- **Use a sentence for each row**, not just a label. "Frost alerts: Get warned when a cold night threatens your plants" tells people what they're agreeing to.
- **Consider a channel matrix instead** if the real question is "push or email?" Rows are events, columns are Push and Email. It's compact and scannable, but it's only better if most people think in channels rather than topics. I'd go with topic groups for a garden app.
- **Frost alerts may deserve a different default.** They're time-sensitive and tied to plant loss, so they're the one most users will want on. Pick the defaults so the common case needs no changes.
- **Review whether 14 is too many.** Merging product news and sale announcements into one "Tips & offers" toggle would cut the list further without losing anything users care about.

If you share your current screen's components or framework, I can sketch the actual markup or the settings data model.
