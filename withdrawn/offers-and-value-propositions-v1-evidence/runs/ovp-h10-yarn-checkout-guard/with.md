## Fields to cut

- **Company name**: you sell to individual knitters, so this is noise. Cut it.
- **Phone number**: you don't need it to ship yarn. Cut it, or make it optional only if your carrier requires it for delivery.
- **"How did you hear about us"**: move it to the order confirmation page as a one-click survey. You still get the data, and it no longer competes with payment.
- **Create a password**: cut it. Create the account after purchase with a "set a password" email or magic link. For a subscription, the customer will need an account to manage it, but they don't need to set a password at checkout.
- **Full name as a separate field**: keep one name field. Put it with the shipping address, since the carrier needs it there anyway.
- **Billing address**: default to "same as shipping" with a checked box. Only show the fields if they uncheck it. Most card processors only need the postal code for AVS.
- **Promo code box**: don't remove it, but hide it behind a "Have a code?" link. A visible empty box sends people off to search for coupons, and some don't come back.

## Order for the rest

1. **Email**: first, so you can send abandoned-cart emails if they leave.
2. **Shipping address**, including name.
3. **Billing address**: a "same as shipping" checkbox, checked by default.
4. **Payment**: card details, plus a "Have a promo code?" link above or beside the order summary.
5. **Place order** button. Say the billing cadence and price next to it (for example "$38 every month, skip or cancel anytime"). Subscriptions lose people over uncertainty about commitment as much as over field count.

That takes you from 10 fields to about 4 or 5 for most people. Also turn on address autocomplete, card autofill attributes (`autocomplete="cc-number"` and similar) and Apple Pay or Google Pay. Wallet payments skip almost every field.

## The "Error 402" message

A 402 is a raw payment-required status code. The customer can't act on it. Replace it with messages that say what happened and what to do next. Map your processor's decline codes roughly like this:

- **Generic decline or do not honor**: "Your card was declined. Please try another card or contact your bank."
- **Insufficient funds**: "That card doesn't have enough available funds. Try another card."
- **Incorrect number, expiry or CVC**: say which field is wrong and highlight it, for example "Check the expiration date."
- **Expired card**: "This card has expired. Please use a different one."
- **AVS or postal code mismatch**: "The billing postal code doesn't match your card. Please check it."
- **Processing or network error**: "Something went wrong on our end. You haven't been charged. Please try again."

Rules for all of them:
- Keep the form filled in. Never clear the card or address fields after an error.
- Put the message next to the payment section, not in a toast that disappears.
- Don't blame the customer ("invalid card"). Don't reveal anything the issuer wouldn't want shown, such as fraud-related reasons. Use the generic decline wording for those.
- Offer a clear next step, such as a different card or a wallet button.
- Log the real decline code on your side so you can see which declines are driving drop-off.

To confirm where people are actually leaving, check your funnel analytics. If most drop-offs happen after card entry rather than before it, the decline handling matters more than the field count.
