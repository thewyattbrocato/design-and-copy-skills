I'd cut **company name** (this is B2C yarn, not B2B), **phone number** (not needed for shipping), and **"create a password"** (make account creation optional post-purchase). Move **promo code to the end** and consider **"how did you hear about us"** as post-purchase analytics, not a checkout blocker.

**Suggested order:**
1. Email
2. Full name
3. Shipping address
4. Billing address (conditional: only if different)
5. Card details
6. Promo code (optional, easy to skip)

**Main tradeoff:** You'll lose "how did you hear about us" attribution data and some profile completeness, but you'll cut checkout length from 9 fields down to ~5-6, which should significantly reduce abandonment. The company name data is probably noise anyway.

**Also:** That "Error 402" message is brutal. Swap it for something like "Your card was declined. Please try another payment method or contact your bank." People need to know what went wrong and what to do next.

Want to dig into whether phone is actually needed (delivery insurance, SMS notifications)? That's the one field I'd validate before cutting.
