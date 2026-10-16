# Checkout field recommendations

## Cut
- **Company name.** It's irrelevant for most yarn buyers. If you want wholesale customers, give them a separate flow.
- **Phone number.** Cut it unless your carrier requires it. If you keep it, make it optional and explain why, for example "for delivery updates."
- **"How did you hear about us."** Move it to the order confirmation page as a one-click survey. You still get the data, and it can't block a sale.
- **Create a password.** Cut it. For a subscription, send a magic-link email after purchase so they can manage it, or offer "set a password" on the confirmation page.
- **Separate billing address.** Default to "billing same as shipping" and show the billing fields only if the box is unchecked. Card payments often only need a postal code.
- **Full name as one field.** Keep a name, but use a single "Full name" field. Don't split it into first and last. Card forms often collect the name anyway.

## Keep, but change
- **Promo code.** Collapse it behind a "Have a promo code?" link. A visible empty box sends people off to search for codes, and some never come back.

## Order of the remaining fields
1. **Email.** This comes first so you can send abandoned-cart emails even if they leave. Check the format as they type.
2. **Shipping name and address.** Use address autocomplete. It cuts typing and bad addresses.
3. **Shipping method and price.** Show the cost of any shipping before they reach payment, because surprise costs are a leading cause of drop-off.
4. **Payment.** Put Apple Pay, Google Pay, and Shop Pay at the top. They fill in email, name, and address in one tap, which can make the other steps unnecessary on mobile. Card details go below that.
5. **Order summary and subscription terms.** Keep these visible throughout. State the price, the billing frequency, the next charge date, and how to cancel. Clear terms reduce hesitation and chargebacks on a subscription.

Use one page, or at most two steps. A progress indicator doesn't help much with only three or four sections.

## Declined cards
"Error 402" tells the customer nothing and many will leave. Fix it in three parts:

- **Say what happened in plain language.** "Your card was declined. This is usually something your bank needs to clear. Please try another card or contact your bank."
- **Match the message to the decline code if your processor returns one.**
  - Insufficient funds: "Your card has insufficient funds. Try a different card."
  - Incorrect CVC or expiry: "The security code looks wrong. Please check it and try again."
  - Expired card: "This card has expired."
  - Generic decline: don't state a reason. Use "Your bank declined this card" and suggest another card.
- **Keep the form filled in.** Don't clear the fields or reload the page. Put the error beside the card field, move focus to it, and offer a wallet payment as an alternative.

For subscriptions, also set up retry and dunning emails for failed renewals. These often recover more revenue than any change to the checkout form.

## How to confirm it worked
Before and after the change, measure completion rate per step, how often each field is abandoned, and the share of declines that end in a successful retry. If you can only test one thing first, test adding the wallet buttons and removing the password field. Those two changes usually matter most.

I can also draft the decline-message copy for each code, or review the checkout code, if you point me to where it lives.
