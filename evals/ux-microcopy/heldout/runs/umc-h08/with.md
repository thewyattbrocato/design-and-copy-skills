**Screen 1**
- Title: Reset your password
- Body: Enter the email you signed up with and we'll send you a link to choose a new one.
- Button: Send reset link
- Error (email not found): We couldn't find an account with that email. Check for typos or try another address.

**Screen 2**
- Title: Check your email
- Body: We sent a link to {email}. It expires in 60 minutes. Didn't get it? Check your spam folder or send it again.
- Link: **Send the link again**

**Screen 3**
- Title: Choose a new password
- Button: Save password
- Success toast: Password updated. You're signed in.

The copy already works, so I changed only the Screen 2 link. "Send it again" means nothing when a screen reader lists links out of context, and "Send the link again" fixes that.

The "email not found" error tells anyone who tries an address whether it has a Tallow account. If you'd rather not reveal that, show Screen 2 for every address, with wording like "If an account exists for {email}, we sent a link." I left your copy as is because that's a product decision.
