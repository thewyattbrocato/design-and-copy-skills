**Screen 1 title:** Reset your password
**Screen 1 body:** Enter the email you signed up with and we'll send you a link to choose a new one.
**Screen 1 button:** Send reset link
**Screen 1 error (email not found):** We couldn't find an account with that email. Check for typos or try another address.
**Screen 2 title:** Check your email
**Screen 2 body:** We sent a link to {email}. It expires in 60 minutes. Didn't get it? Check your spam folder or send it again.
**Screen 2 link:** Send the link again
**Screen 3 title:** Choose a new password
**Screen 3 button:** Save password
**Screen 3 success toast:** Password updated. You're signed in.

- The copy was already clear, so I changed only one string. "Send it again" became "Send the link again" because screen readers list links out of context, and "it" means nothing there.
- The "email not found" error confirms which emails have accounts. If that matters for your security posture, the usual alternative is a neutral message on Screen 1, such as "If an account exists for that email, we've sent a link". That is a product decision, so I left the copy as it is.
