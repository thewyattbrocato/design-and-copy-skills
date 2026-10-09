# Checkout recommendations for the yarn subscription page

## Cut
- **Company name:** Almost no yarn buyers need it. If you have wholesale customers, give them a separate flow.
- **Phone number:** Remove it unless your carrier requires it for delivery. If it's needed, make it optional and say why ("for delivery issues only").
- **"How did you hear about us":** Move it to the order confirmation page, where it costs you nothing.
- **Create a password:** Remove it. After payment, offer "Set a password to manage your subscription" on the confirmation page, or use an emailed magic link. Subscribers do need an account eventually, but not before they've paid.
- **Separate billing address:** Default to "Billing same as shipping" (checked), and only show the billing fields if they uncheck it.
- **Full name as a separate field:** Merge it into the shipping address, which already needs a name. The card form can use that name too.

## Keep, but change
- **Promo code:** Collapse it behind a "Have a promo code?" link. A visible empty box sends people off to search for codes, and some don't come back.

## Order
1. **Email.** This also lets you send abandoned-cart emails if they leave.
2. **Shipping address.** Include the name here, and use address autocomplete.
3. **Plan and delivery summary,** with the price, the renewal cadence and a "cancel anytime" line if it's true. Showing the recurring charge clearly at this step cuts both drop-off and chargebacks.
4. **Payment.** Card details, plus Apple Pay or Google Pay if you can. Express wallets let people skip steps 1–2 entirely, so put them at the top of the page.
5. **Promo code link,** placed near the order total.

That takes you from 10 fields to about 4–5 visible inputs, plus the card.

## The "Error 402" message
Error 402 is "Payment Required." It tells the customer nothing and sounds like the site is broken. Fixes:

- **Show the decline in plain language, next to the card field.** For example: "Your card was declined. Please try another card or contact your bank."
- **Map the processor's decline codes to specific messages.** Stripe, for example, returns codes like `insufficient_funds`, `expired_card`, `incorrect_cvc` and `incorrect_zip`. Say what went wrong and what to do when you can. For a generic bank decline, don't guess the cause. Stick with "contact your bank or try another card."
- **Keep everything they typed.** Don't clear the form or reload the page. Put focus back on the card field.
- **Offer an alternative** like PayPal or a wallet, right by the error.
- **Don't blame the customer** ("invalid card") when the bank declined it.
- **Log the raw code internally** so you can see which declines are costing you the most.

## Order of effort
Do the error message and the password removal first. They're quick and likely to have the biggest effect. Then do the field cuts and the express wallets. A/B test the changes if you have the traffic. Otherwise, compare checkout completion rate before and after.

If you share the checkout code or your payment processor, I can help implement the error mapping and the form changes.
