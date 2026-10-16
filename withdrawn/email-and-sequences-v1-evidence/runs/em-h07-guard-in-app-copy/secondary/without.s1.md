**1) Delayed carrier feed banner** (about two lines)

> Carrier updates are running behind. Tracking info may be up to 30 minutes out of date.

Alternative, if you want the banner to lead with the status:

> Delayed carrier updates. Tracking info on this screen may be up to 30 minutes old.

**2) Refresh failed toast** (one line)

> Couldn't refresh. Try again.

Alternative: `Couldn't refresh. Please try again.`

The toast doesn't say "check your connection" because the failure could be the server not responding, not just the network. If you want to name the network case separately, you could show `No connection. Try again.` when the device is offline and keep the generic line for other failures.
