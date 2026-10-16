Here's a tightened version.

**Screen 1**
- Title: Reset your password
- Body: Enter your email and we'll send you a link to choose a new one.
- Button: Send reset link
- Error (email not found): No account found for that email. Check for typos or try another address.

**Screen 2**
- Title: Check your email
- Body: We sent a reset link to {email}. It expires in 60 minutes. Not there? Check your spam folder.
- Link: Send it again

**Screen 3**
- Title: Choose a new password
- Button: Save password
- Success toast: Password updated. You're signed in.

**What changed and why**
- **Screen 1 body:** "the email you signed up with" is wordy. "Your email" says the same thing.
- **Screen 1 error:** It's shorter and doesn't sound as much like a system failure.
- **Screen 2 body:** I added "reset" so the email is easy to recognize in the inbox. I also dropped "or send it again" because the link right below already does that.
- **Screen 3:** The copy was already tight, so I left it alone.

**One thing to check before you ship:** the "no account found" error tells anyone who types an email whether it's registered. That lets someone test emails to see who uses Tallow. Many teams show the Screen 2 confirmation either way, with wording like "If an account exists for {email}, we sent a link." If you'd rather keep the explicit error for usability, that's a reasonable choice for a habit tracker. Just make it a deliberate one, and consider rate-limiting the endpoint.
