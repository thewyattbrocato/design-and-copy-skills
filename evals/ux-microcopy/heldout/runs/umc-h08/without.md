Your copy is already in good shape. These are small trims, plus one issue to check before you ship.

**Screen 1**
- Title: Reset your password *(no change)*
- Body: Enter your email and we'll send you a link to choose a new password.
- Button: Send reset link *(no change)*
- Error: No account found with that email. Check for typos or try another address.

**Screen 2**
- Title: Check your email *(no change)*
- Body: We sent a link to {email}. It expires in 60 minutes. Didn't get it? Check your spam folder or resend it.
- Link: Resend link

**Screen 3**
- Title: Choose a new password *(no change)*
- Button: Save password *(no change)*
- Toast: Password updated. You're signed in. *(no change)*

**Why these changes**
- **Screen 1 body:** "the email you signed up with" is wordy, and "a new one" depends on the title to make sense. "Your email" and "a new password" read cleanly on their own.
- **Error:** "No account found" is shorter and still tells people what happened.
- **Screen 2 body:** "or send it again" and a link labeled "Send it again" repeat each other. "Resend link" is the more familiar label, and "resend it" in the body then matches it.

**Security issue to check:** the "email isn't found" error lets anyone test whether an email has a Tallow account (account enumeration). Many teams avoid this by always moving to Screen 2 with neutral wording:

> If an account exists for {email}, we sent a link. It expires in 60 minutes. Didn't get it? Check your spam folder or resend it.

With that approach you can drop the Screen 1 error and keep only a format-validation error, such as "Enter a valid email address." If you decide enumeration isn't a concern for Tallow, the error above is fine.

**Screen 3 password rules:** if there are any (minimum length, for example), add a hint under the field, such as "At least 8 characters." Otherwise people find out only when Save fails.
