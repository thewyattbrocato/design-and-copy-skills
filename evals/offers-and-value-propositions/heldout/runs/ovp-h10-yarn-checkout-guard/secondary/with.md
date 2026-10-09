I'd cut **company name**, **phone number**, and **how did you hear about us** — none of those are required to complete a yarn subscription transaction. Phone is nice to have for delivery issues but buyers won't provide it under checkout friction; "how did you hear about us" is pure marketing attribution that works better asked after purchase (via follow-up email) when you're not asking them to spend money.

**Reordered flow:**

1. **Email** (needed for everything downstream)
2. **Full name** (quick, low friction)
3. **Shipping address** (the actual need)
4. **Billing address** (with checkbox: "Same as shipping address" — tick by default)
5. **Promo code** (optional, tempting right before payment)
6. **Card details**
7. **Create a password** (optional here, or move to post-checkout)

That's down from 10 fields to 6–7 visible ones (address sections collapse significantly with the checkbox).

**On the 402 error:** "Error 402" is a bank code that means nothing to customers. Replace it with something like *"Your card was declined. Please check the number, expiration, and CVC, then try again—or use a different payment method."* Give them a path forward, not a number.

The password field is the wildcard—if you auto-generate a temporary one and email it, you can remove this step entirely and save a field. If you want them to set it now (stronger for account ownership), keep it but make it the very last field, after they've already committed mentally by filling out the card.
