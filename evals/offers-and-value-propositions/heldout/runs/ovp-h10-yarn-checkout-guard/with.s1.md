# Checkout fields

## Cut
- **Company name**: wrong for a consumer yarn product. If you have wholesale buyers, give them a separate path.
- **Phone number**: cut it unless your carrier requires it for shipping. If it's required, mark why ("for delivery updates") and keep it after the address.
- **"Create a password"**: let people check out as a guest. Afterward, offer "Save your details" or send a magic-link email.
- **Separate billing address**: default to "Billing same as shipping" (checked). Only reveal billing fields if they uncheck it.
- **Full name as one field**: keep it, but don't split it into first and last unless your systems need that. Add address autocomplete to cut typing.

## Move off the checkout page
- **"How did you hear about us"**: ask on the order confirmation page. It's one click, optional, and doesn't cost you any sales. Don't ask it before payment.
- **Promo code box**: collapse it behind a "Have a code?" link. A visible empty box sends people off to search for codes, and many don't come back.

## Order for the rest
1. **Email**: this also lets you recover abandoned carts.
2. **Shipping name and address**: with autocomplete.
3. "Billing same as shipping" checkbox.
4. **Shipping method and cost**: if you have options.
5. **Promo code** (collapsed link).
6. **Card details**: with a wallet option (Apple Pay, Google Pay, Shop Pay) at the very top of the page, since it skips everything above.
7. **Order summary**: for a subscription, state the price, billing frequency, next charge date, and how to pause or cancel. This is both a trust signal and a way to head off disputes and chargebacks. Keep the summary visible throughout, or on top for mobile.

## The "Error 402" message
402 means "Payment Required", an HTTP status code. Your customers shouldn't see it. Map your payment processor's decline codes to plain messages:

| Decline reason | Message |
|---|---|
| Generic decline | "Your card was declined. Please try another card or contact your bank." |
| Insufficient funds | "That card doesn't have enough available funds. Try another card." |
| Incorrect number, expiry, or CVC | "Check your card number, expiry date, and security code." |
| Expired card | "That card has expired. Please use a different card." |
| Processing or network error | "We couldn't process your payment just now. You haven't been charged. Please try again." |

Also:
- Keep everything they entered. Never clear the form on a decline.
- Show the error right next to the card fields and move focus there.
- Don't say *why* the bank declined if you don't know, because processors often don't tell you.
- Offer an alternative such as a wallet, PayPal, or another card.
- Log the real code on your side for debugging.

## Measure it
Use your analytics to find where people actually drop off (field-level if you can). If most drops happen at the card step, fix the decline handling first. If they happen earlier, the form-length changes above matter most. A/B test the guest checkout and the wallet buttons if you have the traffic.

If you share the checkout code, I can make these changes directly, including the error mapping.
