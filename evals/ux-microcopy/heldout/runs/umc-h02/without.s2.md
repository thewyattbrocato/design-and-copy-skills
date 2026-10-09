**Banner text:**

> **Your payment didn't go through.** We couldn't charge the card ending in 4417. We'll try again automatically in 3 days. Your account stays fully usable until then. If the retry fails, that changes, so update your card now to avoid any interruption.

**Button label:** Update card

(The button should link to Settings > Billing.)

Notes:
- I dropped the "PF-22" code and the "ERROR" prefix, since neither helps the customer. Keep the code in logs or a tooltip if support needs it.
- You said the account is fully usable until the retry fails, but not what happens after. "That changes" is deliberately vague so the banner doesn't promise a specific consequence. If you'd like it plainer, "Your account stays fully usable until then" alone also works. Drop the last sentence.
- A shorter version for narrow layouts: "We couldn't charge your card ending in 4417. We'll retry in 3 days. Update your card to keep things running smoothly."
