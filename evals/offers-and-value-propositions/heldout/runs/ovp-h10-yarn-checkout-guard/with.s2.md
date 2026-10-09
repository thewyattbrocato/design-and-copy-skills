# Checkout fields

## Cut
- **Company name.** You sell to individuals, so this adds friction. If you get wholesale or business buyers, put it behind an "Ordering for a business?" link.
- **Phone number.** Cut it unless your carrier requires it for delivery. If it is required, mark it clearly and say why ("for delivery updates").
- **Create a password.** Use guest checkout. After payment, offer "Save your details? Set a password" on the confirmation page, or send a magic-link email. For a subscription you do need an account, but you can create it silently from the email and let them set a password later.
- **"How did you hear about us."** Move it to the post-purchase confirmation page as an optional one-click question. You still get the data, and it can't cost you a sale.
- **Full name as a separate field from the shipping name.** Collect the name once, in the shipping address.
- **Billing address as a separate form.** Default to a "Billing same as shipping" checkbox, checked. Only reveal the billing fields if they uncheck it.

## Keep, but change
- **Promo code.** Collapse it behind a "Have a promo code?" link. A visible empty box sends people off to search for codes, and some don't come back.

## Order
1. **Email.** Put it first so you can capture abandoned carts. Add a "Continue as guest" note.
2. **Shipping address** with the name in it. Use address autocomplete.
3. **Plan and frequency summary** with a clear price, renewal cadence, and how to skip or cancel. Subscription buyers hesitate over this, so state it plainly near the payment step.
4. **Payment.** Card details, plus Apple Pay and Google Pay at the top, since those skip the form entirely. Billing address is only shown if they uncheck "same as shipping".
5. **Promo code link**, placed above the order total.
6. **Place order button.** Make the label specific, like "Start my subscription – $X/month".

The final form is about 6 fields: email, name, shipping address, card, and optionally a promo code.

# Declined card message

"Error 402" tells the customer nothing and looks like a site failure, so they leave. Fix it in three parts.

**1. Show a human message.** For example:
> "Your card was declined. This is usually something your bank flagged, not a problem with your order. Please check your card details or try a different card."

Keep what they typed. Don't clear the form or reload the page.

**2. Map the decline codes to specific messages.** Your processor returns a reason (Stripe, for example, returns codes like `insufficient_funds`, `incorrect_cvc`, `expired_card`, and `card_declined`). Use those:
- Wrong CVC or expiry: "The security code looks incorrect. Please re-check it."
- Expired card: "This card has expired. Please use a different card."
- Insufficient funds: "Your card was declined. Please try another payment method."
- Generic bank decline: "Your bank declined this charge. You may want to contact them or try another card."

Don't reveal more than the processor's safe-to-show messages. Detailed fraud reasons shouldn't be displayed.

**3. Give them a way forward.**
- Put the error right next to the card field, in text, not color alone, and move focus there.
- Keep the Apple Pay, Google Pay and PayPal options visible as alternatives.
- Log declines with their reason code. That tells you whether you have a real problem, like a misconfigured processor or a CVC or ZIP mismatch rule that is too strict.

# Measuring it
Compare checkout completion before and after. If you can, run the field cuts as an A/B test, since the effect of each change varies by audience. I'd expect the biggest wins from guest checkout, the digital wallets, and the decline message. Fixing the decline message also recovers customers who already wanted to buy.

If you share the checkout code, I can help implement the field changes and the error handling.
