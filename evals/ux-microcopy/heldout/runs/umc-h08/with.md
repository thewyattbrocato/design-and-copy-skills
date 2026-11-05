**Screen 1**
- Title: Reset your password
- Body: Enter the email you signed up with and we'll send you a link to choose a new one.
- Button: Send reset link
- Error, email not found: We couldn't find an account with that email. Check for typos or try another address.

**Screen 2**
- Title: Check your email
- Body: We sent a link to {email}. It expires in 60 minutes. Didn't get it? Check your spam folder or send it again.
- Link: Send the link again

**Screen 3**
- Title: Choose a new password
- Button: Save password
- Success toast: Password updated. You're signed in.

- Your copy already works, so I changed only one thing. "Send it again" becomes "Send the link again" so it still makes sense when a screen reader lists links out of context.
- The "email not found" error tells people which emails have accounts. If that matters for Tallow, use a neutral message on Screen 1 instead, such as "If an account exists for that email, we've sent a link." Then Screen 2 would need to match it.
