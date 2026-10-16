**1) Delayed-feed banner**

> **{Carrier} updates are delayed.** What you see may be up to 30 minutes behind.

The text is about 80 characters, so it should fit in two lines on a phone. "Delayed" matches your term for the feed state. "May be" is accurate because the info isn't necessarily stale.

**2) Failed-refresh toast**

> Couldn't refresh. Try again.

It's short enough for one line. It doesn't say whether the cause was the network or the server, because the user can't act on that difference. The fix is the same either way.

**Alternates**
- Banner, shorter: "{Carrier} is running behind. Tracking may be up to 30 min out of date."
- Toast, a bit warmer: "Couldn't refresh. Please try again."
- Toast, if you want to hint at the cause: "Refresh failed. Check your connection and retry." This is longer and may wrap on small screens. It also points at the network when the server might be the problem.

If the carrier name might be long or missing, use a fallback of "Carrier updates are delayed." so the banner doesn't break.
