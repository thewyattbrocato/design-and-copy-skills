**Cut these:**
- **Company name** — unnecessary for B2C yarn subscriptions
- **"How did you hear about us"** — move to post-purchase survey; it causes friction but isn't required to complete the order

**Reorder like this:**
1. Email (establishes identity, used throughout)
2. Full name
3. Shipping address (the primary need)
4. Billing address (offer a "same as shipping" checkbox to skip this if it matches)
5. Phone (make optional if possible; only truly needed if your shipper requires it)
6. Card details
7. Promo code (put it here at the end — the customer is already committed)
8. Create password (or skip entirely and send a login link via email instead — fewer fields = higher conversion)

**The "Error 402" problem:** That's technically accurate HTTP but meaningless to users. Replace it with something like: *"Your card was declined. Check that your card number, expiration date, and CVV are correct, or try a different payment method."* If you have data from the processor, be more specific: *"Insufficient funds"* or *"Your issuer declined this transaction — contact your bank."*

**Why this order:** You're moving from identity → shipping logistics → payment → optional friction. Email-first establishes the account, shipping address is the core value they want, and putting the promo code at the end means they won't bail if they can't remember a code.

How far along in checkout are people dropping off right now — early fields or at payment?
