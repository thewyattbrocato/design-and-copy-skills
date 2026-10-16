I'd group the 14 toggles by **what the notification is about**, put the two channel masters and quiet hours at the top, and show each row's channel choices inline. Most of the overwhelm comes from the flat list, not the count.

**Proposed layout**

```
Delivery
  Push notifications        [master toggle]
     Quiet hours            [schedule: 10pm–7am]   ← only affects push, so it lives here
  Email notifications       [master toggle]

Garden care
  Watering reminders        Push ☑  Email ☐
  Frost alerts              Push ☑  Email ☐
  Harvest windows           Push ☑  Email ☐

Community
  Friend requests           Push ☑  Email ☐
  Comments on my beds       Push ☑  Email ☐
  Shared bed invites        Push ☑  Email ☑

Ideas & digests
  New plant suggestions     Push ☐  Email ☐
  Plant of the week         Push ☐  Email ☑
  Weekly summary            Email ☑

News & offers
  Product news              Email ☐
  Sale announcements        Email ☐
```

The checkbox values are placeholders. Show only the channels each type actually sends through, and set defaults that match what your backend does.

**Why this works**

- **Grouping by topic** lets people find "the frost thing" in the garden section without scanning 14 labels.
- **A channel grid per row** replaces the separate push and email toggles, so each notification type is a single decision.
- **Marketing sits apart in its own group.** Product news and sale announcements are the most likely to annoy people, and a clear "News & offers" section makes them easy to turn off without touching anything else.
- **Quiet hours sits under push.** Putting it at the bottom reads as a global setting when it only affects push.

**Smaller improvements**

- When a master toggle is off, grey out its children instead of hiding them. People then understand why a row isn't working.
- Collapse groups by default and show a summary such as "3 on" in the header. Expand a group on tap.
- Use plain outcome labels ("Frost warnings for my beds") if the current names are developer-facing.
- Keep the defaults conservative. Turn on the time-sensitive garden alerts and leave the email digests and promotions off until people opt in.

If you want, I can sketch this as a React or SwiftUI component, or check the current screen's code if you point me at it. The repo isn't a git repository here, so I'd need the path to the file.
