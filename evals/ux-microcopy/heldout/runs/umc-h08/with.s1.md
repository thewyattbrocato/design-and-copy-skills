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

Notes:
- The only change is the Screen 2 link. "Send it again" doesn't make sense when a screen reader lists links on their own, so it now names the thing it sends. Everything else was already clear, specific and consistent, so I left it alone.
- Screen 1's error tells anyone who types an email whether that address has a Tallow account. If that matters to you, use a neutral message instead and show Screen 2 for every address: "If an account exists for {email}, we've sent a link."
