**Screen 1**
- Title: Reset your password
- Body: Enter the email you signed up with and we'll send you a link to choose a new one.
- Button: Send reset link
- Error (email not found): We couldn't find an account with that email. Check for typos or try another address.

**Screen 2**
- Title: Check your email
- Body: We sent a link to {email}. It expires in 60 minutes. Didn't get it? Check your spam folder or send it again.
- Link: Send a new link

**Screen 3**
- Title: Choose a new password
- Button: Save password
- Success toast: Password updated. You're signed in.

- The copy already works, so I changed only one string: "Send it again" is now "Send a new link". Out of context, such as in a screen reader's link list, "it" has nothing to point to. The new wording also matches "link" on Screen 1.
- Check with your security team before shipping the "email not found" error. It confirms which addresses have accounts, which some teams avoid. If you'd rather not, use "If an account exists for that email, we've sent a link." and go to Screen 2 either way.
