I'd group the 14 toggles by **what the notification is about**, put the channel-wide controls at the top, and split marketing email into its own section. Here's a layout:

```
Notifications

[ Push notifications            ● on ]   ← master
[ Email notifications           ● on ]   ← master
[ Quiet hours           10pm – 7am  > ]  ← a schedule, not a channel, so it sits apart

GARDEN CARE
  Watering reminders            ●
  Frost alerts                  ●
  Harvest windows               ●

COMMUNITY
  Friend requests               ●
  Comments on my beds           ●
  Shared bed invites            ●

DISCOVERY
  New plant suggestions         ●
  Plant of the week             ●

SUMMARIES & NEWS
  Weekly summary email          ●

MARKETING EMAIL
  Product news                  ○
  Sale announcements            ○
```

Why this works:

- **Two sections are the main fix for overwhelm.** Garden care is the core value and the most time-sensitive, so it goes first. Discovery and marketing are optional, so they go last and can be scanned past.
- **Marketing is separate on purpose.** Product news and sales are promotional, not operational. Users expect to opt out of them independently, and privacy rules such as GDPR and CAN-SPAM treat marketing consent differently. Keeping them apart makes that clear and keeps the other sections from looking like ads.
- **Master toggles go on top and act as gates.** When a master is off, grey out the rows beneath it and show a note such as "Push is off, so these won't reach your phone." Otherwise people flip a row and get no notification with no explanation.
- **Each section header can show a summary.** For example, "Garden care · 3 of 3 on" lets people see the state without expanding anything. You can make the section header itself a toggle when all of its items usually share one setting.
- **Use descriptions, not just labels.** A one-line subtitle under "Frost alerts" ("When temperatures near your beds drop below freezing") helps people decide faster than a bare switch.
- **Consider presets.** A "Essentials only / Everything" choice at the top handles most users who don't want to tune 14 items.

If you want fewer rows, the easiest merges are Friend requests and Shared bed invites into one "Social" toggle, and New plant suggestions and Plant of the week into one "Ideas" toggle. Keep Frost alerts and Watering reminders separate, since users often want one and not the other.
