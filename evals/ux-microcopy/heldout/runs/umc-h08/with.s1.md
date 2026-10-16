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

- The copy already works, so I changed only one thing. "Send it again" became "Send the link again" so the link still makes sense out of context, for example when a screen reader lists links.
- Before you ship, check whether the "email not found" error is intentional. It tells anyone who types an address whether that address has a Tallow account. Many teams show the Screen 2 message for every address instead, and Screen 2's body would then need "If an account exists for {email}, we sent a link."
