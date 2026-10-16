**1) Banner (carrier feed delayed)**

> **{Carrier} updates are running late.** Tracking info may be up to 30 minutes out of date.

If you want a shorter version:

> **Tracking may be behind.** {Carrier} is sending updates up to 30 minutes late.

**2) Toast (refresh failed)**

> Couldn't refresh. Please try again.

Alternative that hints at the cause:

> Couldn't refresh. Check your connection and retry.

**Notes**
- I left out "we'll update automatically" because I don't know if the app does that. If it does, add "We'll update when it catches up" to the banner.
- The toast doesn't say "server error" or "no network," since the user can't act on the difference. Both causes lead to "try again." The second alternative mentions the connection, which covers the more common cause. It's slightly less accurate when the server is the one that failed.
- If the banner is tied to one shipment, use "{Carrier}"; if it can cover several carriers, use "Some carriers" in its place.
