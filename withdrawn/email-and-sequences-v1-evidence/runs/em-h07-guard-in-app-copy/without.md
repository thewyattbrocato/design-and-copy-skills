**1) Banner (delayed carrier feed)**

> **{Carrier} updates are running behind.** Tracking info may be up to 30 minutes out of date.

If you can't pass the carrier name in, use:

> **Carrier updates are running behind.** Tracking info may be up to 30 minutes out of date.

The first sentence says what's happening. The second says what it means for the user. It should fit in about two lines on a phone.

**2) Toast (refresh failed)**

> Couldn't refresh. Try again.

If you have room, this version also covers the no-network case:

> Couldn't refresh. Check your connection and try again.

That one is about 50 characters. It may truncate on narrow phones, so I'd ship the shorter one unless you've tested the longer one.

The failure could be either no network or no server response, so "Check your connection" is a bit of a guess for the second case. The short version is accurate for both.
